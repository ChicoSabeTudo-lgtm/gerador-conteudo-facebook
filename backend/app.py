"""
Aplicação Flask - Backend do Gerador de Conteúdo para Facebook
"""
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from scraper import NewsScraper
from prompt_builder import PromptBuilder
from llm_client import LLMClient
import re

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)  # Habilita CORS para permitir requisições do frontend

# Inicializa os módulos
scraper = NewsScraper()
prompt_builder = PromptBuilder()
llm_client = LLMClient()

def validate_url(url):
    """Valida se a string é uma URL válida"""
    url_pattern = re.compile(
        r'^https?://'  # http:// ou https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domínio
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ou IP
        r'(?::\d+)?'  # porta opcional
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None

@app.route('/health', methods=['GET'])
def health():
    """Endpoint de health check"""
    return jsonify({'status': 'ok', 'message': 'API está funcionando'}), 200

@app.route('/api/generate', methods=['POST'])
def generate_content():
    """
    Endpoint principal para gerar conteúdo
    
    Espera JSON: { "url": "https://..." }
    Retorna JSON com o conteúdo gerado
    """
    try:
        # Valida o request
        data = request.get_json()
        
        if not data or 'url' not in data:
            return jsonify({
                'success': False,
                'error': 'URL não fornecida. Envie um JSON com a chave "url".'
            }), 400
        
        url = data['url'].strip()
        
        # Valida a URL
        if not validate_url(url):
            return jsonify({
                'success': False,
                'error': 'URL inválida. Certifique-se de incluir http:// ou https://'
            }), 400
        
        # Passo 1: Scraping da notícia
        print(f"[INFO] Fazendo scraping da URL: {url}")
        news_data = scraper.scrape(url)
        
        if not news_data['success']:
            return jsonify({
                'success': False,
                'error': news_data['error']
            }), 500
        
        # Passo 2: Construir o prompt
        print("[INFO] Construindo prompt personalizado...")
        prompt = prompt_builder.build_prompt(news_data)
        
        # Passo 3: Gerar conteúdo com LLM
        print("[INFO] Gerando conteúdo com LLM...")
        result = llm_client.generate_content(prompt)
        
        if not result['success']:
            return jsonify({
                'success': False,
                'error': result['error']
            }), 500
        
        # Passo 4: Retornar resultado
        print("[INFO] Conteúdo gerado com sucesso!")
        return jsonify({
            'success': True,
            'data': result['data'],
            'news_info': {
                'title': news_data['title'],
                'url': news_data['url'],
                'domain': news_data['domain']
            }
        }), 200
        
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Erro interno do servidor: {str(e)}'
        }), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """Serve o frontend React"""
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Servidor Flask iniciado!")
    print("📍 Acesse: http://localhost:5000")
    print("📋 Endpoints disponíveis:")
    print("   - GET  /health")
    print("   - POST /api/generate")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5000, debug=True)


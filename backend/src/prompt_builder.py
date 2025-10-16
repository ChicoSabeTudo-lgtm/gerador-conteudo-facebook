"""
Módulo para construir o prompt personalizado baseado nos dados da página
"""

class PromptBuilder:
    def __init__(self):
        # Dados demográficos da página #ChicoSabeTudo
        self.audience = "Homens e mulheres, majoritariamente entre 25 e 44 anos, residentes de grandes centros urbanos do Brasil (especialmente São Paulo e Rio de Janeiro). São pessoas economicamente ativas, que provavelmente se interessam por notícias, atualidades, carreira e tecnologia."
        self.tone = "Informativo, direto e confiável, mas com uma linguagem acessível. Evite ser formal demais. Use um tom que gere autoridade e curiosidade."
    
    def build_prompt(self, news_data):
        """
        Constrói o prompt completo para a API de LLM
        
        Args:
            news_data (dict): Dados da notícia extraídos pelo scraper
            
        Returns:
            str: Prompt formatado
        """
        
        news_content = f"""
TÍTULO: {news_data.get('title', 'N/A')}

CONTEÚDO: {news_data.get('content', 'N/A')}

DESCRIÇÃO: {news_data.get('description', 'N/A')}

URL: {news_data.get('url', 'N/A')}
"""
        
        prompt = f"""Atue como um Diretor de Estratégia de Conteúdo e Growth Hacking, especialista no algoritmo do Facebook. Sua missão é transformar a notícia abaixo em um pacote de conteúdo completo para o Facebook, otimizado para viralização, engajamento profundo e crescimento da página.

**Público-alvo:** {self.audience}
**Tom de Voz da Página:** {self.tone}

**NOTÍCIA A SER TRANSFORMADA:**
{news_content}

Analise a notícia e crie o seguinte:

1. **Análise Estratégica Rápida (Justificativa):**
   - **Ângulo Principal:** Qual é o aspecto mais relevante da notícia para um adulto urbano brasileiro?
   - **Sentimento a ser Evocado:** Qual emoção queremos gerar?
   - **Formato Ideal:** O formato deve ser **Reel (vídeo curto)**. Justifique como a notícia pode ser transformada em um vídeo dinâmico.

2. **Conteúdo para o Reel:**
   - **Roteiro em 3 Segundos:** A primeira cena ou frase que vai prender a atenção.
   - **Estrutura do Vídeo:** Um roteiro simples (narração e sugestão de cenas/imagens) de 15 a 45 segundos, dividido em cenas com tempo, descrição da cena e narração.
   - **Texto para a Tela (Legendas):** Sugestões de texto curtos e impactantes para aparecer sobre o vídeo.

3. **Copy Completa e Pronta para Publicar:**
   - **Crie uma legenda única e coesa, pronta para ser copiada e colada.**
   - **Comece com um gancho forte (primeira linha) para prender a atenção.**
   - **Desenvolva o corpo do texto** resumindo a notícia no tom de voz definido e usando emojis estrategicamente.
   - **Finalize com um CTA (Call to Action) de pergunta aberta**, que seja natural e estimule o debate nos comentários.

4. **Hashtags Estratégicas:**
   - **Crie uma lista única de 5 a 7 hashtags prontas para usar**, combinando 3 de alto volume, 2 de nicho e a hashtag de marca #ChicoSabeTudo.

**IMPORTANTE: Responda APENAS com um JSON válido no seguinte formato (sem markdown, sem explicações adicionais):**

{{
  "analise_estrategica": {{
    "angulo_principal": "texto aqui",
    "sentimento": "texto aqui",
    "formato_justificativa": "texto aqui"
  }},
  "roteiro_reel": {{
    "gancho_3_segundos": "texto aqui",
    "estrutura_video": [
      {{
        "tempo": "0-4s",
        "cena": "descrição da cena",
        "narracao": "texto da narração"
      }}
    ],
    "texto_tela": ["texto 1", "texto 2"]
  }},
  "copy_completa": "texto completo da legenda pronta para publicar",
  "hashtags": "#Tag1 #Tag2 #Tag3 #ChicoSabeTudo"
}}
"""
        
        return prompt


"""
Módulo para construir o prompt personalizado baseado nos dados da página
"""

class PromptBuilder:
    def __init__(self):
        # Dados demográficos da página #ChicoSabeTudo
        self.audience = "Homens e mulheres, majoritariamente entre 25 e 44 anos, residentes de grandes centros urbanos do Brasil (especialmente São Paulo e Rio de Janeiro). São pessoas economicamente ativas, que se interessam por notícias, atualidades, carreira e tecnologia."
        self.tone = "Informativo, direto e confiável, mas com linguagem acessível. Evite ser formal demais. Use um tom que gere autoridade e curiosidade."
    
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
        
        prompt = f"""Analise o texto de notícia fornecido no final deste prompt e, com base nele, crie um conteúdo completo para Facebook, seguindo estritamente a estrutura e as diretrizes abaixo.

**Público-alvo:** {self.audience}

**Tom de Voz:** {self.tone}

---

PARTE 1: SUGESTÕES DE TÍTULOS

Crie 3 seções distintas de títulos, cada uma com 5 sugestões. Os títulos devem ser criativos, otimizados para cliques e refletir o conteúdo da notícia.

**Seção 1: Títulos Diretos e Informativos**
- Foco: Resumir o fato principal de forma clara, objetiva e jornalística.
- Tamanho: Máximo de 80 caracteres
- Exemplo: "Nome da Pessoa é anunciado como novo secretário de Cidade."

**Seção 2: Títulos em Formato de Pergunta (Curiosidade)**
- Foco: Gerar engajamento e curiosidade, incentivando o leitor a querer saber mais.
- Tamanho: Máximo de 100 caracteres
- Exemplo: "O que está por trás da mudança na secretaria de Cidade?"

**Seção 3: Títulos para Engajar (Interação e Compartilhamento)**
- Foco: Gerar interação, comentários, reações e compartilhamentos. Usar linguagem que convide à discussão ou expressão de opinião.
- Tamanho: Máximo de 100 caracteres
- Estratégias: Use expressões como "Você concorda?", "O que você acha?", "Isso é aceitável?", "Chegou a hora de...", "Precisamos falar sobre..."
- Exemplo: "Barroso passa mal no STF: Será que nossos ministros trabalham demais? Você concorda?"

---

PARTE 2: SUGESTÕES DE POSTS PARA O FACEBOOK

Crie 3 opções de posts para o Facebook, cada uma com uma abordagem (tom) diferente.

**Todos os posts devem:**
- Ser escritos em português do Brasil, com linguagem humanizada e em formato de narrativa
- Incluir 1 ou 2 emojis relevantes (ex: 🚔 🤝 🏥 ✊ 🚨 👀 💡)
- Terminar com CTA: "👉 [Frase de convite criativa] em chicosabetudo.com.br 📲"
- Incluir 5 a 7 hashtags relevantes (3 de alto volume + 2 de nicho + #chicosabetudo)
- Respeitar o tempo verbal adequado (presente para eventos em andamento, passado para eventos concluídos)

**Opção 1: Foco na Notícia (Tom Informativo e Direto)**
- Objetivo: Apresentar o fato de forma clara, rápida e objetiva
- Tamanho: MÍNIMO 200 PALAVRAS (sem contar CTA e hashtags)
- Ideal para: Quem quer se informar rapidamente
- Desenvolva o texto com detalhes, contexto e informações relevantes sobre o fato

**Opção 2: Foco na Análise e nos Bastidores (Tom Analítico/Reflexivo)**
- Objetivo: Explorar o contexto, as causas e as possíveis consequências
- Tamanho: MÍNIMO 200 PALAVRAS (sem contar CTA e hashtags)
- Ideal para: Público que gosta de entender o "porquê"
- Aprofunde na análise, contexto histórico, implicações e perspectivas futuras

**Opção 3: Foco no Drama e na Repercussão (Tom de Impacto/Entretenimento)**
- Objetivo: Usar linguagem emocional para atrair pelo impacto ou drama
- Tamanho: MÍNIMO 200 PALAVRAS (sem contar CTA e hashtags)
- Ideal para: Público que acompanha pelo impacto emocional
- Use linguagem envolvente, crie suspense e explore os aspectos emocionais da história

---

**NOTÍCIA A SER TRANSFORMADA:**
{news_content}

**IMPORTANTE: Responda APENAS com um JSON válido no seguinte formato (sem markdown, sem explicações adicionais):**

{{
  "titulos": {{
    "diretos": ["título 1", "título 2", "título 3", "título 4", "título 5"],
    "perguntas": ["título 1", "título 2", "título 3", "título 4", "título 5"],
    "engajamento": ["título 1", "título 2", "título 3", "título 4", "título 5"]
  }},
  "posts": {{
    "informativo": "texto completo do post com emojis, CTA e hashtags",
    "analitico": "texto completo do post com emojis, CTA e hashtags",
    "drama": "texto completo do post com emojis, CTA e hashtags"
  }}
}}
"""
        
        return prompt


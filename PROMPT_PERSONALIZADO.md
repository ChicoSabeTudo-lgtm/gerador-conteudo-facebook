# Prompt Personalizado - Gerador de Conteúdo para Facebook

Este é o prompt completo e personalizado usado pela aplicação, otimizado especificamente para a página **#ChicoSabeTudo**.

---

## 📊 Dados da Página (Base do Prompt)

### Público-Alvo
- **Gênero:** Homens e mulheres
- **Idade:** Majoritariamente entre 25 e 44 anos (49.2% do público)
  - 25-34 anos: 26.3%
  - 35-44 anos: 22.9%
- **Localização:** Grandes centros urbanos do Brasil
  - São Paulo: 27.6%
  - Rio de Janeiro: 15.8%
  - Fortaleza: 10.5%
- **Perfil:** Pessoas economicamente ativas, interessadas em notícias, atualidades, carreira e tecnologia

### Formato Mais Eficaz
- **Reels:** 100% dos novos seguidores vêm deste formato
- **Conclusão:** Todo conteúdo deve ser pensado para vídeos curtos

### Tom de Voz
- **Informativo, direto e confiável**
- **Linguagem acessível** (não formal demais)
- **Gera autoridade e curiosidade**

---

## 📝 Prompt Completo

```
Atue como um Diretor de Estratégia de Conteúdo e Growth Hacking, especialista no algoritmo do Facebook. Sua missão é transformar a notícia abaixo em um pacote de conteúdo completo para o Facebook, otimizado para viralização, engajamento profundo e crescimento da página.

**Público-alvo:** Homens e mulheres, majoritariamente entre 25 e 44 anos, residentes de grandes centros urbanos do Brasil (especialmente São Paulo e Rio de Janeiro). São pessoas economicamente ativas, que provavelmente se interessam por notícias, atualidades, carreira e tecnologia.

**Tom de Voz da Página:** Informativo, direto e confiável, mas com uma linguagem acessível. Evite ser formal demais. Use um tom que gere autoridade e curiosidade.

**NOTÍCIA A SER TRANSFORMADA:**
[Título, conteúdo e URL da notícia]

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

{
  "analise_estrategica": {
    "angulo_principal": "texto aqui",
    "sentimento": "texto aqui",
    "formato_justificativa": "texto aqui"
  },
  "roteiro_reel": {
    "gancho_3_segundos": "texto aqui",
    "estrutura_video": [
      {
        "tempo": "0-4s",
        "cena": "descrição da cena",
        "narracao": "texto da narração"
      }
    ],
    "texto_tela": ["texto 1", "texto 2"]
  },
  "copy_completa": "texto completo da legenda pronta para publicar",
  "hashtags": "#Tag1 #Tag2 #Tag3 #ChicoSabeTudo"
}
```

---

## 🎯 Elementos-Chave do Prompt

### 1. Persona Definida
- "Diretor de Estratégia de Conteúdo e Growth Hacking"
- Força a IA a pensar estrategicamente, não apenas criar conteúdo

### 2. Dados Demográficos Reais
- Baseados nos analytics da página
- Garantem relevância para o público real

### 3. Tom de Voz Específico
- "Informativo, direto e confiável, mas acessível"
- Evita formalismo excessivo
- Mantém autoridade

### 4. Foco em Reel
- 100% dos dados mostram que Reels funcionam
- Todo conteúdo é pensado para vídeo

### 5. Estrutura de Output Definida
- JSON estruturado
- Facilita o parsing e exibição na interface
- Garante consistência

### 6. Copy Completa e Pronta
- Não oferece opções, entrega o resultado final
- Inclui gancho, desenvolvimento e CTA integrados
- Pronta para copiar e colar

### 7. Hashtags Estratégicas
- Combinação de volume e nicho
- Sempre inclui #ChicoSabeTudo
- 5-7 hashtags (quantidade ideal)

---

## 🔄 Fluxo de Processamento

1. **Scraping:** Extrai título, conteúdo e metadados da URL
2. **Prompt Building:** Injeta os dados da notícia no prompt
3. **LLM Processing:** OpenAI API processa com GPT-4.1-mini
4. **JSON Parsing:** Extrai e valida a resposta estruturada
5. **Frontend Display:** Exibe em cards organizados

---

## 📈 Resultados Esperados

### Análise Estratégica
- Identifica o ângulo mais relevante para o público urbano de 25-44 anos
- Define o sentimento apropriado (curiosidade, indignação, esperança, etc.)
- Justifica por que um Reel é o formato ideal

### Roteiro do Reel
- Gancho de 3 segundos extremamente impactante
- Estrutura de 15-45 segundos com timing preciso
- Sugestões de cenas visuais e narração
- Textos curtos para legendas na tela

### Copy Completa
- Gancho forte na primeira linha (emojis + urgência)
- Desenvolvimento claro e acessível
- CTA com pergunta aberta para estimular comentários
- Emojis estratégicos (não excessivos)

### Hashtags
- 3 de alto volume (#Brasil, #Notícias, #STF)
- 2 de nicho (#Justiça, #SaúdePública)
- 1 de marca (#ChicoSabeTudo)

---

## 🛠️ Customização

Para adaptar este prompt para outra página, modifique:

1. **Público-alvo:** Insira os dados demográficos reais
2. **Tom de Voz:** Defina o estilo da marca
3. **Formato Ideal:** Se não for Reel, ajuste para o formato que funciona
4. **Hashtag de Marca:** Substitua #ChicoSabeTudo pela sua

---

## 📊 Métricas de Sucesso

Este prompt foi otimizado para:

- ✅ **Alcance:** Conteúdo pensado para o algoritmo do Facebook
- ✅ **Engajamento:** CTAs que estimulam comentários
- ✅ **Recomendação:** Formato Reel (100% de efetividade comprovada)
- ✅ **Consistência:** Tom de voz alinhado com a marca
- ✅ **Eficiência:** Copy pronta, sem necessidade de edição

---

**Este prompt é o coração da aplicação e foi desenvolvido com base em dados reais da página #ChicoSabeTudo.**


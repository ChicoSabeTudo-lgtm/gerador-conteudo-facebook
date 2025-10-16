# Gerador de Conteúdo para Facebook - #ChicoSabeTudo

Aplicação web completa que transforma qualquer notícia em **títulos otimizados e posts completos** para o Facebook, usando Inteligência Artificial.

## 🎯 Funcionalidades

A aplicação gera automaticamente:

### 1. **Sugestões de Títulos (15 opções)**

Divididos em 3 seções com 5 títulos cada:

#### 📋 **Títulos Diretos e Informativos**
- Foco: Resumir o fato principal de forma clara, objetiva e jornalística
- Tamanho: Máximo de 80 caracteres
- Exemplo: "Ministro Barroso passa mal no STF e é levado para hospital"

#### ❓ **Títulos em Formato de Pergunta**
- Foco: Gerar engajamento e curiosidade
- Tamanho: Máximo de 100 caracteres
- Exemplo: "O que causou o mal-estar do ministro Barroso no STF?"

#### ⚡ **Títulos Curtos e de Impacto**
- Foco: Fortes e diretos para redes sociais
- Tamanho: Máximo de 40 caracteres
- Exemplo: "Barroso no Hospital"

### 2. **Posts para Facebook (3 opções)**

Cada post com um tom diferente:

#### 📢 **Tom Informativo e Direto**
- Apresenta o fato de forma clara e objetiva
- Tamanho: 150-200 caracteres
- Ideal para: Quem quer se informar rapidamente

#### 🔍 **Tom Analítico e Reflexivo**
- Explora o contexto, causas e consequências
- Tamanho: 250-350 caracteres
- Ideal para: Público que gosta de entender o "porquê"

#### 🎭 **Tom de Impacto e Drama**
- Usa linguagem emocional para atrair pelo impacto
- Tamanho: 200-300 caracteres
- Ideal para: Público que acompanha pelo drama emocional

**Todos os posts incluem:**
- ✅ Emojis relevantes (🚨 👀 💡 🏥 etc.)
- ✅ CTA direcionando para chicosabetudo.com.br
- ✅ 5-7 hashtags estratégicas (incluindo #chicosabetudo)
- ✅ Tempo verbal adequado (presente ou passado)

---

## 🌐 URL da Aplicação

**Acesse aqui:** https://8080-iyk66x2twmeqdm9jr47co-3434970c.manusvm.computer

---

## 📖 Como Usar

1. Acesse a URL da aplicação
2. Cole o link completo da notícia no campo de input
3. Clique em "Gerar Conteúdo"
4. Aguarde 5-15 segundos enquanto a IA processa
5. Navegue pelas abas para ver os diferentes títulos e posts
6. Copie o título ou post desejado com um clique no botão "Copiar"

---

## 🎨 Interface

### **Seção de Títulos**
- 3 abas (Diretos, Perguntas, Curtos)
- 5 títulos por aba
- Botão "Copiar" individual para cada título
- Cores diferenciadas por aba

### **Seção de Posts**
- 3 abas (Informativo, Analítico, Drama)
- Descrição do tom de cada post
- Preview completo do post com formatação
- Botão "Copiar Post Completo"

---

## 🚀 Tecnologias Utilizadas

### Backend
- **Flask** - Framework web Python
- **BeautifulSoup4** - Web scraping
- **OpenAI API** - Geração de conteúdo com IA (GPT-4.1-mini)
- **Gunicorn** - Servidor WSGI para produção

### Frontend
- **React 18** - Framework JavaScript
- **Vite** - Build tool
- **TailwindCSS** - Estilização
- **shadcn/ui** - Componentes UI (Tabs, Cards, Buttons)
- **Lucide React** - Ícones

---

## 📊 Dados do Público-Alvo

A aplicação foi otimizada com base nos dados reais da página #ChicoSabeTudo:

- **Público**: Homens e mulheres, 25-44 anos (49.2% do total)
- **Localização**: Grandes centros urbanos (SP 27.6%, RJ 15.8%)
- **Perfil**: Pessoas economicamente ativas, interessadas em notícias e atualidades
- **Tom**: Informativo, direto e confiável, mas acessível

---

## 🛠️ Estrutura do Projeto

```
gerador-conteudo-facebook/
├── backend/
│   ├── app.py              # Aplicação Flask principal
│   ├── scraper.py          # Módulo de web scraping
│   ├── prompt_builder.py   # Construtor do prompt personalizado
│   ├── llm_client.py       # Cliente OpenAI API
│   ├── requirements.txt    # Dependências Python
│   ├── static/             # Frontend build (React)
│   └── venv/               # Ambiente virtual Python
│
└── frontend/
    └── gerador-facebook/
        ├── src/
        │   ├── App.jsx     # Componente principal
        │   └── App.css     # Estilos
        ├── dist/           # Build de produção
        └── package.json    # Dependências Node
```

---

## 🔧 Instalação Local

### Backend

```bash
cd backend
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Frontend

```bash
cd frontend/gerador-facebook
pnpm install
pnpm run build
```

### Executar em Produção

```bash
cd backend
gunicorn -w 2 -b 0.0.0.0:8080 app:app --timeout 120
```

---

## 🔑 Variáveis de Ambiente

A aplicação requer a seguinte variável de ambiente:

- `OPENAI_API_KEY` - Chave da API OpenAI (já configurada no ambiente)

---

## 📝 Prompt Personalizado

O prompt foi desenvolvido especificamente para a página #ChicoSabeTudo, incluindo:

- Dados demográficos do público (25-44 anos, centros urbanos)
- Tom de voz da marca (informativo, direto, acessível)
- 3 seções de títulos com objetivos distintos
- 3 tons de posts para diferentes públicos
- Estrutura de output otimizada (JSON)

---

## ✨ Diferenciais

- ✅ **15 títulos** - 3 estilos diferentes para testar
- ✅ **3 posts completos** - Tons variados para diferentes públicos
- ✅ **Botões de copiar** - Um clique para copiar qualquer conteúdo
- ✅ **Interface com abas** - Navegação intuitiva e organizada
- ✅ **CTA padronizado** - Direciona tráfego para chicosabetudo.com.br
- ✅ **Hashtags estratégicas** - Sempre incluindo #chicosabetudo
- ✅ **Design responsivo** - Funciona em desktop e mobile

---

## 📈 Exemplo de Uso

**Input:** https://www.msn.com/pt-br/noticias/brasil/barroso-passa-mal-no-stf...

**Output:**

### Títulos Diretos:
1. "Ministro Barroso passa mal no STF e é levado para hospital"
2. "Barroso sofre mal-estar no STF e realiza exames médicos"
3. (+ 3 opções)

### Títulos em Pergunta:
1. "O que causou o mal-estar do ministro Barroso no STF?"
2. "Por que Barroso precisou ser levado ao hospital durante sessão?"
3. (+ 3 opções)

### Títulos Curtos:
1. "Barroso no Hospital"
2. "Mal-estar no STF"
3. (+ 3 opções)

### Post Informativo:
```
O ministro Luís Roberto Barroso passou mal durante sessão no STF e foi 
levado para um hospital para realização de exames médicos. O estado de 
saúde dele está sendo monitorado de perto pelas autoridades. 🚨👨‍⚕️

👉 Saiba todos os detalhes em chicosabetudo.com.br 📲

#Barroso #STF #Notícias #SaúdePública #Política #Brasil #chicosabetudo
```

(+ Posts Analítico e Drama)

---

## 🎯 Casos de Uso

1. **Teste A/B de Títulos** - Use os 15 títulos para testar qual gera mais cliques
2. **Adaptação ao Público** - Escolha o tom de post baseado no horário/público
3. **Geração Rápida** - Transforme qualquer notícia em conteúdo em segundos
4. **Consistência de Marca** - Mantenha o tom #ChicoSabeTudo em todos os posts

---

## 🤝 Contribuições

Este projeto foi desenvolvido especificamente para a página #ChicoSabeTudo.

---

## 📄 Licença

Propriedade de #ChicoSabeTudo

---

**Desenvolvido com ❤️ para #ChicoSabeTudo**


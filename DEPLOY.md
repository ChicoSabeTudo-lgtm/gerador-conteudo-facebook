# Guia de Deploy - Gerador de Conteúdo Facebook

## 🚀 Opções de Deploy Permanente

A aplicação está rodando temporariamente em:
**https://8080-iyk66x2twmeqdm9jr47co-3434970c.manusvm.computer**

Para torná-la permanente, você tem as seguintes opções:

---

## Opção 1: Railway (Recomendado - Gratuito)

### Passo a Passo:

1. **Criar conta no Railway**
   - Acesse: https://railway.app
   - Faça login com GitHub

2. **Criar novo projeto**
   - Clique em "New Project"
   - Selecione "Deploy from GitHub repo"

3. **Conectar o repositório**
   - Autorize o Railway a acessar seus repositórios
   - Selecione o repositório do projeto

4. **Configurar variáveis de ambiente**
   - Adicione: `OPENAI_API_KEY` com sua chave da OpenAI

5. **Deploy automático**
   - O Railway detectará automaticamente que é uma aplicação Flask
   - O deploy será feito automaticamente

6. **Obter URL permanente**
   - Após o deploy, você receberá uma URL pública permanente
   - Exemplo: `https://seu-app.up.railway.app`

### Vantagens:
- ✅ Gratuito (500 horas/mês)
- ✅ Deploy automático via Git
- ✅ SSL/HTTPS incluído
- ✅ Domínio personalizado (opcional)

---

## Opção 2: Render (Gratuito)

### Passo a Passo:

1. **Criar conta no Render**
   - Acesse: https://render.com
   - Faça login com GitHub

2. **Criar novo Web Service**
   - Clique em "New +" → "Web Service"
   - Conecte seu repositório GitHub

3. **Configurar o serviço**
   - **Name:** gerador-facebook
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn -w 2 -b 0.0.0.0:$PORT app:app --timeout 120`

4. **Adicionar variáveis de ambiente**
   - `OPENAI_API_KEY`: Sua chave da OpenAI

5. **Deploy**
   - Clique em "Create Web Service"
   - Aguarde o deploy (5-10 minutos)

6. **URL permanente**
   - Você receberá uma URL como: `https://gerador-facebook.onrender.com`

### Vantagens:
- ✅ Gratuito
- ✅ SSL/HTTPS incluído
- ✅ Deploy automático via Git
- ✅ Fácil configuração

### Desvantagens:
- ⚠️ Pode hibernar após 15 minutos de inatividade (plano gratuito)
- ⚠️ Primeira requisição após hibernar pode demorar 30-60 segundos

---

## Opção 3: Vercel (Gratuito)

### Passo a Passo:

1. **Instalar Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Fazer login**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   cd /home/ubuntu/gerador-conteudo-facebook/backend
   vercel --prod
   ```

4. **Configurar variáveis**
   - No dashboard da Vercel, adicione `OPENAI_API_KEY`

### Vantagens:
- ✅ Gratuito
- ✅ Deploy ultra-rápido
- ✅ CDN global
- ✅ SSL/HTTPS incluído

---

## Opção 4: PythonAnywhere (Gratuito com limitações)

### Passo a Passo:

1. **Criar conta**
   - Acesse: https://www.pythonanywhere.com
   - Crie uma conta gratuita

2. **Upload dos arquivos**
   - Use o File Manager para fazer upload do projeto

3. **Configurar Web App**
   - Vá em "Web" → "Add a new web app"
   - Escolha Flask
   - Configure o WSGI file

4. **Instalar dependências**
   ```bash
   pip3.11 install --user -r requirements.txt
   ```

5. **URL permanente**
   - `https://seuusuario.pythonanywhere.com`

### Vantagens:
- ✅ Gratuito
- ✅ Sempre ativo (não hiberna)
- ✅ SSL/HTTPS incluído

### Desvantagens:
- ⚠️ Limitado a 100 segundos de CPU por dia (plano gratuito)
- ⚠️ Não permite conexões externas (pode limitar scraping)

---

## Opção 5: Fly.io (Gratuito)

### Passo a Passo:

1. **Instalar Fly CLI**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Fazer login**
   ```bash
   flyctl auth login
   ```

3. **Inicializar app**
   ```bash
   cd /home/ubuntu/gerador-conteudo-facebook/backend
   flyctl launch
   ```

4. **Configurar variáveis**
   ```bash
   flyctl secrets set OPENAI_API_KEY=sua_chave_aqui
   ```

5. **Deploy**
   ```bash
   flyctl deploy
   ```

### Vantagens:
- ✅ Gratuito (3GB RAM incluídos)
- ✅ Sempre ativo
- ✅ SSL/HTTPS incluído
- ✅ Ótima performance

---

## 📦 Arquivos Necessários para Deploy

O projeto já está preparado com:

- ✅ `requirements.txt` - Dependências Python
- ✅ `app.py` - Aplicação Flask principal
- ✅ `main.py` - Entry point
- ✅ `wsgi.py` - Configuração WSGI
- ✅ `static/` - Frontend React (build)

---

## 🔑 Variável de Ambiente Obrigatória

Todas as plataformas precisam da variável:

```
OPENAI_API_KEY=sk-...
```

**⚠️ IMPORTANTE:** Você precisa criar sua própria chave da OpenAI em:
https://platform.openai.com/api-keys

---

## 🌐 Domínio Personalizado (Opcional)

Após o deploy em qualquer plataforma, você pode configurar um domínio personalizado:

Exemplos:
- `gerador.chicosabetudo.com.br`
- `conteudo.chicosabetudo.com.br`
- `facebook.chicosabetudo.com.br`

Todas as plataformas acima suportam domínios personalizados gratuitamente.

---

## 📊 Recomendação Final

Para **#ChicoSabeTudo**, recomendo:

### 🥇 **1ª Opção: Railway**
- Melhor custo-benefício
- Não hiberna
- Deploy automático
- 500 horas gratuitas/mês

### 🥈 **2ª Opção: Render**
- Totalmente gratuito
- Fácil de usar
- Única desvantagem: hiberna após 15min

### 🥉 **3ª Opção: Fly.io**
- Melhor performance
- Sempre ativo
- Configuração um pouco mais técnica

---

## 🆘 Suporte

Se precisar de ajuda com o deploy, entre em contato através dos canais oficiais do #ChicoSabeTudo.

---

**Desenvolvido com ❤️ para #ChicoSabeTudo**


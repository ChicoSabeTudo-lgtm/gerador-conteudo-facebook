# 🚀 Deploy Permanente - Passo a Passo Detalhado

## 📦 Repositório GitHub

**URL:** https://github.com/ChicoSabeTudo-lgtm/gerador-conteudo-facebook

O código já está no GitHub e pronto para deploy!

---

## ⚡ Opção 1: Railway (MAIS FÁCIL - Recomendado)

### Passo 1: Criar Conta
1. Acesse: https://railway.app
2. Clique em "Login"
3. Escolha "Login with GitHub"
4. Autorize o Railway a acessar sua conta GitHub

### Passo 2: Criar Novo Projeto
1. No dashboard do Railway, clique em "**New Project**"
2. Selecione "**Deploy from GitHub repo**"
3. Procure por "**gerador-conteudo-facebook**"
4. Clique no repositório para selecioná-lo

### Passo 3: Configurar Variável de Ambiente
1. Após selecionar o repositório, clique na aba "**Variables**"
2. Clique em "**+ New Variable**"
3. Adicione:
   - **Nome:** `OPENAI_API_KEY`
   - **Valor:** Sua chave da OpenAI (obtenha em https://platform.openai.com/api-keys)
4. Clique em "**Add**"

### Passo 4: Deploy Automático
1. O Railway detectará automaticamente os arquivos de configuração
2. O deploy começará automaticamente
3. Aguarde 2-5 minutos

### Passo 5: Obter URL Permanente
1. Após o deploy, clique na aba "**Settings**"
2. Role até "**Domains**"
3. Clique em "**Generate Domain**"
4. Você receberá uma URL como: `https://gerador-conteudo-facebook-production.up.railway.app`

### ✅ Pronto! Sua aplicação está no ar!

**Vantagens do Railway:**
- ✅ 500 horas gratuitas por mês
- ✅ Não hiberna (sempre ativo)
- ✅ Deploy automático a cada push no GitHub
- ✅ SSL/HTTPS incluído
- ✅ Fácil de configurar

---

## 🎨 Opção 2: Render (Totalmente Gratuito)

### Passo 1: Criar Conta
1. Acesse: https://render.com
2. Clique em "**Get Started**"
3. Escolha "**Sign up with GitHub**"
4. Autorize o Render

### Passo 2: Criar Web Service
1. No dashboard, clique em "**New +**"
2. Selecione "**Web Service**"
3. Clique em "**Connect a repository**"
4. Procure por "**gerador-conteudo-facebook**"
5. Clique em "**Connect**"

### Passo 3: Configurar o Serviço
Preencha os campos:

- **Name:** `gerador-facebook`
- **Region:** `Oregon (US West)`
- **Branch:** `master`
- **Root Directory:** (deixe vazio)
- **Runtime:** `Python 3`
- **Build Command:** `cd backend && pip install -r requirements.txt`
- **Start Command:** `cd backend && gunicorn -w 2 -b 0.0.0.0:$PORT app:app --timeout 120`

### Passo 4: Adicionar Variável de Ambiente
1. Role até "**Environment Variables**"
2. Clique em "**Add Environment Variable**"
3. Adicione:
   - **Key:** `OPENAI_API_KEY`
   - **Value:** Sua chave da OpenAI

### Passo 5: Deploy
1. Clique em "**Create Web Service**"
2. Aguarde 5-10 minutos para o deploy
3. Você receberá uma URL como: `https://gerador-facebook.onrender.com`

### ⚠️ Observação
O plano gratuito do Render hiberna após 15 minutos de inatividade. A primeira requisição após hibernar pode demorar 30-60 segundos.

---

## 🔥 Opção 3: Vercel (Deploy Rápido)

### Passo 1: Instalar Vercel CLI
No terminal:
```bash
npm install -g vercel
```

### Passo 2: Fazer Login
```bash
vercel login
```

### Passo 3: Deploy
```bash
cd /caminho/para/gerador-conteudo-facebook
vercel --prod
```

### Passo 4: Configurar Variável
1. Acesse: https://vercel.com/dashboard
2. Selecione seu projeto
3. Vá em "**Settings**" → "**Environment Variables**"
4. Adicione `OPENAI_API_KEY`

---

## 🌐 Domínio Personalizado (Opcional)

Após o deploy em qualquer plataforma, você pode configurar um domínio personalizado:

### Sugestões de Domínio:
- `gerador.chicosabetudo.com.br`
- `conteudo.chicosabetudo.com.br`
- `facebook.chicosabetudo.com.br`

### Como Configurar:

#### No Railway:
1. Vá em "**Settings**" → "**Domains**"
2. Clique em "**Custom Domain**"
3. Digite seu domínio
4. Adicione o registro CNAME no seu provedor de DNS

#### No Render:
1. Vá em "**Settings**" → "**Custom Domain**"
2. Digite seu domínio
3. Adicione o registro CNAME no seu provedor de DNS

---

## 🔑 Obter Chave da OpenAI

Se você ainda não tem uma chave da OpenAI:

1. Acesse: https://platform.openai.com/signup
2. Crie uma conta (ou faça login)
3. Vá em: https://platform.openai.com/api-keys
4. Clique em "**Create new secret key**"
5. Dê um nome (ex: "Gerador Facebook")
6. Copie a chave (começa com `sk-...`)
7. **⚠️ IMPORTANTE:** Guarde a chave em local seguro, ela só aparece uma vez!

### Custos da OpenAI:
- Modelo usado: `gpt-4.1-mini`
- Custo aproximado: $0.15 por 1000 requisições
- Para uso moderado (100 posts/dia): ~$4.50/mês

---

## 📊 Monitoramento

Após o deploy, você pode monitorar:

### No Railway:
- **Logs:** Aba "Deployments" → Clique no deploy → "View Logs"
- **Métricas:** Aba "Metrics" (CPU, RAM, Network)

### No Render:
- **Logs:** Aba "Logs" (em tempo real)
- **Eventos:** Aba "Events" (histórico de deploys)

---

## 🔄 Atualizações Automáticas

Todas as plataformas fazem deploy automático quando você faz push no GitHub:

```bash
# Fazer alterações no código
git add .
git commit -m "Melhoria X"
git push origin master

# O deploy será feito automaticamente!
```

---

## ❓ Problemas Comuns

### Erro: "Application failed to respond"
**Solução:** Verifique se a variável `OPENAI_API_KEY` está configurada corretamente.

### Erro: "Module not found"
**Solução:** Certifique-se de que o `requirements.txt` está no diretório `backend/`.

### Erro: "Port already in use"
**Solução:** As plataformas usam a variável `$PORT` automaticamente, não precisa alterar nada.

### Site muito lento
**Solução:** 
- No Render (plano gratuito), a primeira requisição após hibernar é lenta
- Considere usar Railway ou fazer upgrade para o plano pago do Render

---

## 🎯 Checklist Final

Antes de considerar o deploy completo, verifique:

- [ ] Repositório no GitHub está atualizado
- [ ] Variável `OPENAI_API_KEY` está configurada
- [ ] Deploy foi concluído sem erros
- [ ] URL pública está acessível
- [ ] Testou gerar conteúdo com uma notícia
- [ ] Todos os 3 tipos de posts aparecem
- [ ] Botões de copiar funcionam
- [ ] (Opcional) Domínio personalizado configurado

---

## 📞 Suporte

Se encontrar problemas:

1. Verifique os logs da plataforma
2. Confirme que a chave da OpenAI está válida
3. Teste localmente primeiro
4. Entre em contato através dos canais oficiais do #ChicoSabeTudo

---

## 🎉 Sucesso!

Após seguir estes passos, sua aplicação estará:

✅ **Online 24/7** (exceto Render gratuito que hiberna)
✅ **Com HTTPS/SSL** (seguro)
✅ **Com URL pública** (compartilhável)
✅ **Com deploy automático** (atualizações via Git)

---

**Desenvolvido com ❤️ para #ChicoSabeTudo**


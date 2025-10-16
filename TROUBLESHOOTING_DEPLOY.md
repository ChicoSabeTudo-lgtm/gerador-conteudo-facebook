# 🔧 Troubleshooting - Deploy

## Erro: "pip: command not found"

### Problema
```
RUN  cd backend && pip install -r requirements.txt
/bin/bash: line 1: pip: command not found
```

### Causa
A plataforma de deploy está tentando usar um ambiente que não tem Python/pip instalado.

### Solução ✅

Criei 3 soluções alternativas. Escolha a que funcionar melhor:

---

## Solução 1: Usar Dockerfile (RECOMENDADO)

### Arquivos criados:
- ✅ `Dockerfile` - Configuração Docker com Python 3.11
- ✅ `.dockerignore` - Otimização do build

### Para Railway:
1. O `railway.json` foi atualizado para usar `DOCKERFILE`
2. Faça novo deploy - deve funcionar automaticamente

### Para Render:
1. O `render.yaml` foi atualizado para `env: docker`
2. Faça novo deploy - deve funcionar automaticamente

---

## Solução 2: Usar Nixpacks (Railway)

### Arquivo criado:
- ✅ `nixpacks.toml` - Configuração Nixpacks

### Como usar:
1. No Railway, vá em Settings
2. Em "Build", selecione "Nixpacks"
3. O arquivo `nixpacks.toml` será usado automaticamente
4. Faça redeploy

---

## Solução 3: Configuração Manual (Render)

### Passo a passo:

1. **No dashboard do Render:**
   - Vá em "Settings"
   - Mude "Environment" de "Python" para "Docker"
   - Salve

2. **Ou use Python com comandos corretos:**
   - Environment: `Python 3`
   - Build Command: `pip install -r backend/requirements.txt`
   - Start Command: `cd backend && gunicorn -w 2 -b 0.0.0.0:$PORT app:app --timeout 120`

---

## Verificação dos Arquivos

### ✅ Arquivos Atualizados:

1. **Dockerfile**
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY backend/requirements.txt /app/requirements.txt
   RUN pip install --no-cache-dir -r requirements.txt
   COPY backend /app
   EXPOSE 8080
   CMD gunicorn -w 2 -b 0.0.0.0:${PORT:-8080} app:app --timeout 120
   ```

2. **railway.json**
   ```json
   {
     "build": {
       "builder": "DOCKERFILE",
       "dockerfilePath": "Dockerfile"
     }
   }
   ```

3. **render.yaml**
   ```yaml
   services:
     - type: web
       env: docker
       dockerfilePath: ./Dockerfile
   ```

4. **Procfile** (para Heroku/Railway sem Docker)
   ```
   web: gunicorn -w 2 -b 0.0.0.0:$PORT app:app --timeout 120 --chdir backend
   ```

5. **nixpacks.toml** (alternativa para Railway)
   ```toml
   [phases.setup]
   nixPkgs = ['python311', 'pip']
   
   [phases.install]
   cmds = ['cd backend && pip install -r requirements.txt']
   
   [start]
   cmd = 'cd backend && gunicorn -w 2 -b 0.0.0.0:$PORT app:app --timeout 120'
   ```

---

## Testando Localmente (Opcional)

Se você tem Docker instalado localmente:

```bash
# Build
docker build -t gerador-facebook .

# Run
docker run -p 8080:8080 -e OPENAI_API_KEY=sua_chave gerador-facebook

# Testar
curl http://localhost:8080
```

---

## Próximos Passos

### 1. Fazer commit das mudanças:
```bash
git add .
git commit -m "Corrigir configuração de deploy - adicionar Dockerfile"
git push origin master
```

### 2. Fazer redeploy na plataforma escolhida:

#### Railway:
- O deploy será automático após o push
- Ou clique em "Deploy" manualmente

#### Render:
- O deploy será automático após o push
- Ou clique em "Manual Deploy"

### 3. Verificar logs:
- Railway: Aba "Deployments" → "View Logs"
- Render: Aba "Logs"

---

## Outras Soluções de Deploy

Se Railway e Render continuarem com problemas, tente:

### Opção A: Vercel (Serverless)

```bash
npm install -g vercel
cd /caminho/para/gerador-conteudo-facebook
vercel --prod
```

**Vantagens:**
- Deploy ultra-rápido
- Sem Docker necessário
- Configuração automática

### Opção B: Fly.io

```bash
# Instalar Fly CLI
curl -L https://fly.io/install.sh | sh

# Deploy
cd /caminho/para/gerador-conteudo-facebook
flyctl launch
flyctl secrets set OPENAI_API_KEY=sua_chave
flyctl deploy
```

**Vantagens:**
- Usa Docker nativamente
- Sempre ativo
- Gratuito até 3GB RAM

### Opção C: DigitalOcean App Platform

1. Conecte o repositório GitHub
2. Selecione "Dockerfile"
3. Configure variável `OPENAI_API_KEY`
4. Deploy

**Vantagens:**
- Interface simples
- Suporte a Docker
- $5/mês (não gratuito)

---

## Checklist de Deploy

Antes de fazer deploy, verifique:

- [ ] Arquivo `Dockerfile` existe
- [ ] Arquivo `.dockerignore` existe
- [ ] `railway.json` ou `render.yaml` atualizado
- [ ] Variável `OPENAI_API_KEY` configurada na plataforma
- [ ] Código commitado e pushed para GitHub
- [ ] Plataforma conectada ao repositório correto
- [ ] Branch correto selecionado (master)

---

## Logs Úteis

### Se o deploy falhar, procure por:

**Erro de dependências:**
```
ERROR: Could not find a version that satisfies the requirement
```
**Solução:** Verifique `backend/requirements.txt`

**Erro de porta:**
```
Address already in use
```
**Solução:** Certifique-se de usar `$PORT` variável

**Erro de timeout:**
```
Worker timeout
```
**Solução:** Já configurado `--timeout 120`

**Erro de memória:**
```
Killed
```
**Solução:** Reduza workers de 2 para 1 no comando gunicorn

---

## Suporte

Se nenhuma solução funcionar:

1. **Verifique os logs** da plataforma
2. **Copie a mensagem de erro** completa
3. **Tente outra plataforma** (Railway → Render → Fly.io)
4. **Use deploy manual** via Vercel CLI

---

## Status Atual

✅ **Arquivos criados/atualizados:**
- Dockerfile
- .dockerignore
- railway.json
- render.yaml
- nixpacks.toml
- Procfile
- TROUBLESHOOTING_DEPLOY.md (este arquivo)

✅ **Pronto para:**
- Deploy via Docker (Railway, Render, Fly.io)
- Deploy via Nixpacks (Railway)
- Deploy via Procfile (Railway, Heroku)

🔄 **Próximo passo:**
```bash
git add .
git commit -m "Corrigir configuração de deploy"
git push origin master
```

Depois, faça redeploy na plataforma escolhida!

---

**Desenvolvido com ❤️ para #ChicoSabeTudo**


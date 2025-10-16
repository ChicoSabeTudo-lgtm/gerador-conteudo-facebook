# Use Python 3.11 como base
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos
COPY backend/requirements.txt /app/requirements.txt

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do backend
COPY backend /app

# Expõe a porta (será sobrescrita pela variável $PORT)
EXPOSE 8080

# Comando para iniciar a aplicação
CMD gunicorn -w 2 -b 0.0.0.0:${PORT:-8080} app:app --timeout 120


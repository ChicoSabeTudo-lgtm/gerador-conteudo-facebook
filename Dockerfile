# Use Python 3.11 como base
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos primeiro (para cache de camadas)
COPY backend/requirements.txt ./requirements.txt

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do backend
COPY backend/ ./

# Expõe a porta
EXPOSE 8080

# Define a porta padrão (será sobrescrita por $PORT do Railway)
ENV PORT=8080

# Comando para iniciar a aplicação usando a variável $PORT
CMD gunicorn -w 2 -b 0.0.0.0:$PORT app:app --timeout 120


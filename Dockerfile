# Use Python 3.11 como base
FROM python:3.11-slim

# Instala bash (necessário para o script de inicialização)
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos primeiro (para cache de camadas)
COPY backend/requirements.txt ./requirements.txt

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do backend
COPY backend/ ./

# Dá permissão de execução ao script de inicialização
RUN chmod +x start.sh

# Expõe a porta
EXPOSE 8080

# Usa o script de inicialização
CMD ["./start.sh"]


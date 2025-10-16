#!/bin/bash
# Script de inicialização para Railway

# Define porta padrão se $PORT não estiver definida
PORT=${PORT:-8080}

# Inicia o gunicorn com a porta correta
exec gunicorn -w 2 -b 0.0.0.0:$PORT app:app --timeout 120


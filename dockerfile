# Use uma imagem base do Python
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o código-fonte para o diretório de trabalho
COPY sistema.bancario.py .

# Comando para executar o script
CMD ["python", "sistema.bancario.py"]

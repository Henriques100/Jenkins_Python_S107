# Use a imagem base do Python
FROM python:3.9-slim

# Configuração do ambiente
WORKDIR /app

# Copie os arquivos de código e requisitos para o diretório de trabalho
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 5000 para acessar o aplicativo Flask
EXPOSE 5050

# Comando para executar a aplicação Flask
CMD ["python", "app.py"]

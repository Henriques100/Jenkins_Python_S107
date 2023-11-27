# Use a imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Adicionar um grupo com GID 1000
RUN addgroup --gid 1000 mygroup

# Adicionar um usuário com UID 1000 e pertencente ao grupo criado
RUN useradd -m -s /bin/bash -u 1000 -g 1000 jenkins

# Instale as dependências do sistema
RUN apt-get update && \
    apt-get install -y git

# Clone o repositório do GitHub
RUN git clone https://github.com/pallets/flask.git /app/flask

# Instala as dependências do Flask a partir de todos os arquivos .txt no diretório requirements
RUN find /app/flask/requirements -name "*.txt" -exec pip install -r {} \;

# Exponha a porta 5000 para acessar o aplicativo Flask
EXPOSE 5000

# Comando para iniciar o aplicativo Flask
CMD ["python"]

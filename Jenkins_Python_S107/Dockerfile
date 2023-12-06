# Use a imagem base do Jenkins
FROM jenkins/jenkins:latest

# Defina o usuário root temporariamente para instalar dependências
USER root

# Instale as dependências do sistema e o Python 3
RUN apt-get update && \
    apt-get install -y wget build-essential libssl-dev libffi-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev git python3 python3-venv

# Adicione um grupo com GID 1000 (caso não exista)
RUN addgroup --gid 1000 mygroup || true

# Adicione um usuário com UID 1000 e pertencente ao grupo criado
RUN id -u jenkins &>/dev/null || useradd -m -s /bin/bash -u 1000 -g 1000 jenkins

# Clone o repositório do GitHub
WORKDIR /app
RUN git clone https://github.com/pallets/flask.git .

# Crie o ambiente virtual e instale as dependências
RUN python3 -m venv venv && \
    venv/bin/pip install -U pip && \
    venv/bin/pip install -r requirements/dev.txt && \
    venv/bin/pip install -e .

# Crie o diretório de cache e ajuste as permissões
RUN mkdir -p /app/.pytest_cache && \
    chown -R jenkins: /app/.pytest_cache && \
    chmod -R 777 /app/.pytest_cache

# Execute os testes como o usuário jenkins
CMD ["tail", "-f", "/dev/null"]

# Exponha a porta 5000 para acessar o aplicativo Flask
EXPOSE 50000

USER jenkins

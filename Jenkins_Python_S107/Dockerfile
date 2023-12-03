# Use a imagem base do Jenkins
FROM jenkins/jenkins:latest

# Defina o usuário root temporariamente para instalar dependências
USER root

# Instale as dependências do sistema
RUN apt-get update && \
    apt-get install -y wget build-essential libssl-dev libffi-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev git

# Faça o download e instale o Python
RUN wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz && \
    tar xzf Python-3.9.7.tgz && \
    cd Python-3.9.7 && \
    ./configure --enable-optimizations && \
    make -j 8 && \
    make install && \
    cd .. && \
    rm -rf Python-3.9.7.tgz Python-3.9.7

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
CMD ["venv/bin/pytest", "tests"]

# Exponha a porta 5000 para acessar o aplicativo Flask
EXPOSE 5000

USER jenkins

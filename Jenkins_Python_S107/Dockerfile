# Usa a imagem oficial do Jenkins juntamente com a versão do python 3
FROM jenkins/jenkins:lts-jdk11
# Define o diretório de trabalho como /app
USER root

# Copia o conteúdo atual para o diretório de trabalho (/app) no contêiner
RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Itera sobre os arquivos de texto na pasta requirements e instala as dependências
USER jenkins
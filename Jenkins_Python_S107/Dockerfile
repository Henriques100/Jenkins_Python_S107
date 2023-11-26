# Define nossa imagem base
FROM jenkins/jenkins

# Define nosso usuário dentro do container
USER root

# Executa comandos para instalar o Python, o pip e outras dependências
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

# Cria um diretório /flask no contêiner e define como diretório de trabalho
WORKDIR /flask

# Copia os arquivos de aplicação para o diretório de trabalho
COPY . /flask

# Instala as dependências do Flask
RUN for req in $(ls requirements/*.txt); do pip3 install -r $req; done

# Cria um ambiente virtual e ativa-o
RUN python3 -m venv venv
RUN . venv/bin/activate

# Instala o pytest dentro do ambiente virtual
RUN venv/bin/pip3 install pytest

# Ajusta as permissões do diretório .pytest_cache
RUN mkdir -p /flask/.pytest_cache && chown -R jenkins:jenkins /flask/.pytest_cache

# Executa os testes (substitua o comando pelo comando real que você usa para rodar seus testes)
CMD ["venv/bin/python3", "-m", "pytest", "pip-compile-multi"]

# Cria o diretório /opt/npm
RUN mkdir -p /opt/npm

# Ajusta as permissões do diretório /opt/npm
RUN chown -R jenkins:jenkins /opt/npm

# Instalando mailutils (opcional, se necessário)
RUN apt-get install -y mailutils

# Limpa arquivos baixados com apt-get
RUN apt-get clean

# Define o usuário como jenkins
USER jenkins

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

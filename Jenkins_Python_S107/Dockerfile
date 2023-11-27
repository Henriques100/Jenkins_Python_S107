# Define nossa imagem base
FROM python:3.9-slim

# Define nosso usuário dentro do container
USER root

# Instala o Git
RUN apt-get update && apt-get install -y git

# Define o diretório de trabalho
WORKDIR /app

# Clona o repositório do Flask
RUN git clone https://github.com/pallets/flask.git .

# Instala as dependências do Flask
RUN pip install --upgrade pip && pip install .

# Exponha a porta que a aplicação Flask estará escutando
EXPOSE 5000

# Comando para iniciar a aplicação quando o contêiner for iniciado
CMD ["flask", "run", "--host=0.0.0.0"]


# Instalando mailutils (opcional, se necessário)
RUN apt-get install -y mailutils

# Limpa arquivos baixados com apt-get
RUN apt-get clean

# Define o usuário como jenkins
USER jenkins

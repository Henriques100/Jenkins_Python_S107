# Usa a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho como /app
WORKDIR /flask

# Copia o conteúdo atual para o diretório de trabalho (/app) no contêiner
COPY . /flask

# Itera sobre os arquivos de texto na pasta requirements e instala as dependências
RUN for file in flask/requirements/*; do pip3 install --no-cache-dir -r "$file"; done

# Expõe a porta 5000 para o mundo exterior
EXPOSE 5000

# Define o comando a ser executado no início do contêiner
CMD ["python", "run-tests.py"]

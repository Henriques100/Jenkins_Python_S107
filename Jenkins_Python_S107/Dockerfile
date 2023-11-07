# Define a imagem base
FROM python:3.9

# Copia o conteúdo da pasta flask para o contêiner
COPY Jenkins_Python_S107/flask /app

# Define o diretório de trabalho
WORKDIR /app

# Instala as dependências
COPY Jenkins_Python_S107/flask/requirements /app/requirements
RUN for file in requirements/*; do pip install --no-cache-dir -r "$file"; done

# Expõe a porta 5000
EXPOSE 5000

# Executa o aplicativo Python
CMD ["python", "app.py"]

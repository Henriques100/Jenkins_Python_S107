# Define nossa imagem base
FROM python:3.9

# Copie o conteúdo da pasta flask para o contêiner
COPY Jenkins_Python_S107/flask /app

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências
COPY Jenkins_Python_S107/flask/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 5000
EXPOSE 5000

# Execute o aplicativo Python
CMD ["python", "app.py"]

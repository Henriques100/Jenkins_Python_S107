# Estágio 1: Construção e instalação de dependências
FROM python:3.8-slim-buster AS builder

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt /app/

# Instale as dependências especificadas no requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copie o restante do código fonte para o contêiner
COPY . /app/

# Estágio 2: Execução do aplicativo Flask
FROM builder AS final

# Exponha a porta 5050 para acessar o aplicativo Flask
EXPOSE 5050

# Defina as variáveis de ambiente
ENV FLASK_APP=appFlask.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Execute o aplicativo Flask quando o contêiner for iniciado
CMD ["flask", "run", "--host=0.0.0.0", "--port=5050", "--without-threads", "--reload", "--no-debugger", "--no-reload", "--production"]

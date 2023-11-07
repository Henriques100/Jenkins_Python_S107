# Define nossa imagem base
FROM jenkins/jenkins:lts-jdk11

# Evitar travamento de compilação devido ao prompt do usuário
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

# Criar e ativar ambiente virtual
# Usando o nome da pasta final para evitar problemas de caminho com os pacotes
RUN python3.9 -m venv /home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"

# Instalar requisitos
COPY requirements /app/requirements
WORKDIR /app
RUN pip3 install --no-cache-dir wheel
RUN for file in requirements/*; do pip3 install --no-cache-dir -r "$file"; done

# Expor a porta necessária
EXPOSE 5000

# Garantir que todas as mensagens sempre cheguem ao console
ENV PYTHONUNBUFFERED=1

# Ativar ambiente virtual
ENV VIRTUAL_ENV=/home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"

# /dev/shm é mapeado para memória compartilhada e deve ser usado para o heartbeat do gunicorn
# Isso melhorará o desempenho e evitará travamentos aleatórios
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "-k", "gevent", "--worker-tmp-dir", "/dev/shm", "app:app"]

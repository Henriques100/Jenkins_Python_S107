# Use the Jenkins LTS (Long Term Support) image
FROM jenkins/jenkins:lts

# Switch to root user to install dependencies
USER root

# Install necessary packages
RUN apt-get update && \
    apt-get install -y wget build-essential libssl-dev libffi-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev git python3 python3-venv

# Create a Jenkins user
RUN addgroup --gid 1000 mygroup || true && \
    id -u jenkins &>/dev/null || useradd -m -s /bin/bash -u 1000 -g 1000 jenkins

# Set the working directory
WORKDIR /app

# Clone the GitHub repository
RUN git clone https://github.com/pallets/flask.git .

# Create a virtual environment and install dependencies
RUN python3 -m venv venv && \
    venv/bin/pip install -U pip && \
    venv/bin/pip install -r requirements/dev.txt

# Copy the requirements.txt file for the application
COPY ./aplicacao/requirements.txt /app/aplicacao/requirements.txt

# Install application dependencies
RUN venv/bin/pip install -r /app/aplicacao/requirements.txt

# Create a cache directory and adjust permissions
RUN mkdir -p /app/.pytest_cache && \
    chown -R jenkins: /app/.pytest_cache && \
    chmod -R 777 /app/.pytest_cache

# Copy the Flask application
COPY ./aplicacao/appFlask.py /app/appFlask.py

# Switch back to the Jenkins user
USER jenkins

# Set the command to run the Flask application
CMD ["venv/bin/python", "/app/appFlask.py"]

# Expose port 5000 for Flask
EXPOSE 5000

#!/bin/bash

set -e  # Aborta o script em caso de erro

# Exibe o conteúdo do diretório atual
echo "Conteúdo do diretório atual:"
ls

# Muda para o diretório do projeto
cd JENKINS_PYTHON_S107

# Exibe o conteúdo do diretório do projeto
echo -e "\nConteúdo do diretório do projeto:"
ls

# Mensagem informativa sobre a instalação das dependências do Python
echo -e "\nInstalando as dependências do Python..."

# Constrói a imagem Docker usando o Dockerfile
docker build -t S107:latest .

# Configuração do ambiente virtual
docker run --rm -v "$(pwd):/flask" S107:latest python -m venv venv
docker run --rm -v "$(pwd):/flask" S107:latest . venv/bin/activate

# Instalação das dependências dos arquivos de requirements na pasta 'requirements'
for file in flask/requirements/*; do
    if [ -f "$file" ]; then
        docker run --rm -v "$(pwd):/flask" S107:latest pip install -r "$file"
    fi
done

# Comandos específicos do seu aplicativo, como migrações de banco de dados, etc.

# Notificações
echo -e "\nEnviando e-mail com mail do Linux"
echo "Enviando e-mail com mail do Linux" | mail -s "um assunto" ${EMAIL_LIST}

echo -e "\nFim da instalação"

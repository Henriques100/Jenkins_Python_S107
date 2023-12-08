#!/bin/bash

set -e  # Aborta o script em caso de erro

# Caminho do projeto
PROJECT_DIR=$(pwd)/JENKINS_PYTHON_S107

# Exibe o conteúdo do diretório atual
echo "Conteúdo do diretório atual:"
ls

# Exibe o conteúdo do diretório do projeto
echo -e "\nConteúdo do diretório do projeto:"
ls "$PROJECT_DIR"

# Mensagem informativa sobre a instalação das dependências do Python
echo -e "\nConfigurando ambiente virtual e instalando dependências..."

# Construir a aplicação Flask
docker build -t flask-app -f "$PROJECT_DIR/Dockerfile" "$PROJECT_DIR/aplicacao"

# Etapa 'Build'
echo -e "\nExecutando a etapa 'Build'..."
# Adicione aqui comandos específicos para a etapa de construção, se necessário

# Etapa 'Test'
echo -e "\nExecutando a etapa 'Test'..."
testResult=$(docker run -it --rm flask-app pytest tests)
echo "Resultado dos testes: $testResult"
currentBuildResult=$(if [ "$testResult" == "FAILED" ]; then echo "FAILURE"; else echo "SUCCESS"; fi)

# Etapa 'Notifications'
echo -e "\nExecutando a etapa 'Notifications'..."
echo 'Notificação'
echo 'Enviando e-mail para luca.felipe@ges.inatel.br...'
echo 'Enviando mensagem para o canal Slack...'
# Adicione aqui comandos específicos para notificações, se necessário

# Atualiza o resultado do build no Jenkins
echo "Resultado final do build: $currentBuildResult"
# Este comando é específico para o TeamCity. Adapte conforme necessário.
echo "##teamcity[buildStatus status='$currentBuildResult' text='Build $currentBuildResult']"

echo -e "\nFim da instalação"

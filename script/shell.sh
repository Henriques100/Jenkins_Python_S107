ls
cd JENKINS_PYTHON_S107
ls
echo "Instalando as dependências do Python"
# Instalando dependências dos arquivos de requirements na pasta 'requirements'
for file in requirements/*; do
    if [ -f "$file" ]; then
        pip install -r "$file"
    fi
done

echo
sudo apt-get install mailutils
echo "Fim da instalação"
echo "Enviando e-mail com mail do Linux" | mail -s "um assunto" ${EMAIL_LIST}

ls
cd JENKINS_PYTHON_S107
ls
echo "Instalando as dependências do Python"
# 1 - Instalando um pacote específico:
sudo pip install nome_do_pacote
# 2 - Instalando uma versão específica de um pacote:
sudo pip install nome_do_pacote==versao_desejada
# 3 - Instalando a partir de um arquivo requirements.txt:
sudo pip install -r requirements.txt
# 4 - Criar ambiente virtual python:
sudo python -m venv nome_do_ambiente
# 4.1 - Criar ambiente virtual windows
sudo nome_do_ambiente\Scripts\activate
# 4.2 - Criar ambiente virtual macOS e Linux
sudo source nome_do_ambiente/bin/activate

echo
sudo 
sudo 

sudo apt-get install mailutils
echo "Fim da instalacao"
echo "Mandando e-mail com mail do linux" | mail -s "a subject" ${EMAIL_LIST}
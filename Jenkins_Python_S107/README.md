# Jenkins_Python_S107

Projeto de S107

O objetivo do projeto S107 é checar os testes do repositório do github https://github.com/pallets/flask.git e aqueles obtiverem sucesso são enviados para o MySQL e seu tempo de excução no Redis (Banco de dados de Memória).

O framework flask serve para construir aplicações webs.

Comando para construir os constainers: docker-compose -f .\docker-compose-jenkins.yaml build

Comando para executar os containers: docker-compose -f .\docker-compose-jenkins.yaml up
-- O container flask-app deve receber os testes de jenkins-python e inserir os dados ao MySQL e Redis
-- O container mysql-db deve receber os testes bem-sucedidos do jenkins-python
-- O container redis deve receber o tempo de execução de cada teste do jenkins-python
-- O container jenkins-python deve executar os testes presentes no repositório do Flask
 
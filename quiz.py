print('''
    ------------------------------------------------
    Seja bem-vindo ao jogo de perguntas e respostas.
      
    Você responderá 10 perguntas, e saberá o quanto 
    entende do assunto.  
    ------------------------------------------------    
      ''')
print(''' 
      ----------------------------------------
      Questão 1: Qual é a alma mais honesta do Brasil? 
      a) Flávio Dino
      b) Luiz Inácio Lula da Silva
      c) Fernando Henrique Cardoso(FHC)
      d) Fernando Collor de Mello
      e) Nenhuma das alternativas anteriores
      ----------------------------------------
      ''')
resposta = input('Digite uma das opções: ')
pontos = 0

if resposta == 'a' or resposta == 'c' or resposta == 'd' or resposta == 'e':
    print('Errou!')
    pontos += 0
else:
    print('Acertou!') 
    pontos += 10     
    
print(''' 
      ----------------------------------------
      Questão 2: Qual o motivo que o EUA roubou metade do território do México? 
      a) Raça Caucasiana
      b) Ameríndios
      c) Negros
      d) Mulatos
      e) Nenhuma das alternativas anteriores
      ----------------------------------------
      ''')    
resposta = input('Digite uma das opções: ')

if resposta == 'a':
    print('Acertou!')
    pontos += 10
else:
    print('Errou!') 
    pontos += 0  

print(''' 
      ----------------------------------------
      Questão 3: Qual dos países não pertencem à Ásia?
      a) Maldivas
      b) Moldávia
      c) EUA
      d) Barbados
      e) Nenhuma das alternativas anteriores
      ----------------------------------------
      ''')    
resposta = input('Digite uma das opções: ')

if resposta == 'a':
    print('Acertou!')
    pontos += 10
else:
    print('Errou!') 
    pontos += 0  
    
print(''' 
      ----------------------------------------
      Questão 4: De quem é a famosa frase “Penso, logo existo”?
      a) Platão
      b) Galileu Galilei
      c) Descartes
      d) Sócrates
      e) Francis Bacon
      ----------------------------------------
      ''')        
resposta = input('Digite uma das opções: ')

if resposta == 'c':
    print('Acertou!')
    pontos += 10
else:
    print('Errou!') 
    pontos += 0  
    
print(''' 
      ----------------------------------------
      Questão 5: De onde é a invenção do chuveiro elétrico?
      a) França
      b) Inglaterra
      c) Brasil
      d) Austrália
      e) Itália
      ----------------------------------------
      ''')        
resposta = input('Digite uma das opções: ')

if resposta == 'c':
    print('Acertou!')
    pontos += 10
else:
    print('Errou!') 
    pontos += 0      
    
print(''' 
      ----------------------------------------
      Questão 6: Quais são os três predadores do 
      reino animal reconhecidos pela habilidade 
      de caçar em grupo, se camuflar para surpreender 
      as presas e possuir sentidos apurados, respectivamente:
      a) Tubarão branco, crocodilo e sucuri
      b) Tigre, gavião e orca
      c) Leão, tubarão branco e urso cinzento
      d) hiena, urso branco e lobo cinzento
      e) Orca, onça e tarântula
      ----------------------------------------
      ''')        
resposta = input('Digite uma das opções: ')

if resposta == 'd':
    print('Acertou!')
    pontos += 10
else:
    print('Errou!') 
    pontos += 0      

print(''' 
      ----------------------------------------
      Questão 7: Qual a altura da rede de vôlei
      nos jogos masculino e feminino?
      a) 2,4 para ambos
      b) 2,5 m e 2,0 m
      c) 1,8 m e 1,5 m
      d) 2,45 m e 2,15 m
      e) 2,43 m e 2,24 m
      ----------------------------------------
      ''')        
resposta = input('Digite uma das opções: ')

if resposta == 'e':
    print('Acertou!')
    pontos += 10
else:
    print('Errou!') 
    pontos += 0        
    
print(''' 
      ----------------------------------------
      Questão 8: Qual das alternativas abaixo 
      apenas contêm classes de palavras?
      a) Vogais, semivogais e consoantes
      b) Artigo, verbo transitivo e verbo intransitivo
      c) Fonologia, Morfologia e Sintaxe
      d) Substantivo, verbo e preposição
      e) Hiatos, ditongos e tritongos
      ----------------------------------------
      ''')        
resposta = input('Digite uma das opções: ')

if resposta == 'd':
    print('Acertou!')
    pontos += 10
else:
    print('Errou!') 
    pontos += 0          

print(''' 
      ----------------------------------------
      Questão 9: “It is six twenty" ou "twenty 
      past six”. Que horas são em inglês?
      a) 12:06
      b) 6:20
      c) 2:20
      d) 6:02
      e) 12:20
      ----------------------------------------
      ''')        
resposta = input('Digite uma das opções: ')

if resposta == 'b':
    print('Acertou!')
    pontos += 10
else:
    print('Errou!') 
    pontos += 0      

print(''' 
      ----------------------------------------
      Questão 10: Uma alíquota é...
      a) a altura de um sólido geométrico
      b) a medida da base de um retângulo
      c) a metade do valor de uma taxa
      d) um percentual com que um tributo incide
        sobre o valor do objeto tributado
      e) uma fórmula inventada pelo matemático Pitágoras
      ----------------------------------------
      ''')        
resposta = input('Digite uma das opções: ')

if resposta == 'd':
    print('Acertou!')
    pontos += 10
else:
    print('Errou!') 
    pontos += 0       
    
print('Sua pontuação final é: ', pontos)         

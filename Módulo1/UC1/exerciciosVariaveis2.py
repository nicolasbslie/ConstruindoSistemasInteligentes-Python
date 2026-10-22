#Exercício 12
print("12 + 3") #12 + 3
print(12 + 3) #15
print("Resultado:", 12 + 3) #Resultado: 15
print("12", "3") #12 3

#Exercício 13
nome = "Robótica para iniciantes"
sala = "Laboratório 2"
vagas = 24
duracaoHoras = 2.5
inscricoesAbertas = True

print(f"===== AULA =====\nNome: {nome}. Tipo: {type(nome)}\nSala: {sala}. Tipo: {type(sala)}\nVagas: {vagas}. Tipo: {type(vagas)}\nDuração em horas: {duracaoHoras} horas. Tipo: {type(duracaoHoras)}\nInscrições abertas: {inscricoesAbertas}. Tipo: {type(inscricoesAbertas)}")

""" Str = string, que significa que é um texto
Int = inteiro, que significa que é um número inteiro
Float = Float, que siginifica que é um número com virgula
Bool = Booleano, que significa Verdadeiro ou Falso """

#Exercício 14
precoPizza = 48.0
precoBebida = 12.0
amigos = 4
total = precoBebida + precoPizza
totalPorPessoa = total / amigos
print(f"===== CONTA =====\nTotal: {total}\nPreço por pessoa: {totalPorPessoa}, {type(totalPorPessoa)}")

#Exercício 15
livros_disponiveis = 40
print(f"===== BIBLIOTECA =====\nLivros inicias: {livros_disponiveis}") #40
livros_disponiveis += 12
print(f"Recebimento de 12 livros, total: {livros_disponiveis}") #52
livros_disponiveis -= 9
print(f"Empréstimo de 9 livros, total: {livros_disponiveis}") #43
livros_disponiveis += 4
print(f"Devolução de 4 livros, total: {livros_disponiveis}") #47
livros_disponiveis -= 6
print(f"Empréstimos de 6 livros, total: {livros_disponiveis}") #41

#Exercício 16
aluno = "Timóteo"
nota1 = 7.5
nota2 = 8.0
nota3 = 9.5
somaNotas = (nota1 + nota2 + nota3) / 3
print(f"===== NOTA ALUNO =====\nNome: {aluno}\nMédia: {somaNotas}")
nota2 = 6.5
somaNotas = (nota1 + nota2 + nota3) / 3
print(f"===== NOTA ALUNO =====\nNome: {aluno}\nMédia: {somaNotas}")

#Exercício 17
nome_curso = "Python básico" #Antes estava "nome curso"
mensalidade = 89.90
matricula_ativa = True #Antes estava "true"

print("Curso:", nome_curso)
print("Mensalidade:", mensalidade, type(mensalidade)) #Antes estava "Mensalidade"
print("Matrícula ativa:", matricula_ativa)

#Exercício 18
saldo = 80
saldo_anterior = saldo

saldo = saldo - 25
saldo = saldo + 10

print("Saldo anterior:", saldo_anterior) #80
print("Saldo atual:", saldo) #65
#Porque saldo_anterior recebeu somente o valor do primeiro saldo, e não das alterações futuras
saldo += 15
print("Saldo anterior:", saldo_anterior) 
print("Saldo atual:", saldo) 

#Exercício 19
alunos = 20
onibus = 600.00
ingresso = 15.00
lanche = 10.00
valorIngressos = alunos * ingresso
valorLanches = alunos * lanche
total = onibus + valorIngressos + valorLanches
valorPorAluno = total / alunos
print(f"===== PASSEIO ESCOLAR =====\nAlunos: {alunos}\nValor do ônibus: R${onibus}\nValor total dos ingressos: R${valorIngressos}\nValor total dos lanches: R${valorLanches}\nValor total: R${total}\nValor por aluno: R${valorPorAluno}")
alunos = 25
valorIngressos = alunos * ingresso
valorLanches = alunos * lanche
total = onibus + valorIngressos + valorLanches
valorPorAluno = total / alunos
print(f"===== PASSEIO ESCOLAR =====\nAlunos: {alunos}\nValor do ônibus: R${onibus}\nValor total dos ingressos: R${valorIngressos}\nValor total dos lanches: R${valorLanches}\nValor total: R${total}\nValor por aluno: R${valorPorAluno}")

#Exercício 20
informacao = "42"
print(type(informacao))
informacao = 42
print(type(informacao))
informacao = 42.0
print(type(informacao))
informacao = False
print(type(informacao))

""" 42 é inteiro e "42" é um texto, se somar o "42 vai concatenar"
A varável guarda somente o último valor atribuído """

#Exercício 21 - Desafio
nomeRobo = "Atlas"
energia = 100
distanciaPercorrida = 0
amostras = 0
missaEmAndamento = True
print(f"===============================================\n        INFORMAÇÃO             |  Valor Inicial\nEnergia                        |{energia}\nDistância percorrida, em metros|{distanciaPercorrida}\nAmostras coletadas             |{amostras}\nMissão em andamento            |{missaEmAndamento}")

print("O robô percorreu 120 metros, mas isso consumiu 20 pontos de energia.")
energia -= 20
distanciaPercorrida += 120
print("O robô coleta 3 amostras novas, mas isso consumiu 15 pontos de energia.")
energia -= 15
amostras += 3
print("O robô recarregou 10 pontos de energia.")
energia += 10
print("O robô percorre mais 80 metros e isso consumiu mais 25 pontos de energia.")
distanciaPercorrida +=80
energia -= 25
print("O robô coleta mais 2 amostras e isso consumiu mais 10 pontos de energia.")
amostras += 2
energia -= 10
print("O robô terminou sua missão!")
missaEmAndamento = False

#Parte extra
distancia_total = 120 + 80
distancia_media = distancia_total / 4

print(f"===============================================\n        INFORMAÇÃO             |  Valor Final\nEnergia                        |{energia}\nDistância percorrida, em metros|{distanciaPercorrida}\nAmostras coletadas             |{amostras}\nDistância média                |{distancia_media} metros por minuto\nMissão em andamento            |{missaEmAndamento}")
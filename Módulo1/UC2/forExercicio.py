#Exercício 1
""" numero = int(input("Digite um número: "))

if numero > 0:
    for numero in range(1, numero + 1):
        print(numero)
else:
    print("Valor inválido") """

#Exercício 2
""" numero = int(input("Digite um número: "))

if numero > 0:
    for numero in range(numero, -1, -1):
        print(numero)
        continue
    print("Lançamento realizado!")
else:
    print("Valor inválido") """

#Exercício 3
""" limite = int(input("Digite um número inteiro: "))

if limite <= 0:
    print("Limite inválido.")
elif limite == 1:
    print("Não há pares no intervalo.")
else:
    for numero in range(2, limite + 1, 2):
        print(numero) """

#Exercício 4
""" numero = int(input("Digite um número inteiro: "))

for i in range(1, 11):
    resultado = numero * i

    print(numero, "x", i, "=", resultado) """

#Exercício 5
""" soma = 0
positivos = 0

for i in range(1, 7):
    numero = int(input("Digite um número inteiro: "))

    soma = soma + numero

    if numero > 0:
        positivos = positivos + 1

print("Soma dos números:", soma)
print("Quantidade de positivos:", positivos) """

#Exercício 6
""" quantidade = int(input("Quantidade de alunos: "))

if quantidade <= 0:
    print("Quantidade inválida.")

else:
    soma = 0
    aprovados = 0

    for i in range(1, quantidade + 1):
        nota = float(input("Digite a nota do aluno: "))

        while nota < 0 or nota > 10:
            print("Nota inválida! Digite uma nota de 0 a 10.")
            nota = float(input("Digite a nota do aluno: "))

        soma = soma + nota

        if nota >= 7:
            aprovados = aprovados + 1

    media = soma / quantidade

    print("Média da turma:", media)
    print("Alunos com nota a partir de 7:", aprovados) """

#Exercício 7
""" palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

contador = 0

for caractere in palavra:
    if caractere == letra:
        contador = contador + 1

print("A letra aparece", contador, "vezes.") """

#Exercício 8
""" codigo_correto = "ROBO123"
acertou = False

for tentativa in range(1, 4):
    print("Tentativa", tentativa)

    codigo = input("Digite o código: ")

    if codigo == codigo_correto:
        print("Código correto! Acesso permitido.")
        acertou = True

        break

    else:
        print("Código incorreto.")

if acertou == False:
    print("As tentativas acabaram.") """

#Desafio
energia = 100
pontuacao_total = 0
missoes_realizadas = 0

for missao in range(1, 6):

    if energia < 25:
        print("Energia insuficiente")
        break

    pontuacao = int(input(f"Pontuação da missão {missao} (0 a 100): "))

    while pontuacao < 0 or pontuacao > 100:
        print("Pontuação inválida! Digite entre 0 e 100.")
        pontuacao = int(input(f"Pontuação da missão {missao} (0 a 100): "))

    energia -= 25

    pontuacao_total += pontuacao

    missoes_realizadas += 1

print("\n--- RELATÓRIO DE MISSÕES ---")
print(f"Missões realizadas: {missoes_realizadas}")
print(f"Pontuação total: {pontuacao_total}")

if missoes_realizadas > 0:
    media = pontuacao_total / missoes_realizadas
    print(f"Média de pontos: {media}")
else:
    print("Não foi possível calcular a média.")

print(f"Energia restante: {energia}")
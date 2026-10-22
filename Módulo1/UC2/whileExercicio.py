#Exercício 1
""" numero = int(input("Digite um número: "))
contagem = 0
while contagem < numero:
    contagem += 1
    print(contagem) """

#Exercício 2
""" numero = int(input("Digite um número inteiro: "))
contagem = numero + 1

while contagem > 0:
    contagem -= 1
    print(contagem)

print("Lançamento realizado!") """

#Exercício 3
""" numero = int(input("Digite um número para descobrir sua tabuada de 1 a 10: "))
multiplicado = numero
multiplicador = 1

while multiplicador <= 10:
    numero = multiplicado * multiplicador
    print(numero)
    multiplicador += 1 """

#Exercício 4
""" contador = 0
soma = 0

while contador < 5:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1

print("Soma dos números:", soma) """

#Exercício 5
""" alunos = int(input("Quantos alunos tem a turma? "))
contador = 0
media = 0

while contador < alunos:
    if alunos > 0:
        nota = float(input("Digite a média de um aluno: "))
        media += nota

        mediaTurma = media / alunos
        contador += 1
    else:
        print("Alunos inválidos")

print("Média da turma:", mediaTurma) """

#Exercício 6
""" while True:
    nota = float(input("Qual a nota? "))
    if nota > 0:
        print("Nota registrada com sucesso!")
        break
    else:
        print("Nota inválida! Tente novamente") """

#Exercício 7
""" while True:
    print("=== MENU ===")
    print("1 - Somar dois números")
    print("2 - Verificar maioridade")
    print("0 - Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f"{num1} + {num2} = {soma}")
    elif opcao == 2:
        idade = int(input("Qual a sua idade? "))
        if idade >= 18:
            print("É maior de idade, pode entrar")
        else:
            print("Menor de idade, não pode entrar")
    elif opcao == 0:
        print("Saindo...")
        break
    else: 
        print("Opção inválida") """

#Desafio
saldo = 0
while True:
    print("=== CAIXA ELETRÔNICO ===\n1 - Consultar saldo\n2 - Depositar dinheiro\n3 - Sacar dinheiro\n0 - Sair")
    opcao = int(input("Qual opção você deseja? "))
    if opcao == 1:
        print(f"O saldo da sua conta é de: R${saldo}")
    elif opcao == 2:
        deposito = int(input("Qual valor deseja depositar? "))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito realizado, saldo atual R${saldo}")
        else:
            print("Erro ao depositar")
    elif opcao == 3:
        saque = int(input("Qual valor deseja sacar? "))
        if saque > 0 and saque <= saldo:
            saldo -= saque
            print(f"Saque realizado com sucesso, saldo atual R${saldo}")
        else:
            print("Erro ao sacar")
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida")
#Exercício 1
""" nome = input("Qual o seu nome? ")
cidade = input("Qual a sua cidade? ")
idade = int(input("Qual a sua idade? "))
print(f"===== CADASTRO =====\nNome: {nome}\nCidade: {cidade}\nIdade ano que vem: {idade + 1}") """

#Exercício 2
""" preco = float(input("Qual o preço do produto? "))
quantidade = int(input("Qual a quantidade do produto? "))
total = preco * quantidade
desconto = 0
print(f"===== PRODUTO COM DESCONTO =====\nValor total: R${total}")
if total >= 50:
    desconto = total * 0.1
    total = total - desconto
    print(f"Desconto: R${desconto}\nPreço com desconto: {total}") """

#Exercício 3
""" num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O {num1} é maior que {num2}")
elif num2 > num1:
    print(f"O {num2} é maior que {num1}")
else:
    print(f"O {num1} é igual a {num2}") """

#Exercício 4
""" temperatura = float(input("Digite a temperatura: "))
if temperatura < 18:
    print("Ambiente frio")
elif temperatura >= 18 and temperatura < 26:
    print("Ambiente agradável")
else:
    print("Ambiente quente") """

#Exercício 5
""" nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a nota: "))
media = (nota1 + nota2) / 2

if nota1 >=0 and nota1 <= 10 and nota2 >=0 and nota2 <= 10:
    if media >= 7:
        print("Aprovado")
    elif media >=5 and media <= 7:
        print("Recuperação")
    else:
        print("Reprovado")
else:
    print("Nota inválida") """

#Exercício 6
""" idade = int(input("Qual a sua idade? "))
inscricao = input("Você possui inscrição? (s/n)").lower()

if idade >= 0:
    if idade >= 14 and inscricao in "s":
        print("Entrada permitida")
    elif idade >= 14 and inscricao in "n":
        print("Entrada proibida por não ter inscrição")
    elif idade < 14 and inscricao in "s":
        print("Entrada proibida por não ter idade")
    else:
        print("Entrada proibida por não ter idade e inscrição")
else:
    print("Idade inválida") """

#Exercício 7
""" idade = int(input("Qual a sua idade? "))

if idade >= 0:
    if idade < 12 or idade >= 60:
        print("Entrada gratuita")
    else:
        print("Entrada cobrada, valor R$20,00")
else:
    print("Idade inválida") """

#Exercício 8
""" exemplares = 8
retirada = int(input("Quantos exemplares deseja retirar? "))

if retirada >= 0:
    if retirada > exemplares:
        print("Impossível fazer retirada, não há exemplares suficientes")
    else:
        exemplares = exemplares - retirada
        print(f"Pedido confirmado. Exemplares restantes: {exemplares}")
else:
    print("Pedido inválido") """

#Exercício 9
""" num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("===== CALCULADORA =====\nDigite a operação que deseja:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
operacao = int(input("Qual a operação deseja fazer? "))

if operacao >= 1 and operacao <= 4:
    if operacao == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacao == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operacao == 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operacao == 4:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Opção Inválida") """

#Exercício 10
""" idade = int(input("Idade: "))
autorizacao = input("Possui autorização? (sim/nao): ")

if idade >= 16 and autorizacao == "sim":
    print("Participação permitida.")
else:
    print("Participação não permitida.") """

#Desafio Extra
nome = input("Digite o nome do aventureiro: ")
ouro = int(input(f"Digite a quantidade de ouro do(a) {nome}: "))

if ouro < 0:
    print("Quantidade de ouro inválida")
else:
    print("\n===== LOJA DO AVENTUREIRO =====")
    print("1 - Poção de vida: 25 moedas")
    print("2 - Escudo: 60 moedas")
    print("3 - Espada: 100 moedas")

    opcao = input("Escolha um item: ")

    if opcao == "1":
        item = "Poção de vida"
        preco = 25
    elif opcao == "2":
        item = "Escudo"
        preco = 60
    elif opcao == "3":
        item = "Espada"
        preco = 100
    else:
        print("Item inválido")
        preco = 0

    if preco > 0:
        if ouro >= preco:
            ouro = ouro - preco

            print("\n===== COMPRA CONFIRMADA =====")
            print(f"Aventureiro: {nome}")
            print(f"Item adquirido: {item}")
            print(f"Saldo restante: {ouro} moedas")
        else:
            faltam = preco - ouro
            print(f"Saldo insuficiente! Faltam {faltam} moedas.")
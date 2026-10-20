#Exercício 1
""" horas = int(input("Quantas horas você ficou estacionado? "))
valor = 0

if horas > 0:
    if horas < 2:
        valor = 10
        print(f"Total a pagar: R${valor}")
    elif horas >= 2 and horas < 5:
        valor = 20
        print(f"Total a pagar: R${valor}")
    else:
        valor = 30
        print(f"Total a pagar: R${valor}")
else:
    print("Valor incorreto") """

#Exercício 2
""" nivel = int(input("Qual o nível do seu personagem? "))

if nivel > 0:
    if nivel >= 1 and nivel <= 5:
        print("Classificação: Aprendiz")
    elif nivel >= 6 and nivel <= 15:
        print("Classificação: Guerreiro")
    elif nivel >= 16 and nivel <= 30:
        print("Classificação: Veterano")
    else:
        print("Classificação: Lendário")
else:
    print("Valor inválido") """

#Exercício 3
""" usuario_correto = "admin"
senha_correta = "python123"
usuario = input("Qual o seu usuário? ")
senha = input("Qual a sua senha? ")

if usuario == usuario_correto and senha == senha_correta:
    print("Acesso autorizado")
elif usuario == usuario_correto and senha != senha_correta:
    print("Senha incorreta")
else:
    print("Usuário não encontrado")
 """
#Exercício 4
""" salario = float(input("Digite o salário mensal: R$ "))
valor = float(input("Digite o valor do empréstimo: R$ "))
parcelas = int(input("Digite a quantidade de parcelas: "))

valor_parcela = valor / parcelas if parcelas > 0 else 0

if salario < 2000:
    print("Empréstimo recusado: salário abaixo de R$ 2.000,00.")
elif valor > salario * 10:
    print("Empréstimo recusado: valor acima de 10 vezes o salário.")
elif parcelas < 1 or parcelas > 48:
    print("Empréstimo recusado: quantidade de parcelas inválida.")
elif valor_parcela > salario * 0.30:
    print("Empréstimo recusado: parcela acima de 30 por cento do salário.")
else:
    print("Empréstimo aprovado!")
    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
 """
#Exercício 5
""" nome = input("Nome do personagem: ")
vida = int(input("Vida atual: "))
ataque = int(input("Pontos de ataque: "))
vida_inimigo = int(input("Vida do inimigo: "))
defesa = int(input("Pontos de defesa do inimigo: "))

dano = ataque - defesa

if vida <= 0:
    print(f"{nome} não pode atacar, pois está sem vida.")
elif dano <= 0:
    print("O ataque não causou dano.")
else:
    vida_restante = vida_inimigo - dano

    if vida_restante <= 0:
        print("Inimigo derrotado!")
    else:
        print("O inimigo sobreviveu!")
        print(f"Vida restante do inimigo: {vida_restante}")
 """
#Exercício 6
""" idade = int(input("Digite sua idade: "))
matriculado = input("É aluno matriculado? (sim/nao): ").lower()
autorizacao = input("Possui autorização do professor? (sim/nao): ").lower()
disponivel = input("O laboratório está disponível? (sim/nao): ").lower()

if disponivel == "sim" and idade >= 16 and (matriculado == "sim" or autorizacao == "sim"):
    print("Acesso permitido!")
else:
    print("Acesso negado!") """

#Exercício 7
""" compra = float(input("Digite o valor da compra: R$ "))
regiao = input("Digite a região de entrega: ").lower()

if compra <= 0:
    print("Compra inválida.")
elif regiao != "sul" and regiao != "sudeste" and regiao != "centro-oeste" and regiao != "norte" and regiao != "nordeste":
    print("Região inválida.")
else:
    if compra >= 300:
        frete = 0
    elif regiao == "sul":
        frete = 15
    elif regiao == "sudeste":
        frete = 20
    elif regiao == "centro-oeste":
        frete = 25
    else:
        frete = 35

    total = compra + frete

    print(f"Valor da compra: R$ {compra:.2f}")
    print(f"Valor do frete: R$ {frete:.2f}")
    print(f"Valor total: R$ {total:.2f}") """

#Exercício 8
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")
else:
    print("Triângulo inválido.")

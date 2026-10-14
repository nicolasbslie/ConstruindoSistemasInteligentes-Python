#Input
nome = input("Qual é o seu nome? ")
print(f"Nome: {nome}")

#Convertendo String para Int e Float
idade = int(input("Qual a sua idade? "))
#idade = float(input("Qual a sua idade? "))
print(f"No próximo ano você terá {idade + 1} anos")

#If e else
if idade >= 18:
    print("Você já pode ser preso")
else:
    print("Você ainda não pode ser preso")

#Elif
temperatura = float(input("Temperatura: "))

if temperatura >= 35:
    print("Calor intenso.")
elif temperatura >= 30:
    print("Dia quente.")
else:
    print("Temperatura abaixo de 30 graus.")

#And
idade = int(input("Idade: "))
vagas = int(input("Vagas disponíveis: "))

if idade >= 14 and vagas > 0:
    print("Inscrição permitida.")
else:
    print("Inscrição não permitida.")

#Or
categoria = input("Categoria (estudante, professor ou visitante): ")

if categoria == "estudante" or categoria == "professor":
    print("Desconto disponível.")
else:
    print("Sem desconto.")

#Invertendo como se fosse != usa o not
resposta = input("O robô está em manutenção? (sim/nao): ")
em_manutencao = resposta == "sim"

if not em_manutencao:
    print("Robô disponível para uma missão.")
else:
    print("Aguarde o fim da manutenção.")
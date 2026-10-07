#Exercício 1
nome = "Nicolas"
cidade = "São Leopoldo"
idade = 16
tecnologia = "C#"

print(f"===== MEU PERFIL =====\nNome: {nome}\nCidade: {cidade}\nIdade: {idade}\nTecnolgia: {tecnologia}")

#Exercício 2
nome = "PS2"
preco = 300
quantidadeEstoque = 15
disponivel = True

print(f"===== PRODUTO =====\nNome: {nome}\nPreço: {preco}\nQuantidade no estoque: {quantidadeEstoque}\nDisponível: {disponivel}")

#Exercício 3
pontos = 250
pontos += 120
pontos -= 50
pontos += 30

print(f"===== PONTOS =====\nPontuação Final: {pontos}")

#Exercício 4
preco = 18.5
quantidade = 4
total = preco * quantidade

print(f"===== CARRINHO DE COMPRAS =====\nValor da compra: {total}")

#Exercício 5
horas = 7
print(f"===== CONVERSÃO DE HORAS =====\n{horas} equivalem a {horas * 60} minutos")

#Exercício 6
vida = 200
vida -= 45
vida -= 30
vida += 20

print(f"===== VIDA PERSONAGEM =====\nVida final: {vida}")

#Exercício 7
salario = 2800
bonus = 450
salario_final = salario + bonus

print(f"===== SÁLARIO =====\nSalário final: {salario_final}")

#Exercício 8
largura = 6
altura = 7
area = largura * altura

print(f"===== ÁREA TRIÂNGULO =====\nÁrea total: {area}")

#Exercício 9
titulo = "Python"
versao = 3
nota = 9.5
finalizado = False

print("===== TIPAGEM =====")
print(type(titulo))
print(type(versao))
print(type(nota))
print(type(finalizado))

#Exercício 10
nome = "Darth Vader"
classe = "Mestre Sith"
nivel = 100
vida = 200
ataque = 95
defesa = 90
possui_magia = True

poder_total = ataque + defesa

print(f"========================\n      PERSONAGEM      \n========================\nNome: {nome}\nClasse: {classe}\nNível: {nivel}\nVida: {vida}\nAtaque: {ataque}\nDefesa: {defesa}\nPoder total: {poder_total}\nPossui magia: {possui_magia}\n========================")

#Desafio Extra
nome = "Brás"
vida = 60
ouro = 300
nivel = 16

ouro += 50
vida -= 10
ouro -= 100
vida += 17
nivel += 4

print(f"===== EXTRA =====\nNome: {nome}\nVida: {vida}\nOuro: {ouro}\nNível: {nivel}")
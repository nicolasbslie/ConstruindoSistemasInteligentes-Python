#Exercício 1
""" objetos = ["Mouse", "Teclado", "Fone", "Monitor", "Mousepad"]
print(objetos)
print(len(objetos))
print(objetos[0])
print(objetos[-1]) """

#Exercício 2
""" nomes = []

for i in range(4):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("Números digitados:", nomes) """

#Exercício 3
""" numeros = []

for i in range(6):
    numero = int(input("Digite um número"))
    numeros.append(numero)

print("Lista:", numeros)
print("Soma:", sum(numeros))
print("Média:", sum(numeros) / len(numeros))
print("Maior valor:", max(numeros))
print("Menor valor:", min(numeros)) """

#Exercício 4
""" itens = ["corda", "água", "mapa", "água"]

busca = input("Digite o nome do item: ")

if busca in itens:
    print("O item existe na mochila.")
else:
    print("O item não existe na mochila.")

quantidade = itens.count(busca)

print("Quantidade de ocorrências:", quantidade) """

#Exercício 5
""" numeros = []
pares = []

for i in range(8):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print("Lista original:", numeros)
print("Números pares:", pares) """

#Exercício 6
""" nomes = ["Ana", "Bruno", "Ana", "Carla"]

nome = input("Digite o nome que deseja remover: ")

if nome in nomes:
    nomes.remove(nome)
    print("Primeira ocorrência removida.")
else:
    print("Nome não encontrado.")

print("Lista:", nomes)
print("Quantidade restante:", len(nomes)) """

#Exercício 7
""" notas = []

quantidade = int(input("Quantos alunos há na turma? "))

if quantidade <= 0:
    print("Quantidade de alunos inválida.")
else:
    for i in range(quantidade):
        nota = float(input("Digite a nota do aluno: "))

        while nota < 0 or nota > 10:
            print("Nota inválida! Digite uma nota de 0 a 10.")
            nota = float(input("Digite a nota novamente: "))

        notas.append(nota)

    print("Notas:", notas)
    print("Média:", sum(notas) / len(notas))
    print("Maior nota:", max(notas))
    print("Menor nota:", min(notas))

    aprovados = 0

    for nota in notas:
        if nota >= 7:
            aprovados += 1

    print("Notas iguais ou maiores que 7:", aprovados) """

#Exercício 8
""" fila = []

while True:
    print("\n1 - Adicionar pessoa ao final da fila")
    print("2 - Atender a primeira pessoa")
    print("3 - Mostrar a fila e sua quantidade")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da pessoa: ")
        fila.append(nome)
        print("Pessoa adicionada à fila.")
    elif opcao == "2":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print("Pessoa atendida:", atendido)
        else:
            print("A fila está vazia.")
    elif opcao == "3":
        print("Fila:", fila)
        print("Quantidade de pessoas:", len(fila))
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!") """

#Desafio extra
pontuacoes = []

while True:
    print("\n1 - Registrar pontuação")
    print("2 - Mostrar relatório")
    print("3 - Desfazer o último registro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pontuacao = int(input("Digite a pontuação (0 a 100): "))

        while pontuacao < 0 or pontuacao > 100:
            print("Pontuação inválida!")
            pontuacao = int(input("Digite novamente (0 a 100): "))

        pontuacoes.append(pontuacao)
        print("Pontuação registrada.")
    elif opcao == "2":
        if len(pontuacoes) == 0:
            print("Não há missões registradas.")
        else:
            print("Pontuações:", pontuacoes)
            print("Quantidade de missões:", len(pontuacoes))
            print("Total:", sum(pontuacoes))
            print("Média:", sum(pontuacoes) / len(pontuacoes))
            print("Maior pontuação:", max(pontuacoes))

            quantidade = 0

            for pontuacao in pontuacoes:
                if pontuacao >= 70:
                    quantidade += 1

            print("Missões com pelo menos 70 pontos:", quantidade)

            pontuacoes_altas = []

            for pontuacao in pontuacoes:
                if pontuacao >= 70:
                    pontuacoes_altas.append(pontuacao)

            print("Pontuações a partir de 70:", pontuacoes_altas)
    elif opcao == "3":
        if len(pontuacoes) > 0:
            removida = pontuacoes.pop()
            print("Pontuação removida:", removida)
        else:
            print("Não há registro para desfazer.")
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!")
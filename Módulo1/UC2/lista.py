
# 1. Criando listas
notas = [8.0, 6.5, 9.0, 7.5]
alunos = ["Ana", "Bruno", "Carla"]

# Mostrando as listas e a quantidade de elementos
print("Notas:", notas)
print("Quantidade de notas:", len(notas))


# 2. Acessando elementos pelos índices
# O primeiro índice é 0 e o -1 representa o último elemento
print("Primeira nota:", notas[0])
print("Última nota:", notas[-1])


# 3. Alterando um elemento da lista
notas[1] = 7.0
print("Notas alteradas:", notas)


# 4. Adicionando elementos
notas.append(9.5)       # Adiciona ao final
alunos.insert(1, "João") # Adiciona na posição 1

print("Notas:", notas)
print("Alunos:", alunos)


# 5. Removendo elementos
alunos.remove("Bruno")  # Remove pelo valor
ultima_nota = notas.pop() # Remove e retorna o último elemento

print("Alunos:", alunos)
print("Nota removida:", ultima_nota)


# 6. Procurando e contando valores
print("Ana está na lista?", "Ana" in alunos)
print("Quantidade de notas 7.0:", notas.count(7.0))


# 7. Percorrendo uma lista com for
for nota in notas:
    print("Nota:", nota)


# 8. Lendo valores e guardando em uma lista
numeros = []

for i in range(3):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("Números digitados:", numeros)


# 9. Calculando soma, média, maior e menor
if len(notas) > 0:
    print("Soma:", sum(notas))
    print("Média:", sum(notas) / len(notas))
    print("Maior nota:", max(notas))
    print("Menor nota:", min(notas))


# 10. Criando outra lista com valores positivos
valores = [5, -2, 0, 8, -1]
positivos = []

for valor in valores:
    if valor > 0:
        positivos.append(valor)

print("Valores positivos:", positivos)


# 11. Fatiamento: selecionando parte da lista
print("Primeiros dois números:", valores[:2])


# 12. Copiando uma lista
original = [10, 20, 30]
copia = original.copy()

copia[0] = 99

print("Lista original:", original)
print("Lista copiada:", copia)
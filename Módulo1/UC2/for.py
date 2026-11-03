# 1. ESTRUTURA BÁSICA DO FOR

# O for repete um bloco de código para cada valor do range()
# A variável numero recebe os valores de 1 até 5

for numero in range(1, 6):
    print(numero)


# 2. COMO USAR O RANGE()

# range(5) começa no 0 e vai até 4
for numero in range(5):
    print(numero)

# range(1, 6) começa no 1 e vai até 5
for numero in range(1, 6):
    print(numero)

# range(2, 11, 2) começa no 2 e aumenta de 2 em 2
for numero in range(2, 11, 2):
    print(numero)

# range(5, 0, -1) faz uma contagem regressiva
for numero in range(5, 0, -1):
    print(numero)


# 3. REPETIR UMA AÇÃO

# O range(3) faz o código repetir 3 vezes
for repeticao in range(3):
    print("Olá!")


# 4. CONTAR ATÉ UM NÚMERO DIGITADO PELO USUÁRIO

limite = int(input("Contar até: "))

# O limite + 1 permite incluir o número digitado
for numero in range(1, limite + 1):
    print(numero)


# 5. SOMAR NÚMEROS COM ACUMULADOR

# A variável soma guarda o total acumulado
soma = 0

for numero in range(1, 6):
    soma += numero  # Soma o número atual ao total

print("Soma:", soma)


# 6. PERCORRER UM TEXTO

palavra = "Python"

# A variável letra recebe um caractere por vez
for letra in palavra:
    print(letra)


# 7. BREAK E CONTINUE

# BREAK encerra o laço imediatamente
for numero in range(1, 6):
    if numero == 3:
        break  # Para quando numero for igual a 3

    print(numero)

# CONTINUE pula a repetição atual
for numero in range(1, 6):
    if numero == 3:
        continue  # Não mostra o número 3

    print(numero)


# 8. DIFERENÇA ENTRE FOR E WHILE

# FOR: usado quando sabemos quantas vezes queremos repetir
for numero in range(5):
    print(numero)

# WHILE: usado enquanto uma condição for verdadeira
contador = 0

while contador < 5:
    print(contador)
    contador += 1  # Aumenta o contador em 1
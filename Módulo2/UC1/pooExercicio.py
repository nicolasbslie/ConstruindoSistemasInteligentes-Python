#Exercício 1
""" class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

livro1 = Livro("Harry Potter", "J.K. Rowling", 300)
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96)

print("Livro 1:")
print(livro1.titulo, livro1.autor, livro1.paginas)

print("\nLivro 2:")
print(livro2.titulo, livro2.autor, livro2.paginas)
livro1.paginas = 350

print("\nDepois da alteração:")
print(livro1.titulo, livro1.autor, livro1.paginas)
print(livro2.titulo, livro2.autor, livro2.paginas) """

#Exercício 2
""" class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


retangulo1 = Retangulo(4, 3)
retangulo2 = Retangulo(5, 2)

print("Área do retângulo 1:", retangulo1.calcular_area())
print("Área do retângulo 2:", retangulo2.calcular_area()) """

#Exercício 3
""" class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1

    def zerar(self):
        self.valor = 0

contador1 = Contador()
contador2 = Contador()

contador1.incrementar()
contador1.incrementar()
contador1.incrementar()

contador2.incrementar()

print("Primeiro contador:", contador1.valor)
print("Segundo contador:", contador2.valor)

contador1.zerar()

print("\nDepois de zerar:")
print("Primeiro contador:", contador1.valor)
print("Segundo contador:", contador2.valor) """

#Exercício 4
""" class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def repor(self, quantidade):
        if quantidade > 0:
            self.estoque += quantidade
            return True
        else:
            return False

    def vender(self, quantidade):
        if quantidade > 0 and quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            return False

    def valor_em_estoque(self):
        return self.preco * self.estoque

produto = Produto("Caderno", 5.0, 4)

print("Venda de 2:", produto.vender(2))
print("Estoque:", produto.estoque)

print("\nVenda de 3:", produto.vender(3))
print("Estoque:", produto.estoque)

print("\nReposição de 5:", produto.repor(5))
print("Estoque:", produto.estoque)

print("\nReposição de 0:", produto.repor(0))
print("Estoque:", produto.estoque)

print("\nValor em estoque:", produto.valor_em_estoque()) """

#Exercício 5
""" class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

    def emprestar(self):
        if self.emprestado == False:
            self.emprestado = True
            return True
        else:
            return False

    def devolver(self):
        if self.emprestado == True:
            self.emprestado = False
            return True
        else:
            return False

livro = Livro("Dom Casmurro")

print("Emprestar:", livro.emprestar())
print("Está emprestado?", livro.emprestado)

print("\nEmprestar novamente:", livro.emprestar())
print("Está emprestado?", livro.emprestado)

print("\nDevolver:", livro.devolver())
print("Está emprestado?", livro.emprestado)

print("\nDevolver novamente:", livro.devolver())
print("Está emprestado?", livro.emprestado) """

#Exercício 6
""" class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular(self, nome_aluno):
        self.alunos.append(nome_aluno)

    def quantidade_alunos(self):
        return len(self.alunos)

turma1 = Turma("Turma A")
turma2 = Turma("Turma B")

turma1.matricular("João")
turma1.matricular("Maria")

turma2.matricular("Pedro")

print("Turma:", turma1.nome)
print("Alunos:", turma1.alunos)
print("Quantidade:", turma1.quantidade_alunos())

print("\nTurma:", turma2.nome)
print("Alunos:", turma2.alunos)
print("Quantidade:", turma2.quantidade_alunos()) """

#Exercício 7
""" class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def valor_em_estoque(self):
        return self.preco * self.estoque

produtos = [
    Produto("Caderno", 10.0, 2),
    Produto("Caneta", 3.0, 0),
    Produto("Borracha", 2.0, 5)
]

total = 0
sem_estoque = 0

for produto in produtos:
    print("\nNome:", produto.nome)
    print("Estoque:", produto.estoque)
    print("Valor em estoque:", produto.valor_em_estoque())

    total += produto.valor_em_estoque()

    if produto.estoque == 0:
        sem_estoque += 1

print("\nValor total em estoque:", total)
print("Produtos sem estoque:", sem_estoque)

produtos = []

total = 0
sem_estoque = 0

for produto in produtos:
    total += produto.valor_em_estoque()

    if produto.estoque == 0:
        sem_estoque += 1

print("\nLista vazia:")
print("Valor total:", total)
print("Produtos sem estoque:", sem_estoque) """

#Exercício 8
""" class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

conta1 = Conta("João")
conta2 = Conta("Maria")

print("Depositar 50:", conta1.depositar(50))
print("Saldo:", conta1.saldo)

print("\nSacar 20:", conta1.sacar(20))
print("Saldo:", conta1.saldo)

print("\nSacar 40:", conta1.sacar(40))
print("Saldo:", conta1.saldo)

print("\nDepositar -10:", conta1.depositar(-10))
print("Saldo:", conta1.saldo)

print("\nSaldo da segunda conta:", conta2.saldo)"""

#Desafio extra
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

    def emprestar(self):
        if self.emprestado == False:
            self.emprestado = True
            return True
        else:
            return False

    def devolver(self):
        if self.emprestado == True:
            self.emprestado = False
            return True
        else:
            return False

livros = [
    Livro("Dom Casmurro"),
    Livro("Harry Potter"),
    Livro("O Pequeno Príncipe")
]

opcao = -1

while opcao != 0:

    print("\n===== BIBLIOTECA =====")
    print("1 - Mostrar livros e disponibilidade")
    print("2 - Emprestar um livro")
    print("3 - Devolver um livro")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        for livro in livros:
            print("\nTítulo:", livro.titulo)

            if livro.emprestado == True:
                print("Disponibilidade: Emprestado")
            else:
                print("Disponibilidade: Disponível")

    elif opcao == 2:
        titulo = input("Digite o título do livro: ")

        encontrado = False

        for livro in livros:
            if livro.titulo == titulo:
                encontrado = True

                if livro.emprestar() == True:
                    print("Livro emprestado com sucesso!")
                else:
                    print("Este livro já está emprestado!")

        if encontrado == False:
            print("Livro não encontrado")

    elif opcao == 3:
        titulo = input("Digite o título do livro: ")

        encontrado = False

        for livro in livros:
            if livro.titulo == titulo:
                encontrado = True

                if livro.devolver() == True:
                    print("Livro devolvido com sucesso!")
                else:
                    print("Este livro não estava emprestado!")

        if encontrado == False:
            print("Livro não encontrado")

    elif opcao == 0:
        print("Saindo da biblioteca...")

    else:
        print("Opção inválida!")

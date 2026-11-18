# ==========================================
# RESUMO - PROGRAMAÇÃO ORIENTADA A OBJETOS
# ==========================================

# 1. CLASSE E OBJETOS
class Produto:

    # 2. __init__ E ATRIBUTOS
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    # 3. MÉTODO PARA REPOR ESTOQUE
    def repor(self, quantidade):
        if quantidade <= 0:
            return False

        self.estoque += quantidade
        return True

    # 4. MÉTODO PARA VENDER
    def vender(self, quantidade):
        if quantidade <= 0 or quantidade > self.estoque:
            return False

        self.estoque -= quantidade
        return True

    # 5. MÉTODO COM RETURN
    def valor_em_estoque(self):
        return self.preco * self.estoque


# 6. CRIANDO OBJETOS
caderno = Produto("Caderno", 12.0, 5)
caneta = Produto("Caneta", 3.0, 20)

# 7. ACESSANDO ATRIBUTOS
print("Produto:", caderno.nome)
print("Preço:", caderno.preco)
print("Estoque:", caderno.estoque)

# 8. UTILIZANDO MÉTODOS
caderno.repor(3)
caderno.vender(2)

print("\nEstoque atualizado:", caderno.estoque)

# 9. TESTANDO UMA VALIDAÇÃO
if caderno.vender(20):
    print("Venda realizada!")
else:
    print("Venda não realizada!")

# 10. LISTA DE OBJETOS
produtos = [caderno, caneta]

print("\n--- LISTA DE PRODUTOS ---")

total = 0

for produto in produtos:
    print("Nome:", produto.nome)
    print("Estoque:", produto.estoque)

    valor = produto.valor_em_estoque()
    total += valor

print("\nValor total em estoque:", total)


# 11. OBJETOS INDEPENDENTES
outro_caderno = Produto("Caderno", 12.0, 10)

outro_caderno.vender(2)

print("\nCaderno original:", caderno.estoque)
print("Outro caderno:", outro_caderno.estoque)


# 12. LISTA DENTRO DE UMA CLASSE
class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular(self, nome_aluno):
        self.alunos.append(nome_aluno)


manha = Turma("Manhã")
manha.matricular("Ana")

print("\nAlunos da manhã:", manha.alunos)

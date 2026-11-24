# Exercício 1
""" import tkinter as tk

janela = tk.Tk()

janela.title("Minha Aplicação")
janela.geometry("300x200")

texto = tk.Label(
    janela,
    text="Olá, mundo!",
    font=("Arial", 14),
    fg="blue"
)
texto.pack(pady=20)

janela.mainloop() """

# Exercício 2
""" import tkinter as tk

janela = tk.Tk()
janela.title("Contador de cliques")
janela.geometry("300x150")

contador = 0

def contar():
    global contador
    contador += 1
    rotulo.config(text=f"Cliques: {contador}")

rotulo = tk.Label(janela, text="Cliques: 0")
rotulo.pack(pady=15)

botao = tk.Button(janela, text="Clique aqui", command=contar)
botao.pack()

janela.mainloop() """

#Exercício 3
""" import tkinter as tk

janela = tk.Tk()
janela.title("Formulário de cadastro")
janela.geometry("350x250")

def cadastrar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    email = entrada_email.get()

    if nome == "" or idade == "" or email == "":
        resultado.config(text="Preencha todos os campos!")
    else:
        resultado.config(text=f"Nome: {nome}\nIdade: {idade}\nE-mail: {email}")

tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1)

tk.Label(janela, text="Idade:").grid(row=1, column=0, padx=10, pady=10)
entrada_idade = tk.Entry(janela)
entrada_idade.grid(row=1, column=1)

tk.Label(janela, text="E-mail:").grid(row=2, column=0, padx=10, pady=10)
entrada_email = tk.Entry(janela)
entrada_email.grid(row=2, column=1)

botao = tk.Button(janela, text="Cadastrar", command=cadastrar)
botao.grid(row=3, column=1, pady=10)

resultado = tk.Label(janela, text="")
resultado.grid(row=4, column=0, columnspan=2)

janela.mainloop() """

#Exercício 4
""" import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora simples")
janela.geometry("350x250")

def calcular(operacao):
    try:
        valor1 = float(entrada1.get())
        valor2 = float(entrada2.get())

        if operacao == "+":
            resultado = valor1 + valor2

        elif operacao == "-":
            resultado = valor1 - valor2

        elif operacao == "*":
            resultado = valor1 * valor2

        elif operacao == "/":
            if valor2 == 0:
                rotulo_resultado.config(text="Não é possível dividir por zero!")
                return
            resultado = valor1 / valor2

        rotulo_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        rotulo_resultado.config(text="Digite valores válidos!")

tk.Label(janela, text="Primeiro valor:").pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Segundo valor:").pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

tk.Button(janela, text="+", command=lambda: calcular("+")).pack(side="left", padx=20)
tk.Button(janela, text="-", command=lambda: calcular("-")).pack(side="left")
tk.Button(janela, text="*", command=lambda: calcular("*")).pack(side="left")
tk.Button(janela, text="/", command=lambda: calcular("/")).pack(side="left")

rotulo_resultado = tk.Label(janela, text="Resultado:")
rotulo_resultado.pack(pady=30)

janela.mainloop() """

#Exercício 5
import tkinter as tk

janela = tk.Tk()
janela.title("Cadastro de personagens RPG")
janela.geometry("400x400")

personagens = []

def cadastrar():
    nome = entrada_nome.get()
    classe = entrada_classe.get()
    nivel = entrada_nivel.get()
    vida = entrada_vida.get()

    if nome == "" or classe == "" or nivel == "" or vida == "":
        resultado.config(text="Preencha todos os campos!")
        return

    try:
        nivel = int(nivel)
        vida = int(vida)

        if nivel <= 0 or vida <= 0:
            resultado.config(text="Nível e vida devem ser positivos!")
            return

    except ValueError:
        resultado.config(text="Nível e vida devem ser números!")
        return

    personagem = f"Nome: {nome} | Classe: {classe} | Nível: {nivel} | Vida: {vida}"

    personagens.append(personagem)

    lista.config(text="\n".join(personagens))

    resultado.config(text="Personagem cadastrado!")

    entrada_nome.delete(0, tk.END)
    entrada_classe.delete(0, tk.END)
    entrada_nivel.delete(0, tk.END)
    entrada_vida.delete(0, tk.END)

tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Classe:").pack()
entrada_classe = tk.Entry(janela)
entrada_classe.pack()

tk.Label(janela, text="Nível:").pack()
entrada_nivel = tk.Entry(janela)
entrada_nivel.pack()

tk.Label(janela, text="Pontos de vida:").pack()
entrada_vida = tk.Entry(janela)
entrada_vida.pack()

tk.Button(janela, text="Cadastrar personagem", command=cadastrar).pack(pady=10)

resultado = tk.Label(janela, text="")
resultado.pack()

tk.Label(janela, text="Personagens cadastrados:").pack()

lista = tk.Label(janela, text="", wraplength=380, justify="left")
lista.pack(pady=10)

janela.mainloop()
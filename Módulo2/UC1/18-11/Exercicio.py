# Crie uma tela que contém uma espécie de formulário:
# Ela pede nome, email e cidade
# Crie um Entry para cada um deles
# Coloque um Label em cima de cada Entry
#Crie um botão que, ao clicar, mostra a seguinte frase no terminal:
# "Olá fulano, seu email é tal e você é de tal cidade"
import tkinter as tk

janela = tk.Tk()
janela.title("Exercício Formulário")
janela.geometry("800x600")

#Label formulário
texto = tk.Label(
    janela, 
    text="Formulário", 
    font=("Arial", 14), 
    fg="black" 
)
texto.pack(pady=20)

#Label nome
texto = tk.Label(
    janela, 
    text="Digite seu nome: ", 
    font=("Arial", 14), 
    fg="black" 
)
texto.pack(pady=20)
#Entry nome
entradaNome = tk.Entry(
    janela,
    width=30
)
entradaNome.pack(pady=10)

#Label email
texto = tk.Label(
    janela, 
    text="Digite seu email: ", 
    font=("Arial", 14), 
    fg="black" 
)
texto.pack(pady=20)
#Entry email
entradaEmail = tk.Entry(
    janela,
    width=30
)
entradaEmail.pack(pady=10)
#Label cidade
texto = tk.Label(
    janela, 
    text="Digite sua cidade: ", 
    font=("Arial", 14), 
    fg="black" 
)
texto.pack(pady=20)
#Entry cidade
entradaCidade = tk.Entry(
    janela,
    width=30
)
entradaCidade.pack(pady=10)

#Exibir mensagem
def exibir_mensagem():
    nome = entradaNome.get()
    email = entradaEmail.get()
    cidade = entradaCidade.get()
    print(f"Olá {nome}, seu email é {email}, e você é de {cidade}")

botao = tk.Button(
    janela,
    text="Enviar",
    command=exibir_mensagem
)
botao.pack(pady=10)

janela.mainloop()
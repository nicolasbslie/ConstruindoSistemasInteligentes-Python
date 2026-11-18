# Comando para criar ambiente virtual
# py -m venv .venv
# source .venv/Scripts/activate

# Comando que roda para ver se está funcionando
# python -m tkinter

# Importa a biblioteca tkinter com o apelido de 'tk'
import tkinter as tk

# Cria a janela principal
janela = tk.Tk()

janela.title("Minha primeira aplicação")
janela.geometry("400x300")

# Componente que cria um texto da janela
texto = tk.Label(
    janela, # em que tela ele aparece
    text="Seja bem-vindo(a)!", # Qual o texto dele
    font=("Arial", 14), # Qual a fonte de texto e tamanho
    fg="blue" # Qual a cor do texto
)
texto.pack(pady=20)

# Cria um componente que permite digitar texto
entrada = tk.Entry(
    janela, # Em qual tela ele vai
    width=30
)
entrada.pack(pady=10)

# Mensagem do botão
def exibir_mensagem():
    print("Botão clicado!")
# Cria um componente de botão
botao = tk.Button(
    janela,
    text="Clique aqui",
    command=exibir_mensagem
)
botao.pack(pady=10)

# Função que mantém a aplicação em execução
janela.mainloop()
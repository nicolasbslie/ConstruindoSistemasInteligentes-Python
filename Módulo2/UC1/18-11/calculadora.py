import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("800x600")

#Label número 1
texto = tk.Label(
    janela,
    text="Digite um número:",
    font=("Arial", 14),
    fg="blue"
)
texto.pack(pady=20)
#Entry número 1
entradaNumero1 = tk.Entry(
    janela,
    width=30
)
entradaNumero1.pack(pady=10)

#Label número 2
texto = tk.Label(
    janela,
    text="Digite outro número:",
    font=("Arial", 14),
    fg="blue"
)
texto.pack(pady=20)
#Entry número 2
entradaNumero2 = tk.Entry(
    janela,
    width=30
)
entradaNumero2.pack(pady=10)

#Botão Somar
def somar():
    numero1 = int(entradaNumero1.get())
    numero2 = int(entradaNumero2.get())
    print(numero1 + numero2)

botao = tk.Button(
    janela,
    text="Somar",
    command=somar
)
botao.pack(pady=30)

janela.mainloop()
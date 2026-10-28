analista = input("Nome ou apelido do analista: ")
identificacao = input("Identificação da mensagem: ")
grupos = int(input("Quantidade de grupos de símbolos: "))
tempoGrupo = float(input("Tempo por grupo, em minutos: "))


if grupos <= 0 or tempoGrupo <= 0:
    print("Dados inválidos")
else:
    total = grupos * tempoGrupo


    print("\n--- FICHA DA MENSAGEM ---")
    print("Analista:", analista)
    print("Identificação:", identificacao)
    print("Quantidade de grupos:", grupos)
    print("Tempo total:", total, "minutos")


    if total <= 60:
        print("Análise dentro do prazo")
    else:
        print("Reorganizar o trabalho")

# A identificação é texto porque serve para identificar a mensagem, podendo conter letras e números. O float() é adequado para o tempo porque permite usar números decimais, como 2,5 minutos.
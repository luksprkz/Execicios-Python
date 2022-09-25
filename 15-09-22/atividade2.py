while True:
    try:
        numero = int(input("Qual é o número escolhido? "))
        numero = str(numero)
        print(f'O número {numero} tem {len(numero)} caracteres ')
        break
    except ValueError:
        print("O input não é um número valido, digite um número válido. ")
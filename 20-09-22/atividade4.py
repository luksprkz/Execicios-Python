while True:
    nome = input('Qual é o seu nome? ')
    sexo = input('Qual é o seu sexo? ')
    idade = int(input('Qual é a idade? '))
    if sexo == 'F' and idade >18:
        print(f'{nome} ACEITA!')
        break
    else:
        print(f'{nome} NÃO ACEITO(A)')
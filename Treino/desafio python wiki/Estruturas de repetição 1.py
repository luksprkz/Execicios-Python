nota = float(input('Qual foi a sua nota?'))
while nota > 10:
    nota = float(input('Digite uma nota válida: '))
if nota <= 10:
    print(f'A sua nota foi: {nota}')
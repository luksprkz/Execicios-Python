repeticoes = 7
i = 0
numero = int(0)
while (i < (repeticoes)):
    nota = int(input("Qual foi a nota?"))
    numero = numero + nota
    i = i + 1
print(f'A soma das notas é {numero}',f'\nA média das notas é {numero/7}')

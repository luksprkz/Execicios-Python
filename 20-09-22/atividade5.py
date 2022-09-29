LISTA = []
for x in range(5):
    numero = int(input('Número: '))
    LISTA.append(numero)
print(f'O maior número é \'{max(LISTA)}\' e o menor número é \'{min(LISTA)}\'')
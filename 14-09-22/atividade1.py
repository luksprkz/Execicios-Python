LISTA = []
for x in range(2):
    numero = int(input('Digite o número desejado?'))
    LISTA.append(numero)
if LISTA[0]+LISTA[1] > 100:
    print(f'{LISTA[0]+LISTA[1]-10}')
else:
    print(f'{LISTA[0]+LISTA[1]}')
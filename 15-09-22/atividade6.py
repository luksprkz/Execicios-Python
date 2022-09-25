LISTA = []
numero = ()
while numero != 0:
        numero = int(input('\nDigite 0 para parar o programa e receber o resultado ou Digite o número que você quer acrescentar à lista:'))
        LISTA.append(numero)
if numero == 0:
    print('\nO programa parou') 
    print(f'O maior número entre{LISTA[:]} é: {max(LISTA)}')
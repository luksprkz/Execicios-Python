LISTA = []
numero = ()
while numero != 0:
        numero = int(input('\nDigite 0 para parar o programa e receber o resultado ou Digite o número que você quer acrescentar à soma:'))
        LISTA.append(numero)
if numero == 0:
    print('\nO programa parou') 
    print(f'A soma dos números{LISTA[:]} é: {sum(LISTA)}')


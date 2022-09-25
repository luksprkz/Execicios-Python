while True:
    try:
        y = ()
        while y != 0:
            y = int(input('\nDigite 0 para parar o programa ou Digite um número inteiro válido:'))
            while y >= 99999:
                print('\nTente um número menor')
                y = int(input('\nDigite 0 para parar o programa ou Digite um número inteiro válido:'))
            for x in range(y):
                    print(x+1,end=" ")
        if y == 0:
            print('\nO programa parou')
            break
    except ValueError:
        print('\nDigite apenas números: ')
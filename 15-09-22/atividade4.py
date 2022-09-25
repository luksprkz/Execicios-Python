senha = (input('Digite a senha:'))
senha1 = (input('Digite novamente a senha:'))
if senha1 == senha:
    print('As senhas são iguais, fim do programa')
else:
    while senha1 != senha:
        print ('As senhas não são iguais')
        senha = (input('Digite a senha:'))
        senha1 = (input('Digite novamente a senha:'))
        if senha1 == senha:
            print('As senhas são iguais, fim do programa')
            break
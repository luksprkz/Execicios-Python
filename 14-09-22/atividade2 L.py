controle = ''
ALCOOL = []
GASOLINA = []
while (controle != 's'):
    print ('a.Alcool',"\ng.Gasolina",'\ns.Sair')
    controle = input('Digite um comando:')
    if  controle == ("a") :
         alcool = float(input("Quantos litros foram vendidos?"))
         ALCOOL.append(alcool)
         if ALCOOL[0] > 20:
            print ('O total a pagar é:',((ALCOOL[0]*5.20)-ALCOOL[0]*0.05))
         else: 
            print (f'O total a pagar é:{(ALCOOL[0]*5.20)-ALCOOL[0]*0.03}')
    elif controle == ("g"):
        gasolina = float(input("Quantos litros foram vendidos?"))
        GASOLINA.append(gasolina)
        if GASOLINA[0] > 20:
            print (f'O total a pagar é:{(GASOLINA[0]*6.10)-GASOLINA[0]*0.06}')
        else:
            print (f'O total a pagar é:{(GASOLINA[0]*6.10)-GASOLINA[0]*0.04}')
    print('Comando inválido, tente novamente')
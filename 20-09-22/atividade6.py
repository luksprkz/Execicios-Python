LISTA = []
for x in range(3):
    num = input('Valores: ')
    LISTA.append(num)
if LISTA[0]>= LISTA[1]+LISTA[2] or LISTA[1]>= LISTA[0]+LISTA[2] or LISTA[2]>= LISTA[0]+LISTA[1]:
    print('Valores inválidos para formação de um triângulo!')
else: 
    if LISTA[0] == LISTA[1] and LISTA[1] == LISTA[2]:
        print('Triângulo Equilátero')
    elif LISTA[0] != LISTA[1] != LISTA[2]:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isóceles')
LISTA = []
for x in range(5):
    valor = int(input('Informe um valor'))
    LISTA.append(valor)
check = int(input('Que valor você quer saber se está na lista? '))
if LISTA.count(check)>0:
    print('O valor se encontra na lista!')
#ou
if check in LISTA:
    print('O valor se encontra na lista!')

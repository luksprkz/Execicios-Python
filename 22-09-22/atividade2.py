LISTA= []
for x in range(3):
    nomes = input('Adicione os nomes: ')
    LISTA.append(nomes)
print('Lista inicial',LISTA)
LISTA.pop(0)
print('Lista após a remoção',LISTA)
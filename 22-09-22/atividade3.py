LISTA = []
for x in range(3):
    nomes = input('Adicione os nomes: ')
    LISTA.append(nomes)
print('Lista inicial',LISTA)    
remover = input('Que nome deseja remover?')
LISTA.remove(remover)
print('Lista após remoção', LISTA)
add = input('Que outro nome deseja adicionar?')
add_pos = int(input('Em que posição?'))
LISTA.insert(add_pos, add)
print('Lista final', LISTA)
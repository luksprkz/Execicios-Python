LISTA = []
x = int(input('Quantos nomes? '))
for y in range(x):
    nomes = input('Nome: ')
    nomes = nomes.title()
    ordem = int(input('Em que posição deseja colocar o nome?'))
    ordem = ordem-1
    LISTA.insert(ordem, nomes)

for indice, opcoes in enumerate(LISTA):
    print(f'{indice}: {opcoes}')

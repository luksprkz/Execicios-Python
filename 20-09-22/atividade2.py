LISTA = []
for x in range(5):
    nome = input('Informe um nome: ')
    LISTA.append(nome)

exibir = input('Que nome deseja exibir? ')
if exibir in LISTA:
    print(f'O nome {exibir} aparece {LISTA.count(exibir)} vezes')
else:
    print('O nome escolhido não é um dos nomes informados.')    
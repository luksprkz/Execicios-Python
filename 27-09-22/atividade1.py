dicionario = {}
for x in range(3):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    dicionario.update({nome:idade})

acess_nome = input('Que nome quer saber se está no dicionário? ')
if acess_nome in dicionario:
    print(f'{acess_nome} tem {dicionario.get(acess_nome)} anos e está no dicionário')
else:
    print(f'{acess_nome} não está na lista')
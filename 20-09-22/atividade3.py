LISTA = [
[], #input do nome
[], #input de altura
[], #input de peso
[] #input de idade
]
def funcao(atributo, numero):
    while True:
        atributo = input(f'Informe {atributo} ')
        atributo = atributo.title()
        LISTA[numero].append(atributo)
        break
y=3
for x in range(3):
    loop_break = input(f'O programa aceita dados de apenas mais {y} pessoas. Digite \'S\' para sair ')
    loop_break = loop_break.upper()
    y-=1
    if loop_break == 'S':
        break
    funcao('Nome', 0)
    funcao('Altura', 1)
    funcao('Peso', 2)
    funcao('Idade', 3)
escolha = input('Você quer ver os dados de quem? ')
escolha = escolha.title()
ordem = LISTA[0].index(escolha)
if escolha in LISTA[0]:
    print(f'{LISTA[0][ordem]} tem {LISTA[1][ordem]} de altura, {LISTA[2][ordem]}kg e {LISTA[3][ordem]} ano')
else:
    print('Nome não encontrado na lista')
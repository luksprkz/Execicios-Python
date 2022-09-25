PRODUTOS = []
for x in range(4):
    produtos = (input('Quais foram os produtos comprados?'))
    PRODUTOS.append(produtos)

QUANTIDADES = []
for x in range(4):
    quantidade = float(input('Quais foram as quantidades compradas, respectivamente?'))
    QUANTIDADES.append(quantidade)

PRECOS = []
for x in range(4):
    precos = float(input('Quais foram os preços dos produtos, respectivamente?'))
    PRECOS.append(precos)

print(f'{int(QUANTIDADES[0])}g de {PRODUTOS[0]} custaram: R${PRECOS[0]}',
f'\n{QUANTIDADES[1]}g de {PRODUTOS[1]} custaram: R${PRECOS[1]}',
f'\n{QUANTIDADES[2]}g de {PRODUTOS[2]} custaram: R${PRECOS[2]}',
f'\n{QUANTIDADES[3]}g de {PRODUTOS[3]} custaram: R${PRECOS[3]}')

    
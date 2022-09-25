#receber o código da peça
x = input('Qual é o código da peça?')
#receber o valor por unidade
y = float(input('Qual é o valor unitário da peça?'))
#receber a quantidade de peças vendidas
z = int(input('Quantas peças foram vendidas?'))
#calcular o valor total da peça(quantidade x valor unitário da peça)
#mostrar o código da peça e o valor total dela
print('O código da peça é:',(x),'.')
print('O valor total das peças é:',(y*z),'.')
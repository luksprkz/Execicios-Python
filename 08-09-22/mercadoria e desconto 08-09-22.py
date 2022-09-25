#receber o preço da mercadoria e o percentual de desconto
preçoInicial = float(input('Qual é o preço da mercadoria?'))
dPorcent = float(input('Seu salário aumentou em quantos %?'))
#calcular o preço após o desconto
dReal = int(preçoInicial*(dPorcent/100))
preçoFinal = preçoInicial - dReal
#imprimir o preço com desconto
print('O desconto será de :',dReal,'reais')
print('O preço da mercadoria após o desconto é:',preçoFinal)
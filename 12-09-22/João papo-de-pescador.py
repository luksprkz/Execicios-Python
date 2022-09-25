#receber quantos quilos ele trouxe 
produto = int(input('Quantos quilos de pescado você trouxe?'))
#definir o valor da multa por quilos excedentes e a quantidade da qual não pode passar sem receber multa
produtoLimite = 50
excesso = produto-50 
multa = excesso*4
#imprimir quantos quilos ele excedeu e quanto ele deve pagar de multa
print('Você excedeu o limite em:', excesso,'quilos')
print('Você deverá pagar: R$',multa,'de multa')
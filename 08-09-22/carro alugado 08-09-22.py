#receber a quantidade de km percorridos
kmP = int(input('Quantos km foram percorridos?'))
#receber os dias em que o carro esteve alugado
dA = int(input('Por quantos dias o carro esteve alugado?'))
#calcular o preço a ser pago
VkmP = kmP*0.15
VdA = dA*60
Vf = VkmP+VdA
#imprimir o preço a ser pago
print('O valor devido é: R$',Vf)
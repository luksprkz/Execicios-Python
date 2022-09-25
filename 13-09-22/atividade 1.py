#receber dividendo e divisor
x = float(input('Qual é o dividendo?'))
y = float(input('Qual é o divisor?'))
#imprimir o resto
z = int(x%y)
while z >=1:
    print (f'O resto da divisão é:{z}')
    break
else:
    print('A divisão não tem resto')
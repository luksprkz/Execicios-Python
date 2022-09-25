#recerber a altura
Gender = (input('Qual o seu sexo?')) 
h = float(input('Qual é a sua altura?'))

#calcular o peso ideal para homens e mulheres
PesoIdealHomem = int((72.7*h)-58)
PesoIdealMulher = int((62.1*h)-44.7)
if Gender == ('Mulher'):
    print(f'O peso ideal para uma mulher da sua altura é: {PesoIdealMulher}')
else:
    print(f'O peso ideal para um homem da sua altura é: {PesoIdealHomem}')

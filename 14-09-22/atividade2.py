
ALCOOL = []
GASOLINA = []
combustivel = input('Qual foi o combustível escolhido?')
if combustivel == 'Gasolina':
      gasolina = float(input('Quantos litos foram comprados?'))
      GASOLINA.append(gasolina)
elif combustivel == 'Álcool':
  alcool = float(input('Quantos litos foram comprados?'))
  ALCOOL.append(alcool)
else:
  while combustivel != ('Gasolina', 'Álcool'):
    print('O combustível informado não é valido, informe um combustivel válido.')
    combustivel = input('Qual foi o combustível escolhido?')
    if combustivel == 'Gasolina':
      gasolina = float(input('Quantos litos foram comprados?'))
      GASOLINA.append(gasolina)
      break
    elif combustivel == 'Álcool':
      alcool = float(input('Quantos litos foram comprados?'))
      ALCOOL.append(alcool)
      break
if len(GASOLINA) != 0:
  if gasolina > 20:
    print (f'{(GASOLINA[0]*6.10)-gasolina*0.06}')
  else:
    print (f'{(GASOLINA[0]*6.10)-gasolina*0.03}')
if len(ALCOOL) != 0:
  if alcool>20:
    print (f'{(ALCOOL[0]*5.20)-alcool*0.05}')
  else:
    print (f'{(ALCOOL[0]*5.20)-alcool*0.03}')
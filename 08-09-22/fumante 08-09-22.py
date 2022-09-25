#receber quantos cigarros a pessoa fuma por dia
CigDia = int(input('Quantos cigarros você fuma por dia?'))
#receber quantos anos essa pessoa já fumou
AnosFum = int(input("Há quantos anos você fuma?"))
#calcular quanto tempo de vida a pessoa perdeu devido ao fumo
minutos_perdidos_por_ano = (CigDia*10)*365*AnosFum
dias_perdidos = int(minutos_perdidos_por_ano/1440)
#imprimir o tempo perdido em dias
print('O hábito de fumar diminuiu sua expectativa de vida em:',dias_perdidos, 'dias. Pare de fumar urgentemente')
#receber raio
raio = float(input('Qual é o raio do circulo?'))
π = 3.14
#calcular perímetro e área
perimetro = int(2*(π*raio))
area =  int(π*(raio**2))
#imprimir perímetro e área
print('O perimetro do circulo é:',(perimetro))
print('A área do circulo é:',(area))
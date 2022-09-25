N1 = float(input ("Qual foi a sua primeira nota?"))
N2 = float(input ("Qual foi a sua segunda nota?"))
N3 = float(input ("Qual foi a sua terceira nota?"))
N4 = float(input ("Qual foi a sua quarta nota?"))

x = ((N1+N2+N3+N4)/4)

print (x)

if x == 10:
    print ("Aprovado com louvor!")
    print ("Vá na secretaria pegar o seu diploma!")
elif x >= 7:
    print ("Você está aprovado!")
    print ("Vá na secretaria pegar o seu diploma!")
elif x >= 5:
    print ("Recuperação")
    print ("Vá na secretaria marcar sua recuperação")
elif x >= 1:
    print ("Reprovado!")
    print ("Da próxima vez, estude mais!")
else:
    print ("Tu é burro ein...")


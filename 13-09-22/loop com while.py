#imprimir os números impares e pares e depois todos os números de 1 a 100
for x in range(100):
    if x % 2 != 0:
        continue
    print(x, end = " ",)
else:
    print('\n \nA contagem acabou\n')
for x in range(100):
    if x % 2 == 0:
        continue
    print(x, end = " ")
else:
    print('\n \nA contagem acabou\n')
for x in range(100):
    print(x,end=" ")
#receber nome e idade de 5 pessoas e imprimir esses dados
repeticoes = 5
i = 0
número = int(0)
texto = ""
while (i < (repeticoes)):
    nome = input("Qual é o seu nome?")
    idade = int(input("Qual é a sua idade?"))
    texto = nome +','+ texto
    número = número + idade
    i = i + 1
#imprimir a média e a soma das idades
print(f'A média das idades de: {texto} é de {int(número/repeticoes)} anos', f'\nA soma das idades de: {texto} é de {número} anos')





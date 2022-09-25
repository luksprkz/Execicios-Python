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
número = int(0)
texto = ""
for final in range(5):
    nome = input("\nQual é o seu nome?")
    idade = int(input("\nQual é a sua idade?"))
    número = número + idade
    texto = texto + nome + ', '      
#imprimir a média e a soma das idades
print(f'A média das idades de {texto} é de {int(número/(final+1))} anos', f'\nA soma das idades de: {texto} é de {número} anos')
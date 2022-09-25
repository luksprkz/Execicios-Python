#receber o valor do salário e a porcentagem de aumento
salario1= float(input('Qual é o seu salário?'))
porcentagemDeAumento = float(input('Seu salário aumentou em quantos %?'))
aumento = salario1*(porcentagemDeAumento/100)
salario2 = salario1+aumento
#imprimir o novo salário e em quanto ele foi aumentado
print('Seu salario aumentou em:',aumento)
print('Seu novo salário é ', salario2)
FIBONACCI =[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10.946,17.711,8.657,46.368,75.025,121.393,196.418,317.811,514.229,832.040]
n = int(input('Qual é o número de repetições?'))
x = 0
if n > 30:
        print('Limite máximo da sequência atingido.')
        n = int(input('Qual é o número de repetições?'))
else:
    while n > x:
        print(FIBONACCI[0:n])
        break


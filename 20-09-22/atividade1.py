x = int(input('Número: '))
y = 1

while x <=10:
    print(f'\nTabuada de {x}: \n')
    while y<=10:
        print(f'{x} + {y} = {x+y}')
        y += 1
    break
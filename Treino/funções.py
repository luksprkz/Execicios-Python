def dog_info(age, name):
    print(f'{name} tem {age} anos de idade')

dog_info(8, 'Totó')

def funcao_exemplo(amor, idade):
    print(f'{amor} é o meu amor, ela tem {idade} anos de idade')

funcao_exemplo('Bia', 22)

def modify_case_upper(upper):
    return upper.upper()
    
def modify_case_lower(lower):
    return lower.lower()

names = ['Pedro, Bia, Ana']
for name in names:
    print(modify_case_upper(name))



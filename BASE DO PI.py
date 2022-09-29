CAR = [ #Matriz de possíveis atributos do automóvel 
    [], #lista para adicionar os itens do pedido
    ['Pálio', 'Gol', 'Siena', 'Hb20', 'Hilux', 'S10', 'Hilux'],
    ['Vermelha', 'Prata', 'Preta', 'Azul', 'Branca'],
    ['Fosco', 'Metálica', 'Sólida', 'Perolizada'],
    ['Vidro Elétrico', 'Ar-Condicionado', 'Direção Hidráulica', 'Câmbio Automático', 'Banco De Couro'],
    [] #lista para o valor final do pedido
]

PRICES = { #Dicionário de preços
    'Pálio':1000, 
    'Gol':2000, 
    'Siena':3000, 
    'Hb20':5000,
    'S10':6000, 
    'Hilux':6000,
    'Vermelha':0, 
    'Prata':0, 
    'Preta':0, 
    'Azul':0, 
    'Branca':0, 
    'Fosco':50, 
    'Metálica':20, 
    'Sólida':0, 
    'Perolizada':100, 
    'Vidro Elétrico':20, 
    'Ar-Condicionado':30, 
    'Direção Hidráulica':20, 
    'Câmbio Automático':25,
    'Banco De Couro':50, 
}

def function(choice, number): #função para loop para choices

    while True:

        funcList(number)

        if number == 4:
            check = all(item in CAR[0] for item in CAR[4])
            if check is True:
                print('\nVocê adicionou todos os opcionais disponíveis ao seu pedido.')
                break
            optional = input('\n Deseja acrescentrar algum opcional? \n S / N ')
            optional = optional.upper()
            if optional == 'N': 
                break 

        choice = input('\nQual você prefere? ')
        choice = choice.title()

        if choice in CAR[number]:
            CAR[0].append(choice)
            CAR[5].append(PRICES.get(choice))
            print(f'\n{choice} adicionado ao seu pedido!')
            if number !=4: break
        else:
            print('\nEscolha inválida, digite uma opção disponível')

def funcList(number): #função modificadora da primeira função

    if number != 4:
        print('Opções disponíveis: ')
        CAR[number].sort() 
        for index, opcoes in enumerate(CAR[number]):
            print(f'{index}: {opcoes}')
    else:  
        print('Opcionais disponíveis: ') 
        for index, optionals in enumerate(list(set(CAR[4])-set(CAR[0]))):
            print(f'{index}: {optionals}')  
        print('Sair')
        
function('modelo', 1)

function('cor', 2)

function('pintura', 3)

function('opcional', 4)

print(f"\nSeu pedido foi: {', '.join(CAR[0][0:3])}. \n\nVocê escolheu os opcionais: {', '.join(CAR[0][3:])}.\n\nO valor total do pedido é de R${sum(CAR[5])}")

CAR[0].clear()
CARRO = [ #Matriz de possíveis atributos do automóvel 
    [], #lista para adicionar os itens do pedido
    ['Pálio', 'Gol', 'Siena', 'Hb20', 'Hilux', 'S10', 'Hilux'],
    ['Vermelha', 'Prata', 'Preta', 'Azul', 'Branca'],
    ['Fosco', 'Metálica', 'Sólida', 'Perolizada'],
    ['Vidro Elétrico', 'Ar-Condicionado', 'Direção Hidráulica', 'Câmbio Automático', 'Banco De Couro'],
    [] #lista para somar o valor final do pedido
]

PRECOS = { #Dicionário de preços
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

def funcao(escolha, numero): #função para loop para escolhas
    while True:
        lista(numero)
        if numero == 4:
            check = all(item in CARRO[0] for item in CARRO[4])
            if check is True:
                print('\nVocê adicionou todos os opcionais disponíveis ao seu pedido.')
                break
            opcional = input('\n Deseja acrescentrar algum opcional? \n S / N ')
            opcional = opcional.upper()
            if opcional == 'N': 
                break 
        escolha = input('\nQual você prefere? ')
        escolha = escolha.title()
        if escolha in CARRO[numero]:
            CARRO[0].append(escolha)
            CARRO[5].append(PRECOS.get(escolha))
            print(f'\n{escolha} adicionado ao seu pedido!')
            if numero !=4: break
        else:
            print('\nEscolha inválida, digite uma opção disponível')

def lista(numero): #função modificadora da primeira função
    if numero != 4:
        print('Opções disponíveis: ') 
        for indice, opcoes in enumerate(CARRO[numero]):
            print(f'{indice}: {opcoes}')
    else:  
        print('Opcionais disponíveis: ') 
        for indice, opcionais in enumerate(list(set(CARRO[4])-set(CARRO[0]))):
            print(f'{indice}: {opcionais}')  
        print('Sair')
while True:  
       
    funcao('modelo', 1)

    funcao('cor', 2)

    funcao('pintura', 3)

    funcao('opcional', 4)

    print(f"\nSeu pedido foi: \n{', '.join(CARRO[0][0:3])}. \nVocê escolheu os opcionais:\n{', '.join(CARRO[0][3:])}. O valor total do pedido é de R${sum(CARRO[5])}")
    CARRO[0].clear()
    break
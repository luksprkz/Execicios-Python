DICIO ={}
nome = input('Nome: ')
senha = int(input('Senha: '))
altura = input('Altura: ')
peso = input('Peso: ')
idade = input('Idade: ')
cpf = input('CPF: ')
DICIO.update({nome:senha, altura:altura, peso:peso, idade:idade, cpf:cpf })

nome_1 = input('Nome: ')
senha_1 = int(input('Senha: '))

if nome_1 in DICIO and senha_1 == DICIO.get(nome):
    print(F'Altura: {altura}, peso: {peso}kg, idade:{idade} anos, CPF: {cpf}')
else:
    print('Nome e senha não conferem')
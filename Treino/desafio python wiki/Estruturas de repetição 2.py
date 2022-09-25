usuario = input('Qual é o usuário? ')
senha = input('Qual é a sua senha?')
while senha == usuario:
    senha = input('A senha não pode ser igual ao usuário, digite uma senha válida: ')
if senha != usuario:
    print('Senha cadastrada com sucesso')
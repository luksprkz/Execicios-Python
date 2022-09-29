LISTA = []
while len(LISTA) < 10:
    resposta = input('Sim ou Não?')
    resposta = resposta.title()
    if resposta == 'Sim' or resposta == 'Nao':
        LISTA.append(resposta)
    else:
        print('Resposta inválida!')
    
print('Os usuários respoderam \'Sim\'', LISTA.count('Sim'), 'vezes')
print('Os usuários respoderam \'Não\'', LISTA.count('Nao'), 'vezes')
contacts = {
    'Pedro':{'Pedro':95488349},
    'Beatriz':{'Beatriz':84569822},
    'Ana':{'Ana':94653891},
    'Lucas':{'Lucas':8648977},
    'Nazaré':{'Nazaré':59875631},
    'Paulo':{'Paulo':94149495},
    'Vitor':{'Vitor':914845996}
}

ACTIONS = ['Incluir', 'Excluir', 'Alterar', 'Apenas Consultar']

while True:
    while True:
        print('\n')
        for index, x in enumerate(ACTIONS):
            print(f'{index+1}: {x}')
        break
    try:
        choice = int(input('\nQue ação deseja realizar?'))
        if choice == 1:
            try:
                addName = input('\nQuem você deseja adicionar a lista de contatos?')
                addName = addName.title()
                addNumber = int(input(f'\nQual é o número de {addName}? '))

                contacts.update({addName : addNumber})
                break
            except ValueError:
                print(f'\npenas números são aceitos. Digite o número para contato de {addNumber}')
        elif choice == 2:
            try:
                deleteContact = input('\nQue contato deseja excluir? ')
                deleteContact = deleteContact.title()
                del contacts[deleteContact]
                print(f'\n{deleteContact} excluído(a) dos contatos!')
                break
            except KeyError:
                print(f'\nContato {deleteContact} inexistente, impossível excluir. Digite um contato existente.')
        elif choice == 3:
            try:
                changePerson = input('\nContato a ser alterado: ')
                changePerson = changePerson.title()
                changeNumber = int(input(f'\nNovo número de {changePerson}: '))
                contacts[changePerson][changePerson]= changeNumber
                break
            except KeyError:
                print(f'\nContato {changePerson} inexistente, impossível alterar o número. Digite um contato existente.')
            except ValueError:
                print(f'\npenas números são aceitos. Digite o novo número para contato de {changePerson}')
        elif choice == 4:
            try:
                check = input(f'\nDe quem você quer ver o número? ')
                check = check.title()
                print('\nO número de {} é: {}\n'.format(check, contacts[check][check]))
                break
            except KeyError:
                print(f'\nContato {check} inexistente. Digite um contato existente.')
    except ValueError:
        print('\nEscolha inválida, digite uma opção disponível.')

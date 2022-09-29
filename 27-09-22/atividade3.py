d = {}
while True:
    try:
        qnt = int(input(f'\nQuantos animais deseja adicionar? '))

        for i in range(qnt):
            nome = input('Nome do animal: ')
            nome = nome.title()
            especie = input('Especie: ')
            especie = especie.title()
            d_nome = nome
            d[d_nome] = {}
            d[d_nome]['Nome do animal'] = nome
            d[d_nome]['Especie'] = especie

        choice = input(f'\nQue animal deseja ver?')
        choice = choice.title()

        print('\n{} é um {}.'.format(d[choice]['Nome do animal'], d[choice]['Especie']))
        break

    except ValueError:
        print('\nQuantidade inválida, digite um número\n')


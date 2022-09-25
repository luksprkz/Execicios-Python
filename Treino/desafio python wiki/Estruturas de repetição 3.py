DICIONARIO = {'f':'Feminino', 'm':'Masculino','s':'Solteiro(a)', 'c':'Casado(a)','v':'Viúvo(a)', 'd':'Divorciado(a)'}
nome = input('Qual é o nome? ')
while (len(nome)) <= 3:
    nome = input('Nome inválido, informe um nome válido?')
if (len(nome)) > 3:
    print('Tudo certo com o nome.')
idade = int(input('Qual é a idade? '))
while idade > 120:
    idade = int(input('Resposta inválida, informe a idade correta: '))
if idade <= 120:
    print('Tudo certo com o idade.')
salario = input('Qual é o salário? ')
print('Tudo certo com o salário.')    
while True:
    sexo = input('Qual é o sexo? \nf. \nm.\n: ')
    if sexo == "f" or sexo == 'm':
        sexo = DICIONARIO.get(sexo)
        print('Tudo ok com o sexo.')
        break       
    else:
        print("Resposta inválida, informe o sexo")
while True:
    estado_civil = input('Qual é o estado civil? \ns. \nc. \nv. \nd.')
    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd' :
        estado_civil = DICIONARIO.get(estado_civil)
        print('Tudo certo com o estado civil.')
        break
    else:
        print('Resposta inválida, informe um estado civil válido')

print(f'O seu nome é: {nome} \nSua idade é: {idade} anos \nSeu salário é: R${salario} \nO seu sexo é: {sexo} \nO seu estado civil é: {estado_civil}')

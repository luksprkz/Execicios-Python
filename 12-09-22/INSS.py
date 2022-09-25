#receber quanto o usuário é pago por hora e quantas horas por mês ele trabalha
salHora = float(input('Quanto você recebe por hora trabalhada?'))
horasTrab = int(input('Quantas horas você trabalha por mês?'))
#calcular quanto ele recebe bruto por mês e por ano
salMesBruto = salHora*horasTrab
#calcular os descontos feitos no salário - INSS:11%, IR:8%, Sindicato:5%, e quanto ele paga por ano para cada um destes
INSS = salMesBruto*0.11
IR = salMesBruto*0.08
Sindicato = salMesBruto*0.05
salMesLiq = ((salMesBruto-INSS)-IR)-Sindicato
#imprimir: salário bruto(mês e ano), IR, INSS, , Sindicato e salário líquido(mês e ano)
print('Seu salário bruto é de: R$',salMesBruto,'por mês e R$',salMesBruto*12,'por ano')
print('Você paga R$',INSS, 'por mês e R$', INSS*12, 'por ano ao INSS')
print('Você paga R$',IR, 'por mês e R$', IR*12, 'por ano de Imposto de Renda')
print('Você paga R$',Sindicato, 'por mês e R$', Sindicato*12, 'por ano ao Sindicato')
print('Seu salário líquido é de R$',salMesLiq,'por mês e R$',salMesLiq*12,'por ano' )
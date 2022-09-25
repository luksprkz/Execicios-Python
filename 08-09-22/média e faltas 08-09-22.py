#definir as médias  
nM, nJ, nA, nC = 6, 7, 8, 5
#definir a quantidade de faltas
fM, fJ, fA, fC = 20, 30, 10, 25

#definir se nota e presença são suficientes para aprovação e imprimir o resultado
M = 'aprovada' if nM >= 7 and fM <= 25 else 'reprovada'
print(f'Maria foi {M}')
J = 'aprovado' if nJ >= 7 and fJ <= 25 else 'reprovado'
print(f'José foi {J}')
A = 'aprovada' if nA >= 7 and fA <= 25 else 'reprovada'
print(f'Ana foi {A}')
C = 'aprovado' if nC >= 7 and fC <= 25 else 'reprovado'
print(f'Carlos foi {C}')
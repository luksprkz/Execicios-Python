#fazer a lista das temperaturas]
T = [-10, -8, 0, 1, 2, 5, -2, -4]
mínima = T[0]  # A escolha do primeiro elemento é arbitrária, poderia ser qualquer elemento válido
máxima = T[0]
soma = 0
for e in T:
    if e < mínima:
        mínima = e
    if e > máxima:
        máxima = e
    soma = soma + e
print(f"Temperatura máxima: {máxima} °C",f"\nTemperatura mínima: {mínima} °C",f"\nTemperatura média: {soma / len(T)} °C","\nfim do algoritimo")

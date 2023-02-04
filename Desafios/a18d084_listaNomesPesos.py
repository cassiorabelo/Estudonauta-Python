opcaoContinuar = 's'
individuo = []
pessoas = []
contador = 1
menorPeso = maiorPeso = 0

while opcaoContinuar == 's':
    individuo.append(str(input(f'Nome {contador}: ')))
    individuo.append(float(input(f'Peso {contador} (kg): ')))
    if contador == 1:
        menorPeso = maiorPeso = individuo[1]
    else:
        if individuo[1] < menorPeso:
            menorPeso = individuo[1]
        if individuo[1] > maiorPeso:
            maiorPeso = individuo[1]
    pessoas.append(individuo[:])
    individuo.clear()
    contador += 1
    while True:
        opcaoContinuar = str(input('Continuar (s/n): ')).strip().lower()
        if opcaoContinuar in 'sn':
            break

print(f'\nCadastros: {len(pessoas)}')
print(f'Maior peso: {maiorPeso}kg -', end=' ')
for pessoa in pessoas:
    if pessoa[1] == maiorPeso:
        print(pessoa[0], end=', ')
print('\b\b')
print(f'Menor peso: {menorPeso}kg -', end=' ')
for pessoa in pessoas:
    if pessoa[1] == menorPeso:
        print(pessoa[0], end=', ')
print('\b\b')

n = cont = soma = 0
while True:
    n = float(input(f'{cont + 1}º valor: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Soma dos {cont} valores: {soma}')

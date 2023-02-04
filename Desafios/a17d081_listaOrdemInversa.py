numbersList = []
continueOption = 's'
while continueOption == 's':
    value = float(input(f'Valor {len(numbersList) + 1}: '))
    numbersList.append(value)
    while True:
        continueOption = str(input('Deseja continuar? (s/n): ')).strip().lower()
        if continueOption in 'sn':
            break
numbersList.sort(reverse=True)
print(f'\nQuantidade de valores digitados: {len(numbersList)}')
print(f'Valores em ordem decrescente: {numbersList}')
print('Valor 5', 'encontrado' if 5 in numbersList else 'não encontrado.')

numbers = list()
continueOption = 's'
counter = 1
while continueOption == 's':
    value = float(input(f'Valor {counter}: '))
    counter += 1
    if value not in numbers:
        numbers.append(value)
        print('Valor inserido')
    else:
        print('Valor duplicado não inserido')
    while True:
        continueOption = str(input('Deseja continuar? (s/n): ')).strip().lower()
        if continueOption in 'sn':
            break
numbers.sort()
print(f'Valores inseridos: {numbers}')

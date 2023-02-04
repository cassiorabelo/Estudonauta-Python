numbers = []
evens = []
odds = []
continueOption = 's'
while continueOption == 's':
    value = int(input(f'Valor {len(numbers) + 1}: '))
    numbers.append(value)
    while True:
        continueOption = str(input('Deseja continuar? (s/n): ')).strip().lower()
        if continueOption in 'sn':
            break
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
print(f'\nLista completa: {numbers}',
      f'\nPares: {evens}',
      f'\nÍmpares: {odds}')

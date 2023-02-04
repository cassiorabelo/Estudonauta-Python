numbers = []
for c in range(1, 6):
    value = float(input(f'Valor {c}: '))
    if c == 1 or value > max(numbers):
        numbers.append(value)
        print('Valor inserido na posição final')
    else:
        for position, number in enumerate(numbers):
            if value <= number:
                numbers.insert(position, value)
                print(f'Valor inserido na posição {numbers.index(value)}')
                break
print(f'\nValores inseridos: {numbers}')

numbers = list()
for c in range(1, 6):
    numbers.append(int(input(f'Valor {c}: ')))

print(f'Maior: {max(numbers)} (valor(es)', end=' ')
for position, number in enumerate(numbers):
    if number == max(numbers):
        print(position + 1, end=' ')
print('\b)')

print(f'Menor: {min(numbers)} (valor(es)', end=' ')
for position, number in enumerate(numbers):
    if number == min(numbers):
        print(position + 1, end=' ')
print('\b)')

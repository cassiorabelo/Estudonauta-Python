from random import randint
numerosAleatorios = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('Números aleatórios: ', end='')
for numero in numerosAleatorios:
    print(numero, end=' ')
print(f'\nMaior: {max(numerosAleatorios)}')
print(f'Menor: {min(numerosAleatorios)}')

numeros = [[], []]
for entrada in range(1, 8):
    valor = int(input(f'Valor {entrada}: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print('~' * 40)
print(f'Pares: {numeros[0]}')
print(f'Ímpares: {numeros[1]}')

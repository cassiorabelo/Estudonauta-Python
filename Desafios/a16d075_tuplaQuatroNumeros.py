numerosDigitados = (int(input('Valor 1: ')), int(input('Valor 2: ')),
                    int(input('Valor 3: ')), int(input('Valor 4: ')))
pares = 0

print(f'Frequência do número 9: {numerosDigitados.count(9)}')

print(f'Posição do primeiro número 3:', end=' ')
if 3 in numerosDigitados:
    print(numerosDigitados.index(3) + 1)
else:
    print('não encontrado')

print(f'Números pares:', end=' ')
for numero in numerosDigitados:
    if numero % 2 == 0:
        print(numero, end=' ')
        pares += 1
if pares == 0:
    print('nenhum encontrado')

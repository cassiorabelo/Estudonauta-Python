soma = 0
cont = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        soma += c
        cont += 1
print('Soma dos ímpares múltiplos de 3 entre 1 e 500: {}'.format(soma))
print('Quantidade de números somados: {}'.format(cont))

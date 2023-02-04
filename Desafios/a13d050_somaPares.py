soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Número inteiro: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Quantidade de números pares informados = {}'.format(cont))
print('Soma dos pares = {}'.format(soma))

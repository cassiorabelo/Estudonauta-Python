n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor inteiro: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        if n % 2 != 0:
            impar += 1
print('Quantidade de pares: {}\nQuantidade de ímpares: {}'.format(par, impar))

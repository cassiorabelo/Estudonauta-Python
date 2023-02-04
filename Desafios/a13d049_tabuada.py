n = int(input('Número inteiro: '))
print('\033[034mTABUADA DO {}\033[m\n'.format(n))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))

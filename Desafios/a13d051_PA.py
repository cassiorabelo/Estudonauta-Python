n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('10 primeiros termos da PA: ')
for c in range(n, n + 9 * r + 1, r):
    print('{} '.format(c))

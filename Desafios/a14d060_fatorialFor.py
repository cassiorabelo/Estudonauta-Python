n = int(input('Número inteiro: '))
c = n
fatorial = 1
print('{}! = '.format(n), end='')
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(fatorial)

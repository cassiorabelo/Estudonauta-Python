n = int(input('Número inteiro: '))
verifica = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;34m{}\033[m'.format(c), end=' ')
        verifica += 1
    else:
        print('\033[0;37m{}\033[m'.format(c), end=' ')
if verifica == 2:
    print('\nO número {} é primo.'.format(n))
else:
    print('\nO número {} não é primo.'.format(n))

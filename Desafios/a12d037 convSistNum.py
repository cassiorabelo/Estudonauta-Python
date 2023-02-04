n = int(input('Número inteiro (base 10): '))
sistema = int(input('''Sistema para conversão:

1 - Binário
2 - Octal
3 - Hexadecimal

Opção: '''))
if sistema == 1:
    print('\n\033[1;32m{}\033[m na base 10 = \033[1;32m{}\033[m na base 2'.format(n, bin(n)[2:]))
elif sistema == 2:
    print('\n\033[1;32m{}\033[m na base 10 = \033[1;32m{}\033[m na base 8'.format(n, oct(n)[2:]))
elif sistema == 3:
    print('\n\033[1;32m{}\033[m na base 10 = \033[1;32m{}\033[m na base 16'.format(n, hex(n)[2:]))
else:
    print('\nOpção inválida.')

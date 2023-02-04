print('-' * 30)
print('{:^30}'.format('NÚMEROS POR EXTENSO'))
print('-' * 30)
numerosPorExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
                     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
                     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
optContinue = 's'
while optContinue == 's':
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
    print(f'Número digitado: {numerosPorExtenso[n]}')
    while True:
        optContinue = str(input('Deseja continuar? (S/N): ')).strip().lower()
        if optContinue in 'sn':
            break

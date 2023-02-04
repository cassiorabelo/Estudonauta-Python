def valida_int(texto):
    while True:
        try:
            valor_inserido = int(input(texto))
        except (ValueError, TypeError):
            print('\033[31mValor inválido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[34m(vazio)\033[m')
            return 0
        else:
            return valor_inserido


def valida_float(texto):
    while True:
        try:
            valor_inserido = float(input(texto))
        except (ValueError, TypeError):
            print('\033[31mValor inválido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[34m(vazio)\033[m')
            return 0
        else:
            return valor_inserido


inteiro = valida_int('Número inteiro: ')
real = valida_float('Número real: ')
print(f'Valores válidos digitados\nInteiro: {inteiro}\nReal: {real}')

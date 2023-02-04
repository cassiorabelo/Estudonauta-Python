def valida_inteiro(texto):
    while True:
        valor = input(texto)
        if valor.isnumeric():
            valor = int(valor)
            break
        print(f'\033[31mValor inválido.\033[m')
    return valor


numero = valida_inteiro('Digite um número inteiro: ')
print(f'Número digitado: {numero}')

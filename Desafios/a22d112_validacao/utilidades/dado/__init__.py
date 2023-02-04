def leia_dinheiro(texto):
    valor_valido = False
    while True:
        valor = str(input(texto)).replace(',', '.')
        if valor.count('.') <= 1:
            valor_checagem = valor.replace('.', '')
            if valor_checagem.isnumeric():
                valor = float(valor)
                valor_valido = True
        if valor_valido:
            break
        print(f'\033[31mValor inválido. \033[m')
    return valor

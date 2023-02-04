def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número.
    :param numero: o numero para o qual o fatorial deve ser calculado;
    :param show: opcional - define se são exibidos os passos do cálculo;
    :return: retorna o fatorial do numero informado
    """
    resultado_fatorial = 1
    for c in range(numero, 0, -1):
        resultado_fatorial *= c
        if show:
            print(c, end=' = ' if c == 1 else ' x ')
    return resultado_fatorial


print(fatorial(5, True))

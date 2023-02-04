def metade(valor=0):
    valor /= 2
    return valor


def dobro(valor=0):
    valor *= 2
    return valor


def aumento(valor=0, taxa=0):
    taxa /= 100
    valor *= (1 + taxa)
    return valor


def reducao(valor=0, taxa=0):
    taxa /= 100
    valor *= (1 - taxa)
    return valor


def monetario(valor, moeda_utilizada='R$'):
    valor = str(f'{moeda_utilizada} {valor:.2f}').replace('.', ',')
    return valor

def metade(valor):
    valor /= 2
    return valor


def dobro(valor):
    valor *= 2
    return valor


def aumento(valor, taxa):
    taxa /= 100
    valor *= (1 + taxa)
    return valor


def reducao(valor, taxa):
    taxa /= 100
    valor *= (1 - taxa)
    return valor

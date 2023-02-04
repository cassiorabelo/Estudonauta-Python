def metade(valor=0, formato_monetario=True):
    valor /= 2
    if formato_monetario:
        return monetario(valor)
    else:
        return valor


def dobro(valor=0, formato_monetario=True):
    valor *= 2
    if formato_monetario:
        return monetario(valor)
    else:
        return valor


def aumento(valor=0, taxa=0, formato_monetario=True):
    taxa /= 100
    valor *= (1 + taxa)
    if formato_monetario:
        return monetario(valor)
    else:
        return valor


def reducao(valor=0, taxa=0, formato_monetario=True):
    taxa /= 100
    valor *= (1 - taxa)
    if formato_monetario:
        return monetario(valor)
    else:
        return valor


def monetario(valor, moeda_utilizada='R$'):
    valor = str(f'{moeda_utilizada} {valor:.2f}').replace('.', ',')
    return valor

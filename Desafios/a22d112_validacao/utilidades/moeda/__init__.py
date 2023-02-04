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


def resumo(valor, taxa_aumento=0, taxa_reducao=0):
    quadro_resumo = dict()
    quadro_resumo['Preço analisado'] = monetario(valor)
    quadro_resumo['Dobro do preço'] = dobro(valor)
    quadro_resumo['Metade do preço'] = metade(valor)
    quadro_resumo[f'{taxa_aumento}% de aumento'] = aumento(valor, taxa_aumento)
    quadro_resumo[f'{taxa_reducao}% de redução'] = reducao(valor, taxa_reducao)
    print('-' * 35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-' * 35)
    for chave, valor in quadro_resumo.items():
        print(f' {chave:<22}{valor}')
    print('-' * 35)

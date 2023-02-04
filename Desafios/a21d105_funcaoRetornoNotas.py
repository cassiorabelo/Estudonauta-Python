def analisar_notas(*notas, exibir_situacao=False):
    """
    Análise de notas informadas, verificando a maior, a menor e a média;
    :param notas: notas informadas para análise;
    :param exibir_situacao: opcional - indica se a situação deve ser exibida;
    :return:dicionário com as informações de análise das notas.
    """
    analise_notas = dict()
    analise_notas['Total'] = len(notas)
    analise_notas['Maior'] = max(notas)
    analise_notas['Menor'] = min(notas)
    analise_notas['Média'] = sum(notas) / len(notas)
    if exibir_situacao:
        if analise_notas['Média'] >= 7:
            analise_notas['Situação'] = 'boa'
        elif analise_notas['Média'] >= 5:
            analise_notas['Situação'] = 'regular'
        else:
            analise_notas['Situação'] = 'ruim'
    return analise_notas


print(analisar_notas(9, 8, 9.3, 7, 9, 9.5, 10, 4, exibir_situacao=True))
help(analisar_notas)

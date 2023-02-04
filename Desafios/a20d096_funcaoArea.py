def calculo_area(def_largura, def_comprimento):
    area = def_largura * def_comprimento
    print(f'Área: {def_largura:.2f}m x {def_comprimento:.2f}m = {area:.2f}m²')


print('Cálculo de área')
print('-' * 20)
larguraInformada = float(input('Largura (m): '))
comprimentoInforado = float(input('Comprimento (m): '))
calculo_area(larguraInformada, comprimentoInforado)

altura = float(input('Informe a altura da parede (m): '))
largura = float(input('Informe a largura da parde (m): '))
area = altura * largura
rendimentoTinta = 2
necessidadeTinta = area / rendimentoTinta
print('Área da parede: {}m²\nTinta necessária: {}l'.format(area, necessidadeTinta))

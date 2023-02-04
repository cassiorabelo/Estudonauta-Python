from Desafios.a22d107_analisePreco import moeda

preco = float(input('Preço (R$): '))
print(f'Metade de R$ {preco} = R$ {moeda.metade(preco)}')
print(f'Dobro de R$ {preco} = R$ {moeda.dobro(preco)}')
print(f'Aumento de 10% em R$ {preco} = R$ {moeda.aumento(preco, 10)}')
print(f'Redução de 13% em R$ {preco} = R$ {moeda.reducao(preco, 13)}')

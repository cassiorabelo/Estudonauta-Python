from Desafios.a22d109_formatoMonetarioEmbutidoFuncoes import moeda

preco = float(input('Preço (R$): '))
print(f'Metade de {moeda.monetario(preco)} = {moeda.metade(preco)}')
print(f'Dobro de {moeda.monetario(preco)} = {moeda.dobro(preco)}')
print(f'Aumento de 10% em {moeda.monetario(preco)} = {moeda.aumento(preco, 10)}')
print(f'Redução de 13% em {moeda.monetario(preco)} = {moeda.reducao(preco, 13)}')

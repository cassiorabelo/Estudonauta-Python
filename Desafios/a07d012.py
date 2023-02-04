preco = float(input('Preço do produto (R$): '))
desc = 0.05
novoPreco = preco * (1 - desc)
print('Novo preço, com {}% de desconto: R$ {:.2f}'.format(desc*100, novoPreco))

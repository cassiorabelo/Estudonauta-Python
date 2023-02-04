print('LISTA DE COMPRAS')

nomeMaisBarato = ''
nItens = valorTotal = nProdutosMaisde1000 = precoMaisBarato = 0

while True:
    optContinua = 'x'

    print(f'\nItem {nItens + 1}')
    nomeItem = str(input('Nome do item: '))
    precoItem = float(input('Preço do item (R$): '))
    valorTotal += precoItem

    if precoItem > 1000:
        nProdutosMaisde1000 += 1
    if precoItem < precoMaisBarato or nItens == 0:
        precoMaisBarato = precoItem
        nomeMaisBarato = nomeItem

    nItens += 1

    while optContinua not in 'sn':
        optContinua = str(input('Continua? (S/N) ')).strip().lower()
    if optContinua == 'n':
        break

print(f'\nValor total: R$ {valorTotal:.2f}')
print(f'Quantidade de produtos com valor superior a R$ 1000.00: {nProdutosMaisde1000}')
print(f'Produto mais barato: {nomeMaisBarato} (R$ {precoMaisBarato:.2f})')

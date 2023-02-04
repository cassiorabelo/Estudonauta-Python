produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9)

print('~' * 50)
print('{:^50}'.format('LISTA DE PREÇOS'))
print('~' * 50)

for posicao, produto in enumerate(produtos):
    if posicao % 2 == 0:
        print(f'{produto:.<40}', end='')
    else:
        print(f' R$ {produto:>6.2f}')
print('~' * 50)

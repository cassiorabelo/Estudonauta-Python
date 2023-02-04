historico = dict()
golsPartidas = list()
golsTotais = 0
historico['nome'] = str(input('Nome do jogador: '))
quantidadePartidas = int(input('Quantidade de partidas: '))
for partida in range(1, quantidadePartidas + 1):
    golsPartidas.append(int(input(f'Quantidade de gols na partida {partida}: ')))
historico['gols'] = golsPartidas[:]
historico['total'] = sum(golsPartidas)

print('-=' * 30 + '-')
print(historico)

print('-=' * 25 + '-')
for chave, valor in historico.items():
    print(f'O campo {chave} tem o valor {valor}.')

print('-=' * 25 + '-')
print(f'O jogador {historico["nome"]} jogou {len(historico["gols"])} partidas')
for indice, gols in enumerate(historico['gols']):
    print(f'\t=> Na partida {indice + 1}, fez {gols} gols.')
print(f'Foi um total de {historico["total"]} gols.')

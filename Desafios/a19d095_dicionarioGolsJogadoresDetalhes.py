historicoJogador = dict()
historicos = list()
golsPartidas = list()

while True:
    historicoJogador['Nome'] = str(input('Nome do jogador: '))
    quantidadePartidas = int(input('Quantidade de partidas: '))
    for partida in range(1, quantidadePartidas + 1):
        golsPartidas.append(int(input(f'\tQuantidade de gols na partida {partida}: ')))
    historicoJogador['Gols'] = golsPartidas[:]
    historicoJogador['Total'] = sum(golsPartidas)
    historicos.append(historicoJogador.copy())
    golsPartidas.clear()
    historicoJogador.clear()
    while True:
        opcaoContinuar = str(input('Continuar (S/N): ')).strip().upper()
        if opcaoContinuar in 'SN':
            break
        print('Opção inválida. ', end='')
    print('-' * 47)
    if opcaoContinuar == 'N':
        break

print(f'{"N":^5}{"Nome":<15}{"Gols":<20}{"Total":<5}')
print('- ' * 23 + '-')
for indice, jogador in enumerate(historicos):
    print(f'{indice + 1:^5}{jogador["Nome"]:<15}{str(jogador["Gols"]):<20}{jogador["Total"]:<5}')
print('-' * 47)

while True:
    opcaoDetalhar = int(input('Detalhar jogador N (999 para encerrar): '))
    if opcaoDetalhar == 999:
        break
    elif opcaoDetalhar <= 0 or opcaoDetalhar > len(historicos):
        print('Opção inválida. ', end='')
    else:
        opcaoDetalhar -= 1
        print('-' * 47)
        print(f'Detalhes do jogador {historicos[opcaoDetalhar]["Nome"].upper()}')
        for jogo, gols in enumerate(historicos[opcaoDetalhar]["Gols"]):
            print(f'\tNo jogo {jogo + 1} fez {gols} gols.')
        print('-' * 47)

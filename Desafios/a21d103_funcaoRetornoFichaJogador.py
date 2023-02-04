def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nomeJogador = str(input('Nome do jogador: '))
golsJogador = str(input('Número de gols: '))
ficha(nomeJogador, golsJogador)

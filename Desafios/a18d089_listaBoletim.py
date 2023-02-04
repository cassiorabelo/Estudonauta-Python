opcaoContinua = 's'
boletins = list()
opcaoDetalhes = 0

while opcaoContinua == 's':
    aluno = str(input(f'Aluno {len(boletins) + 1}: '))
    notas = [float(input('Nota 1: ')), float(input('Nota 2: '))]
    media = (notas[0] + notas[1]) / 2
    boletins.append([aluno, notas, media])
    while True:
        opcaoContinua = str(input('Continuar (s/n): '))
        if opcaoContinua in 'sn':
            break
print('-' * 30)
print(f'{"N":^5}{"Aluno":^18}{"Média":^7}')
print('-' * 30)
for indice, registro in enumerate(boletins):
    print(f'{indice:^5}{registro[0]:<18}{registro[2]:^7.1f}')
print('-' * 30)

while True:
    opcaoDetalhes = int(input('Exibir detalhes (99 para encerrar). N: '))
    if opcaoDetalhes == 99:
        break
    if 0 <= opcaoDetalhes < len(boletins):
        print('-' * 30)
        print(f'Aluno: {boletins[opcaoDetalhes][0]}')
        print(f'Notas: {boletins[opcaoDetalhes][1][0]:.1f} / {boletins[opcaoDetalhes][1][1]:.1f}')
        print('-' * 30)

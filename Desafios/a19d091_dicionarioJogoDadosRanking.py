from random import randint
from time import sleep
from operator import itemgetter
textoAzul = '\033[34m'
limpaFormatacao = '\033[m'

resultado = dict()
for jogador in range(1, 7):
    resultado[f'Jogador {jogador}'] = randint(1, 6)

print(f'{textoAzul}JOGADAS{limpaFormatacao}')
for jogador, jogada in resultado.items():
    print(f'\t{jogador}: {jogada}')
    sleep(1)

ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)
print(f'\n{textoAzul}RANKING{limpaFormatacao}')
for indice, jogador in enumerate(ranking):
    print(f'{indice + 1}º {jogador[0]}')

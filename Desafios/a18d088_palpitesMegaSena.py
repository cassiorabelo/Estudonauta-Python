from random import randint
from time import sleep
print('.*' * 20)
print(f'{"Gerador de jogos para a Mega Sena":^40}')
print('.*' * 20)
cadaJogo = []
todosJogos = []
quantidadeJogos = int(input('Quantidade de jogos: '))
for c in range(0, quantidadeJogos):
    while len(cadaJogo) < 6:
        numeroJogado = randint(1, 60)
        if numeroJogado not in cadaJogo:
            cadaJogo.append(numeroJogado)
    cadaJogo.sort()
    todosJogos.append(cadaJogo[:])
    cadaJogo.clear()

print('.' * 40)
for indice, jogo in enumerate(todosJogos):
    sleep(1)
    print(f'Jogo {indice + 1}: {jogo}')
sleep(1)
print('.' * 40)
sleep(1)
print('May the luck be with you *.*')
sleep(1)

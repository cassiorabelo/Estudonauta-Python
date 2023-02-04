from random import randint
from time import sleep
print('-' * 30)
print('    PEDRA, PAPEL, TESOURA')
print('-' * 30)
escolhaJogador = int(input('''Escolha sua jogada:

1 - PEDRA
2 - PAPEL
3 - TESOURA

Opção: '''))
if escolhaJogador != 1 and escolhaJogador != 2 and escolhaJogador != 3:
    print('\nOpção inválida ¬¬')
else:
    if escolhaJogador == 1:
        print('\nVocê escolheu PEDRA')
    elif escolhaJogador == 2:
        print('\nVocê escolheu PAPEL')
    elif escolhaJogador == 3:
        print('\nVocê escolheu TESOURA')
    escolhaPrograma = randint(1, 3)
    print('\nEu escolhi', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('. ', end='')
    sleep(1.2)
    if escolhaPrograma == 1:
        print('PEDRA\n')
    elif escolhaPrograma == 2:
        print('PAPEL\n')
    elif escolhaPrograma == 3:
        print('TESOURA\n')
    sleep(1)
    if escolhaJogador == escolhaPrograma:
        print('\nEmpatamos :|')
    elif escolhaJogador == 1 and escolhaPrograma == 3 \
            or escolhaJogador == 2 and escolhaPrograma == 1 \
            or escolhaJogador == 3 and escolhaPrograma == 2:
        print('Você ganhou :(')
    else:
        print('Ganhei! :D')
sleep(10)

from random import randint
from time import sleep
seq = ''
espera = 1
print(seq)
sleep(espera)
p1 = seq
while p1 == seq:
    proximo = str(randint(0, 9))
    seq = str(seq + proximo)
    for c in range(0, len(seq)):
        print(seq[c], end='')
        sleep(0.5)
    espera += 0.2
    sleep(espera)
    # limpar a tela
    p1 = str(input('\nRepita a sequência: '))
    sleep(0.8)
print('Você acertou até a sequência de {} dígitos \o/'.format(len(seq) - 1))

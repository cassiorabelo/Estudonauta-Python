from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 20)
print('Estou pensando em um número inteiro de 0 a 5. Tente adivinhar qual é o número:')
print('-=-' * 20)
palpite = int(input())
print('...')
sleep(1)
print('...')
sleep(1)
print('...')
sleep(2)
if palpite == n:
    print('Acertou! \o/')
else:
    print('Não :/\nPensei no {}'.format(n))

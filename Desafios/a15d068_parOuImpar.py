from random import randint
from time import sleep
optP1 = soma = cont = 0

print('~' * 40)
print('PAR ou ÍMPAR?')

while True:
    while optP1 != 1 and optP1 != 2:
        print('~' * 40)
        optP1 = int(input('Escolha:\n(1) Ímpar\n(2) Par\nOpção: '))
    nP1 = int(input('Agora o número: '))
    nCpu = randint(0, 5)
    soma = nP1 + nCpu
    print(f'Eu escolhi... ', end='')
    sleep(1.2)
    print(nCpu)
    sleep(0.8)
    if (optP1 + soma) % 2 != 0:
        print('\nGanhei! :]\n')
        sleep(1.5)
        break
    cont += 1
    print('\nGANHOU! \o/')
    sleep(1.5)
    optP1 = 0
print(f'Você {cont} x 1 Eu')

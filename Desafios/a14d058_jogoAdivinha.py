from random import randint
nCPU = randint(1, 10)
nP1 = int(input('Adivinhe o número de 1 a 10 em que estou pensando: '))
jogadas = 1
while nP1 != nCPU:
    jogadas += 1
    print('Não é esse :(')
    if nP1 < nCPU:
        nP1 = int(input('Tente um maior: '))
    elif nP1 > nCPU:
        nP1 = int(input('Tente um menor: '))
if jogadas == 1:
    print('Acertou! De primeira! :D')
else:
    print('Acertou! :D\nVocê precisou de {} palpites.'.format(jogadas))

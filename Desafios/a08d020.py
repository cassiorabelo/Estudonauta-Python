import random
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
# sorteio = sample(lista, k=4), com k igual ao número de amostras
print('A ordem sorteada é: {}'.format(lista))

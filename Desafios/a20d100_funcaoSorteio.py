from random import randint


def sorteia(lista_numeros):
    for c in range(0, 5):
        lista_numeros.append(randint(0, 9))
    print(f'Números sorteados:', end=' ')
    for numero in lista_numeros:
        print(numero, end=' ')
    print()


def soma_pares(lista_numeros):
    soma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'Soma dos valores pares em {lista_numeros} = {soma}')


numeros = list()
sorteia(numeros)
soma_pares(numeros)

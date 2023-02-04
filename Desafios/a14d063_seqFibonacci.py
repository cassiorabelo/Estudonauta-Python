print('-' * 30 + '\nSequência de Fibonacci\n' + '-' * 30)
n = int(input('Número de termos a exibir: '))
anterior = 0
atual = 1
proximo = 1
c = 2
print('\n{} primeiros termos da sequência:'.format(n))
print(anterior, end=', ')
print(atual, end=', ')
while c < n:
    c += 1
    proximo = atual + anterior
    print(proximo, end='')
    print(', ' if c < n else '', end='')
    anterior = atual
    atual = proximo
print('\n\nFim :)')
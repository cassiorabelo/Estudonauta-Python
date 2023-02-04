n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
ordem = [n1, n2, n3]
if n1 > n2:
    ordem = [n2, n1, n3]
if n2 > n3:
    ordem = [n3, n2, n1]
menor = ordem[0]
maior = ordem[-1]
print('O menor entre os três números é o {}'.format(menor))
print('O maior entre os três números é o {}'.format(maior))

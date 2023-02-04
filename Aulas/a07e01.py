n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma entre {0} e {1} é {2} \nO produto entre {0} e {1} é {3}'.format(n1, n2, s, m), end=' >>> ')
print('A divisão entre {} e {} é {:.3f}'.format(n1, n2, d))

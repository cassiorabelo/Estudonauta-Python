n = int(input('Número de 0 a 9999: '))
und = n % 10
dez = n % 100 // 10
cen = n % 1000 // 100
mil = n // 1000
print('Unidade: {}\nDezena: {}\nCentena: {}\nUnid. milhar: {}'.format(und, dez, cen, mil))

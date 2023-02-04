# from math import sqrt, pow
# c1 = float(input('Cateto 1: '))
# c2 = float(input('Cateto 2: '))
# h = sqrt(pow(c1, 2) + pow(c2, 2))
# print('Hipotenusa: {:.2f}'.format(h))

from math import hypot
c1 = float(input('Cateto 1: '))
c2 = float(input('Cateto 2: '))
h = hypot(c1, c2)
print('Hipotenusa: {:.2f}'.format(h))

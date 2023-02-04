import math
a = float(input('Informe um ângulo qualquer (graus): '))
radA = math.radians(a)
sinA = math.sin(radA)
cosA = math.cos(radA)
tanA = math.tan(radA)
print('sen({}°) = {:.3f}'.format(a, sinA))
print('cos({}°) = {:.3f}'.format(a, cosA))
print('tan({}°) = {:.3f}'.format(a, tanA))

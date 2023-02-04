primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador = 1
print('10 primeiros termos da PA:')
while contador <= 10:
    print('{}'.format(termo), end='')
    print(', ' if contador < 10 else '', end='')
    termo += razao
    contador += 1
print('\n\nCabou :)')

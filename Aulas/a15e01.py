n = s = 0
while True:
    n = int(input('Valor: '))
    if n == 999:
        break
    s += n
print(f'Soma dos valores: {s}')

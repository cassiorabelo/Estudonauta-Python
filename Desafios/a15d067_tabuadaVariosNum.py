while True:
    n = int(input('Tabuada do número: '))
    if n < 0:
        break
    print('-' * 40)
    for c in range(1, 11):
        prod = n * c
        print(f'{n} x {c} = {prod}')
    print('-' * 40, end='\n')
print('\nFim :)')

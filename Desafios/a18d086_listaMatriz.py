matriz = [[], [], []]
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Valor [{linha}, {coluna}]: '))
        matriz[linha].append(valor)
print('\nMatriz:')
for linha in matriz:
    print(f'\n{linha[0]:^5}{linha[1]:^5}{linha[2]:^5}')

matriz = [[], [], []]
somaPares = somaTerceiraColuna = maiorSegundaLinha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Valor [{linha}, {coluna}]: '))
        matriz[linha].append(valor)
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
        if coluna == 2:
            somaTerceiraColuna += matriz[linha][coluna]
        if linha == 1 and coluna == 0 or matriz[1][coluna] > maiorSegundaLinha:
            maiorSegundaLinha = matriz[1][coluna]

print('\nMatriz:')
for linha in matriz:
    print(f'\n{linha[0]:^5}{linha[1]:^5}{linha[2]:^5}')
print(f'\nSoma pares: {somaPares}')
print(f'Soma terceira coluna: {somaTerceiraColuna}')
print(f'Maior valor da segunda linha: {maiorSegundaLinha}')

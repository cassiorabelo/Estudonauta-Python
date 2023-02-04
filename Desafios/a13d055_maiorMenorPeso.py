maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Peso {} (kg): '.format(c+1)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('''Maior peso: {:.2f}kg
Menor peso: {:.2f}kg'''.format(maior, menor))

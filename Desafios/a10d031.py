distancia = float(input('Distância da viagem (km): '))
if distancia <= 200:
    precoKm = 0.50
else:
    precoKm = 0.45
precoTotal = distancia * precoKm
print('Preço da viagem: R$ {:.2f}'.format(precoTotal))

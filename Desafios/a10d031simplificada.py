distancia = float(input('Distância da viagem (km): '))
precoKm = 0.50 if distancia <= 200 else 0.45
print('Preço da viagem: R$ {:.2f}'.format(distancia * precoKm))
N
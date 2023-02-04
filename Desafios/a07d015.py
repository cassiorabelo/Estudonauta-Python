diarias = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Quantos quilômetros foram rodados? '))
precoDiarias = 60
precoKm = 0.15
total = diarias * precoDiarias + km * precoKm
print('\nO total a pagar é de R$ {:.2f}'.format(total))

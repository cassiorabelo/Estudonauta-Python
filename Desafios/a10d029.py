velocidade = int(input('Velocidade (km/h): '))
velocidadeMax = 80
multaKm = 7
multaTotal = (velocidade - velocidadeMax) * 7
if velocidade > velocidadeMax:
    print('Velocidade excedida! Multa: R$ {:.2f}'.format(multaTotal))
else:
    print('Velocidade dentro do limite permitido.')
print('Tenha um bom dia! Dirija com segurança!')
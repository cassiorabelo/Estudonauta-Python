print('=' * 50)
print('{:^50}'.format('CAIXA ELETRÔNICO - Banco CeV'))
print('-' * 50)
print('Solicitação de Saque \nCédulas disponíveis: R$ 50, R$ 20, R$ 10, R$ 1')
print('=' * 50)
valorSaque = int(input('\nValor (R$): '))
valorCedula = 50
nCedulas = 0
valorRestante = valorSaque

print('-' * 50)
print('O saque será composto por:')
while True:
    if valorRestante >= valorCedula:
        valorRestante -= valorCedula
        nCedulas += 1
    else:
        if nCedulas > 0:
            print(f'{nCedulas} cédula(s) de R$ {valorCedula}')
        nCedulas = 0
        if valorCedula == 50:
            valorCedula = 20
        elif valorCedula == 20:
            valorCedula = 10
        elif valorCedula == 10:
            valorCedula = 1

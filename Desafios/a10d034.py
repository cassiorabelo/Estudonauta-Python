salario = float(input('Salário: '))
if salario > 1250:
    txAumento = 0.10
else:
    txAumento = 0.15
aumento = salario * txAumento
novoSalario = salario + aumento
print('Aumento: {:.2f}\nNovo salário: {:.2f}'.format(aumento, novoSalario))

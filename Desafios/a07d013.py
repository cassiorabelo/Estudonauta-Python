sal = float(input('Salário atual: '))
aumento = 0.15
novoSalario = sal * (1 + aumento)
print('O novo salário, após {}% de aumento, é de R$ {:.2f}'.format(aumento * 100, novoSalario))

nome = 'José'
idade = 33
salario = 7987.3
print('O %s tem %d anos e recebe R$ %.2f' % (nome, idade, salario))  # Python 2
print('O {} tem {} anos e recebe R$ {:.2f}'.format(nome, idade, salario))  # Python 3
print(f'O {nome} tem {idade} anos e recebe R$ {salario:.2f}')  # Python 3.6+

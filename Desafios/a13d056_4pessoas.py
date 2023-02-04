somaIdades = 0
maiorIdade = 0
maisVelho = ''
contHomens = 0
contMulheres20menos = 0
contTodos = 0
for c in range(1, 5):
    print('\033[1;034mPESSOA {}\033[m'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F/M): '))
    somaIdades += idade
    contTodos += 1
    if sexo in 'Mm':
        contHomens += 1
        if idade > maiorIdade:
            maiorIdade = idade
            maisVelho = nome
    if sexo in 'Ff' and idade < 20:
        contMulheres20menos += 1
    print('-'*20)
mediaIdades = somaIdades / contTodos
print('Média de idade: {:.2f}'.format(mediaIdades))
if contHomens > 0:
    print('Homem mais velho: {} ({} anos)'.format(maisVelho, maiorIdade))
else:
    print('Homem mais velho: N/A')
print('Mulheres com menos de 20 anos: {}'.format(contMulheres20menos))

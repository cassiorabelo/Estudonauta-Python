nCadastros = nMaiores18 = nHomens = nMulheresMenoresDe20 = 0
print('CADASTRO DE PESSOAS')
while True:
    sexo = optContinua = 'x'

    print(f'\nCadastro {nCadastros + 1}')
    idade = int(input('Idade: '))
    while sexo not in 'fm':
        sexo = str(input('Sexo (F/M): ')).lower()
    nCadastros += 1
    if idade > 18:
        nMaiores18 += 1
    if sexo == 'm':
        nHomens += 1
    if idade < 20 and sexo == 'f':
        nMulheresMenoresDe20 += 1
    while optContinua not in 'sn':
        optContinua = str(input('Continua? (S/N) ')).lower()
    if optContinua == 'n':
        break

print('\nTotais de cadastros: ')
print(f'Maiores de 18 anos - {nMaiores18}')
print(f'Homens cadatrados - {nHomens}')
print(f'Mulheres menores de 20 anos - {nMulheresMenoresDe20}')

acimaMediaIdade = list()
cadastro = dict()
mediaIdades = 0
mulheres = list()
pessoas = list()
while True:
    cadastro['Nome'] = str(input('Nome: '))
    while True:
        cadastro['Sexo'] = str(input('Sexo (F/M): ')).strip().upper()
        if cadastro['Sexo'] in 'FM':
            break
        print('Opção inválida. ', end='')
    cadastro['Idade'] = int(input('Idade: '))
    pessoas.append(cadastro.copy())
    while True:
        opcaoContinuar = str(input('Continuar (S/N): ')).strip().upper()
        if opcaoContinuar in 'SN':
            break
        print('Opção inválida.', end=' ')
    print('-' * 30)
    if opcaoContinuar == 'N':
        break

print(f'Cadastros: {len(pessoas)}')

for cadastro in pessoas:
    mediaIdades += cadastro['Idade'] / len(pessoas)
print(f'Média de idade {mediaIdades:.1f}')

for cadastro in pessoas:
    if cadastro['Sexo'] == 'F':
        mulheres.append(cadastro['Nome'])
print('Mulheres cadastradas:')
if len(mulheres) > 0:
    for mulher in mulheres:
        print(f'\t{mulher}')
else:
    print('\tNenhuma mulher encontrada.')

for cadastro in pessoas:
    if cadastro['Idade'] > mediaIdades:
        acimaMediaIdade.append(cadastro.copy())
print('Pessoas com idade acima da média:')
if len(acimaMediaIdade) > 0:
    for cadastro in acimaMediaIdade:
        if cadastro['Idade'] > mediaIdades:
            print('\t', end='')
            for chave, valor in cadastro.items():
                print(f'{chave}: {valor}; ', end='')
            print()
else:
    print('\tNenhuma pessoa encontrada.')

print(f'\n{" FIM ":-^30}')

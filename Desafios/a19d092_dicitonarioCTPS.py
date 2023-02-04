from datetime import date
anoAtual = date.today().year
cadastro = {'Nome': str(input('Nome: ')),
            'Idade': anoAtual - int(input('Ano de nascimento: ')),
            'CTPS': int(input('Nº CTPS (inserir 0 caso não possua): '))}
if cadastro['CTPS'] != 0:
    cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Idade para aposentadoria'] = cadastro['Ano de contratação'] + 35 - anoAtual + cadastro['Idade']
print('-=' * 25 + '-')
for chave, valor in cadastro.items():
    print(f'{chave}: {valor}')

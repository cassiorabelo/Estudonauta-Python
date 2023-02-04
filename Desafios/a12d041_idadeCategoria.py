import datetime
anoNasc = int(input('Ano de nasccimento: '))
agora = datetime.datetime.now()
anoAtual = int(agora.strftime('%Y'))
idade = anoAtual - anoNasc
print('Categoria:')
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')

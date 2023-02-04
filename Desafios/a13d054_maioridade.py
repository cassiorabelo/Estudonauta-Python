from datetime import date
anoAtual = date.today().year
nMaiores = 0
nMenores = 0
for c in range(0, 7):
    anoNasc = int(input('Ano de nascimento pessoa {}: '.format(c+1)))
    if anoAtual - anoNasc >= 18:
        nMaiores += 1
    else:
        nMenores += 1
print('''Atingiram a maioridade: {}
Não atingiram a maioridade: {}'''.format(nMaiores, nMenores))

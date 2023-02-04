from datetime import date
sexo = int(input('''Sexo: 
[1] Feminino
[2] Masculino
Opção: '''))
if sexo == 1:
    print('Não há obrigatoriedade para alistamento.')
elif sexo == 2:
    anoAtual = date.today().year
    anoNasc = int(input('Ano de nascimento: '))
    idade = anoAtual - anoNasc
    print('{} ano(s) em {}.'.format(idade, anoAtual))
    if idade == 18:
        print('O ano de alistamento é o atual.')
    elif idade > 18:
        diferenca = idade - 18
        anoAlist = anoAtual - diferenca
        print('O ano de alistamento ocorreu há {} ano(s), em {}.'.format(diferenca, anoAlist))
    elif idade < 18:
        diferenca = 18 - idade
        anoAlist = anoAtual + diferenca
        print('O ano de alistamento ocorrerá daqui a {} ano(s), em {}.'.format(diferenca, anoAlist))
else:
    print('Opção inválida.')

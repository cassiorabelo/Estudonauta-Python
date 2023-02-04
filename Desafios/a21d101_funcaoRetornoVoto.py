def voto(ano_nascimento):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return f'{idade} anos: voto NÃO PERMITIDO'
    elif 16 <= idade < 18 or idade > 65:
        return f'{idade} anos: voto FACULTATIVO'
    else:
        return f'{idade} anos: voto OBRIGATÓRIO'


anoNascimento = int(input('Ano de nascimento: '))
print(voto(anoNascimento))

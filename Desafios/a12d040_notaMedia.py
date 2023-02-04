nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Média: {}\n\033[31mREPROVADO'.format(media))
elif 5 <= media < 7:
    print('Média: {}\n\033[34mRECUPERAÇÃO'.format(media))
else:
    print('Média: {}\n\033[32mAPROVADO'.format(media))

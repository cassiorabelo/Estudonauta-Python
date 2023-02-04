sexo = str(input('Sexo (F/M): ')).strip()
while sexo not in 'FfMm':
    print('Opção inválida.')
    sexo = str(input('Sexo (F/M): ')).lower().strip()
print('Obrigado!')

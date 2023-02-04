resultadoAluno = {}
resultadoAluno['Nome'] = str(input('Nome: '))
resultadoAluno['Média'] = float(input('Média: '))
if resultadoAluno['Média'] >= 7:
    resultadoAluno['Situação'] = 'Aprovado'
elif 7 > resultadoAluno['Média'] >= 5:
    resultadoAluno['Situação'] = 'Recuperação'
else:
    resultadoAluno['Situação'] = 'Reprovado'
for chave, valor in resultadoAluno.items():
    print(f'{chave}: {valor}')

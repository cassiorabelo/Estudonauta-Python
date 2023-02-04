infoIndividuo = []
cadastroPessoas = []
qtdMaiores = qtdMenores = 0
for pessoa in range(1,4):
    infoIndividuo.append(str(input(f'Nome {pessoa}: ')))
    infoIndividuo.append(int(input(f'Idade {pessoa}: ')))
    cadastroPessoas.append(infoIndividuo[:])
    infoIndividuo.clear()

for pessoa in cadastroPessoas:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
        qtdMaiores += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        qtdMenores += 1

print(f'Quantidade de maiores: {qtdMaiores} \nQuantidade de menores: {qtdMenores}')
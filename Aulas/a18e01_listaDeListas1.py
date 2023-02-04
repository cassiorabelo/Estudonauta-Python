dadosIndividuo = list()
dadosIndividuo.append('Gustavo')
dadosIndividuo.append(40)
cadastroPessoas = list()
cadastroPessoas.append(dadosIndividuo[:]) # É necessário fazer a cópia da lista filha. Se adicionada a própria lista,
                                          # alterações reletirão em todos os objetdos da lista mãe
dadosIndividuo[0] = ('Maria')
dadosIndividuo[1] = (22)
cadastroPessoas.append(dadosIndividuo[:])

print(cadastroPessoas)

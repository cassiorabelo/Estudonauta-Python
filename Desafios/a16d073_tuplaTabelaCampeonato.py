classificacao = ('Cruzeiro', 'Grêmio', 'Vasco', 'Bahia', 'Sampaio Corrêa',
                 'Ituano', 'Sport', 'Criciúma', 'Londrina', 'Guarani',
                 'CRB', 'Ponte Preta', 'Vila Nova', 'Chapecoense', 'Tombense',
                 'Novorizontino', 'CSA', 'Brusque', 'Operário-PR', 'Náutico')
print(f'5 primeiros colocados: {classificacao[0:5]}')
print(f'4 últimos colocados: {classificacao[-4:]}')
print(f'Times em ordem alfabética: {sorted(classificacao)}')
print(f'Posição da Chapecoense: {classificacao.index("Chapecoense") + 1}º')

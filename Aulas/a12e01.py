nome = str(input('Nome: ')).title().strip()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'José':
    print('Seu nome é muito popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica':
    print('Belo nome!')
else:
    print('Que nome comum.')
print('Tenha um bom dia, {}!'.format(nome))

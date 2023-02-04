nome = 'Guanabara'
cores = {'limpa': '\033[m',
         'nome': '\033[1;33m',
         'normal': '\033[34m'}
print('{0}Olá{3}!{0} Seja bem-vindo{3},{0} {1}{2}{3}!'.format(cores['normal'], cores['nome'], nome, cores['limpa']))

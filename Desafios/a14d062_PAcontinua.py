primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
exibir = 10
exibirMais = 1
contador = 1
while exibirMais != 0:
    print('\n{} primeiros termos da PA:'.format(exibir))
    while contador <= exibir:
        print('{}'.format(termo), end='')
        print(', ' if contador < exibir else '', end='')
        termo += razao
        contador += 1
    exibirMais = int(input('\nExibir mais quantos termos? '))
    exibir += exibirMais
    termo = primeiro
    contador = 1

from time import sleep


def contador(inicio, fim, passo):
    ajuste_fim = 0
    if passo == 0:
        passo = 1
    if inicio <= fim:
        passo = abs(passo)
        ajuste_fim = 1
    elif inicio > fim:
        passo = -abs(passo)
        ajuste_fim = -1
    print(f'Contagem do {inicio} ao {fim} de {abs(passo)} em {abs(passo)}')
    for c in range(inicio, fim + ajuste_fim, passo):
        print(c, end=' ')
        sleep(0.3)
    print('- fim :)')
    sleep(0.3)
    print('-' * 60)


contador(1, 10, 1)
contador(10, 0, 2)

print(f'{"CONTAGEM PERSONALIZADA":^60}')
inicioInformado = int(input('Início: '))
fimInformado = int(input('Fim: '))
passoInformado = int(input('Passo: '))
contador(inicioInformado, fimInformado, passoInformado)

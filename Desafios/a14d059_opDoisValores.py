from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opt = 0
while opt != 5:
    opt = int(input('''\n===== Operações =====
(1) somar
(2) multpicar
(3) maior
(4) novos valores
(5) sair
Opção: '''))
    if opt == 1:
        soma = n1 + n2
        print('\n{} + {} = {}'.format(n1, n2, soma))
    elif opt == 2:
        produto = n1 * n2
        print('\n{} x {} = {}'.format(n1, n2, produto))
    elif opt == 3:
        if n1 > n2:
            print('\n{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('\n{} é maior que {}'.format(n2, n1))
        elif n1 == n2:
            print('\nOs valores são iguais')
    elif opt == 4:
        n1 = float(input('\nPrimeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opt == 5:
        print('\nFim :)')
    else:
        print('\nOpção inválida')
    sleep(2)

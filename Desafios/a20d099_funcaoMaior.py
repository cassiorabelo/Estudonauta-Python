from time import sleep


def maior_valor(* valores):
    contador = maior = 0
    print('-' * 70)
    if len(valores) == 0:
        print('Não foi informado qualquer valor.')
    else:
        print(f'Foram informados os valores:', end=' ')
        for valor in valores:
            sleep(0.5)
            print(valor, end=' ')
            if contador == 0 or valor > maior:
                maior = valor
            contador += 1
        print(f'- um total de {contador} valores.')
        print(f'O maior deles é o {maior}.')


maior_valor(2, 9, 4, 5, 7, 1)
maior_valor(4, 7, 0)
maior_valor(1, 2)
maior_valor(6)
maior_valor()

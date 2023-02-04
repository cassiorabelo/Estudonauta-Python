n = soma = 0
contador = 1
while n != 999:
    n = int(input('{}º inteiro (999 para finalizar): '.format(contador)))
    if n == 999:
        print('Soma do 1º ao {}º inteiros: {}'.format(contador - 1, soma))
    else:
        soma += n
        contador += 1

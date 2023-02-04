n = soma = contador = menor = maior = 0
opcao = 's'
while opcao == 's':
    contador += 1
    n = float(input('{}º valor: '.format(contador)))
    soma += n
    if contador == 1:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
    opcao = str(input('Deseja continuar? (S/N): ').lower())
    while opcao != 's' and opcao != 'n':
        opcao = str(input('Opção inválida.\nDeseja continuar? (S/N): ').lower())
media = soma / contador
print('\nMédia entre os {} valores: {}'.format(contador, media))
print('Maior valor: {}'.format(maior))
print('Menor valor: {}'.format(menor))

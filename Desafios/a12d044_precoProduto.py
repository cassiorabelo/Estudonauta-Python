preco = float(input('Preço do produto: '))
condicao = int(input('''Condições de pagamento:
(1) Dinheiro
(2) Cheque à vista
(3) Cartão

Opção: '''))
if condicao == 3:
    parcelas = int(input('\nNúmero de parcelas: '))
    if parcelas == 1:
        desconto = 0.05
        precoFinal = preco * (1 - desconto)
        print('Preço original: R$ {:.2f}\nDesconto: {:.0f}%\nPreço final: R$ {:.2f}'.format(preco,
                                                                                      desconto * 100, precoFinal))
    elif parcelas == 2:
        precoFinal = preco
        print('Preço: R$ {:.2f}'.format(preco))
    else:
        txJuros = 0.20
        precoFinal = preco * (1 + txJuros)
        print('Preço original: R$ {:.2f}\nTaxa de juros: {:.0f}%\nPreço final: R$ {:.2f}'.format(preco,
                                                                                           txJuros * 100, precoFinal))
else:
    desconto = 0.10
    precoFinal = preco * (1 - desconto)
    print('Preço original: R$ {:.2f}\nDesconto: {:.0f}%\nPreço final: R$ {:.2f}'.format(preco, desconto * 100, precoFinal))

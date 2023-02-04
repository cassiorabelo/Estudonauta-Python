valorCasa = float(input('Valor da casa (R$): '))
salario = float(input('Salário do comprador: '))
tempo = int(input('Tempo para pagamento (anos): '))
nParcelas = tempo * 12
vrParcela = valorCasa / nParcelas
if vrParcela / salario <= 0.30:
    print('Proposta de financiamento: \033[33m{} '
          'parcelas mensais\033[m de \033[33mR$ {:.2f}\033[m.'.format(nParcelas, vrParcela))
else:
    print('Solicitação de financiamento \033[31mnegada\033[m.')

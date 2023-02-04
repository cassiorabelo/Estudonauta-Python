from Desafios.a22d112_validacao.utilidades import moeda
from Desafios.a22d112_validacao.utilidades import dado

preco = dado.leia_dinheiro('Preço (R$): ')
moeda.resumo(preco, 20, 30)

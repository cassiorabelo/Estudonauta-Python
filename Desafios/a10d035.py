print('\033[34m_-=-' * 15, '\033[m')
print(' ' * 18, 'ANALISADOR DE TRIÂNGULO')
print('\033[34m_-=-' * 15, '\033[m')
segReta1 = float(input('Medida do segmento de reta 1: '))
segReta2 = float(input('Medida do segmento de reta 2: '))
segReta3 = float(input('Medida do segmento de reta 3: '))
if segReta1 + segReta2 > segReta3 and segReta1 + segReta3 > segReta2 and segReta2 + segReta3 > segReta1:
    print('Os segmentos \033[1;32mPODEM \033[mformar um triângulo.')
else:
    print('Os segmentos \033[1;31mNÃO PODEM \033[mformar um triângulo.')

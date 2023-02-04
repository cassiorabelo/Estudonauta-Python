print('\033[34m_-=-' * 15, '\033[m')
print(' ' * 18, 'ANALISADOR DE TRIÂNGULO \033[33m2.0')
print('\033[34m_-=-' * 15, '\033[m')
seg1 = float(input('Segmento de reta 1: '))
seg2 = float(input('Segmento de reta 2: '))
seg3 = float(input('Segmento de reta 3: '))
if seg1 + seg2 <= seg3 or seg1 + seg3 <= seg2 or seg2 + seg3 <= seg1:
    print('Os segmentos de reta \033[1;31mNÃO FORMAM\033[m um triângulo.')
else:
    print('Os segmentos de reta formam um triângulo:')
    if seg1 == seg2 == seg3:
        print('\033[33mEQUILÁTERO')
    elif seg1 == seg2 != seg3 or seg1 != seg2 == seg3 or seg1 == seg3 != seg2:
        print('\033[33mISÓCELES')
    else:
        print('\033[33mESCALENO')

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
if n1 > n2:
    print('O \033[1;33mprimeiro valor\033[m é \033[1;34mmaior\033[m')
elif n2 > n1:
    print('O \033[1;33msegundo valor\033[m é \033[1;34mmaior\033[m')
else:
    print('\033[1;33mNão existe\033[m valor maior, os dois são \033[1;34miguais\033[m')

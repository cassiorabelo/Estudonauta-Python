frase = str(input('Frase: ')).strip().lower()
print('Ocorrências de "a": {}'.format(frase.count('a')))
print('Posição do primeiro "a": {}'.format(frase.find('a')+1))
print('Posição do último "a": {}'.format(frase.rfind('a')+1))

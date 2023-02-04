frase = str(input('Frase: ')).replace(' ', '').upper()
esarf = ''
for c in range(len(frase)-1, -1, -1):
    esarf += frase[c]
if frase == esarf:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')

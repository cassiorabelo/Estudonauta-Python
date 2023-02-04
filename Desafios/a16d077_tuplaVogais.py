words = ('casa', 'ovo', 'gratis', 'paralelepipedo')
for word in words:
    print(f'A palavra {word.upper()} possui as vogais: ', end='')
    for letter in word:
        if letter in 'aeiou':
            print(letter, end=' ')
    print()

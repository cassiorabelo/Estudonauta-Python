# analisa uma expressão matemática e verifica se está válida em relação ao uso dos parênteses
stack = []
expression = str(input('Expressão: '))
for character in expression:
    if character == '(':
        stack.append(character)
    elif character == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(character)
            break
print(f'Expressão válida' if len(stack) == 0 else 'Expressão inválida')

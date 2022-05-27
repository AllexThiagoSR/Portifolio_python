expressao = input('Digite sua expressão: ').strip().lower()
a = b = 0
for i in expressao:
    if i == '(':
        a += 1
    elif i == ')':
        b += 1
if a == b:
    print('Sua expressão é válida!')
elif a != b:
    print('Sua expressão é inválida!')

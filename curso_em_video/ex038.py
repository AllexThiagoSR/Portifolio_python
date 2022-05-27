from funverinu import is_number
nu1 = input('Digite um número: ').strip()
nu2 = input('Digite outro número: ').strip()
if is_number(nu1) and is_number(nu2):
    nu1 = int(nu1)
    nu2 = int(nu2)
    if nu1 > nu2:
        print('O primeiro número é maior que o segundo.')
    elif nu2 > nu1:
        print('O segundo número é maior que o primeiro.')
    else:
        print('Não existe valor maior, os dois são iguais.')
else:
    print('Digite apenas números por favor')

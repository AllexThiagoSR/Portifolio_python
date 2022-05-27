def leiaint(frase=''):
    from funverinu import is_int
    num = input(frase)
    if is_int(num):
        num = int(num)
        return num
    print('Isso não é um valor numérico')


n = leiaint('Digite um número: ')
if n is not None:
    print(f'Você digitou o número {n}')

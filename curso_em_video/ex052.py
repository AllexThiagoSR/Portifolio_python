from funverinu import is_number
nu = input('Digite um número: ').strip()
c = 0
if is_number(nu):
    nu = int(nu)
    for i in range(1, nu + 1, 1):
        if nu % i == 0:
            c += 1
    if c > 2 and nu > 1:
        print(f'O número {nu} não é primo')
        print(c)
    elif c <= 2:
        print(f'O número {nu} é primo')
        print(c)

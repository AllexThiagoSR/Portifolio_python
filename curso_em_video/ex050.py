from funverinu import is_number
i = 0
soma = 0
while i <= 5:  # while i < 6: ou while i != 6
    nu = input('Digite um valor: ').strip()
    i += 1
    if is_number(nu):
        nu = int(nu)
        if nu % 2 == 0:
            soma += nu
    else:
        print('Apenas números por favor')
        i -= 1
print(f'A soma dos números pares digitados é igual a {soma}')

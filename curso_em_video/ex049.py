from funverinu import is_number
print('=== TABUADA ===')
nu = input('Digite o número do qual deseja ver a tabuada: ').strip()
if is_number(nu):
    nu = int(nu)
    for i in range(0, 11, 1):
        print(f'{i:>3} x{nu:>3} = {i * nu:>3}')
else:
    print('Apenas números por favor')

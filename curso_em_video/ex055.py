from funverinu import is_number
pesos = []
i = 0
while i < 5:
    print()
    peso = input(f'Digite o peso da {i + 1}ª pessoa: ').strip()
    if is_number(peso):
        i += 1
        peso = float(peso)
        pesos.append(peso)
    else:
        print()
        print('Digite apenas números por favor')
print()
print(f'O maior peso digitado foi {max(pesos)}kg o peso da {pesos.index(max(pesos)) + 1}ª pessoa')
print(f'O menor peso digitado foi {min(pesos)}kg o peso da {pesos.index(min(pesos)) + 1}ª pessoa')

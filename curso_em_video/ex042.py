from funverinu import is_number
lad = []
for i in range(0, 3, 1):
    while True:
        val = input(f'Digite o valor do {i + 1}ª lado: ').strip()
        if is_number(val):
            val = float(val)
            lad.append(val)
            break
        else:
            print('Digite apenas números')
print('As medidas')
for j in lad:
    print(j, end=' ')
if lad[0] + lad[1] > lad[2] and lad[0] + lad[2] > lad[1] and lad[1] + lad[2] > lad[0]:
    print()
    print('Podem formar um triângulo')
    if lad[0] == lad[1] == lad[2]:
        print('Triângulo EQUILÁTERO')
    elif lad[0] == lad[1] != lad[2] or lad[1] == lad[2] != lad[0] or lad[0] == lad[2] != lad[1]:
        print('Triângulo ISÓSCELES')
    elif lad[0] != lad[1] != lad[2]:
        print('Triângulo ESCALENO')
else:
    print()
    print('Não podem formar um triângulo')

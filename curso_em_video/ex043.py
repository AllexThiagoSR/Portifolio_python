from funverinu import is_number
massa = input('Digite a massa da pessoa: (kg) ').strip()
altura = input('Digite a altura da pessoa: (m) ').strip()
if is_number(massa) and is_number(altura):
    imc = float(massa) / (float(altura) ** 2)
    print(f'O imc dessa pessoa é: {imc:.2f}.')
    print('Status: ', end='')
    if imc < 18.5:
        print('ABAIXO DO PESO')
    elif 18.5 <= imc <= 25:
        print('PESO IDEAL')
    elif 25 < imc <= 30:
        print('SOBREPESO')
    elif 30 < imc <= 40:
        print('OBESIDADE')
    elif imc > 40:
        print('OBESIDADE MÓRBIDA')
else:
    print('Digite apenas números por favor')

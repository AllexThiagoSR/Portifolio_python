from funverinu import is_number
num1 = 0
num2 = 0


def lernum():
    while True:
        global num1
        num1 = input('Primeiro valor: ').strip()
        global num2
        num2 = input('Segundo valor: ').strip()
        if is_number(num1) and is_number(num2):
            num1 = int(num1)
            num2 = int(num2)
            break
        else:
            print('Digite apenas números por favor')
            print()


lernum()
while True:
    print('\t[1] - Somar\n\t[2] - Multiplicação\n\t[3] - Maior\n\t[4] - Trocar valores\n\t[5] - Sair do programa')
    op = input('Opção que deseja fazer: ').strip()
    print()
    if op == '1':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif op == '2':
        print(f'{num1} x {num2} = {num1 * num2}')
    elif op == '3':
        if num1 > num2:
            print('O maior número é: ', num1)
        elif num2 > num1:
            print('O maior número é: ', num2)
        else:
            print('Os dois números são iguais')
    elif op == '4':
        print('Trocando valores')
        lernum()
    elif op == '5':
        print('Fechou')
        break
    print('=' * 50)

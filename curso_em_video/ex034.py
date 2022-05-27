from funverinu import is_number
sal = input('Digite o salário do funcionário: R$').strip()
novo_sal = 0
if is_number(sal):
    sal = float(sal)
    if sal > 1250:
        novo_sal = sal + (sal * 0.1)
    elif sal <= 1250:
        novo_sal = sal + (sal * 0.15)
    print(f'O novo salário do funcionário é: R${novo_sal:.2f}')
else:
    print('Digite apenas números')
from funverinu import is_number
nu = input('Digite o número que deseja converter: ').strip()
op = input('Digite a base para qual deseja converter esse número? ').strip().upper()
if is_number(nu):
    nu = int(nu)
    if op in 'BINARIO':
        print(bin(nu))
    elif op in 'OCTAL':
        print(oct(nu))
    elif op in 'HEXA':
        print(hex(nu))

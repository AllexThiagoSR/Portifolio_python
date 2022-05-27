from math import trunc as t

num = float(input('Digite um número: '))
print(f'O número digitado foi {num} e sua parte inteira é {num:.0f}')
num = t(num)
print(f'Sua parte inteira é {num}')

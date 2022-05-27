from math import sqrt as sr

op = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjascente: '))
hip = sr(op ** 2 + adj ** 2)
print(f'A hipotenusa desse triângulo vale: {hip}')

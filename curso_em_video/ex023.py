nu = int(input('Digite um número qualquer entre 0 e 9999: '))
u = nu // 1 % 10
de = nu // 10 % 10
ce = nu // 100 % 10
um = nu // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {de}')
print(f'Centena: {ce}')
print(f'Unidade de milhar: {um}')

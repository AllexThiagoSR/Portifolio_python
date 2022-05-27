from math import sin as s, cos as c, tan as t, radians as rar

ang = float(input('Digite um valor de um ângulo qualquer: '))
ang = rar(ang)
print(ang)
print(f'Seno: {s(ang)}')
print(f'Cosseno: {c(ang)}')
print(f'Tangente: {t(ang)}')


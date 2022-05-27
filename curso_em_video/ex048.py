soma = 0
c = 0
for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
        c += 1
print(f'A soma dos {c} valores solicitados é igual a {soma}')

def sorteia():
    from random import randint
    from time import sleep
    print(f'Sorteando valores:')
    for i in range(0, 5, 1):
        valor = randint(0, 10)
        print(valor, end=' ')
        lis.append(valor)
        sleep(0.5)


def somapar(lista):
    soma = 0
    print(f'Somando valores pares da lista {lis}, resultado:', end=' ')
    for i in lista:
        if i % 2 == 0:
            soma += i
    return soma


lis = list()
sorteia()
print()
print(f'Valores sorteados: {lis}')
print(somapar(lis))

lista = []
x = 0
for i in range(0, 5, 1):
    while True:
        val = input('Digite um valor para adicionar à lista: ').strip()
        try:
            val = int(val)
            break
        except ValueError:
            print('Digite apenas números por favor')
    if i == 0 or val > lista[-1]:
        print('Valor adicionado na última posição')
        lista.append(val)
    else:
        for j in range(len(lista) - 1, -1, -1):
            if lista[j] > val:
                if val not in lista:
                    lista.insert(j, val)
                    x = j
                else:
                    lista.pop(x)
                    lista.insert(j, val)
                    x = j
            continue
        print(f'Valor {val} adicionado na posição {x}')
print('=' * 100)
print(lista)

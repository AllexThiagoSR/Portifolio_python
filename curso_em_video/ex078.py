lista = []
for i in range(0, 5, 1):
    while True:
        print()
        num = input(f'Digite um valor para a posição {i}: ').strip()
        try:
            num = int(num)
            break
        except ValueError:
            print('Digite apenas números')
            print()
    lista.append(num)
print()
print(f'O maior valor da lista é {max(lista)}, encontrado na posição {lista.index(max(lista))}')
print(f'O menor valor da lista é {min(lista)}, encontrado na posição {lista.index(min(lista))}')

def contagem(fim, inicio=0, passo=1):
    passo = passo * (-1) if passo < 0 else passo
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim > inicio:
        if passo > 0:
            while inicio <= fim:
                print(inicio, end=' ')
                inicio += passo
            print('FIM')
        else:
            print('Isso retornará um loop infinito, erro')
    elif inicio > fim:
        while fim <= inicio:
            print(inicio, end=' ')
            inicio -= passo
        print('FIM')


contagem(1, 10)
print('=' * 100)
contagem(10, 0, -2)
print('=' * 100)

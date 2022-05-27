def maior(*args):
    from time import sleep
    print('Analisando os valores passados...')
    try:
        for i in args:
            print(i, end=' ')
            sleep(0.5)
        mais = max(args)
        print(f'. Foram informados {len(args)} valores no total')
        print(f'Maior valor informado: {mais}')
    except ValueError:
        print(f'{0} Foram informados 0 valores no total')
        print(f'Maior valor informado: 0')


print('=' * 100)
maior(2, 9, 4, 5, 7, 1)
print('=' * 100)
maior(4, 7, 0)
print('=' * 100)
maior(1, 2)
print('=' * 100)
maior(6)
print('=' * 100)
maior()

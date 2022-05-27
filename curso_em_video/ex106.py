print('\033[1;33m=' * 19)
print(f"{'Interactive help':^19}")
print('=' * 19)
while True:
    print('\033[1;37m')
    func = input('Desja ver a documentação de qual função? (Fim - encerra) ').strip().lower()
    print('\033[1;34m')
    print('=' * 100)
    if func == 'fim':
        print('\033[1;31m')
        print('Encerrou')
        break
    help(func)
    print('=' * 100)


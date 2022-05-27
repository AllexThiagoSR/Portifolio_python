def fun():
    from time import sleep

    def lin(fra, li='\033[m'):
        print(f'{li}', end='')
        print('~' * (len(fra) + 4))
        print(f'  {fra}')
        print('~' * (len(fra) + 4))

    def manu():
        lin(fra='\033[1;43mSistema de Ajuda Pyhelp', li='\033[1;43m')
        while True:
            q = str(input('\033[mFunção(FIM encerra)> ')).strip().upper()
            if q == 'FIM':
                i = 0
                print('Encerrando', end='')
                while i < 3:
                    sleep(1)
                    print('.', end='')
                    i += 1
                break
            lin(fra=f'\033[1;44mAcessando o manual do comando {q}', li='\033[1;44m')
            sleep(2)
            print('\033[1;47m', end='')
            help(q)

    manu()


fun()

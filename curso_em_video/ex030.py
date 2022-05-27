nu = input('Digite um número: ').strip()
if nu.isnumeric():
    nu = int(nu)
    fra = f'O número {nu} é'
    if nu % 2 == 0:
        print(fra, '\033[1;33mPAR')
    elif nu % 2 != 0:
        print(fra, '\033[1;36mÍMPAR')
else:
    print('Digite apenas números')

import datetime
ano = input('Digite um ano: (Digite 0 para pegar o ano atual) ').strip()
if ano.isnumeric():
    ano = int(ano)
    if ano == 0:
        ano = datetime.datetime.today().year
    if ano % 4 == 0:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')
else:
    print('Digite apenas números')

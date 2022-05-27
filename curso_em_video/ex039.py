import datetime
from funverinu import is_number
ano_atual = datetime.datetime.today().year
ano = input('Em qual ano o voluntário nasceu? ').strip()
if is_number(ano):
    ano = int(ano)
    idade = ano_atual - ano
    print(idade)
    if idade < 18:
        print(f'Faltam {18 - idade} anos para que você precise se alistar.')
    elif idade == 18:
        print('Está na hora exata de você se alistar')
    elif idade > 18:
        print(f'Você está {idade - 18} anos atrasado para o alistamento')
else:
    print('Digite apenas números por favor')

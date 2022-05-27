from funverinu import is_number
from datetime import datetime
ano_atual = datetime.today().year
ano = input('Digite o ano de nascimento do atleta: ').strip()
if is_number(ano):
    idade = ano_atual - int(ano)
    print(f'O atleta tem {idade} anos')
    if idade <= 9:
        print('Atleta, MIRIM')
    elif 9 < idade <= 14:
        print('Atleta, INFANTIL')
    elif 14 < idade <= 19:
        print('Atleta, JÚNIOR')
    elif 19 < idade <= 25:
        print('Atleta, SÊNIOR')
    elif idade > 25:
        print('Atleta, MASTER')

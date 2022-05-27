from datetime import datetime
from funverinu import is_number
ano_atual = datetime.today().year
maior = 0
menor = 0
i = 0
while i < 7:  # ou while i < 7:
    print()
    ano_nasc = input(f'Digite o ano de nascimento da {i + 1}ª pessoa: ').strip()
    if is_number(ano_nasc):
        i += 1
        ano_nasc = int(ano_nasc)
        idade = ano_atual - ano_nasc
        if idade < 18:
            menor += 1
        elif idade >= 18:
            maior += 1
print()
print(f'{maior} das {i} pessoas são maiores de idade.')
print(f'{menor} das {i} pessoas são menores de idade.')

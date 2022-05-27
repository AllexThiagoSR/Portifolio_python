def voto(nascimento):
    from datetime import datetime
    ano = datetime.today().year
    idade = ano - nascimento
    if 18 <= idade <= 70:
        return f'Com {idade} anos: VOTO ORBIGATÓRIO'
    elif 16 <= idade < 18 or 70 < idade:
        return f'Com {idade} anos: VOTO OPICIONAL'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'


print('=' * 100)
while True:
    try:
        ano_nascimento = int(input('Em que ano você nasceu? ').strip())
        break
    except ValueError:
        print('Apenas valores númericos')
print(voto(ano_nascimento))

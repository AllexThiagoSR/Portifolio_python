extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = input('Digite um número entre 0 e 20 do qual deseja ver a escrita por extenso: ').strip()
    try:
        num = int(num)
    except ValueError:
        print('Digite apenas números por favor.')
        continue
    if 0 <= num <= 20:
        print(extenso[num])
    else:
        print('Digite um número entre 0 e 20')
        continue
    resp = 'ala'
    while resp not in 'NnSs':
        resp = input('Deseja ver outro? [S/N]').strip().upper()[0]
    print('=' * 100)
    if resp == 'N':
        print(f'{"PROGRAMA ENCERRADO":-^26}')
        break
    print('Continua')

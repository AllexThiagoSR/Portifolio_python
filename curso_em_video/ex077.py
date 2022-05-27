tupla = ('macaco', 'barriga', 'carroça', 'aprender', 'ostracismo')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')

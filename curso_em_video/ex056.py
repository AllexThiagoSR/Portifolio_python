from funverinu import is_number
i = 0
mais = ''
mai = 0
tot = 0
men = 0
while i < 4:
    print(f'===== {i + 1} PESSOA =====')
    nome = input(f'Nome: ').strip().title()
    idade = input(f'Idade: ').strip()
    sexo = input(f'Sexo(m/f): ').strip().upper()[0]
    print()
    if is_number(idade):
        idade = int(idade)
    else:
        print()
        print('Em "idade" digite apenas números.')
        continue
    tot += idade
    if sexo == 'F' and idade < 20:
        men += 1
    if sexo == 'M' and i == 0 or idade > mai:
        mai = idade
        mais = f'O homem mais velho é {nome} com {idade} anos de idade'
    i += 1
med = tot / 4
print(f'A média de idade desse grupo é de {med:.2f} anos')
print(f'Ao todo há {men} mulheres com menos de 20 anos')
print(mais)

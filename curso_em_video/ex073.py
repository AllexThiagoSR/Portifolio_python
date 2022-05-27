times = ('São Paulo', 'Coritiba', 'Corinthians', 'Atlético-MG', 'Ceará SC', 'Avaí', 'Cuiabá', 'Bragantino', 'Juventude',
         'Flamengo', 'Atlético-GO', 'Santos', 'Fluminense', 'Palmeiras', 'Fortaleza', 'América-MG', 'Botafogo',
         'Internacional', 'Goiás', 'Athletico-PR')
print('5 primeiros times da tabela:')
for i in times[0:5]:
    print(f'{times.index(i) + 1}ª posição: {i}')
print()
print('4 últimos times da tabela:')
for i in times[16:]:
    print(f'{times.index(i) + 1}ª posição: {i}')
print()
print(f'Posição do time Goiás: {times.index("Goiás") + 1}')
print()
times = sorted(times)
print('Times em ordem alfabética:')
for i in times:
    print(f'{i}')

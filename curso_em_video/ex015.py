print('ALUGUEL DE CARROS')
dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram rodados? '))
print(f'O carro foi alugado por {dia} dias (R${dia * 60:.2f})')
print(f'O carro rodou {km}km (R${km * 0.15:.2f})')
print(f'O preço total do aluguel foi: R${(60 * dia) + (0.15 * km):.2f}')

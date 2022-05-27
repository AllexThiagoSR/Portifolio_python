cida = str(input('Digite o nome da cidade em que você mora: '))
cida = cida.upper().strip().split()
print(f'O nome da sua cidade começa com santo? {"SANTO" in cida[0]}')

velo = input('Qual a velocidade atual do carro em km/h? ').strip()
if velo.isnumeric():
    velo = float(velo)
else:
    print('Digite apenas números por favor')
if velo <= 80:
    multa = 0
elif velo > 80:
    multa = (velo - 80) * 7
    print('\033[1;31mMULTADO!!! Você excedeu o limite de 80km/h', sep='')
    print(f'Terá que paga uma multa de \033[01;36mR${multa:.2f}')
print('\033[1;32mTenha um bom dia e dirija com segurança!')

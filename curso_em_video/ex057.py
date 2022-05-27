seixo = input('Informe seu sexo M-masculino/F-feminino/O-outro: ').strip().upper()[0]
while seixo not in 'MmFfOo':  # while not seixo == 'M' or not seixo == 'F' or not seixo == 'O':
    seixo = input('Opção inválida, por favor informe seu sexo: ').strip().upper()[0]
if seixo == 'M':
    seixo = f'Sexo Masculino registrado'
elif seixo == 'F':
    seixo = f'Sexo Feminino registrado'
elif seixo == 'O':
    seixo = f'Sexo Outro registrado'
print(seixo)

frase = input('Digite a frase que deseja checar: ').strip().upper()
frase = frase.replace(' ', '')
frase_inversa = ''
for i in range(len(frase) - 1, -1, -1):
    frase_inversa += frase[i]
if frase == frase_inversa:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')

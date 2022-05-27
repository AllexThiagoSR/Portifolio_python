far = str(input('Digite um frase: ')).strip().upper()
print(f'Nessa frase você digitou a letra "a" {far.count("A")} vezes')
print(f'A primeira letra "a" apareceu na posição {far.find("A") + 1} da lista')
print(f'A última letra "a" apareceu na posição {far.rfind("A") + 1} da lista')

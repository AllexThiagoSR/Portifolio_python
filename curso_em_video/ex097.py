def escreva(frase='Sem frase'):
    return '=' * (len(frase) + 4) + f'\n  {frase}\n' + '=' * (len(frase) + 4)


print(escreva(frase=input('Digite uma frase: ')))

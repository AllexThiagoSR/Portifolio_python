perg = {
    'Pergunta 1': {'pergunta': 'Quanto é 1+1?',
                   'respostas': {'a': 3, 'b': 2, 'c': 10},
                   'resposta_certa': 'b'},
    'Pergunta 2': {'pergunta': 'Qual a cor do cavalo branco de Napoleão',
                   'respostas': {'a': 'branco', 'b': 'preto', 'c': 'cor de arco-íris', 'd': 'marrom'},
                   'resposta_certa': 'd'},
}
resp = '1'
cer = 0
for k, v in perg.items():
    print()
    print(f'{k}: {v["pergunta"]}')
    print('Opções: ')
    for i, j in v['respostas'].items():
        print(f'[{i}]: {j}')
    while resp not in v['respostas'].keys():
        print()
        while not resp.isalpha():
            resp = input('Qual a resposta certa? ').strip().lower()
        if resp == v['resposta_certa']:
            print('Acertou')
            cer += 1
        elif resp in v['respostas'].keys():
            print(f'Errou, a resposta era letra {v["resposta_certa"]}')
    resp = '1'
porc_acer = (cer * 100) / len(perg)
print(f'Quantidade de respostas certas: {cer}')
print(f'Você acertou {porc_acer}% das respostas')

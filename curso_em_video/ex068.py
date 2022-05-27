from random import randint
i = 0
print('=' * (len('JOGO DE PAR OU ÍMPAR') + 4))
print('  JOGO DE PAR OU ÍMPAR')
print('=' * (len('JOGO DE PAR OU ÍMPAR') + 4))
while True:
    while True:
        jogador = input('Digite um valor: ').strip()
        try:
            jogador = int(jogador)
            pc = randint(0, 10)
            break
        except ValueError:
            print('Digite apenas números')
    esc = 'a'
    while esc not in 'PpIi':
        esc = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
        if esc == 'P':
            esc = 'PAR'
            break
        else:
            esc = 'ÍMPAR'
            break
    win = 'PAR' if (pc + jogador) % 2 == 0 else 'ÍMPAR'
    print('=' * (len(f'Você pôs {jogador} e a maquina pôs {pc}, totalizanco {pc + jogador}, ou seja, {win}') + 2))
    print(f'Você pôs {jogador} e a maquina pôs {pc}, totalizanco {pc + jogador}, ou seja, {win}')
    print('=' * (len(f'Você pôs {jogador} e a maquina pôs {pc}, totalizanco {pc + jogador}, ou seja, {win}') + 2))
    if esc == win:
        print('Você ganhou, Parabéns')
        print('Vamos novamente...')
        print('=' * 50)
        i += 1
        continue
    print('Você perdeu, mais sorte na próxima')
    break
print('=' * 50)
print(f'Você ganhou {i} vezes seguidas')

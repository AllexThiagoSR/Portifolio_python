from funverinu import is_number
from random import randint
opcao = ('Pedra', 'Papel', 'Tesoura')
print('[0] - Pedra\n[1] - Papel\n[2] - Tesoura')
s_jogada = input('Qual a sua jogada? ').strip()
if is_number(s_jogada):
    s_jogada = int(s_jogada)
    m_jogada = randint(0, 2)
    if s_jogada < len(opcao):
        print('-=' * 50)
        print(f'Você jogou {opcao[s_jogada]}\nA máquina jogou {opcao[m_jogada]}')
        print('-=' * 50)
        if s_jogada == m_jogada:
            print('Empate')
        else:
            if m_jogada == 0:
                if s_jogada == 1:
                    print('Você ganhou')
                elif s_jogada == 2:
                    print('Você perdeu')
            elif m_jogada == 1:
                if s_jogada == 0:
                    print('Você perdeu')
                elif s_jogada == 2:
                    print('Você ganhou')
            elif m_jogada == 2:
                if s_jogada == 0:
                    print('Você ganhou')
                elif s_jogada == 1:
                    print('Você perdeu')
    else:
        print('Não há essa opção')

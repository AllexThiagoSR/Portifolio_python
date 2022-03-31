pala = 'alicate'.upper().strip()
d = []
dc = []
digi = list(range(0, len(pala)))

for e in range(0, len(digi)):
    digi[e] = '_'

p2 = ''
print(f'A palavra tem {len(pala)} letras')
print(digi)

while True:

    print()
    print(f'Você tem mais {10 - len(d)} tentativas de letras')
    let = input('Digite uma letra: ').upper().strip()

    if let == pala:
        print(f'Oloko, acertou, a palavra realmente era {pala}')
        break
    if len(let) > 1 or not let.isalpha():
        print(f'Digite apenas uma letra e não digite números, por favor!!!')
        continue

    for i in range(0, len(pala)):
        if let == pala[i]:
            print(f'A letra "{let}" existe na posição {i + 1}')
            digi[i] = let

    if let in pala:
        dc.append(let)

    elif let not in pala:
        print(f'Não tem a letra "{let}" nessa palavra')
        d.append(let)

    if len(d) == 10:
        print('Infelizmente você gastou todas seus palpites, tente de novo')
        break

    p = input('Tem um palpite? Se sim digite ele aqui, se não apenas aperter enter: ').upper().strip()

    if p == pala:
        print(f'Oloko, acertou, a palavra realmente era {p}')
        break

    elif p == '':
        print('Sem palpite ainda, huh?')

    else:
        print('Eroooouuuuuu')

    print(f'Palavra a ser adivinhada: {digi}')
    print(f'Letras digitadas corretamente: {dc}')
    print(f'Letras digitadas equivocadamente: {d}')

    for c in digi:
        p2 += c

    if p2 == pala:
        print(f'Parabens você adivinhou todas as letras')
        break

    else:
        p2 = ''

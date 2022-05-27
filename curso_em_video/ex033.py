pri = input('Primeiro valor: ').strip()
seg = input('Segundo valor: ').strip()
ter = input('Terceiro valor: ').strip()
mai = 0
men = 0
if pri.isnumeric() and seg.isnumeric() and ter.isnumeric():
    pri = int(pri)
    seg = int(seg)
    ter = int(ter)

    if pri > seg and pri > ter:
        mai = pri
    elif seg > pri and seg > ter:
        mai = seg
    elif ter > pri and ter > seg:
        mai = ter
    else:
        mai = pri

    if pri < seg and pri < ter:
        men = pri
    elif seg < pri and seg < ter:
        men = seg
    elif ter < pri and ter < seg:
        men = ter
    else:
        men = pri
    print(f'O maior número digitado foi: {mai}')
    print(f'O menor número digitado foi: {men}')
else:
    print('Digite apenas números')

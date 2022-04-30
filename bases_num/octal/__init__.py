def octal(num=0, show=False):
    q = num
    oc = ''
    ot = '0o'
    if q < 8:
        oc += str(q)
    elif q >= 8:
        while True:
            r = q % 8
            q = q // 8
            if q < 8:
                oc += str(r)
                oc += str(q)
                break
            elif q >= 8:
                oc += str(r)
    ot += oc[-1::-1]
    return (ot, num) if show else ot

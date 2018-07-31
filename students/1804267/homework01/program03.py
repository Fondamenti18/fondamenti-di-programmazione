def crit(lz):
    ln = ""
    for el in reversed(lz):
        if 'a' <= el <= 'z':
            if el not in ln:
                ln = el + ln
    return ln

def codifica(chiave, testo):
    lp = crit(chiave)
    lo = sorted(lp)
    finale = {}
    for lett in range(len(lp)):
        finale[lo[lett]] = lp[lett]
    tc = ""
    for lett in testo:
        if lett in finale:
            tc += finale[lett]
        else:
            tc += lett
    return tc

def decodifica(chiave, testo):
    lp = crit(chiave)
    lo = sorted(lp)
    finale = {}
    for lett in range(len(lp)):
        finale[lp[lett]] = lo[lett]
    tc = ""
    for lett in testo:
        if lett in finale:
            tc += finale[lett]
        else:
            tc += lett
    return tc
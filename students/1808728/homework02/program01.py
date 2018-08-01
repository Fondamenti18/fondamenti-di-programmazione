def post(fposts,insieme):
    testo = open(fposts,'r').read()
    testo = testo.replace('<POST>','mh147td ')
    testo = testo.lower()
    import string
    Y = string.punctuation 
    testo = testo.translate(str.maketrans(Y,'                                '))
    testo = testo.split()
    lunt = len(testo)
    risultato = []
    lunS = len(insieme)
    ins = ' '.join(insieme).lower()
    if lunS > 1:
        contatore = 0
        ins = ins.split()
        while contatore < lunS:
            i = ins[contatore]
            while i in testo:
                a = testo.index(i)
                b = testo[:a]
                b = b[::-1]
                c = b.index('mh147td')
                ID = b[c-1]
                del testo[a]
                if ID in risultato:
                    pass
                else:
                    risultato+= [ID]
            contatore+=1
    else:
        while ins in testo:
            a = testo.index(ins)
            b = testo[:a]
            b = b[::-1]
            c = b.index('mh147td')
            ID = b[c-1]
            del testo[a]

            risultato+= [ID]
    return(set(risultato))
        


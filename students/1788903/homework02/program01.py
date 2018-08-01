
def post(fposts,insieme):
    bufsize = 65536
    with open(fposts, 'r', encoding = 'utf-8') as f:
        t = f.readlines(bufsize)
    parole = list(insieme)
    parole = [x.lower() for x in parole]
    tNuovo = ''
    tNuovo2 = ''
    tNuovo3 = []

    for x in t:
        if x != '\n':
            tNuovo += x

    for x in tNuovo:
        conversione = '''',-.()"!?;_{}[]^&%$£|@:+*=ï»¿/'''
        tNuovo2 += ' ' if x in conversione else x

    listaTesto = tNuovo2.split('<POST>')
    for x in listaTesto:
        tNuovo3 += [(x.replace('\n',' ')).strip()]

    for x in tNuovo3:
        tNuovo3 = [x.lower() for x in tNuovo3 if x != '']

    testoLav = []
    for x in tNuovo3:
        testoLav += [x.split(' ')]

    valore = []
    for x in parole:
        for y in testoLav:
            if x in y:
                valore += [y[0]]

    return(set(valore))

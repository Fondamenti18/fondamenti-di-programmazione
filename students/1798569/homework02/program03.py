def decod(pfile, codice):
    'dimensioni struttura,lista struttura e insieme iniziale'
    dim=len(codice)
    listaCod=list(codice)
    ins1=set()
    insRet=set()
    'apertura file, creazione insieme parole'
    with open (pfile) as f:
        a=f.readline()
        while a != '':
            a=a.rstrip('\n')
            if len(a)==dim:
                ins1.add(a)
            a=f.readline()
    'svolgimento'
    while ins1!=set():
        par=ins1.pop()
        listaPar=list(par)
        controllo2=0
        x=0
        while x<dim:
            y=x+1
            controllo1=0
            while y<dim:
                if listaCod[x]==listaCod[y]:
                    if listaPar[x]==listaPar[y]:
                        controllo1+=1
                else:
                    if listaPar[x]!=listaPar[y]:
                        controllo1+=1
                y+=1
            if y!=dim+1 and controllo1==dim-x-1:
                controllo2+=1
            x+=1
        if controllo2==dim:
            insRet.add(par)
    return insRet







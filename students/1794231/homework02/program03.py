
def decod(pfile, codice):
    diz={}
    lisk=[]
    listasingoli=[]
    for c in range(len(codice)):
        if codice[c] in diz:
            diz[codice[c]].append(c)
        else:
            diz[codice[c]]=[c]
            lisk.append(codice[c])
    for k in lisk:
        if len(diz[k])<2:
            listasingoli.append(diz[k][0])
            del diz[k]
    print(listasingoli)
    print(diz)
    righ=[]
    l=len(codice)
    with open (pfile) as f:
        for linea in  f:
            flag=False
            if len(linea)-1==l:
                if diz:
                    flag=True
                    for kdop in diz:
                        temp=linea[int(diz[kdop][0])]
                        for n in diz[kdop]:
                            if linea[int(n)]!=temp:
                                flag=False
                            for kd in diz:
                                if kd!=kdop:
                                    if linea[int(diz[kd][0])]==linea[int(diz[kdop][0])]:
                                        flag=False
                    for sing in listasingoli:
                        if linea[sing] in linea[0:sing] or linea[sing] in linea [(sing+1):(l-1)]:
                            flag=False
                else:
                    insieme=set(linea)
                    if len(linea)==len(insieme):
                        flag=True
            if flag:                         
              righ.append(linea[:-1])
    righe=set(righ)
    return righe






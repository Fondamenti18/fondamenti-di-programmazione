def conv(n):
    join=True #creo un parametro join che di default ha valore true
    unita = ['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    teens = ['','undici','dodici','tredici','quattordici','quindici','sedici', \
             'diciassette','diciotto','diciannove']
    decine = ['','dieci','venti','trenta','quaranta','cinquanta','sessanta','settanta', \
            'ottanta','novanta']
    migliaia_sing = ['','mille','unmilione','unmiliardo','unbiliardo']
    migliaia_plur = ['','mila','milioni','miliardi','biliardi']
    parole = []
    if n==0:
        parole.append('zero')
    else:
        nStringa = str(n)
        nStringaLen = len(nStringa)
        numGruppi = int((nStringaLen+2)/3) #divido il numero in gruppi da tre numeri 123456=123.456
        nStringa = nStringa.zfill(numGruppi*3) #aggiunge 0 per raggiumgere gruppi da tre 002.999
        for i in range(0,numGruppi*3,3):
            c,t,u = int(nStringa[i]),int(nStringa[i+1]),int(nStringa[i+2]) #ho definito le tre variabili in contemporanea
            g = int(numGruppi-(i/3+1)) #c=centinaia t=teens/decine u=unita g=posizione rispetto ai gruppi
            if c>=1:
                if c>1:
                    parole.append(unita[c])
                if t==8:
                    parole.append('cent')
                else:
                    parole.append('cento')
            if t>1:
                if u!=1 and u!=8:
                    parole.append(decine[t])
                else:
                    parole.append(decine[t][:-1]) #t è il mio punto di partenza
                if u>=1:
                    parole.append(unita[u])
            elif t==1:
                if u>=1:
                    parole.append(teens[u])
                else:
                    parole.append(decine[t])
            else:
                if u>=1:
                    parole.append(unita[u])
            if (g>=1) and ((c+t+u)>0):
                if u==1 and c==0 and t==0:
                    parole.remove('uno')
                    parole.append(migliaia_sing[g])
                else:
                    parole.append(migliaia_plur[g])
    if join:
        return ''.join(parole)
    return parole

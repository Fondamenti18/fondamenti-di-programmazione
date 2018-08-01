def pianifica(fcompiti,insi,fout):
    testo = open(fcompiti,'r').read()
    testo = testo.replace('sub',' sub ')
    testo = testo.replace('comp',' comp ')
    testo = testo.split()
    ins = list(insi)
    lunI = len(ins)
    lunT = len(testo)
    contatore = 0
    diz = {}
    diz1 = {}
    while lunT > contatore:
        bo = testo[contatore]
        if bo == 'comp':
            contatore +=1
            a = testo[contatore]
            diz1[a] = []
            contatore+=+1
            if contatore >= lunT:
                break
            else:
                b = testo[contatore]
                if b == 'sub':
                    contatore+=+1
                    c = testo[contatore]
                    diz1[a] = c
                    contatore+=+1
                else:
                    pass
    contatore = 0
    while lunI > contatore:
        bo = str(ins[contatore])
        if bo in diz1:
            a = diz1[bo]
            if a == []:
                diz[bo] = a
                contatore+=1
            else:
                c = [a]
                M = []
                while a != M:
                    b = diz1[a]
                    if b == []:
                        pass
                    else:
                        c+= b.split()
                    a = b
                diz[bo] = c[::-1]
                contatore+=1
        else:
            contatore+=1
    import json
    with open(fout, "w") as f:
        json.dump(diz, f)  
             
        
    

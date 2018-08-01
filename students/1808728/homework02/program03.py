def decod(pfile, codice):
    insiemeP = open(pfile,'r').read()
    listaP = insiemeP.split()
    c1 = ''.join(sorted(set(codice), key=codice.index))
    lunP = len(listaP)
    contatore = 0
    listaPi = []
    while contatore < lunP:
        parola = listaP[contatore]
        try:
            p1 = ''.join(sorted(set(parola), key=parola.index))
            z = str.maketrans(p1,c1)
            p2 = parola.translate(z)
            if p2 == codice:
                listaPi += [parola]
                contatore +=1
            else:
                contatore +=1
        except:
            contatore +=1
            
    
    

    
    listaPi = set(listaPi)
    return(listaPi)  






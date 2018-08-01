def decod(pfile, codice):
    codice=str(codice)
    lunghezza_codice=len(codice)
    elementicodice=len(set(codice))
    insieme=set()
    with open(pfile,"r") as f:
        for i in f:
            i=i.rstrip()
            if  len(i)==lunghezza_codice and len(set(i))==elementicodice:
                dizionario="".maketrans(codice,i)
                test=codice.translate(dizionario)
                if test==i:
                    insieme.add(i)
    return insieme

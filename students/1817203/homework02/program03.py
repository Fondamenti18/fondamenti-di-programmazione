def decod(pfile, codice):
    f=open(pfile,encoding='utf-8')
    parola=f.readline()
    insieme=set()
    y=set(codice)
    ly=len(y)
    lc=len(codice)
    lcodice=(list(codice))
    while parola!='':
            lparola=list(parola[:-1])
            x=set(lparola)
            if len(lparola)==lc and len(x)==ly:
                diz=cread(lparola,lcodice)
                ltest=codifica(lparola,diz)
                if ltest==lcodice:
                    insieme.add(parola[:-1])
            parola=f.readline()
    f.close()
            
    return insieme

def cread(lparola,lcodice):
    diz={}
    for x in range(len(lcodice)):
        if not lparola[x] in diz:
            diz[lparola[x]]=lcodice[x]
    return diz
            
def codifica(lparola,diz):
    ltest=[]
    for x in range(len(lparola)):
        ltest+=diz[lparola[x]]
    return ltest
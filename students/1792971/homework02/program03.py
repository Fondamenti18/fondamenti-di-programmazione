def decod(pfile, codice):
    file=open(pfile)
    parole=set(file.read().split("\n"))
    file.close()
        
    compatibili=trova_compatibili(parole,codice)
    return compatibili
        
def trova_compatibili(parole,codice):
    compatibili=set()
    for parola in parole:
        if len(parola)<len(codice):
            seq=""
        else:
            ass=associa(parola,codice)
            seq=""
            for c in parola:
                i=trova_indice(c,ass)
                if i==-1:
                    seq=""
                    break
                else:
                    seq+=ass[i][1]
        if seq==codice:
            compatibili.add(parola)
            
    return compatibili

def associa(parola,codice):
   i=0
   j=0
   ass=[]
   
   while i<len(parola) and j<len(codice):
      ass+=[(parola[i],codice[j])]
      i+=1
      j+=1
            
   return elimina_copie(ass)

def elimina_copie(lc):
    i=0
    while i<len(lc)-1:
        j=i+1
        while j<len(lc):
            if lc[i][0]==lc[j][0] or lc[i][1]==lc[j][1]:
                lc.pop(j)
            else:
                j+=1
        i+=1
    return lc

def trova_indice(c,ass):
    i=0
    pos=-1
    trovato=False
    while i<len(ass) and trovato==False:
        if c in ass[i]:
            pos=i
            trovato=True
        else:
            i+=1
    return pos
    

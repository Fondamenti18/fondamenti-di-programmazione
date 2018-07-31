def decod(pfile,codice):
    f=open(pfile)
    lista= []                              
    lista1=[]
    for c in f:
        lista.append((f.readline()).replace('\n',''))
    f.close
    for x in lista:
        if len(x)==len(codice):
            if lettere(x,codice)==codice:
                lista1.append(x)
                
    return set(lista1)


        
def lettere(stringa,codice):
    d={}
    y=0
    x=0
    s=''
    while x<len(stringa):
       while y<len(codice):
            if stringa[x] not in d.keys() and codice[y] in d.values():
                return '' 
            elif stringa[x] in d.keys():
                x+=1
                y+=1
            else:
                d[stringa[x]]=codice[y]
    x+=1
    y+=1
    for t in stringa:
        s+=d[t]
    return s
   
   
      

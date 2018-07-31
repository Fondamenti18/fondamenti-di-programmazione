def decod(pfile,codice):
    f=open(pfile)
    lista= []                              #((f.read()).replace('\n',' ')).split()
    
    for c in f:
        lista.append((f.readline()).replace('\n',''))
    for x in lista:
        if len(x)==len(codice):
            if lettere(x,codice)==codice:
                lista+=x
    return set(lista)


        
def lettere(stringa,codice):
    d={}
    y=0
    x=0
    s=''
    while x<len(stringa):
       while y<len(codice):
            if stringa[x] in d :
                x+=1
                y+=1
            else:
                d[stringa[x]]=codice[y]
    x+=1
    y+=1
    for t in stringa:
        s+=d[t]
    return s
   
      

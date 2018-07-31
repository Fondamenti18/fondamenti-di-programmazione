def codifica(chiave,testo_in_chiaro):
    '''inserire qui la vostra implementazione'''
    ls=[]
    chiave = modifiche(chiave)
    chiave = occorrenze(chiave)
    result = list(chiave)
    result.sort()
    testo_crittografato=[]
    c=0
    for i in chiave:
        ls+=[[result[c],i]]
        c+=1
    testo_in_chiaro=list(testo_in_chiaro)
    return ''.join(sostituzione(testo_in_chiaro,testo_crittografato,ls))
def decodifica(chiave, testo_crittografato):
    '''inserire qui la vostra implementazione'''
    ls=[]
    chiave = modifiche(chiave)
    chiave = occorrenze(chiave)
    result = list(chiave)
    result.sort()
    testo_in_chiaro=[]
    c=0
    for i in chiave:
        ls+=[[i,result[c]]]
        c+=1
    testo_crittografato=list(testo_crittografato)
    return ''.join(sostituzione(testo_crittografato,testo_in_chiaro,ls))
def modifiche(chiave):
    chiave = chiave.replace(' ','')
    for x in chiave: 
       if x.islower()==0:
            chiave = chiave.replace(x,'') 
    return chiave
def occorrenze(text):
    lista=list(text)
    for i in lista:
        while lista.count(i)>1:
                lista.remove(i)
    for i in lista:
        while lista.count(i)>1:
                lista.remove(i)
    return lista
def sostituzione(testo1,testo2,ls):
    for x in testo1:
        y=0
        z=0
        while y<len(ls):
            if x==ls[y][0]:
                testo2+=ls[y][1]
                z=1
                break
            y+=1
        if z==0:    
            testo2+=[x]
    return testo2

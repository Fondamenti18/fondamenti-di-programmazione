def value(lista):
    for i in lista:
        while lista.count(i)>1:
            lista.remove(i)
    return (lista)



def lowers(lista):
    for i in range(len(lista)-1,-1,-1):
        if not lista[i].islower()==True and not lista[i].isnumeric():
            del(lista[i])
    return lista



def codifica(lista,testo):
    lista=list(lista)
    lista=value(lista)
    lista=lowers(lista)   
    ls_1=sorted(lista)      
    ls_1.append(' ')
    lista.append(' ')
    testo=list(testo) 
    word=''
    
    for i in range(0,len(testo)):
        for l in range(0,len(ls_1)):
            if testo[i]==ls_1[l]:
              word=lista[l]
            elif not testo[i] in ls_1:               
              word=testo[i]  
        testo[i] = word
    testo=''.join(testo)
    return(testo)

def decodifica(lista,testo):
    lista=list(lista)
    lista=value(lista)
    lista=lowers(lista)   
    ls_1=sorted(lista)      
    ls_1.append(' ')
    lista.append(' ')
    testo=list(testo) 
    word=''

    for i in range(0,len(testo)):
        for l in range(0,len(ls_1)):
            if testo[i]==lista[l]:
                word=ls_1[l]
            elif not testo[i] in lista:               
              word=testo[i]  
        testo[i]=word
    testo=''.join(testo)
    return(testo)

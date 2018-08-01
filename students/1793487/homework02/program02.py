import re
import json

def ID(fcompiti):
    lista_ID = []
    for line in open(fcompiti,'r'):
        ID = re.sub('[^\d]' , '', line) #al posto di replace
        lista_ID.append(ID)
    return lista_ID
    

def alberi(fcompiti,num_compiti):
        l=[0 for i in range(num_compiti+1)]
        t=open(fcompiti,'r').readlines() #apro e leggo il file subito
        for indice,line in enumerate(t): #ottengo l'indice e la linea
            if 'sub' in line:
                M = re.sub('[^\d]' , '', line)
                N =  re.sub('[^\d]' , '', t[indice-1])  #t[indice-1] considera il testo, l'indice della riga dove si trova e poi sale di una riga(ecco perche -1)
                l[int(N)]=int(M)
        return l
    

def lista_sub(l,ID):
    l_sub=[]
    while l[int(ID)]: #indice della lista corrisponde al comp
        ID=l[int(ID)]    #il sub = indice
        l_sub.insert(0,ID) #cosi metto l'ID all'inizio
    return l_sub


def pianifica(fcompiti,insi,fout):
    lista_ID=set(ID(fcompiti))
    num_compiti=len(set(lista_ID))
    l=alberi(fcompiti,num_compiti)
    dizionario={}
    for n in insi:
        if n in lista_ID:
            lista=lista_sub(l,int(n))
            for i in range(len(lista)):
                lista[i]=str(lista[i])  
            dizionario[n]=lista    #n = chiave dizionario ha come valore la lista
    a=json.dumps(dizionario)
    with open(fout,'w') as fout:
        fout.write(a)
    return 

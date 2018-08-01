"""
Created on Thu Nov  2 21:53:51 2017

@author: NICO
"""

import json

def listtoint(lista):
    l=[]
    for i in lista:
        l+=[int(i)]
    return l

def listtostring(lista):
    l=[]
    for i in lista:
        l+=[str(i)]
    return l

def dictionarytostring(d):
    d2={}
    for i in d:
        d2[str(i)]=listtostring(d[i])
    return d2


def pianifica(fcompiti,insi,fout):
    primo=1
    p=[]
    num=0
    i=0
    temp=[]
    d={}
    ris={}
    f=open(fcompiti,"r")
    for linea in f:                                         #
        linea=linea.replace("\n","")                        #elimino i ritorni a capo
        linea=linea.replace(" ","")                         #elimino gli spazi

        p+=linea.split(" ")                                 #memorizzo in p una lista contenente la stringa "comp" o "sub" e subito a fianco il numero





    
    while(i<len(p)):
        if(p[i][0]=='c'):                                   #se l'elemento corrente è "comp"
            if(primo==1):                                   #se è il primo, non lo inserisco, in quanto n ha ancora il valore di inizializzazione, non quello effettivo
                primo=0                                     #disattivo il controllore
            else:                                           #se non è il primo, quindi ho un valore in n
                d[num]=temp                                 #metto nel dizionario al valore corrente la lista dei requisiti
                temp=[]                                     #e svuoto la lista
            num=int(p[i].replace("comp",""))                #memorizzo in num il numero corrente
            
        elif(p[i][0]=='s'):                                 #se l'elemento corrente è "sub"
            temp+=[int((p[i].replace("sub","")))]                               #aggiungo alla lista temp, il numero successivo nella lista
        i=i+1                                               #incremento il contatore    
    d[num]=temp                                             #al dizionario d, al campo num, associo la lista temp





    t=[]                                                   

    



    ins= listtoint(insi)
    for h in ins:                                           #faccio scorrere ogni elemento di insi
        if(h in d):                                         #se l'elemento corrente è presente nel dizionario
            for i in d[h]:                                  #per ogni elemento della lista corrispondente all'elemento
                if(i in d):                                 #e se un suo requisito ha un requisito
                    t+=d[i]                                 #aggiungo anche quello alla lista temporanea
                    t+=[i]                                      #aggiungo l'elemento stesso a una lista temporanea
                else:
                    t+=[i]

            ris[str(h)]=t                                   #aggiungo al dizionario finale la lista temporanea
            t=[]                                            #e la svuoto
    res=dictionarytostring(ris)
    a=json.dumps(res)
    with open(fout,"w") as file:
        file.write(str(a))
    file.close()
            
            
            
        




    

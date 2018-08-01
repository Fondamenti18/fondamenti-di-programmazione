def decodificatore(configurazione):
    import itertools
    global lista,num_npresente,risposta,kcontt,risposta_temp,lista_trovata,caso5_1,coppia5_1,numero_trovato
    n=configurazione[0]
    lung_conf=len(configurazione)
    coppia=configurazione[lung_conf-1]
    if lung_conf > 11 and min(coppia[1])==0 and max(coppia[1])==n:
        lista=pulizia_combinazioni(coppia[0])
    elif lung_conf > 11 and min(coppia[1])==0 and caso5_1==0 and (min(coppia[1])+max(coppia[1]))==n-1:
        lista1=[]
        kcont=0
        kpos=0
        tupla_lista=coppia[0]
        tupla_l=list(tupla_lista)
        for k in range (len(tupla_l)):
                if tupla_l[k]==num_npresente:kpos=k
        coppia_finale=configurazione[11]
        risposta1=coppia_finale[0]
        numero_trovato=coppia5_1[kpos]
        lista_trovata[kpos]=coppia5_1[kpos]
        caso5_1=1
    
        for i in range (len(lista)):
            tupla_lista=lista[i]
            si_pres=0
            for k in tupla_lista:
                if k == num_npresente:
                    si_pres=1
            if tupla_lista[kpos] == coppia5_1[kpos] and si_pres==0:                  
                    kcont=kcont+1
                    lista1.append(tupla_lista)
        lista=lista1
        lista_t1=[]
        lista_t2=[]  
        for j in risposta1:
            for k in range (n):
                if j != numero_trovato:
                    lista_t1=list(lista_trovata)
                    if lista_trovata[k] == 10:
                        lista_t1[k]=j
                        lista_t1=tuple(lista_t1)
                        lista_t2.append(lista_t1)
        lista=lista_t2
    if lung_conf > 11 and min(coppia[1]) ==1 and (min(coppia[1])+ max(coppia[1])) ==n and caso5_1==0:
        coppia5_1=coppia[0]
        lista_temp=[]
        lista_l=[]     
        for k in range (n):
            lista_temp=list(risposta)
            if lista_trovata[k] == 10:
                lista_temp[k]=num_npresente
                lista_temp=tuple(lista_temp)
                lista_l.append(lista_temp)
        lista_l.extend(lista)
        lista=lista_l
    if lung_conf > 11 and max(coppia[1]) == 2:
        lista_temp=[]
        lista_t1=[]
        lista_t2=[]
        lista_p=list(coppia[0])
        kcontt=0
        for k in lista_p:
            if k != 10 and k!= numero_trovato:
                lista_trovata[kcontt]=k
            else:
                kcontt=kcontt+1
        if lista_trovata.count(10)==0: 
                lista_trovata=tuple(lista_trovata)
                lista_temp.append(lista_trovata)
                lista_temp.extend(lista)
                lista=lista_temp
        else:
             set1=set(lista_trovata)
             for k in range (len(lista)):
                  coppia_t=lista[k]
                  set2=set(list(coppia_t))
#==============================================================================
                  if set1.issuperset(set2) == False:
#                       print ('sttt',set1.issuperset(set2))

                      lista_t2=tuple(coppia_t)
                      lista_t1.append(lista_t2)
             lista=lista_t1
#==============================================================================
    
    if lung_conf < 12 :
#==============================================================================
        risposta=trova_sequenza(lung_conf,n,coppia,configurazione)

        lista=[]
        if lung_conf > 10:
            n_lun=len(risposta)
            lista=  list(itertools.permutations(risposta,n_lun))      

    else:
        coppia_finale=configurazione[11]
        risposta=coppia_finale[0]
        coppia1=configurazione[lung_conf-1]
        risposta=coppia1[0]
        risposta=lista[0]
        lista[0:1]=[]
    return risposta

def numero_combinazioni(proposta):
    import itertools
    global lista 
    n_lun=len(proposta)
    lista=  list(itertools.permutations(proposta,n_lun))      
    kcont=0
    lista1=[]
    kpos=0
    for k in proposta:
        lista1=[]
        for i in range (len(lista)):
             tupla_lista=lista[i]
             if tupla_lista[kpos] != k :
                 kcont=kcont+1
                 lista1.append(tupla_lista)
        kpos=kpos+1
        lista=lista1
    return lista

def pulizia_combinazioni(proposta):
       global lista 
       kcont=0
       lista1=[]
       kpos=0
       for k in proposta:
           lista1=[]
           for i in range (len(lista)):
                tupla_lista=lista[i]
                if tupla_lista[kpos] != k :
                    kcont=kcont+1
                    lista1.append(tupla_lista)
           kpos=kpos+1
           lista=lista1
       return lista


def trova_sequenza(lung_conf,n,coppia,configurazione):
        global num_npresente,lista_trovata,caso5_1,kcont_lung
        num_npresente=0
        lista_trovata=[]
        risposta=[]
        if lung_conf == 1:
            for i in range (n):
                risposta.append(0)
        elif lung_conf < 11 :
            for i in range (n):
                risposta.append(lung_conf-1)
        else:
            risposta=coppia[0]
        if lung_conf == 11 :
           risposta=[]
           for i in range (1,lung_conf):
               coppia=configurazione[i]
               if max(coppia[1])==1:
                   risposta.append(max(coppia[0]))
               else:
                   num_npresente=max(coppia[0])
        for i in range (n):
            lista_trovata.append(10)
        caso5_1=0


        return risposta    
'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista 
(eventualmente vuota) degli identificativi dei  figli del nodo. Gli identificativi dei nodi 
all'interno delle liste sono in ordine lessicografico crescente.



Ecco un esempio di dizionario d che rappresenta un dizionario-albero

d={
'a':['b'],
'b':['c','d'],
'c':['i'],
'd':['e','l'],
'e':['f','g','h'],
'f':[],
'g':[],
'h':[],
'i':[],
'l':[]
}

L'albero rappresentato da d e'

                             'a'
                              |
                _____________'b'____________             
               |                            |            
              'c'                  ________'d'_______   
               |                  |                  |  
              'i'         _______'e'_______         'l'
                         |        |        |               
                        'f'      'g'      'h'
                                  
                                 


Implementare le seguenti funzioni:

1) 
la funzione genera_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

produce   il  dizionario-albero che rappresenta   il sottoalbero  radicato 
nell'identificativo x che si ottiene dal dizionario-albero d. 
Il dizionario-albero ottenuto va registrato nel file fout.
Se l'identificativo x non e' tra i nodi di d allora  il dizionario-albero prodotto 
deve essere vuoto.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
genera_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'f': [], 'g': [], 'h': [], 'e': ['f', 'g', 'h'], 'l': [], 'd': ['e', 'l']}



2)
la funzione cancella_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

ricava  da d il sottoalbero radicato in x e lo salva nel file fout.
Se x non e' presente tra le chiavi di  d allora  il dizionario-albero d non viene modificato.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
cancella_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'a': ['b'], 'b': ['c'], 'c': ['i'], 'i':[]}


3)
la funzione dizionario_livelli(fnome, fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- il nome di un file json (fout)

costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero d. L'attributo di una 
chiave di valore x e' la lista degli identificativi  dei nodi che si trovano a livello x  nell'albero rappresentato da d. 
La lista è ordinata lessicograficamente ed in modo crescente. 
Il dizionario cosi' costruito va registrato nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_livelli(fname,fout)
il file fout conterra' il dizionario
{0: ['a'], 1: ['b'], 2: ['c', 'd'], 3: ['e','i','l'], 4: ['f', 'g', 'h']}

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- un intero y
- il nome di un file json (fout)

costuisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero 
rappresentato dal dizionario-albero d, Attributo di una chiave di valore x e' il numero 
di antenati di grado y che ha il nodo con identificativo x nell'albero.
Registra il dizionario costruito nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_gradi_antenati(fnome,2,fout)
il file fout conterra' il dizionario 
{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.
'''




import json

def genera_sottoalbero(fnome,x,fout):
    diz1=json.loads(open(fnome).read())
    diz2={}
    aggiungi_c(x,diz1,diz2)
    with open (fout, 'w') as f:
        json.dump(diz2, f)
    return    
    
def aggiungi_c(c,diz1,diz2): 
    #riempie il diz2 con gli el dal diz1, ricorsivamente.
    figli=diz1[c]
    diz2[c]=figli
    if figli==[]:
        return diz2
    else: 
        for el in figli:
            aggiungi_c(el,diz1,diz2)

    ##############################################2###########################

def cancella_sottoalbero(fnome,x,fout):
    diz1=json.loads(open(fnome).read())
    delate_c(x,diz1)
    madre=trova_madre(x,diz1)
    diz1[madre].remove(x)
    with open (fout, 'w') as f:
        json.dump(diz1, f)
    return
    
    
def delate_c(c,diz1): 
    #cancella il sottoalbero che ha come radice c, ricorsivamente.
    figli=diz1.pop(c)
    if figli==[]:
        return diz1
    else: 
        for el in figli:
            delate_c(el,diz1)
            
def trova_madre(l,diz):
    #scandisce se l è nelle liste che compongono diz-values, se lo trova riporta il valore di k 
    #corrispondente, altrimenti restituisce 0
    for k,v in diz.items():
        lista=v
        if l in lista:
            return k

######################################################3####################

def dizionario_livelli(fnome,fout):
    diz1=json.loads(open(fnome).read())
    diz2={}
    chiave=0
    nonne=[]  
    for k in diz1.keys():
        if è_nonna(k,diz1):
            nonne.append(k)
            break
    riempi_diz2(nonne,diz1,diz2,chiave)
    with open(fout, 'w') as f:
        json.dump(diz2, f)
    return 
            
def riempi_diz2(c,diz1,diz2,chiave):
    #riempie il dizionario di out. c all'inizio è ['nonna']. ricorre facendo la stessa operazione con tutti i figli. 
    if chiave not in diz2.keys():
        diz2[chiave]=c
    else: 
        diz2[chiave]+=c
    chiave=chiave+1
    for el in c:
        figli=diz1[el]
        if figli==[]:
            pass
        else:
            riempi_diz2(figli, diz1,diz2,chiave)
    for el in diz2.values():
        el.sort()
    return diz2

def è_nonna(c,diz1):
    #ritorna una lista vuota se c è alla base dell'albero (non è figlio di nessuno)
    lista=[]
    for el in diz1.values():
        if c in el:
            lista=+1
    return lista==[]
        
################################################### 4 ##### come lo avevo capito io (mannaggiadio) #######################
'''def dizionario_gradi_antenati(fnome,y,fout):
    diz1=json.loads(open(fnome).read())
    diz2={}
    diz3={}
    diz4={}
    dizionario_livelli_2(diz1,diz2)
    print(diz2)
    for k,v in diz2.items():
        for el in v:
            diz4[el]=k
    print(diz4)
    for el in diz1.keys():
        liv_antenato=diz4[el]-y
        if liv_antenato<0:
            diz3[el]=0
        else: 
            diz3[el]=len(diz2[liv_antenato])
    print(diz3)
    
    
    
def dizionario_livelli_2(diz1,diz2):
    #stessa funzione di prima ma alleggerita lì dove possibile
    chiave=0
    nonne=[]  
    for k in diz1.keys():
        if è_nonna(k,diz1)==[]: 
            nonne.append(k)
    riempi_diz2_2(nonne,diz1,diz2,chiave)
    return diz2
    
def riempi_diz2_2(c,diz1,diz2,chiave):
    #riempie il dizionario di out. c all'inizio è ['nonna']. ricorre facendo la stessa operazione con tutti i figli. 
    #rispetto a quella di sopra si risparmia l'ultimo ciclo per ordinare
    if chiave not in diz2.keys():
        diz2[chiave]=c
    else: 
        diz2[chiave]+=c
    chiave=chiave+1
    for el in c:
        figli=diz1[el]
        if figli==[]:
            pass
        else:
            riempi_diz2(figli, diz1,diz2,chiave)
    return diz2 '''

######################################## 4 ########################################
def dizionario_gradi_antenati(fnome,y,fout):
    diz1=json.loads(open(fnome).read())
    diz3={}
    u=0
    for k in diz1.keys():
        if è_nonna(k,diz1): 
            nonna=k
            break
    spinaci(nonna, diz1, diz3,u,y)
    with open (fout, 'w') as f:
        json.dump(diz3,f)
    return
    
    
def spinaci(el, diz1, diz3, u,y):
    diz3[el]=u
    figli=diz1[el]
    if len(figli)==y:
        u+=1
    for x in figli: 
        spinaci(x,diz1, diz3, u,y)
    return
    
    
    
    
'''  N.B.
per favore ricordiamoci che:
    se dobbiamo rimuovere un elemento da un dizionario o cicliamo e direttamente eliminiamo, ma su una copia altrimenti si 
    impiccia con gli indici, 
    oppure facciamo come ho fatto, ovvero una funzione a parte e poi cancelliamo dalla lista con .remove('')
    Dalla lista si può cancellare durante il ciclo con [:]
    (bacini)
'''
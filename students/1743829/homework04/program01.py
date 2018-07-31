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
La lista e' ordinata lessicograficamente ed in modo crescente. 
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

def albero(diz,x,diz_ris):
    if x in diz:
        if diz[x]==[]:
            diz_ris[x]=[]
        if diz[x]!=[]:
            diz_ris[x]=diz[x]
            for i in diz[x]:
                albero(diz,i,diz_ris)
        return diz_ris
    
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    diz_ris={}
    diz_1={}
    with open(fnome) as f:
        diz=json.load(f)
        diz_ris=albero(diz,x,diz_1)
        
    with open(fout,'w') as g:
        json.dump(diz_ris,g)

def cancella_elementi(diz,x):
    if x in diz:
        if diz[x]==[]:
            del diz[x]
        else:
            for i in diz[x]:
                cancella_elementi(diz,i)
                if i in diz:
                    del diz[i]
            if x in diz:        
                del diz[x]
    return diz


def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        diz=json.load(f)
        diz_ris=cancella_elementi(diz,x)
        for i in diz:
            if x in diz[i]:
                diz[i].remove(x)
        
    with open(fout,'w') as g:
        json.dump(diz_ris,g)

def insieme_valori(lista):
    val=set()
    for i in lista:
        for elem in i:
            val.add(elem)
    return val

def livelli(diz,arg,diz1,h):
    diz_copia=diz.copy()
    for i in diz_copia:
        if i in arg:
            del diz[i]
    listaval=[]
    for i in diz:
        listaval+=[i]
        del diz_copia[i]
        for el in diz[i]:
            arg.remove(el)
    diz1[h]=sorted(listaval)
    if len(diz_copia)>0:
        livelli(diz_copia,arg,diz1,h+1)
    return diz1

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    diz1={}
    arg=set()
    with open(fnome) as f:
        diz=json.load(f)
        lista_val=list(diz.values())
        arg=insieme_valori(lista_val)
        diz_ris=livelli(diz,arg,diz1,0)
        
    with open(fout,'w') as g:
        json.dump(diz_ris,g)

def grado(diz,nodo_grad,diz_ris):
    for nodo in nodo_grad:
        figli=diz[nodo]
        if figli!=[]:
            for figlio in figli:
                diz_ris[figlio]=diz_ris[nodo]+1
                diz_ris=grado(diz,diz[figlio],diz_ris)
        else:
            diz_ris[nodo]+=1
    return diz_ris

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    diz_ris={}
    val=set()
    with open(fnome) as f:
        diz=json.load(f)
        nodo_grad=[]
        for chiave in diz:
            if len(diz[chiave])==y:
                nodo_grad+=[chiave]
        for elem in diz:
            diz_ris[elem]=0
        diz_ris=grado(diz,nodo_grad,diz_ris)
        
    with open(fout,'w') as g:
        json.dump(diz_ris,g)

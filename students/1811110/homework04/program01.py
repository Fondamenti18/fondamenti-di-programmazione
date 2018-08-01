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
                                  |
                                 'i'


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

-------------------------------------------------------
'''
import json

def ape(fnome):       #mette json nel dizionario
    with open(fnome) as f:
        diz = json.load(f)

    return diz

def chiuse(fout,diz):
    json.dump(diz,open(fout, 'w'))








def otto(x,diz,ris):
    ris[x]=diz[x]
    for k in diz[x]:
        ris[k]=diz[k]
        otto(k,diz,ris)
    return ris
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    diz=ape(fnome)
    ris={}
    if x in diz:
        ris=otto(x,diz,ris) 
    else:
        ris={}

    chiuse(fout,ris)





    

def canc(x,diz,ris):
    for k in diz[x]:
        del ris[k]
        canc(k,diz,ris)
    return ris

def canc_p(x,diz,ris):
    del ris[x]
    ls=[]
    for k in ris:
        ls=ris[k]
        for c in ls:
            if x==c:
                b=ls.index(x)
                del ls[b]
                ris[k]=ls
    return ris
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    diz=ape(fnome)
    ris={}
    ls=[]
    a=x
    if x in diz:
        ris= diz.copy()
        ris=canc(x,diz,ris)
        ris=canc_p(a,diz,ris)
        chiuse(fout,ris)
        
    else:
        chiuse(fout,diz)







def verifica(livello,liv,ls):
    if livello in liv:
        ls+=liv[livello]
        ls.sort()
        liv[livello]=ls
    else:
        liv[livello]=ls

def ello(diz,liv,livello,rad):
    ls=[]
    ls.append(rad)
    verifica (livello, liv,ls)
    f=diz[rad]
    if f!='[]':
        for foc in f:
            liv=ello(diz,liv,livello+1,foc)
    return liv

def abb_v(diz):
    foc=next(iter (diz.keys()))
    def tp(diz,foc):
        liv=foc
        for p,el in diz.items():
            if foc in el:
                liv=tp(diz,p)
        return liv
    ant=tp(diz,foc)
    return ant

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    liv={}
    diz=ape(fnome)
    radice=abb_v(diz)   
    liv=ello(diz,liv,0,radice)
    chiuse(fout,liv) 
 



def cond(el,y,gra):
    if len(el)==y:
        gra+=1
    return gra

def padre(diz,ris,gra,y,rad):
    ris[rad]=gra
    el=diz[rad]
    gra=cond(el,y,gra)
    for foc in el:
        ris=padre(diz,ris,gra,y,foc)
    return ris

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    diz=ape(fnome)
    radice=abb_v(diz) 
    ris={}
    ris=padre(diz,ris,0,y,radice)
    chiuse(fout,ris)   

    
    

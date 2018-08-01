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

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as diz:
        dizionario=json.load(diz)
    risultato=crea_diz(dizionario,x)
    with open(fout,'w') as out:
        json.dump(risultato,out)
        
def crea_diz(dizionario,x):
    d={}
    d.update({x:dizionario[x]})
    for y in d[x]:
        d.update(crea_diz(dizionario,y))
    return d
    
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as diz:
        dizionario=json.load(diz)
    ris=elimina_diz(dizionario,x)
    for chiave in ris:
        for y in ris[chiave]:
            if y==x:
                ris[chiave].remove(y)
    with open(fout,'w') as out:
        json.dump(ris,out)
    
def elimina_diz(dizionario,x):
    if dizionario[x]==[]:
        del(dizionario[x])
    else:
        for figlio in dizionario[x]:
            dizionario = elimina_diz(dizionario,figlio)
        del(dizionario[x])
    return dizionario

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as diz:
        dizionario=json.load(diz)
    l=dizionario.values()
    valori=set()
    for x in l:
        for j in x:
            valori.add(j)
    for y in dizionario:
        if y not in valori:
            radice=y
    ris=crea_livelli(dizionario, radice, 0)
    for x in ris:
        ris[x].sort()
    with open(fout,'w') as out:
        json.dump(ris,out)
    
def crea_livelli(dizionario,radice,liv):
    livelli={}
    if liv in livelli:
        livelli.update({liv:livelli[liv]+[radice]})
    else:
        livelli[liv]=[radice]
    for y in dizionario[radice]:
        d2 = crea_livelli(dizionario,y,liv+1)
        for x in d2:
            if x in livelli:
                livelli[x] += d2[x]
            else:
                livelli[x] = d2[x]
    return livelli

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as diz:
        dizionario=json.load(diz)
    l=dizionario.values()
    valori=set()
    for x in l:
        for j in x:
            valori.add(j)
    for z in dizionario:
        if z not in valori:
            radice=z
    ris=crea_gradi(dizionario,radice,y,0)
    with open(fout,'w') as out:
        json.dump(ris,out)
    
    

def crea_gradi(dizionario,radice,y,npar):
    gradi={}
    gradi[radice]= npar
    for x in dizionario[radice]:
        if len(dizionario[radice])==y:
            gradi.update(crea_gradi(dizionario,x,y,npar+1))
        else:
            gradi.update(crea_gradi(dizionario,x,y,npar))
    return gradi
    
            


    
        



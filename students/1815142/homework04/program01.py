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

def esplora_sottoalbero(t, x, d):
    if x not in t:
        return d
    d[x]=t[x]
    for i in t[x]:
        d=esplora_sottoalbero(t,i,d)
    return d

def calcolo_livelli(d, t, cont):
    if len(d[cont])==0:
        d.pop(cont)
        return d
    l=[]
    if len(d[cont])>0:
        for i in d[cont]:
            for g in t[i]:
                l.append(g)
        d[cont+1]=sorted(l)
    return calcolo_livelli(d, t, cont+1)

def genera_sottoalbero(fnome,x,fout):
    '''
    la funzione genera_sottoalbero(fnome,x,fout) ,produce il  dizionario-albero che rappresenta
    il sottoalbero  radicato nell'identificativo x che si ottiene dal dizionario-albero d. 
    Il dizionario-albero ottenuto va registrato nel file fout. Se l'identificativo x non e' tra
    i nodi di d allora  il dizionario-albero prodotto deve essere vuoto.
    '''
    t=open(fnome)
    t=json.load(t)
    d={}
    t=esplora_sottoalbero(t, x, d)
    file=json.dumps(d)
    p=open(fout, 'w')
    p.write(file)
    return d

def cancella_sottoalbero(fnome,x,fout):
    '''
    la funzione cancella_sottoalbero(fnome,x,fout) ricava da d il sottoalbero radicato in x e
    lo salva nel file fout. Se x non e' presente tra le chiavi di  d allora  il dizionario-albero
    d non viene modificato.
    '''
    t=open(fnome)
    t=json.load(t)
    d={}
    d=esplora_sottoalbero(t, x, d)
    for i in d.keys():
        if i in t:
            t.pop(i)
    for i in t.values():
        if x in i:
            i.remove(x)
    file=json.dumps(t)
    p=open(fout, 'w')
    p.write(file)
    return t
        

def dizionario_livelli(fnome,fout):
    '''
    la funzione dizionario_livelli(fnome, fout) che costruisce il  dizionario che ha come  chiavi i
    livelli del dizionario-albero d. L'attributo di una chiave di valore x e' la lista degli
    identificativi  dei nodi che si trovano a livello x nell'albero rappresentato da d. La
    lista e' ordinata lessicograficamente ed in modo crescente. Il dizionario cosi' costruito va
    registrato nel file fout.
    '''
    t=open(fnome)
    t=json.load(t)
    d={}
    lc=[]
    for i in t:
        lc.append(i)
    cont=0
    a=lc[cont]
    l=[]
    l.append(a)
    d[cont]=l
    calcolo_livelli(d, t, cont)
    file=json.dumps(d)
    p=open(fout, 'w')
    p.write(file)
    return d

def dizionario_gradi_antenati(fnome,y,fout):
    '''
    la funzione dizionario_gradi_antenati(fnome,y,fout) che costuisce  il dizionario che ha
    come chiavi gli identificativi dei nodi dell'albero rappresentato dal dizionario-albero
    d, Attributo di una chiave di valore x e' il numero di antenati di grado y che ha il nodo
    con identificativo x nell'albero. Registra il dizionario costruito nel file fout.
    {'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}
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
    '''
    t=open(fnome)
    t=json.load(t) #dizonario base
    r=[]
    for i in t:
        if len(t[i])==y:
            r.append(i)#insieme dei nodi con y figli in ordine di ritrovamento
    d={}
    lc=[]
    for i in t:
        lc.append(i)
    cont=0
    a=lc[cont]
    k={}
    cont=0
    for g in r:
        cont+=1
        for i in t:
            d={}
            v=esplora_sottoalbero(t, g, d)
            if (i not in v or i==g) and i not in k:
                k[i]=cont-1
            if i in v and i!=g:#d=dizionario con livello come chiave e elementi come oggetto
                k[i]=cont
    file=json.dumps(k)
    p=open(fout, 'w')
    p.write(file)
    return k

if __name__=='__main__':
    None
    





            
    

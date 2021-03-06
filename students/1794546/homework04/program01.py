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

def crea(diz, x, diz1):       
    if x not in diz:
        return []
    if x in diz:
        diz1[x]=diz[x]
        y=diz1[x]
        if y!=[]:
            for el in y:
                crea(diz, el, diz1)
    return diz1

def genera_sottoalbero(fnome,x,fout): #crea come ricorsiva
    with open(fnome) as f:
        testo=''.join(f.read())
        diz = json.loads(testo)
        diz1={}
        diz_alb=crea(diz, x, diz1)
        with open(fout, 'w') as o:
            json.dump(diz_alb, o)
   
def elimina(diz, x):       
    if x not in diz:
        return diz
    if x in diz:
        diz1={}
        B=crea(diz, x, diz1)
        C = {k:v for k,v in diz.items() if k not in B}
        return C

def cancella_sottoalbero(fnome,x,fout): #crea come ricorsiva
    with open(fnome) as f:
        testo=''.join(f.read())
        diz = json.loads(testo)
        diz_alb=elimina(diz, x)
        for i in diz_alb:
            while x in diz_alb[i]:
                diz_alb[i].remove(x)
        with open(fout, 'w') as o:
            json.dump(diz_alb, o)
   
def primo(diz):
    for el in diz:
        if diz.values!=el:
            capo=[str(el)]
            return capo
        
def livello(diz,capo,liv=0):    #per quale motivo non funzioniiiiiiiiii???????
    if not capo:    
        return {}   
    dizi = {}
    lis = []
    for elem in capo:
        dizi.setdefault(liv,[]).append(elem)
        lis.extend(diz.get(elem,[]))
    dizi.update(livello(diz,sorted(lis),liv+1))
    return dizi

def dizionario_livelli(fnome,fout): #livello come ricorsiva
    with open(fnome) as f:
        testo=''.join(f.read())
        diz = json.loads(testo)
        capo=primo(diz)
        dizio=livello(diz, capo, liv=0)
        with open(fout, 'w') as o:
            json.dump(dizio, o)  


def nonso(d,y):
    l=list(d.values())
    di={}
    for Y in l:
        for X in Y:
            if X==y:
                w=l.index(Y)
                v=list(d.keys())
                
                for t in range(len(v[:w+1])):
                    di.setdefault(v[t],l[t])
    return di


def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as f:
        testo=''.join(f.read())
        diz = json.loads(testo)
        diz2={}
        for el in diz:
            dizi=elimina(diz, el)
            di=nonso(dizi,el)
            w=0
            for e in di:
                if len(di[e])==y:
                    w=w+1
            diz2.setdefault(el, w)
        with open(fout, 'w') as o:
            json.dump(diz2, o)
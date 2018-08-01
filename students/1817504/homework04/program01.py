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
#1
def genera_sottoalbero(fnome,x,fout):
    with open(fnome) as f:
        diz_alb=json.load(f)
    risposta={}
    if x in diz_alb:
        risposta=aggiungi(x,diz_alb,risposta)
    with open(fout,'w') as f:
        json.dump(risposta,f)

def aggiungi(x,diz_alb,risposta):
    risposta[x]=diz_alb[x]
    for i in diz_alb[x]:
        risposta=aggiungi(i,diz_alb,risposta)
    return risposta
    
#2
def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as f:
        diz_alb=json.load(f)
    if x in diz_alb:
        diz_alb=remove(x,diz_alb)
        
        for i in diz_alb.keys(): #toglie la x dala lista dell'antenato
            if x in diz_alb[i]:
                diz_alb[i].remove(x)
            
    with open(fout,'w') as f:
        json.dump(diz_alb,f)

def remove(x,diz_alb):
    for i in diz_alb[x]:
        remove(i,diz_alb)
    diz_alb.pop(x)
    return diz_alb
    
#3
def dizionario_livelli(fnome,fout):
    with open(fnome) as f:
        diz_alb=json.load(f)
        
    ins_valori=set()
    for i in diz_alb.keys():
        for j in diz_alb[i]:
            ins_valori.add(j)
    for chiave in diz_alb.keys():
        if chiave not in ins_valori:
            radice=chiave
            break
        
    risposta=ordina_elem_diz(crea_diz_lvl(radice,diz_alb,0,{}))
    with open(fout,'w') as f:
        json.dump(risposta,f)


def crea_diz_lvl(radice,diz_alb,livello,risposta):
    if livello not in risposta:
        risposta[livello]=[radice]
    else:
        risposta[livello]+=[radice]
    for i in diz_alb[radice]:
        crea_diz_lvl(i,diz_alb,livello+1,risposta)
    return risposta

def ordina_elem_diz(diz):
    for x in diz:
        diz[x]=sorted(diz[x])
    return diz
#4
def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as f:
        diz_alb=json.load(f)
        
    ins_valori=set()
    for i in diz_alb.keys():
        for j in diz_alb[i]:
            ins_valori.add(j)
    for chiave in diz_alb.keys():
        if chiave not in ins_valori:
            radice=chiave
            break
            
    risposta=crea_diz_antenati(radice,radice,diz_alb,{},y)
    with open(fout,'w') as f:
        json.dump(risposta,f)

def crea_diz_antenati(radice,nodo,diz_alb,risposta,y):
    if radice==nodo: risposta[nodo]=0
    else:
        if len(diz_alb[radice])==y: i=1
        else: i=0
        risposta[nodo]=risposta[radice]+i
    for figlio in diz_alb[nodo]:
        crea_diz_antenati(nodo,figlio,diz_alb,risposta,y)
    return risposta

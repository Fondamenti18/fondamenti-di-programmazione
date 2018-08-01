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
'''
import json
def crea_diz(fnome):
    with open(fnome) as f:
        stringa=f.read()
    return json.loads(stringa)

def genera(radice,diz):
    ret=dict()
    if radice in diz.keys():
        ret[radice]=diz[radice]
        for i in diz[radice]:
            diz2=genera(i,diz)
            for i in diz2.keys():
                ret[i]=diz[i]
    return ret
    
def cancella(x,diz):
    ret=diz
    if x in ret.keys():
        lista=ret.pop(x)
        for i in lista:
            ret=cancella(i,ret)
    cancella_foglia(x,ret)
    return ret

def cancella_foglia (x,diz):
    for i in diz.keys():
        lista=diz[i]
        if x in lista:
            lista.remove(x)
            return
    return

def definisci_root(diz):
    chiavi=set(diz.keys())
    valori=set()
    for a in chiavi:
        lista=diz[a]
        for i in lista:
            valori.add(i)
    c=chiavi-valori
    return c.pop()
            
def genera_sottoalbero(fnome,x,fout):
    diz =crea_diz(fnome)
    ret=genera(x,diz)
    salva(ret,fout)
    
def salva(diz, fout):
    uscita=open(fout, 'w', encoding='utf-8')
    json.dump(diz,uscita)
    uscita.close()
        
def cancella_sottoalbero(fnome,x,fout):
    diz=crea_diz(fnome)
    ret=cancella(x,diz)
    salva(ret,fout)
    
def dizionario_livelli(fnome,fout):
    diz=crea_diz(fnome)
    root=definisci_root(diz)
    ret=dict()
    ret[0]=[root]
    genera_livelli(root,diz,0,ret)
    for c in ret.keys():
        ret[c].sort()
    salva(ret,fout)
    
def genera_livelli(x,diz, cont,ret):
    lista=diz[x]
    if cont+1 in ret.keys():
        lista2=ret[cont+1]
        for i in lista:
            lista2.append(i)
    else:
        if len(lista)>0:
            ret[cont+1]=lista
    for a in lista:
        genera_livelli(a,diz,cont+1,ret)

def dizionario_gradi_antenati(fnome,y,fout):
    diz=crea_diz(fnome)
    antenati=conta_antenati(diz,y)
    salva(antenati,fout)

def conta_antenati(diz,grado):
    root=definisci_root(diz)
    padri=definisci_padri(diz)
    antenati=dict()
    for i in set(diz.keys())-{root}:
        if i not in antenati.keys():
            antenati[i]=0
            verifica_padre(i,diz,padri,grado, antenati,root)
    return antenati
    
def verifica_padre(nome, diz, padri, grado, antenati,root):
    if nome==root:  
        antenati[nome]=0
        return 0
    padre=padri[nome]
    cont=0
    if(definisci_grado(padre,diz)==grado):
        cont+=1
    cont+=verifica_padre(padre,diz,padri,grado,antenati,root)
    antenati[nome]=cont
    return cont

def definisci_padri(diz):
    padri=dict()
    for i in diz.keys():
        for j in diz[i]:
            padri[j]=i
    return padri

def definisci_grado(nodo,diz):
    return len(diz[nodo])
    
                


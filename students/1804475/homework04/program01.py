'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista 
(eventualmente vuota) degli identificativi dei  figli del nodo. Gli identificativi dei nodi 
all'interno delle liste sono in ordine lessicografico crescente.



Ecco un esempio di dizionario d che rappresenta un dizionario-albero

d={
'b':['c','d'],
'c':['i'],
'd':['e','l'],
'e':['f','g','h'],
'f':[],
'g':[],
'a':['b'],
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

- il nome di un file json contenente un dizionario-albero  d (fnome)
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
- il nome di un file json contenente un dizionario-albero  d (fnome)
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

def ricorsione_generaalbero(r,dizionario,x):
    r[x]=dizionario[x]
    for s in dizionario[x]:
        r[s]=dizionario[s]
        ricorsione_generaalbero(r,dizionario,s)
    return r
        
    

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as file:
        dizionario=json.load(file)
    r=dict()
    ricorsione_generaalbero(r,dizionario,x)
    file= open(fout,"w")
    json.dump(r,file)
    file.close()
    
        
def ricorsione_cancella(dizionario,x):
    for s in dizionario[x]:
        ricorsione_cancella(dizionario,s)
    del dizionario[x]

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as file:
        dizionario=json.load(file)
    ricorsione_cancella(dizionario,x)
    for s in dizionario:
        if x in dizionario[s]:
            dizionario[s].remove(x)
    file= open(fout,"w")
    json.dump(dizionario,file)
    file.close()

class Nodo():
    '''definisco la classe di un albero'''
    def __init__(self,nome):
        '''nome nodo e figlio nodo'''
        self.nome=nome
        self.figli=list()

    def stampa_albero(self):
        print(self.nome)
        for figlio in self.figli:
            figlio.stampa_albero()

def genera_albero(d,nomeNodo):
    '''Genera un albero partendo dal dizionario d e dal nodo nomeNodo'''
    radice = Nodo(nomeNodo)
    for figlio in d[nomeNodo]:
        radice.figli += [genera_albero(d, figlio)]
    return radice


def ricorsione_liv(r,radice,liv):
    if liv in r: #se livello in risultato dizionario
        r[liv]+=[radice.nome]#aggiungo alla chiave livello del risultato dizionario il nome del nodo
    else:
        r[liv]=[radice.nome]#crealo te
    for x in radice.figli:
        ricorsione_liv(r,x,liv+1)
    r[liv].sort()

def dizionario_livelli(fnome,fout):
    with open(fnome) as file:
        dizionario=json.load(file)
    padre=trova_padre(dizionario)
    radice=genera_albero(dizionario,padre)
    r = {}
    ricorsione_liv(r,radice,liv=0)
    file=open(fout,'w')
    json.dump(r,file)
    file.close()


def ricorsione_antenati(i,nodo,y,m):
    m[nodo.nome]=i
    if y ==len(nodo.figli):#se y è uguale al numero dei figli
        i+=1
    for x in nodo.figli:
        ricorsione_antenati(i,x,y,m)

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    i=0
    with open(fnome) as file:
        dizionario=json.load(file)
    padre=trova_padre(dizionario)
    albero=genera_albero(dizionario,padre)
    m = {}
    ricorsione_antenati(i,albero,y,m)
    file=open(fout,'w')
    json.dump(m,file)
    file.close()
    
def trova_padre(dizionario):
    lista1=set(dizionario.keys())
    lista3=set()
    for lista in dizionario.values():
        for x in lista:
            lista3.add(x)
    for x in lista1:
        if x not in lista3:
            return x
            

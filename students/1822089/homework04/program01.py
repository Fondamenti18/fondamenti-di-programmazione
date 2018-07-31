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

- il nome di un file json contenente un dizionario-albero  d (fnome)
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
La lista e' ordinata lessicograficamente ed in modo crescente. 
Il dizionario cosi' costruito va registrato nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_livelli(fname,fout)
il file fout conterra' il dizionario
{0: ['a'], 1: ['b'], 2: ['c', 'd'], 3: ['e','i','l'], 4: ['f', 'g', 'h']}

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fnome)
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

class Nodo:
    #Variabile di classe K=figlio ; V=oggetto padre
    figlio_padre={}
    
    def __init__(self, n):
        #Assegna un 'nome' al nodo e una lista di figli (inizialmente vuota)
        self.nome = n
        self.lista_figli = []

d_out={}
def genera_sottoalbero(fnome,x,fout):
    global d_out
    d_out={}
    #Load mi ritorno il tipo di dati estratto dal file (deserealizza il formato json)
    d=json.load(open(fnome))
    recurs_generate(d,x)
    #Dump serializza l'oggetto in formato json
    json.dump(d_out, open(fout,"w"))
    return

#Funzione ricorsiva per generare il sotto-albero
def recurs_generate(d,x):
    try:
        d_out[x]=d[x] #Aggiunge un sotto-albero (padre o foglia) al dizionario finale
        for nodo in d[x]: #Ripete le operazioni per ogni nodo figlio di x
            recurs_generate(d,nodo)
        return d_out
    except KeyError: #Se x non e' una chiave del dizionario
        return


def cancella_sottoalbero(fnome,x,fout):
    d=json.load(open(fnome))
    if x in d: #Se x non e una chiave del dizionario
        recurs_delete(d,x)
        clean_dict(d,x)
    json.dump(d,open(fout,"w"))
    return

#Funzione ricorsiva per cancellare il sotto-albero
def recurs_delete(d,x):
    #Elimina i dizionario x e' continua con i sotto-alberi
    for nodo in d.pop(x):
        
        recurs_delete(d,nodo)
    return

#Rimuove valori x in ogni chiave, se presenti
def clean_dict(d,x):
    for n in d:
        if x in d[n]: d[n].remove(x)
    return

def stampa_tree_indentations(nodo,livello=0):
    #Aggiunge 2*livello spazi prima del file
    print("  "*2*livello + nodo.nome)
    for figlio in nodo.lista_figli:
        stampa_tree_indentations(figlio, livello+1)

def dizionario_livelli(fnome,fout):
    global d_out
    d_out={}
    
    d=json.load(open(fnome,"r"))
    
    root=find_root(d)
    recurs_levels(d,root)
    
    json.dump(d_out, open(fout,"w"))
    return

#Funzione per trovare la radice dell'albero
def find_root(d):
    root=""
    #contiene tutti i valori del dizionario
    dict_values_str = str(list(d.values())).replace("[","").replace("]","").replace(" ","")
    dict_values_set = set(dict_values_str.replace("'","").split(","))
    for nodo in d:
        if nodo not in dict_values_set:
            root=nodo
            break
    return root

#Funzione ricorsiva per la creazione del dizionario dei livelli
def recurs_levels(d,n,level=0):
    #Aggiorna dizionario
    try:
        d_out[level]+=[n]
    except KeyError: #se la chiave 'level' non esiste ancora
        d_out[level]=[n]
    
    d_out[level].sort()
    #Esegue le operazioni per ogni nodo
    for nodo in d[n]:
        recurs_levels(d,nodo,level+1)
    return

def dizionario_gradi_antenati(fnome,y,fout):
    global d_out
    d_out={}
    
    d=json.load(open(fnome,"r"))
    
    #Ottengo la radice dal dizionario
    root=find_root(d)
    #Creo l'albero per ottenere i padri, i figli e l'oggetto 'radice'
    root_obj=tree_son_parent(d,root)
    #Aggiunge la radice al dizionario
    d_out[root]=0
    #Effettua i controlli degli antenati
    recurs_antenati(root_obj,y)
    #print(Nodo.figlio_padre)
    
    json.dump(d_out,open(fout,"w"))
    return

#Costruisce il dizionario {figlio:padre} e la lista dei figli per ogni nodo
def tree_son_parent(d,n):
    nodo=Nodo(n)
    #Aggiunge il 'padre' alla radice
    Nodo.figlio_padre[n]=""
    for figlio in d[n]:
        #Dopo le ricorsioni accedera' all'albero da sotto verso sopra
        nodo.lista_figli+=[tree_son_parent(d,figlio)] #Aggiunge i figli ad ogni nodo
        #Aggiunge il padre (oggetto) ad ogni nodo
        Nodo.figlio_padre[figlio]=nodo
    #Ritorna l'oggetto 'radice'
    return nodo

#Costruisce ricorsivamente il dizionario
def recurs_antenati(root_obj,y):
    #Scorre ogni nodo nelle 'lista_figli'
    for nodo in root_obj.lista_figli:
        global x
        x=0
        #Aggiorno il dizionario
        d_out[nodo.nome]=gradi_antenati(nodo,y)
        recurs_antenati(nodo,y)
    return
x=0
#Trova il numero di antenati di grado y
def gradi_antenati(n_obj,y,cont=0):
    global x
    figlio=n_obj.nome
    padre=Nodo.figlio_padre[figlio]
    if padre=="":
        x=cont
        return cont
    if len(padre.lista_figli)==y:
        return gradi_antenati(padre,y,cont+1)
    gradi_antenati(padre,y,cont)
    return x





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
albero={}
sottoAlbero={}
livelloAlbero={}
listaTuple=[]


def genera_sottoalbero(fnome,x,fout):
    albero.clear()
    albero.update(apriFile(fnome))    
    sottoAlbero.clear()
    scorriAlbero(x)
    saveFile(fout,sottoAlbero)
    

def cancella_sottoalbero(fnome,x,fout): 
    albero.clear()
    albero.update(apriFile(fnome))
    sottoAlbero.clear()   
    eliminaAlbero(x)
    saveFile(fout,albero)
    

def dizionario_livelli(fnome,fout):
    dizionario={}
    sortDiz={}
    albero.clear()
    albero.update(apriFile(fnome))
    contaAlbero(dizionario,list(albero.keys())[0],0)
    sortDiz=sortLivelli(dizionario)
    saveFile(fout,sortDiz)
 

def dizionario_gradi_antenati(fnome,y,fout):
    listaAntenati={}
    albero.clear()
    albero.update(apriFile(fnome))
    for key in albero.keys():
        listaAntenati[key]=antenati(key,y,0)
    saveFile(fout,listaAntenati)
    
    
def putValue(diz,chiave,valore):
    
    if chiave in diz:
        lista=diz[chiave]
    else:
        lista=[]
    lista.append(valore)
    diz[chiave]=lista
    

def apriFile(nome_file):
    with open(nome_file, 'r') as f:
        data = json.load(f)
        if not f.closed:
            f.close()
    return data


def saveFile(nome_file,dati):
    with open(nome_file, 'w') as f:
        json.dump(dati, f)
        if not f.closed:
            f.close()


def scorriAlbero(chiave):
    if albero[chiave] == '':
        sottoAlbero[chiave]=[]
        return
    else:
        sottoAlbero[chiave]=albero.get(chiave)
        for val in albero.get(chiave):
            scorriAlbero(val)
        
def eliminaAlbero(chiave):
    scorriAlbero(chiave)
    keys=sottoAlbero.keys()
    for key in keys:
        del albero[key]
    for key in albero.keys():
        if chiave in albero[key]:
            albero[key].remove(chiave)
    
def contaAlbero(dizionario,chiave,livello):
    putValue(dizionario,livello,chiave)
    if albero[chiave] == '':
        return
    else:
        for val in albero.get(chiave):
            contaAlbero(dizionario,val,livello+1)            
def sortLivelli(diz):
    for key in diz.keys():
        diz[key]=sorted(diz[key])
    return diz

def antenati(nodo,parent,cont):
    if nodo==list(albero.keys())[0]:  
        return cont
    else:        
        for x in albero:
            if nodo in albero.get(x):
                if parent==len(albero[x]):
                    cont+=1            
                return antenati(x,parent,cont)
  









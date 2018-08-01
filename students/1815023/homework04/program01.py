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

#-------Funzioni mie---------

class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.lista_figli = []


def crea_albero_da_nodo(diz, radice):
    '''Crea un albero da un dizionario partendo dalla chiave radice'''
    albero = Nodo(radice)
    if diz[radice] != []:
        for figlio in diz[radice]:
            albero.lista_figli += [crea_albero_da_nodo(diz,figlio)]
    return albero

def albero_in_dizionario(radice,diz):
    if radice.lista_figli == []:
        diz[radice.valore] = []
    else:
        for figlio in radice.lista_figli:
            if radice.valore not in diz:
                diz[radice.valore] = [figlio.valore]
            else:
                diz[radice.valore] += [figlio.valore]
            albero_in_dizionario(figlio,diz)

def canc_sottoalbero_diz(nodo, diz):
    for figlio in diz[nodo]:
        canc_sottoalbero_diz(figlio, diz)
    diz.pop(nodo)

def livelli_in_dizionario(albero, diz, h=0):
    '''Inserisce nel diz i livelli dell'albero con i relativi nodi'''
    if h in diz:
        diz[h].append(albero.valore)
    else:
        diz[h] = [albero.valore]
    for figlio in albero.lista_figli:
        livelli_in_dizionario(figlio, diz, h+1)
        diz[h+1].sort()

def conta_antenati(albero, y, diz, count = 0):
    ''' Conta il numero di antenati di grado y e ritorna un dizionario'''
    diz.update({albero.valore:count})
    if albero.lista_figli == []: return 0
    if len(albero.lista_figli) == y:
        for figlio in albero.lista_figli:
            conta_antenati(figlio, y, diz, count+1)
    else:
        for figlio in albero.lista_figli:
            conta_antenati(figlio, y, diz, count)


def trova_radice(diz):
    ris = set()
    for lista in diz.values():
        for el in lista:
            ris.add(el)

    for chiave in diz:
        if chiave not in ris:
            return chiave



#-------Funzioni dell'esercizio-----------

def genera_sottoalbero(fnome, x, fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        diz = json.load(f)

    sottoalbero = crea_albero_da_nodo(diz, x)

    ris = {}
    albero_in_dizionario(sottoalbero,ris)

    with open(fout,'w') as f:
        json.dump(ris,f)



def cancella_sottoalbero(fnome, x, fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        diz = json.load(f)

    for nodo in diz:
        if x in diz[nodo]:
            diz[nodo].pop(diz[nodo].index(x))

    canc_sottoalbero_diz(x, diz)

    with open(fout,'w') as f:
        json.dump(diz,f)


def dizionario_livelli(fnome, fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        diz = json.load(f)
    radice = trova_radice(diz)
    albero = crea_albero_da_nodo(diz, radice)

    ris = {}

    livelli_in_dizionario(albero, ris)

    with open(fout,'w') as f:
        json.dump(ris,f)


def dizionario_gradi_antenati(fnome, y, fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as f:
        diz = json.load(f)
    
    radice = trova_radice(diz)
    albero = crea_albero_da_nodo(diz, radice)
    ris = {}
    
    conta_antenati(albero, y, ris)
    
    with open(fout,'w') as f:
        json.dump(ris,f)

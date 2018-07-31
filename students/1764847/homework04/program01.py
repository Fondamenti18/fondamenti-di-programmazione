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

class Nodo(object):
    '''Oggetto nodo'''
    def __init__(self, valore, listaFigli):
        self.valore = valore
        self.litsaFigli = listaFigli
        
    def __str__(self):
        return str(self.valore) + ' ' + str(self.litsaFigli) 
        

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    albero = readFile(fnome)
    # Dizionario vuoto
    diz = {}
    # Chiama la funzione ricorsiva e mette in d il dizionario risultato
    d = genSubTree(albero, x, diz)
    # Converte in json il dizionario
    j = json.dumps(d)
    # Apre il file in scrittuta
    f = open(fout, 'w')
    # scrive il file
    f.write(j)
    # Chiude il file
    f.close()
    
    
    
def genSubTree(albero,x, diz):
    '''Prende in inmput il perecorso file di un albero, un nodo ed un 
    dizionario vuoto, Restituisce il sottoalbero con radice x'''
    # Se x non è presente nel dizionario restituisce il dizionario voto
    if not x in albero:
        return diz
    # Costruise il nodo
    nodo = Nodo(x, albero[x])
    # Associa come chiave il valore del nodo e come attributo la lista dei suoi figli
    diz[nodo.valore] = nodo.litsaFigli
    # Chiama ricorsivamente la funzione su tutti i figli
    for figlio in nodo.litsaFigli:
        genSubTree(albero, figlio, diz)
    #Restituisce il dizionario
    return diz

    
    
def readFile(fname):
    '''Prende in input un file json e lo restituisce'''
    f = open(fname, 'r')
    d = json.load(f)
    f.close()
    return d
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    # Dizionario vuoto
    diz = {}
    # Salva il dizionario in albero
    albero = readFile(fnome)
    # Radice 
    radice = searchRad(rotation(albero))
    # Chiama la funzione ricorsiva
    d = delSubTree(albero,x,diz, 0, radice, albero)
    # Converte in frmato json
    j = json.dumps(d)
    # Apre il file in scrittura
    f = open(fout, 'w')
    # Scrive sul file
    f.write(j)
    f.close()
    
def delSubTree(albero, x, diz, i, k, d):
    '''Elimina il sottoalbero con radice x'''
    lstF = []
    if x not in d:
        return diz
    
    nodo = Nodo(k, d[k])
    # Se il valore e' diverso da x
    if nodo.valore != x:
        # Per ogni figlio nella lista figli
        for figlio in nodo.litsaFigli:
            # Se figlio e' diverso da x lo aggiunge alla lista
            if figlio != x:
                lstF.append(figlio)
        diz[nodo.valore] = lstF
    # Chiama ricorsivamente la funzione su tutti i figli
    for figlio in lstF:
        delSubTree(albero,x,diz,i + 1, figlio, d)
    return diz
    
    

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    d = readFile(fnome)
    radice = searchRad(rotation(d))
    #lstKey = list(d.keys())
    diz = {0 : [radice], 1 : sorted(d[radice])}
    nodo = Nodo(radice, d[radice])
    lstFigli = nodo.litsaFigli
    res = levels1(d, diz, 2, lstFigli, [])
    j = json.dumps(res)
    f = open(fout, 'w')
    f.write(j)
    f.close()
    
    
def levels1(d, diz, cnt, lstFigli, lst):
    # Se la lista e' vuota restituisce il dizionario
    if lstFigli == []:
        return diz
    # Per ogni figlio in lstFigli
    for i in lstFigli:
        # Aggiunge i figli di i nella lista
        lst += d[i]
    # Se lst non e' vuota
    if lst != []:
        # Aggiunge al dizionario una nuova chiave che rappresenta l'altezza
        # e come valore la lista ordinata di tutti i nodi che si trovano in quell'altezza
        diz[cnt] = sorted(lst)
    # Chiama la funzione ricorsivamente 
    levels1(d, diz, cnt +1, lst, [])
    return diz
    
    

def rotation(albero):
    '''Effettua una rotazione di 180 gradi dell'albero'''
    #d = readFile(fnome)
    diz = {}
    for i in albero:
        for j in albero[i]:
            diz[j] = i
    return diz

def searchRad(albRot):
    '''Restituisce la radice dell'albero'''
    for i in albRot:
        if not albRot[i] in albRot:
            return albRot[i]

def createsTree(diz):
    '''Restituisce un dizionario con chiave il valore del nodo
    del nodo e come attributo la lista dei nodi da percorrere per
    arrivare alla radice'''
    lstKey = list(diz)
    diz1 = {}
    lst = []
    j = 0
    for i in diz:
        c = lstKey[j]
        j += 1
        diz1[i] = fRic(c, diz, lst)
        lst = []
    return diz1

def fRic(n, diz, lst):
    if not n in diz:
        return lst
    lst.append(diz[n])
    n = diz[n]
    fRic(n,diz,lst)
    return lst
        

def deegres(d, diz, y, albero, lstKey):
    '''Prende in input un dizionario fornito dalla 
    funzione createsTree, un indice, un dizionario,
    un valore y, un albero, e la lista delle chiavi dell'albero 
    (createsTree).
    Restituisce il dizionario richiesto'''
    for i in range(0,len(lstKey)):
        nodo = Nodo(lstKey[i], d[lstKey[i]])
        cnt = 0
        for figlio in nodo.litsaFigli:
            ff = Nodo(figlio, albero[figlio])
            if len(ff.litsaFigli) == y:
                cnt += 1
        diz[nodo.valore] = cnt
    return diz
    
    
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    albero = readFile(fnome)
    radice = searchRad(rotation(albero))
    #lstKey = list(albero)
    albRot = rotation(albero)
    d = createsTree(albRot)
    lstKey = list(d.keys())
    diz = {radice : 0}
    dizionario = deegres(d, diz, y, albero, lstKey)
    j = json.dumps(dizionario)
    f = open(fout, 'w')
    f.write(j)
    f.close()
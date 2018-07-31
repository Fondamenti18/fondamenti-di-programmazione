'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero e l'attributo della chiave e' la lista 
(eventualmente vuota) degli identificativi dei figli del nodo. Gli identificativi dei nodi 
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

- il nome di un file json contenente un dizionario-albero d (fnome)
- un identificativo x
- il nome di un file json (fout)

produce il dizionario-albero che rappresenta il sottoalbero radicato 
nell'identificativo x che si ottiene dal dizionario-albero d. 
Il dizionario-albero ottenuto va registrato nel file fout.
Se l'identificativo x non e' tra i nodi di d allora il dizionario-albero prodotto 
deve essere vuoto.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
genera_sottoalbero(fnome,'d',fout)
il file fout conterra' il dizionario
{'f': [], 'g': [], 'h': [], 'e': ['f', 'g', 'h'], 'l': [], 'd': ['e', 'l']}



2)
la funzione cancella_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero d (fnome)
- un identificativo x
- il nome di un file json (fout)

ricava da d il sottoalbero radicato in x e lo salva nel file fout.
Se x non e' presente tra le chiavi di d allora il dizionario-albero d non viene modificato.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
cancella_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'a': ['b'], 'b': ['c'], 'c': ['i'], 'i':[]}


3)
la funzione dizionario_livelli(fnome, fout) che, presi:
- il nome di un file json contenente un dizionario-albero d (fnome)
- il nome di un file json (fout)

costruisce il dizionario che ha come chiavi i livelli del dizionario-albero d. L'attributo di una 
chiave di valore x e' la lista degli identificativi dei nodi che si trovano a livello x nell'albero rappresentato da d. 
La lista è ordinata lessicograficamente ed in modo crescente. 
Il dizionario cosi' costruito va registrato nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_livelli(fname,fout)
il file fout conterra' il dizionario
{0: ['a'], 1: ['b'], 2: ['c', 'd'], 3: ['e','i','l'], 4: ['f', 'g', 'h']}

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, presi:
- il nome di un file json contenente un dizionario-albero d (fnome)
- un intero y
- il nome di un file json (fout)

costruisce il dizionario che ha come chiavi gli identificativi dei nodi dell'albero 
rappresentato dal dizionario-albero d. Attributo di una chiave di valore x e' il numero 
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

def leggiFile(fnome):
    with open(fnome) as f:
        fileLetto = json.load(f)
    return fileLetto

def scriviFile(contenuto , fout , modalita):
    with open(fout , modalita) as f:
        json.dump(contenuto, f)

def scava(leggi , x , albero):
    albero[x] = leggi[x]

    # Se caso base
    if albero[x] == []:
        return albero

    # Scandisce i valori di albero[x] (quindi gli elementi della lista)
    for i in albero[x]:
        scava(leggi , i , albero)
    
    # Una volta finito tutto, mi ritorna il dizionario
    return albero

def scavaContando(leggi , chiave , albero , livello):
    # append lo fa solo se la chiave e' presente
    if livello in albero:
        albero[livello].append(chiave)
        albero[livello].sort()
    else:
        albero[livello] = []
        albero[livello].append(chiave)
    
    # Scandisce i valori di leggi[chiave] (quindi gli elementi della lista)
    for elementi in leggi[chiave]:
        albero = scavaContando(leggi , elementi ,  albero , livello + 1)
    
    return albero

def leggiPrimo(dizionario):
    valori = dizionario.values()
    chiavi = dizionario.keys()
    
    # set di una stringa (la chiave) ritorna un set (quindi un insieme senza duplicati)
    c = set()
    tmp = []
    for scorri in chiavi:
        tmp.append(scorri)
    c = set(tmp)
    
    # set di una lista ritorna un set separato da ,
    v = set()
    for scorri in valori:
        v |= set(scorri)

    zero = c - v
    zero = str(zero)
    zero = zero.replace("'",'')
    zero = zero.replace("{",'')
    zero = zero.replace("}",'')
    
    return zero

def cercaAntenati(chiave , leggi , albero , grado , contatore):
    albero[chiave] = contatore

    if len(leggi[chiave]) == grado:
        contatore += 1
    
    # Se caso base
    if leggi[chiave] == []:
        return
    
    # Scandisce i valori di leggi[chiave] (quindi gli elementi della lista)
    for elementi in leggi[chiave]:
        cercaAntenati(elementi , leggi , albero , grado , contatore)
        
    return albero

# ===========================
# ==== FUNZIONI HOMEWORK ====
# ===========================


def genera_sottoalbero(fnome,x,fout):
    # leggi e' un dizionario
    leggi = leggiFile(fnome)
    
    # Se l'identificativo x non e' tra i nodi di leggi
    if x not in leggi:
        scriviFile('{}' , fout , 'w')
        return
    
    risultatoFinale = dict()
    risultatoFinale = scava(leggi , x , dict())
    
    scriviFile(risultatoFinale , fout , 'w')


def cancella_sottoalbero(fnome,x,fout):
    # leggi e' un dizionario
    leggi = leggiFile(fnome)

    # Se l'identificativo x non e' tra i nodi di leggi
    if x not in leggi:
        return
    
    risultatoSottoAlbero = scava(leggi , x , dict())
    
    # Scandisce gli indici di risultatoFinale
    risultatoFinale = leggi.copy()
    tmp = leggi.copy()
    for i in risultatoFinale:
        if i in risultatoSottoAlbero:
            del tmp[i]

    # Mi restituisce i valori del dizionario
    valori = tmp.values()
    # Questo mi serve per cancellare un valore da un nodo
    for cerca in valori:
        if x in cerca:
            cerca.remove(x)
            break

    # tmp ora ha i valori aggiornati
    risultatoFinale = tmp.copy()
    scriviFile(risultatoFinale , fout , 'w')
    

def dizionario_livelli(fnome,fout):
    # leggi e' un dizionario
    leggi = leggiFile(fnome)
    # zero e' una stringa della chiave di partenza
    zero = leggiPrimo(leggi)
    
    risultatoFinale = scavaContando(leggi , zero , dict() , 0)
    scriviFile(risultatoFinale , fout , 'w')

def dizionario_gradi_antenati(fnome,y,fout):
    # leggi e' un dizionario
    leggi = leggiFile(fnome)
    # zero e' una stringa della chiave di partenza
    zero = leggiPrimo(leggi)
    risultatoFinale = cercaAntenati(zero , leggi , dict() , y , 0)
    scriviFile(risultatoFinale , fout , 'w')

if __name__ == '__main__':
    #genera_sottoalbero('Alb10.json','d','tAlb10_1.json')
    #cancella_sottoalbero('Alb10.json','d','tAlb10_2.json')
    #dizionario_livelli('Alb10.json','tAlb10_3.json')
    #dizionario_gradi_antenati('Alb10.json',2,'tAlb10_4.json')
    #dizionario_livelli('Alb100.json','tAlb100_3.json')
    genera_sottoalbero('Alb50000.json','anglofobo','tAlb50000_1.json')
    cancella_sottoalbero('Alb50000.json','zarzuela','tAlb50000_2.json')
    dizionario_livelli('Alb50000.json','tAlb50000_3.json')
    dizionario_gradi_antenati('Alb50000.json',2,'risAlb50000_4.json')

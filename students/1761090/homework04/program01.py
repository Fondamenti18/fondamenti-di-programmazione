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
La lista ordinata lessicograficamente ed in modo crescente. 
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

def genera_sottoalbero(fnome,nodo,fout, albero=None): 
    gestisci_file = albero is None  # controllo se la prima chiamata, in caso gestisco i file
    if gestisci_file: # se l'albero e' vuoto 
        with open(fnome) as f: #apri l'albero 
            albero = json.load(f) #carico il file

    dizionario = {nodo: [figlio for figlio in albero[nodo]]} # inizializzo il dizionario con i figli del nodo corrente
    for figlio in dizionario.copy()[nodo]:  # per ogni figlio del nodo corrente, aggiorno il dizionario ricorsivamente
        dizionario.update(genera_sottoalbero(fnome, figlio, fout, albero)) #aggiorno il dizionario con funzione update con chiamata ricorsiva


    if gestisci_file and fout: # se l'albero e' vuoto
        with open(fout, 'w') as f: #scrivo il file in uscita
            json.dump(dizionario, f)

        return

    return dizionario

'''     trova la radice tramite differenza insiemistica: l'unico nodo che non figlio di nessun nodo la radice    '''
def trova_radice(albero): #trovo la radice dell'albero 
    figli_totali = set([figlio for figli in albero.values() for figlio in figli]) # metto in un insieme i figli dell'albero 
    nodi_totali = set(albero.keys()) # metto i nodi in un insieme

    return nodi_totali.difference(figli_totali).pop() # faccio la differenza tra i nodi

def cancella_sottoalbero(fnome,nodo,fout, albero=None):
    gestisci_file = albero is None  # controllo se e' la prima chiamata, in caso gestisco i file
    if gestisci_file: # se l'albero e' vuoto 
        with open(fnome) as f: # apro il file
            albero = json.load(f)

    if not albero[nodo]:    # caso base: sono una foglia, allora mi tolgo dall'albero
        albero.pop(nodo)
    else:
        # ricorsione: per ogni figlio, prima elimino ricorsivamente i loro sottoalberi, poi elimino i figli stessi
        for figlio in albero[nodo][:]: # per figlio in tutti i nodi dell'albero
            albero = cancella_sottoalbero(fnome, figlio, fout, albero) # albero senza sotto albero
            albero[nodo].remove(figlio) # rimuovo il figlio 
        albero.pop(nodo)    # infine elimino il nodo corrente

    if gestisci_file:
        for n, figli in albero.items():     # rimuovo il puntatore al nodo della prima chiamata dal padre di nodo
            if nodo in figli: # se nodo è in figli
                figli.remove(nodo) # rimuovo il nodo
                break #rompo il ciclo 

        with open(fout, 'w') as f:
            json.dump(albero, f)
        return

    return albero


def dizionario_livelli(fnome,fout, dizionario=None, albero=None, indice_livello=0):
    gestisci_file = dizionario is None  # controllo se e' la prima chiamata, in caso gestisco i file
    if gestisci_file: # se l'albero e' vuoto
        with open(fnome) as f:
            albero = json.load(f) # carico l'albero
            dizionario = {}         # inizializzo tutti i valori ed effettuo la prima chiamata ricorsiva
            radice = trova_radice(albero) # trovo la radice
            dizionario[indice_livello] = [radice] # ho l'indice
            dizionario_livelli(fnome, fout, dizionario, albero, indice_livello + 1) # chiamata ricorsiva


    if indice_livello > 0: # se il livello e' 0 
        '''se non era la prima chiamata significa che non siamo al livello 0, allora per ogni nodo del livello superiore
        aggiungo i suoi figli al livello corrente'''
        lista_livello = []
        for nodo in dizionario[indice_livello-1]: 
            for figlio in albero[nodo]:
                lista_livello.append(figlio)

        if lista_livello:   # se non sono arrivato all'ultimo livello, scendo ricorsivamente
            dizionario[indice_livello] = sorted(lista_livello)
            dizionario_livelli(fnome, fout, dizionario, albero, indice_livello + 1)

        ''' poiche ogni volta passo il riferimento all'oggetto dizionario (ne esiste una sola istanza)
        esso viene modificato dalle chiamate ricorsive, e quando si ritorna alla prima chiamata, la variabile dizionario
        vede l'istanza correttamente modificata di esso; di conseguenza non serve che questa funzione ritorni nulla'''

    if gestisci_file:
        with open(fout, 'w') as f:
            json.dump(dizionario, f)


def dizionario_gradi_antenati(fnome,y,fout, albero = None, dizionario=None, nodo=None, count=0):
    gestisci_file = albero is None  # controllo se e' la prima chiamata, in caso gestisco i file
    if gestisci_file:
        with open(fnome) as f:
            albero = json.load(f)

        dizionario = {}     # inizializzo tutti i valori
        nodo = trova_radice(albero)

    dizionario[nodo] = count    # assegno il numero di antenati di grado y al nodo corrente

    if len(albero[nodo]) == y:
        count+=1
        # se il nodo corrente e' di grado y, tutti i suoi discendenti avranno un numero count+1 di antenati con grado y

    for figlio in albero[nodo]:
        dizionario_gradi_antenati(fnome, y, fout, albero, dizionario, figlio, count)

    if gestisci_file:
        with open(fout, 'w') as f:
            json.dump(dizionario, f)

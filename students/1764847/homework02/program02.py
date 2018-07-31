'''
Un  file di compiti contiene  informazioni su un insieme  di compiti da eseguire.
Esistono  due tipologie di compiti:
- compiti che possono essere eseguiti indipendentemente dagli altri.
- compiti da svolgere  solo al termine di un compito preliminare.
I compiti del primo tipo sono codificati nel file mediante una linea che contiene
in sequenza le due sottostringhe "comp" ed "N" (senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "N" e' l'ID del compito (un numero positivo).
Compiti del secondo tipo sono codificati nel file mediante due linee di codice.
-- la prima  linea,  contiene in sequenza le due sottostringhe "comp" ed "N" 
(senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "N" e' l'ID del compito (un numero positivo).
-- la seconda linea (immediatamente successiva nel file) contiene 
in sequenza le due sottostringhe "sub" ed "M" (senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "M" e' l'ID del compito preliminare.

il seguente file di compiti contiene informazioni su 4 compiti (con identificativi 1,3,7 e 9). 
I compiti con identificativi 1 e 9 possono essere svolti indipendentemente dagli altri mentre i compiti 
con identificativo 3 e 7 hanno entrambi un compito preliminare.

comp 3
 sub 9
        comp1
comp              9
    comp 7
sub3

Scrivere la funzione pianifica(fcompiti,insi,fout) che prende in input:
- il percorso di un file (fcompiti) 
- un insieme  di ID di compiti da cercare (insi)
- ed il percorso di un file (fout) 
e che salva in formato JSON nel file fout un dizionario (risultato).

Il dizionario (risultato) dovra' contenere come chiavi gli identificativi (ID) dei compiti 
presenti in fcompiti e richiesti nell'insieme insi.
Associata ad ogni ID x del dizionario deve esserci una lista contenente  gli identificativi (ID) dei compiti 
che bisogna eseguire prima di poter eseguire il compito x richiesto
(ovviamente la lista di un ID di un compito che non richie un compito preliminare risultera' vuota ). 
Gli (ID) devono comparire nella lista nell'ordine di esecuzione corretto, dal primo fino a quello precedente a quello richiesto 
(ovviamente il primo ID di una lista non vuota corripondera' sempre ad un compito che non richiede un compito preliminare). 


Si puo' assumere che:
 - se l' ID di un compito che richieda un compito preliminare e' presente  in fcompiti 
    allora anche l'ID di quest'ultimo e' presente in fcompiti
 - la sequenza da associare al compito ID del dizionario esiste sempre
 - non esistono cicli (compiti che richiedono se' stessi anche indirettamente)


Ad esempio per il file di compiti  fcompiti contenente:

comp 3
 sub 9
        comp1
comp              9
    comp 7
sub3

al termine dell'esecuzione di  pianifica(fcompiti,{'7','1','5'}, 'a.json')
il file 'a.json' deve contenere il seguente dizionario
{'7':['9','3'],'1':[]}


Per altri esempi vedere il file grade02.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''
        
def pianifica(fcompiti,insi,fout):
    '''Prende in input il percorso file di un file,
    un insieme di id di compiti da cercare ed un percorso
    file dove salvare il risultato. Restituisce un dizionario
    in formato json che contiene come chiave gli id dei compiti
    presenti nell'insieme e come valore una lista che contiene
    gli id dei compiti che bisogna eseguire prima di poter eseguire
    il compito'''
    import json
    diz = creaDiz(readText(fcompiti))
    d = {}
    for i in insi:
        if i in diz:
            d[i] = []
    key = list(d.keys())
    for i in key:
        d[i] = cerca(i, key, diz)
    rJson = json.dumps(d)
    f = open(fout, 'w')
    f.write(rJson)
    f.close()
    
            
def cerca(key, listaChiavi, dizionario):
    '''Prende in input una chiave, una lista di chiavi
    e un dizionario. Restituisce una lista che contiene
    tutti i compiti sub della chiave'''
    lst = []
    c = key
    i = 0
    while True:
        if i >= len(listaChiavi):
            i = 0
        if len(dizionario[c]) < 1:
            break
        else:
            lst.append(dizionario[c])
            c = dizionario[c]
        i += 1
    lst = invertiLista(lst)
    return lst
   

     
def invertiLista(lst):
    '''Presa in input una lista, ne restituisce un'altra
    uguale ma con gli elementi invertiti'''
    lista = []
    for i in range(len(lst)-1, -1, -1):
        lista.append(lst[i])
    return lista
    

        

def readText(file):
    '''Prende in input un file e restituisce una litsa
    di righe del file senza spazi all'inizio e alla fine'''
    f = open(file, 'r', encoding = 'utf-8')
    lstRighe = f.readlines()
    f.close()                                       
    for riga in range(len(lstRighe)):               
        lstRighe[riga] = lstRighe[riga].strip()     
    return lstRighe



def creaDiz(lst):
    '''Presa in input una lista di compiti,
    restituisce un dizionario dove come chiave 
    c'e' il compito e come valore il sub se esiste,
    altrimenti la stringa vuota'''
    d = {}
    for i in range(len(lst)):
        if 'comp' in lst[i]:
            d[cleanS(lst[i])] = ''
        elif 'sub' in lst[i]:
            d[cleanS(lst[i-1])] = cleanS(lst[i])
    return d
            

            
def cleanS(s):
    '''Prende in input una stringa qualsiasi,
    ne restituisce un'altra formata da soli numeri'''
    stri = ''
    for i in s:
        if i.isdigit():
            stri += i
    return stri
    
            
    
    
    

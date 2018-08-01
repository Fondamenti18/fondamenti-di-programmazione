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


import json
from os.path import getsize

def pianifica(fcompiti,insi,fout):
    '''funzione che fa il dump in json'''
    b = bytearray(getsize(fcompiti))
    diz = {}
    with open(fcompiti,'rb',buffering=64000) as f:   #apro il file
        f.readinto(b)
    listCompiti = b.decode(encoding='utf8').splitlines()
    dizCompSubb = dizCompSub(listCompiti)
    setID = set(map(lambda x: getHwID(x),listCompiti))  #mi creo un insieme con tutti gli ID
    insiemeID = insi.intersection(setID)
    for id in insiemeID:
        diz[id] = dizCompSubList(dizCompSubb,id)


    with open(fout,'w',encoding='utf8') as f:
        json.dump(diz,f)  #dump del json

def checkNextSub(compiti,index):
    """funzione che controlla se il compito successivo e' sub o comp(true or false)"""
    try:
        return 'sub' in compiti[index+1]   #se 'sub' è presente nella riga successiva ritorna true se no falso
    except IndexError:  #se l'indice sfora stiamo all'ultima posizione da controllare
        return 'sub' in compiti[-1]    #quindi vedo direttamente a -1


def getHwID(compiti):
    """funzione che ritorna l'id del compito/sub"""
    id = '' #mi dichiaro la stringa id vuota
    for x in compiti:    #per ogni parola nella riga del compito
        if x.isdigit(): #se e' un numero
            id += x #append del numero a id
        elif id != '':  #se x non è numero e id non è vuoto
            break   #fa il break
    return id   #ritorna l'id

def dizCompSub(compiti):
    """funzione che ritorna un dizionario con il comp e il suo sub {comp:sub}"""
    diz = {}
    for x in range(len(compiti)):
        if checkNextSub(compiti, x):
            try:
                diz[getHwID(compiti[x])] = getHwID(compiti[x+1])
            except:
                diz[getHwID(compiti[-2])] = getHwID(compiti[-1])
    return diz


def dizCompSubList(dizSub,id):
    lst = []
    while id in dizSub:
        id = dizSub[id]
        lst.insert(0,id)
    return lst







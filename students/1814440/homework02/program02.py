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
comp 9
comp 7
sub 3

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

def eseguiJoin(primo,secondo):
    ''' ritorna la parte stringa e la pate numero delle due righe lette '''
    parola1=''.join([c for c in primo if c.isalpha()])
    parola2=''.join([c for c in secondo if c.isalpha()])
    numero1=''.join([c for c in primo if c.isdigit()])
    numero2=''.join([c for c in secondo if c.isdigit()])
    return parola1,parola2,numero1,numero2

def registra(parola2,numero1,numero2,diz):
    if parola2=='sub': # se vero vuol dire che in secondo ho il compito da fare prima del primo
        diz[numero1]=numero2
    else:
        diz[numero1]=[]
        
def creaDiz(diz,fcompiti):
    with open(fcompiti,'r',encoding='utf-8') as f: # apro il file
        primo=f.readline()
        secondo=f.readline()
        parola1,parola2,numero1,numero2=eseguiJoin(primo,secondo)
        registra(parola2,numero1,numero2,diz)
        while True:
            if parola2=='sub': # se il primo ed il secondo formano un homework a se stante
                primo=f.readline()
                secondo=f.readline()
                parola1,parola2,numero1,numero2=eseguiJoin(primo,secondo)
                try:
                    l=secondo.split()[0]
                    registra(parola2,numero1,numero2,diz)
                except:
                    diz[numero1]=[]
                    return diz
            else:
                primo=secondo
                secondo=f.readline()
                parola1,parola2,numero1,numero2=eseguiJoin(primo,secondo)
                registra(parola2,numero1,numero2,diz)

def calcola(diz,compito):
    ''' calcola per ogni compito la lista dei compiti da eseguire prima di esso in ordine '''
    lista=[]
    n=''
    while True:
        try:
            n=diz[compito]
        except:
            return None
        if n==[]:
            lista.reverse()
            return lista
        lista.append(n)
        compito=n

def creaSecondo(diz,insi):
    ''' creo il dizionario che poi registrerò come JSON'''
    ret={}
    for compito in insi:
        l=calcola(diz,compito)
        if l!=None:
            ret[compito]=l
    return ret

def scriviJSON(ret,fout):
    ''' scrivo il JSON nel file '''
    with open(fout,'w') as f:
        json.dump(ret,f)
    
def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    diz={}
    diz=creaDiz(diz,fcompiti) # creao il dizionario che contiene come chiave il compito e come argomento l'eventuale compito da svolgere prima
    ret=creaSecondo(diz,insi)
    scriviJSON(ret,fout)

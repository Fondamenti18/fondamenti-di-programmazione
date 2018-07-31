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
import re, json, sys
sys.setrecursionlimit(3000)  
def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    diz = fd(fcompiti, insi)
    with open(fout, 'w') as out:
        json.dump(diz, out)
 
 
def f(file):
    diz = {}
    with open(file, mode='r', encoding='utf-8') as u:
        l = u.readlines()
    for k, v in enumerate(l):
        if v != l[-1]:
            if "comp" in v and "sub" not in l[k+1]:
                v = re.sub('[a-z]', '', v).strip()
                diz[v] = []
        else:
            if "comp" in l[-1]:
                v = re.sub('[a-z]', '', v).strip()
                diz[v] = []  
    return diz
 
def fb(file):
    diz = {}
    with open(file, mode='r', encoding='utf-8') as u:
        l = u.readlines()
    for k, v in enumerate(l):
        if v != l[-1]:
            if "comp" in v and "sub" in l[k+1]:
                v = re.sub('[a-z]', '', v).strip()
                y = re.sub('[a-z]', '', l[k+1]).strip()
                diz[v] = y           
    return diz
                   
def fc(file, insi):
    y = f(file)
    x = fb(file)
    diz = {}
    for z in insi:
        if y.get(z) != None:
            #print(y.get(z), x.get(z))
            diz[z] = y.get(z)
        elif x.get(z) != None:
            diz[z] = [''.join(x.get(z))]
    return diz
 
def fd(p, insi):
    f = fc(p, insi)
    x = fb(p)
    for el in f.items():
        l.clear()
        numero = ''.join(el[1])
        if numero:
            ok = costruisci_compito(x, numero)
            a = f.get(el[0])
            a += ok  
    return reverse_list(f)
 
def reverse_list(d):
    for el in d.keys():
        if isinstance(d[el], int) is False:
            d[el] = list(reversed(d.get(el)))
    return d       

l = []
def costruisci_compito(f, numero):
    if f.get(numero):
        l.append(f.get(numero))
        return costruisci_compito(f, f.get(numero))
    return l


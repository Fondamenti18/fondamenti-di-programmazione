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
import sys

def space_rmv_i(lst, t = 0):
    if t == 1: lst = lst.split(' ')
    while True:
        if lst[0] == '' and len(lst) > 1:
            del lst[0]
        else: break
    if t == 1: return " ".join(lst)
    else: return lst

def space_rmv_f(lst, t = 0):
    if t == 1: lst = lst.split(' ')
    while True:
        if lst[len(lst)-1] == '' and len(lst) > 1:
            del lst[len(lst)-1]
        else: break
    if t == 1: return " ".join(lst)
    else: return lst

def find_id(string):
    i = 0
    strid = ""
    while True:
        if string[i].isdigit():
            strid += string[i]
            i += 1
        else: break
    return strid

def risfc(lst, keys):
    c = 0
    while c < len(lst):
        lst[c] = lst[c].replace(str(keys[c]), " ", 1).replace("sub", " ", 1)
        lst[c] = space_rmv_i(lst[c], 1)
        lst[c] = space_rmv_f(lst[c], 1)
        c += 1
    return lst

def diz_gen(lst):
    c = 0
    keys = ""
    while c < len(lst):
        keys += str(find_id(lst[c])) + " "
        c += 1
    keys = keys.split(" ")
    lst = risfc(lst, keys)
    diz = dict(zip(keys, lst))
    return diz

def listina(dizion, ricerca, lista, ctrl=0):
    if ctrl == 1:
        lista = []
    a = dizion[ricerca]
    if a != '':
        lista.append(a)
        return listina(dizion, a, lista)
    else:
        return list(reversed(lista))

def dizionone(diz, lstsrch):
    c = 0
    lst = []
    while c < len(lstsrch):
        if lstsrch[c] in diz:
            lst.append(listina(diz, lstsrch[c], [], 1))
        else:
            del lstsrch[c]
            continue
        c += 1
    return dict(zip(lstsrch,lst))

def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    sys.setrecursionlimit(3000)
    fin = open(fcompiti,"r",encoding="utf-8")
    content = fin.read().replace("\n", " ").split("comp")
    c = 0
    while c < len(content):
        content[c] = space_rmv_i(content[c], 1)
        c += 1
    content = space_rmv_i(content)
    diz = diz_gen(content)
    with open(fout, "w", encoding="utf-8") as out:
        json.dump(dizionone(diz, list(insi)), out)
    fin.close()
    out.close()
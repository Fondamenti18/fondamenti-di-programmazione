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

def fun(diz,insi):
    '''la funzione fun crea un dizionario che associa ad ogni compito richiesto gli ID dei comipiti
        da cui dipende'''
    diz3 = {}
    for key in diz.keys():
        key0 = str(key)
        l = []
        if key0 in insi:
            # uso il while al posto della ricorsione
            while key0 in diz.keys():
                l.append(diz[key0])
                key0 = str(diz[key0])
            diz3[key] = l
    return(diz3)


def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    import json

    with open(fcompiti) as f:
        testo = f.read()
    compiti = testo.splitlines()

    # Compiti2 e' una lista che contiene solamente 'compN' e 'subM', si eliminano percio' tutti gli spazi inutili.
    compiti2 = []
    for stringa in compiti:
        stringa2 = ''
        for el in stringa:
            if el.isalnum():
                stringa2 += el
            else:
                pass
        compiti2.append(stringa2)

    # Creo delle tuple che saranno della forma (compN,[]) se sono del primo tipo, (compN,subM) se del secondo tipo.
    #  Queste tuple saranno contenute nella lista l_tuple.'''
    l_tuple = []
    l = len(compiti2)
    for i in range(l):
        tupla = ()
        c = compiti2[i].find('sub')
        if c == 0:
            tupla = (compiti2[i - 1], compiti2[i])
        else:
            tupla = (compiti2[i], [])
        l_tuple.append(tupla)

    # Creo una copia di l_tuple, che chiamo l_tuple2, che conterra' gli stessi elementi di l_tuple, ma 'slitttati' di uno verso destra.
    l_tuple2 = l_tuple[1:]
    l_tuple2.append(l_tuple[0])

    # Infine l_tuple3 conterra' le coppie comp-sub o comp-[] definitive.
    l_tuple3 = []
    for tupla1, tupla2 in zip(l_tuple, l_tuple2):
        if tupla1[0] == tupla2[0]:
            l_tuple3.append(tupla2)
        else:
            l_tuple3.append(tupla1)

    # diz e' un dizionario che associa gli ID. Piu' precisamente associa ad ogni ID di un compito gli ID dei compiti da cui dipende.
    diz = {}
    for tupla in l_tuple3:
        ident = tupla[0][4:]
        if tupla[1] == []:
            diz[ident] = tupla[1]
        else:
            sub = tupla[1][3:]
            diz[ident] = sub

    # creo diz3 tramite la funzione fun definita esternamente dalla funzione fcompiti
    diz3 = fun(diz,insi)

    # elimino l'elemento [] che viene riportato dopo ogni compito indipendente.
    for val in diz3.values():
        if val:
            for el in val[:]:
                if not el: val.remove(el)
            # metodo reverse poichè la lista di Id che creo è al contrario
            val.reverse()


    # salvo in json il dizionario da ritornare, nel file fout
    with open(fout, 'w') as f:
        json.dump(diz3, f)


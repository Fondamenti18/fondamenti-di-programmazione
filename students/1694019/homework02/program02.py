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

def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    with open(fcompiti, 'r', encoding = 'utf-8') as f: file = f.read()
    file0 = file.split()
    file0 = setta_list(file0)
    dizR = dict()
    dizF = dict()
    for x in range(len(file0)): #scorro e creo le prime coppie
        if file0[x] == 'comp':
            dizR[file0[x+1]] = []
        elif file0[x] == 'sub':
            dizR[file0[x-1]].append(file0[x+1])
    for k in dizR.keys():
        if k in insi:
           dizF[k] = dizR[k]
           if len(dizR[k]) > 0:
               vt = dizR[k][0] #vedi metodo .get()
               while len(dizR[vt]) > 0: #controlla ricorsivamente se ci sono sub compiti
                   if vt in dizR.keys() and len(dizR[vt]) > 0:
                       dizR[k].append(dizR[vt][0])
                       vt = dizR[vt][0]
    for k1 in dizF.keys():
        dizF[k1] = list(reversed(dizF[k1])) #ordino elementi in lista-valore
    with open(fout,'w') as f: #salva file out json
        json.dump(dizF,f)

def setta_list(lista): #setta la lista con alternanza comp-id / sub-id
    fileR = list()
    for elemento in lista:
        if elemento.isalpha() == False and elemento.isdigit() == False:
            numero, compito = setta_str(elemento)
            fileR.append(compito)
            fileR.append(numero)
        else:
            fileR.append(elemento)
    return fileR


def setta_str(stringa): #pulisce il file JSON da evenutali spazi e numeri collegati a str
    stringa = list(stringa)
    numero = ""
    compitoS = ""
    for x in stringa:
        if x.isdigit(): numero += x
        else: compitoS += x
    return numero,compitoS

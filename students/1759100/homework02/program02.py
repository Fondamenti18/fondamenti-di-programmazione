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
    dizionario=dict()
    ls=[]
    with open(fcompiti) as f:
        f=f.read()
        f=f.split()
        f=controllo(f)
        print(insi,f)
        for identificativo in insi:
            dizionario=cerca(identificativo,f,dizionario)
        for x in dizionario.keys():
            #if dizionario[x]!=[]:
                #for sub in dizionario[x]:
                 #   if sub in dizionario.keys():
                  #      dizionario[x]+=dizionario[sub]
                   # else:
                    #    dizionario[x]+=cerca_sub(sub,f)
            dizionario[x].reverse()
       # print(dizionario)
    with open(fout,'w') as file:
        json.dump(dizionario,file)
        

def controllo(lst):
    index=0
    while index<len(lst):
        if lst[index]!='comp' and lst[index]!='sub' and lst[index][0] not in '01234567890':
            compito=''
            numerocompito=''
            for char in lst[index]:
                if char not in '0123456789':
                    compito+=char
                else: numerocompito+=char
            lst[index:index+1]=[compito,numerocompito]
        index+=1
    return lst

def cerca_sub(compito,lista,ls):
    for i in range(len(lista)):
        if lista[i]==compito and lista[i-1]=='comp':
            if i!=len(lista) and i!=len(lista)-1 and lista[i+1]=='sub':
                ls+=lista[i+2]
                cerca_sub(lista[i+2],lista,ls)
            else: ls+=[]
    return ls
        
def cerca(compito,lista,dizionario):
    for i in range(len(lista)):
        if lista[i]==compito and lista[i-1]=='comp':
            if lista[i+1]=='sub':
                dizionario[lista[i]]=[lista[i+2]]
                ls=[]
                dizionario[lista[i]]+=cerca_sub(lista[i+2],lista,ls)
            else: dizionario[lista[i]]=[]
    return dizionario

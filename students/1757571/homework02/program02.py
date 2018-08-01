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

        
def cleanList(myWorks):
    #Funzione che presa in input una lista di compiti, produce una lista corretta
    #con solo stringhe comp, sub e rispettivi id
    myNewWorks=[]
    for string in myWorks:
        if string=="comp" or string=="sub" or string.isdigit()==True:
            myNewWorks.append(string)
        else:
            if string[0]=="c":
                myNewWorks.append(string[0:4])
                myNewWorks.append(string[4:])
            elif string[0]=="s":
                myNewWorks.append(string[0:3])
                myNewWorks.append(string[3:])
    return myNewWorks

def createFlag(myWorks, iden):
    #Data una lista ed un numero iden da cercare, ritorna la flag necessaria 
    #all'ottimizzazione del ciclo di createDict
    WorkLen=len(myWorks)
    index=0
    while index<WorkLen:
        if myWorks[index]==iden:
            if myWorks[index-1]=="comp":
                return index
            else:
                index=index+1
        else:
            index=index+1


def orderList(Associated):
    #Ordina la lista riscrivendola al contrario
    trueList=[]
    for element in reversed(Associated):
        trueList.append(element)
    return trueList

def createAssociation(myWorks, iden, Associated):
    #Data una lista ed un iden da ricercare, crea le associazioni necessarie da
    #relazionare alla chiave del dizionario di createDict
    LenWorks=len(myWorks)
    if iden in myWorks:
        flag=createFlag(myWorks, iden)
        if flag!=LenWorks:
            if myWorks[flag+1]=="comp" and myWorks[flag-1]=="comp":
                Associated= Associated+[]
            elif myWorks[flag+1]=="sub":
                newFlag=createFlag(myWorks,myWorks[flag+2])
                Associated=Associated+[myWorks[flag+2]]
                if newFlag!=LenWorks-1:
                    if myWorks[newFlag+1]=="sub":
                        Associated=Associated+[myWorks[newFlag+2]]
                        createAssociation(myWorks, newFlag, Associated)
        return orderList(Associated)
         

def createDict(myWorks,insi):
    #Crea il dizionario da scrivere nel file .json
    Dict={}
    for iden in insi:
        Associated=[]
        if iden in myWorks:
            Dict.update({iden:createAssociation(myWorks,iden,Associated)})
    return Dict
            
            
def pianifica(fcompiti,insi, fout):
    with open(fcompiti, 'r') as f:
        works=f.read()
        
    dirtyWorks=works.split()
    myWorks=cleanList(dirtyWorks)
    myDict=createDict(myWorks, insi)
    with open(fout, 'w') as r:
        finalFile=json.dump(myDict,r)
        
    return finalFile

  
    

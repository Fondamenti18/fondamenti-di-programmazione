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
e che salva in formato JSON nel file fout un finalDict (risultato).

Il finalDict (risultato) dovra' contenere come chiavi gli identificativi (ID) dei compiti 
presenti in fcompiti e richiesti nell'insieme insi.
Associata ad ogni ID x del finalDict deve esserci una lista contenente  gli identificativi (ID) dei compiti 
che bisogna eseguire prima di poter eseguire il compito x richiesto
(ovviamente la lista di un ID di un compito che non richie un compito preliminare risultera' vuota ). 
Gli (ID) devono comparire nella lista nell'ordine di esecuzione corretto, dal primo fino a quello precedente a quello richiesto 
(ovviamente il primo ID di una lista non vuota corripondera' sempre ad un compito che non richiede un compito preliminare). 


Si puo' assumere che:
 - se l' ID di un compito che richieda un compito preliminare e' presente  in fcompiti 
    allora anche l'ID di quest'ultimo e' presente in fcompiti
 - la sequenza da associare al compito ID del finalDict esiste sempre
 - non esistono cicli (compiti che richiedono se' stessi anche indirettamente)


Ad esempio per il file di compiti  fcompiti contenente:

comp 3
 sub 9
        comp1
comp              9
    comp 7
sub3

al termine dell'esecuzione di  pianifica(fcompiti,{'7','1','5'}, 'a.json')
il file 'a.json' deve contenere il seguente finalDict
{'7':['9','3'],'1':[]}


Per altri esempi vedere il file grade02.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''
        
from json import dump

def pianifica(fcompiti,insi,fout):
    
         
    linesList = open_file(fcompiti)
    rawDict = dict_creator(linesList)
    rawDict = dict_adjuster(rawDict,linesList)
    finalDict = occurrences_finder(rawDict,insi)
    finalDict = list_reverser(finalDict)
    json_writer(fout,finalDict)
                

def open_file(fcompiti):

    with open(fcompiti, 'r') as f: 
        fileContent = f.read()
        
    return fileContent.split("\n")


def dict_creator(linesList):

    rawDict = {}
    
    for index, line in enumerate(linesList):
        canAdd = False
        if "comp" in line:
            key = line.replace("comp", "").strip() 
            if "comp" in linesList[index+1]: 
                rawDict[key] = "" 
        elif "sub" in line:
            value = line.replace("sub", "").strip() 
            canAdd = True
        if canAdd: 
            rawDict[key] = value

    return rawDict


def dict_adjuster(rawDict,linesList):

    if 'comp' in linesList[-2]:
        last = linesList[-2]
        last = last.replace("comp", "").strip()
        rawDict[last] = linesList[-1]

    return rawDict


def occurrences_finder(rawDict,insi):

    finalDict = {}
    
    for element in insi:
        if element in rawDict:
            value = element
            finalDict[element] = []
            while rawDict[value] != "":
                finalDict[element].append(rawDict[value])
                value = rawDict[value]

    return finalDict


def list_reverser(finalDict):

    for element in finalDict:
        reversedList = finalDict[element]
        reversedList.reverse()
        finalDict[element] = reversedList

    return finalDict

def json_writer(fout,finalDict):

    with open(fout, 'w') as fp:
        dump(finalDict,fp)
    




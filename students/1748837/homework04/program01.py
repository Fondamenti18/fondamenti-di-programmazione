'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista 
(eventualmente vuota) degli identificativi dei  figli del nodo. Gli identificativi dei nodi 
all'interno delle liste sono in ordine lessicografico crescente.



Ecco un esempio di dizionario d che rappresenta un dizionario-albero

d={
'a':['b'],
'b':['c','d'],
'c':['i'],
'd':['e','l'],
'e':['f','g','h'],
'f':[],
'g':[],
'h':[],
'i':[],
'l':[]
}

L'albero rappresentato da d e'

                             'a'
                              |
                _____________'b'____________             
               |                            |            
              'c'                  ________'d'_______   
               |                  |                  |  
              'i'         _______'e'_______         'l'
                         |        |        |               
                        'f'      'g'      'h'


Implementare le seguenti funzioni:

1) 
la funzione genera_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

produce   il  dizionario-albero che rappresenta   il sottoalbero  radicato 
nell'identificativo x che si ottiene dal dizionario-albero d. 
Il dizionario-albero ottenuto va registrato nel file fout.
Se l'identificativo x non e' tra i nodi di d allora  il dizionario-albero prodotto 
deve essere vuoto.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
genera_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'f': [], 'g': [], 'h': [], 'e': ['f', 'g', 'h'], 'l': [], 'd': ['e', 'l']}



2)
la funzione cancella_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

ricava  da d il sottoalbero radicato in x e lo salva nel file fout.
Se x non e' presente tra le chiavi di  d allora  il dizionario-albero d non viene modificato.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
cancella_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'a': ['b'], 'b': ['c'], 'c': ['i'], 'i':[]}


3)
la funzione dizionario_livelli(fnome, fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- il nome di un file json (fout)

costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero d. L'attributo di una 
chiave di valore x e' la lista degli identificativi  dei nodi che si trovano a livello x  nell'albero rappresentato da d. 
La lista e' ordinata lessicograficamente ed in modo crescente. 
Il dizionario cosi' costruito va registrato nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_livelli(fname,fout)
il file fout conterra' il dizionario
{0: ['a'], 1: ['b'], 2: ['c', 'd'], 3: ['e','i','l'], 4: ['f', 'g', 'h']}

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- un intero y
- il nome di un file json (fout)

costuisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero 
rappresentato dal dizionario-albero d, Attributo di una chiave di valore x e' il numero 
di antenati di grado y che ha il nodo con identificativo x nell'albero.
Registra il dizionario costruito nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_gradi_antenati(fnome,2,fout)
il file fout conterra' il dizionario 
{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.
'''




import json

def genera_sottoalbero(fnome,x,fout):
    originalDict=json.load(open(fnome))
    with open(fout,'w') as f:
        json.dump(createDict(originalDict,x,dictionary={}),f)
    

def cancella_sottoalbero(fnome,x,fout):
    originalDict=json.load(open(fnome))
    toDelete=createDict(originalDict,x,dictionary={})                                         #i nodi da cancellare
    dictionary={i:originalDict[i] for i in originalDict.keys() if i not in toDelete.keys()}   #dizionario pulito da quei nodi
    for i in dictionary.keys():
        for x in dictionary[i]:
            if x not in dictionary.keys():
                dictionary[i].remove(x)                                                       #rimuovo dal dizionario pulito tutti i valori che non sono nodi
    with open(fout,'w') as f:
        json.dump({i:originalDict[i] for i in originalDict.keys() if i not in toDelete.keys()} ,f)
    

def dizionario_livelli(fnome,fout):
     originalDict=json.load(open(fnome))
     disorderedDict=countDict(originalDict,{},findRoot(originalDict),0)
     for i in disorderedDict.keys():
         disorderedDict[i].sort()
     with open(fout,'w') as f:
        json.dump(disorderedDict,f)
 

def dizionario_gradi_antenati(fnome,y,fout):
    originalDict=json.load(open(fnome))
    with open(fout,'w') as f:
        json.dump(findAncestors(originalDict,findRoot(originalDict),y,{},0),f)


def createDict(originalDict,x,dictionary):
    if x not in originalDict:
        return dictionary
    else:
        dictionary[x]=originalDict[x]
        if dictionary[x]:
            for i in dictionary[x]:
                dictionary=createDict(originalDict,i,dictionary)
    return dictionary

def countDict(originalDict,dictionary,node,count):
    if count in dictionary.keys():              #controllo se il livello gia è presente nel dizionario
        dictionary[count].append(node)          #se lo è aggiungo il nodo in esame a la lista corrispondente al livello
        #dictionary[count].sort()
    else:
        dictionary[count]=[node]
    if originalDict[node]:
        for i in originalDict[node]:
            dictionary=countDict(originalDict,dictionary,i,count+1)
    else:
        return dictionary
    return dictionary

def findAncestors(originalDict,node,y,dictionary,count):
    dictionary[node]=count
    if not(originalDict[node]):
        return dictionary
    if len(originalDict[node])==y:
        for i in originalDict[node]:
            dictionary=findAncestors(originalDict,i,y,dictionary,count+1)
    else:
        for i in originalDict[node]:
            dictionary=findAncestors(originalDict,i,y,dictionary,count)
    return dictionary


#funzione di comodo che trova la radice
def findRoot(originalDict):
    values=[]
    for i in originalDict.values():
        values+=i
    values=set(values)
    for i in originalDict.keys():
        if i not in values:
            return i

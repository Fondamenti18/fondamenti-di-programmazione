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


{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}

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
La lista è ordinata lessicograficamente ed in modo crescente. 
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
    '''inserire qui il vostro codice'''
    jsonOutDict=dict()
    fpIn=open(fnome,'r')
    jsonInDict=json.load(fpIn)
    result=recFunc1(jsonInDict,x,jsonOutDict)
    fpIn.close()
    fpOut=open(fout,'w')
    json.dump(result,fpOut)
    fpOut.close()


def recFunc1(jsonInDict,index,jsonOutDict):
    for itemIdx in jsonInDict[index]:
        recFunc1(jsonInDict,itemIdx,jsonOutDict)
    jsonOutDict[index]=jsonInDict[index]
    return jsonOutDict
    
def primo(jsonInDict):
    chiave=''
    insieme=set()
    for x in jsonInDict.values():
        for y in x:
            insieme.add(y)
    for g in jsonInDict.keys():
        if g not in insieme:
            chiave=g
    return chiave

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    jsonOutDict=dict()
    fpIn=open(fnome,'r')
    jsonInDict=json.load(fpIn)
    result=recFunc2(jsonInDict,primo(jsonInDict),x,jsonOutDict)
    fpIn.close()
    fpOut=open(fout,'w')
    json.dump(result,fpOut)
    fpOut.close() 

def recFunc2(jsonInDict,index,keyDel,jsonOutDict):
    if index != keyDel:
        if keyDel in jsonInDict[index]:
            appo=jsonInDict[index]
            appo.remove(keyDel)
            jsonOutDict[index]=appo
        else:
            jsonOutDict[index]=jsonInDict[index]
        for itemIdx in jsonInDict[index]:
                recFunc2(jsonInDict,itemIdx,keyDel,jsonOutDict)
    return jsonOutDict



def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    jsonOutDict=dict()
    fpIn=open(fnome,'r')
    jsonInDict=json.load(fpIn)
    result=recFunc3(jsonInDict,primo(jsonInDict),jsonOutDict)
    fpIn.close()
    fpOut=open(fout,'w')
    json.dump(result,fpOut)
    fpOut.close() 

def recFunc3(jsonInDict,index,jsonOutDict, livello=0):
    if livello in jsonOutDict:
        appo=list(jsonOutDict[livello])
        appo.append(index)
        appo.sort()
        jsonOutDict[livello]=appo
    else:
        jsonOutDict[livello]=[index]
    livello+=1
    for itemIdx in jsonInDict[index]:
        recFunc3(jsonInDict,itemIdx,jsonOutDict, livello)
    return jsonOutDict
     

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    jsonOutDict=dict()
    fpIn=open(fnome,'r')
    jsonInDict=json.load(fpIn)
    result=recFunc4(y,jsonInDict,primo(jsonInDict),jsonOutDict)
    fpIn.close()
    fpOut=open(fout,'w')
    json.dump(result,fpOut)
    fpOut.close() 

def recFunc4(ygrado,jsonInDict,index,jsonOutDict, livello=0):
    for nodo in jsonInDict[index]:
        grado=len(jsonInDict[index])
        if grado!=ygrado:
            recFunc4(ygrado,jsonInDict,nodo,jsonOutDict,livello)
        else:
            livello=livello+1
            recFunc4(ygrado,jsonInDict,nodo,jsonOutDict,livello)
            livello=livello-1
    ls=jsonOutDict.keys()
    if index not in ls:
        jsonOutDict[index]=livello
    return jsonOutDict

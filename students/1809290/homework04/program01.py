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
def trova_figli(valore,d,d3):    
    if valore not in d3:
        d3[valore]=[]
        
    for figlio in d[valore]:
        trova_figli(figlio,d,d3)
    return d3
    
def genera_sottoalbero(fnome,x,fout):
    d=json.load(open(fnome))
    file=open(fout,'w')
    d2={}
    if x in d:
        d2=trova_figli(x,d,d2)
        for k in d2:
            d2[k]=d[k]
    #print(d2)
    json.dump(d2,file)
    file.close()
    return d2
    
#genera_sottoalbero('Alb100.json','ultras','prova.json')

def cancella_sottoalbero(fnome,x,fout):
    d=json.load(open(fnome))
    file=open(fout,'w')
    d2={}
    risposta={}
    if x in d:
        d2=trova_figli(x,d,d2)
        for k in d2:
            del d[k]
    for k in d:
        if x in d[k]:
            d[k].remove(x)
    
    json.dump(d,file)
    file.close()
    return d
#cancella_sottoalbero('Alb10.json','d','prova.json')


def dizionario_livelli(fnome,fout):
    d=json.load(open(fnome))
    file=open(fout,'w')
    cont=0
    d3={}
    risposta={}
    for x in d:
        for t in d[x]:
            d3[t]=t
    for x in d:
        if x not in d3:
            risposta[cont]=[x]
            cont=1
            risposta[cont]=d[x]
    for x in d:
        d2={}
        lista=[]
        for k in d[x]:
            #print(d[x],k,'-------------------')
            if d[k]!=[]:
                d2[k]=d[k]
        if d2!={}:
            cont+=1
            for k in d2:
                lista+=(d2[k])
                lista.sort()
            risposta[cont]=lista
    
    json.dump(risposta,file)
    file.close()
    return risposta
            
        #print(cont,qprima)
    
    #file=open(fout,'w')
    #json.dump(                     d                           ,file)
    #file.close()
    #print(f)
#dizionario_livelli('Alb100.json','prova.json')
 

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''

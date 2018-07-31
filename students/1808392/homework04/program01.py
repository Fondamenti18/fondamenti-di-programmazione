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
import sys
#sys.setrecursionlimit(999999)
def genera_sottoalbero(fnome,x,fout):
    
    with open(fnome) as f:
        diz = json.load(f)
        res = {}
        if x in diz.keys():
            res = gen_tree(diz,x,res)
    with open(fout,'w') as out:         
        json.dump(res,out)

def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as f:
        diz = json.load(f)
        res = {}
        if x in diz.keys():
            res = gen_tree(diz,x,res)
               
    for key in diz.copy().keys():
        if key in res:
            del diz[key]
            continue
        
        if x in diz[key]:
            diz[key].remove(x)
        
    with open(fout,'w') as out:    
        json.dump(diz,out)    
        
    

def dizionario_livelli(fnome,fout):
    with open(fnome) as f:
        diz = json.load(f)
    keyP = trova_padre(diz)
    assegna = 0
    ret={}
    ret[assegna] =[keyP]
    diz = gen_treeL(diz,ret,[keyP],assegna+1)
    
    #ordino
    ris={}
    for key in diz.keys():
        ris[key] = sorted(diz[key])
        
    with open(fout,'w') as out:    
        json.dump(ris,out)

def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as f:
        diz = json.load(f)

    keyP = trova_padre(diz)
    assegna = 0
    ret={}
    ret[assegna] =[keyP]
    ret = gen_treeL(diz,ret,[keyP],assegna+1)
    ris={}
    for key in ret.keys():
        for value in ret[key]:
            count=0    
            count = trova_ant(diz,ret,y,value,key-1,count)
            ris[value] = count

    with open(fout,'w') as out:    
        json.dump(ris,out)

def gen_tree(diz,x,ret):
    ret[x] = diz[x]
    for el in diz[x]:
        ret[el] = diz[el]
        if diz[el] != []:
            for j in diz[el]:
                gen_tree(diz,j,ret)
        else:
            ret[el] = []
    return ret

def gen_treeL(diz,ris,lst,key):
    mylst = [diz[x] for x in lst if diz[x] != [] ]
    if mylst != []:
        for el in lst:
            for val in diz[el]:
                if key in ris.keys():
                    ris[key].append(val)
                else:
                    ris[key] = [val]
        gen_treeL(diz,ris,ris[key],key+1)
    else:
         return ris
    
    return ris

def trova_ant(diz,ret,NumAnt,key,keyR,countAnt):

    if keyR > 0: # chiave ret
        for value in ret[keyR]:  # per ogni valore della riga precedente quella che analizzo

            if key in diz[value]: # se la chiave che cerco è presente 
                if len(diz[value])==NumAnt: # e il grado è corretto
                        
                    countAnt+=1 # incremento
                    keyR -= 1
                    
                    countAnt = trova_ant(diz,ret,NumAnt,value,keyR,countAnt)
                else: # chiave trovata, ma sbagliato il grado, lo lancio variando chiave e keyr
                    keyR-=1
                        
                    countAnt = trova_ant(diz,ret,NumAnt,value,keyR,countAnt)
                    
                
        if countAnt == 0: # se non l'ho trovato, lo cerco nel nodo precedente... fino al primo       
            keyR-=1
            countAnt = trova_ant(diz,ret,NumAnt,key,keyR,countAnt)
            
        return countAnt
    else:
        return countAnt

def trova_padre(diz):
    # trovo la radice
    myset = diz.values()
    for key in diz.keys():
        
        if key not in myset:
            return key
    return 0

#args        = ('Alb10.json',2,'tAlb10_4.json')
#explanation = ''
#dizionario_gradi_antenati(*args)
#with open('tAlb10_4.json', encoding='utf8')as f: d1=load(f)
#with open('risAlb10_4.json', encoding='utf8')as f: d2=load(f)
#check(d1,d2, args,explanation, ('tAlb10_4.json','risAlb10_4.json')  )

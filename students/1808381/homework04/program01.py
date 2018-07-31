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

- il nome di un file json contenente un dizionario-albero  d (fnome)
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

- il nome di un file json contenente un dizionario-albero  d (fnome)
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
- il nome di un file json contenente un dizionario-albero  d (fnome)
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
- il nome di un file json contenente un dizionario-albero  d (fnome)
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

    with open(fnome) as s:
        dictionary = json.load(s)
    ris = {}
    
    tree = Tree(dictionary)
    ris = tree.findSons(x, ris)

    with open(fout, 'w') as outfile:
       json.dump(ris, outfile)
    return ris


def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    
    with open(fnome) as s:
        dictionary = json.load(s)
    ris = {}
    
    tree = Tree(dictionary)
    ris = tree.findSons(x, ris)
    for k in ris.keys():
        del dictionary[k]
        for j in dictionary.values():
            if k in j:
                j.remove(k)
   
    with open(fout, 'w') as outfile:
       json.dump(dictionary, outfile)   
           
    return dictionary
    
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    
    with open(fnome) as s:
        dictionary = json.load(s)
    
    tree = Tree(dictionary)
    ris1 = {}
    
    for x in dictionary.keys(): 
        ris1[x] = 0
        break
            
    for k,v in dictionary.items():
        
            a = tree.findSonsSingular(k)
            
            for el in a:
                ris1[el] = ris1[k]+1
    
      
    result = diz_invert(ris1)
    
    for k,v in result.items():
        result[k] = sorted(list(v))
    
    with open(fout, 'w') as outfile:
       json.dump(result, outfile)
    return result


def diz_invert(d):
    d2 = {}
    for k,v in d.items():
       
        if v not in d2:
    
            d2[v] = [k]
        else:
            d2[v] += [k]
    return d2    
        
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''

    with open(fnome) as s:
        dictionary = json.load(s)
    ris = {}
    ris1 = {}
    
    tree = Tree(dictionary)
    n = tree.findfathers(ris, dictionary)
    
    for k,v in dictionary.items():
        ris[k] = len(v)

    
    
    for k,v in n.items():
        count = 0
        
        for el in v:
            if el != '':
                if ris[el] == y:
                    
                    count +=1
        ris1[k] = count
    
    l = dict(sorted(ris1.items()))
    
     
    with open(fout, 'w') as outfile:
       json.dump(l, outfile)
    
    return l
    
class Tree(object):
    
    def __init__(self, dictionary):
        self.tree = dictionary

    def findSons(self, args, ris):

        ris[args] = self.tree[args]
        valore = self.tree[args]
        for i in valore:
            self.findSons(i, ris)
        
        return ris 
    
    def findSonsSingular(self, args):
        ris = ()
        if type(args) == list:
            for  el in args:
                ris += self.tree[el]
        else:
            ris = self.tree[args]
        
        return tuple(ris)
    

    def findfathers(self, ris, ris1):
        
        ris2 = {}
        for k,v in ris1.items():
            ris2[k] = ''
            break
        
        for k,v in ris1.items():
               
            for el in v:
                ris2[el] = k
        
        for k,v in ris2.items():
            
     
            if v in ris2:
                ris2[k] += ','+ris2[v]
        
        for k,v in ris2.items():
            
            ris2[k] = list(set(v.split(',')))
            ris2[k].remove('')
        
        return ris2


















if __name__ == '__main__':
    dizionario_gradi_antenati('Alb100.json', 2, 'tAlb100_4.json')

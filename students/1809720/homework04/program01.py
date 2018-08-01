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

def genera_sottoalbero(fnome,x,fout):
    
    save_list = [x]  
    file = json.load(open(fnome))    
    dict_copy = file.copy()
        
    def add(key):
        for value in dict_copy[key]:
            if value in save_list:
                add(value)
            save_list.append(value)
            
    for key in file:

        if key in save_list:
            add(key)
        else:
            del dict_copy[key]
    
    with open(fout, 'w') as fp:
        json.dump(dict_copy, fp)
    
            

def cancella_sottoalbero(fnome,x,fout):
    
    del_list = [x]  
    file = json.load(open(fnome))    
    dict_copy = file.copy()
    
    
    def add(key):
        for value in dict_copy[key]:
            if value in del_list:
                add(value)
            del_list.append(value)
            
    i = 0
    for key in file:
        if key in del_list:
            add(key)
            del dict_copy[key]
    for val in file.values():
        i=0
        while i<len(val):
            if val[i] in del_list:
                del val[i]
            i+=1

    with open(fout, 'w') as fp:
        json.dump(dict_copy, fp)
        
def dizionario_livelli(fnome,fout):
    
    file = json.load(open(fnome))    
    
    
    def level_dict(lista,elementi,iniz):
        final_d = {}
        new_elems = []
        if not elementi:
            return {}   
        for elem in elementi: # per ogni figlio della lista figli corrente
            final_d.setdefault(iniz,[]).append(elem)
            new_elems.extend(lista.get(elem,[]))
            new_elems.sort()
        final_d.update(level_dict(lista,new_elems,iniz+1))
        return final_d
    
    def search_root(bu):
        hold = bu
        for x in file.items():
            for a in x:
                if hold in x[1]:
                    return False
        return True
    
    def svani():          
        for x in file:
            check = True 
            check = search_root(x)
            if check:
                return x
    
    root = svani()
    nroot = root.split()
    d = level_dict(file,nroot,0)
    
    with open(fout, 'w') as fp:
        json.dump(d, fp)
    
def dizionario_gradi_antenati(fnome,y,fout):
    '''funzione'''
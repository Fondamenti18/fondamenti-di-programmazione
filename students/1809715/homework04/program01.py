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

def get_sottoalbero(d,x):

    r = {}
    
    if x not in d.keys():
        return r

    r[x] = d[x]
    for l in d[x]:
        r.update(get_sottoalbero(d, l))

    return r

def get_dad(d, k):
    
    dad = False
    for key, value in d.items():
        if k in value:
            dad = key
            break
        
    return dad

def get_ancestors(d, dad):
    ancestors = []
    while dad:
        dad = get_dad(d, dad)
        if dad:
            ancestors.append(dad)
    return ancestors

def load_json(fnome):
    with open(fnome) as json_data:
       return json.load(json_data)

def dump_json(fnome, data):
    with open(fnome, 'w') as fp:
        json.dump(data, fp)
        
    
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    d = load_json(fnome)
    r = get_sottoalbero(d,x)
    dump_json(fout, r)


def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    r = {}
    d = load_json(fnome)
    h = get_sottoalbero(d,x)
    for k in d.keys() - h.keys():
       r[k] = d[k]
       if (x in r[k]):
           r[k].remove(x)
           
    dump_json(fout, r)

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    d = load_json(fnome)

    glob_ant = {}
    output = {}
    count = 0

    for i in d:
      if not i in glob_ant:
       glob_ant[i] = count
      else:
       count = glob_ant[i]
      for j in d[i]:
       glob_ant[j] = count + 1

    for x in glob_ant:
     if not str(glob_ant[x]) in output:
        output[str(glob_ant[x])] = []
     if not x in output[str(glob_ant[x])]:
        output[str(glob_ant[x])].append(x)
     output[str(glob_ant[x])].sort()


    dump_json(fout,output)
    

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    d = load_json(fnome)
    glob_ant = {}
    for i in d:
        glob_ant[i] = {}
    for i in d:
        if not d[i] == 0:
            for j in d[i]:
                glob_ant[j][i] = len(d[i])
                undo = i
                while len(glob_ant[undo]) != 0:
                    for z in glob_ant[undo]:
                        glob_ant[j][z] = len(d[z])
                        undo = z
    return glob_ant

    output = {}
    for i in glob_ant:
        output[i] = 0
        for j in glob_ant[i]:
            if glob_ant[i][j] == y:
                output[i] = output[i] + 1

    return output

    dump_json(fout, output)


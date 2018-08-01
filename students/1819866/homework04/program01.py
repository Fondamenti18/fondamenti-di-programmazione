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
ù


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
    with open(fnome) as f:
        diz = json.loads(f.read())
    s = '{' + ricorsione1(diz, x).replace("'", '"')[:-2] + '}'
    with open(fout, 'w') as f:
        f.write(s)

def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as f:
        diz = json.loads(f.read())
    result = ricorsione2(diz, x)
    for k in result:
        if x in result[k]:
            v = result[k].index(x)
            del(result[k][v])
    with open(fout, 'w') as f:
        f.write(str(result).replace("'", '"'))

def dizionario_livelli(fnome,fout):
    with open(fnome) as f:
        diz1 = json.loads(f.read())
    diz2 = {}
    counter = 0
    keys, values = set(), set()
    for k in diz1:
        keys.add(k)
        for v in diz1[k]:
            values.add(v)
    radice = list(keys - values)
    result = ricorsione3(diz1, diz2, counter, radice)
    for k in result: result[k] = sorted(result[k])
    with open(fout, 'w') as f:
        f.write(str(result).replace("'", '"'))
 

def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as f:
        diz1 = json.loads(f.read())
    diz2 = {}
    counter = 0
    keys, values = set(), set()
    for k in diz1:
        keys.add(k)
        for v in diz1[k]:
            values.add(v)
    radice = list(keys - values)
    result = ricorsione4(diz1, diz2, counter, radice)
    with open(fout, 'w') as f:
        f.write(str(result).replace("'", '"'))
    
def ricorsione1(diz, value):
    if value not in diz: return '{}'
    elif diz[value] == []: return '"' + value + '"' +': '+ str(diz[value]) + ', '
    else:
        s = '"' + value + '"' +': '+ str(diz[value]) + ', '
        for i in range(len(diz[value])):
            s += ricorsione1(diz, diz[value][i])
        return s

def ricorsione2(diz, value):
    if value not in diz: return diz
    if diz[value] == []: 
        del(diz[value])
        return diz
    else:
        for el in diz[value]:
            diz = ricorsione2(diz, el)
        del(diz[value])
        return diz
    
def ricorsione3(diz1, diz2, counter, lista):
    diz2[str(counter)] = []
    lista2 = []
    for el in lista: 
        diz2[str(counter)] += [el]
        if len(diz1[el]) != 0: lista2 += diz1[el]
    counter1 = counter +1
    if lista2 != []: ricorsione3(diz1, diz2, counter1, lista2)
    return diz2
    
def ricorsione4(diz1, diz2, counter, lista):
    for el in lista: 
        diz2[el] = counter
        if len(diz1[el]) == 2:
            counter1 = counter + 1
            lista = diz1[el]
            ricorsione4(diz1, diz2, counter1, lista)
        elif len(diz1[el]) > 0:
            counter2 = counter
            lista = diz1[el]
            ricorsione4(diz1, diz2, counter2, lista)
    return diz2

    
        
        

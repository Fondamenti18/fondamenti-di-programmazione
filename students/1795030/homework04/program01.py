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
    file = open(fnome).read()
    dizionario = json.loads(file)
    dic_risultato = {}
    dic_risultato[x] = dizionario[x]
    lista = dizionario[x]
    for chiave in lista:
        x = chiave
        dic_risultato = ricorsiva1(dizionario, x, dic_risultato)
    with open(fout, 'w') as f:
        json.dump(dic_risultato, f)
    return dic_risultato

def ricorsiva1(dizionario, x, dic_risultato):
    lista = dizionario[x]
    dic_risultato[x] = dizionario[x]
    for chiave in lista:
        x = chiave
        dic_risultato = ricorsiva1(dizionario, x, dic_risultato)
    return dic_risultato

def cancella_sottoalbero(fnome,x,fout):
    dizionario = json.loads(open(fnome).read())
    dizionario2 = genera_sottoalbero(fnome, x, fout)
    for keys in dizionario2:
        for key in dizionario:
            lista = dizionario[key]
            if keys in lista:
                lista.remove(keys)
                dizionario[key] = lista
        dizionario.pop(keys)
    with open(fout, 'w') as f:
        json.dump(dizionario, f)
    return dizionario

def dizionario_livelli(fnome,fout):
    dizionario = json.loads(open(fnome).read())
    albero_composto = componi_albero(dizionario, None)
    risultato = {}
    _livelli(albero_composto, 0, risultato)
    with open(fout, 'w') as f:
        json.dump(risultato, f)

def _livelli(dizionario, livello, risultato):
    for key, value in dizionario.items():
        if not livello in risultato:
            risultato[livello] = [key]
        else:
            risultato[livello].append(key)
        _livelli(value, livello+1, risultato)
    if livello == 0:
        for key in risultato:
            risultato[key] = sorted(risultato[key])

def ricorsione(dic_livelli, dizionario, nodo, lista):
    nodo += 1
    lista1 = []
    for x in lista:
        lista1 += dizionario[x]
        lista1.sort()
    if lista1 == []:
        return dic_livelli
    else:
        dic_livelli[nodo] = lista1
        return ricorsione(dic_livelli, dizionario, nodo, lista1)

def dizionario_gradi_antenati(fnome, y, fout):
    d= json.loads(open(fnome).read())
    albero_composto = componi_albero(d, None)
    dizionario_risultato = {}
    Ricorsiva2(albero_composto, y, dizionario_risultato, 0)
    with open(fout, 'w') as f:
        json.dump(dizionario_risultato, f)
    return dizionario_risultato

def Ricorsiva2(albero_composto, y, dizionario_risultato, tot):
    for key, value in albero_composto.items():
        dizionario_risultato[key] = tot
        prev_tot = tot
        if len(value) == y:
            tot += 1
        Ricorsiva2(value, y, dizionario_risultato, tot)
        tot = prev_tot
        
def componi_albero(d, kk):
    risultato = {}
    for key, value in d.items():
        risultato[key] = {}
        for i in value:
            risultato[key][i] = {}
    elim = []
    sposta_figli(risultato, risultato, 0, elim)
    for key in elim:
        if key in risultato:
            del risultato[key]
    return risultato

def sposta_figli(risultato, subr, livello, elim):
    for key in subr:
        if livello>0 and key in risultato:
            if risultato[key] != None:
                subr[key] = risultato[key]
                risultato[key] = None
                elim.append(key)
        if subr[key] != None:
            sposta_figli(risultato, subr[key], livello + 1, elim)
            

if __name__ == '__main__':
    print(genera_sottoalbero('Alb10.json', 'd', 'risAlb10_gs.json'))
    print(cancella_sottoalbero('Alb10.json', 'd', 'risAlb10_gs2.json'))
    print(dizionario_livelli('Alb10.json', 'risAlb10_gs3.json'))
    print(dizionario_gradi_antenati('Alb10.json', 2, 'risAlb10_gs4.json'))

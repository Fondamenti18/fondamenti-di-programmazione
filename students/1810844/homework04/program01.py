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

def gen(diz,dizio,nod):
    dizio[nod] = diz[nod]
    for ramo in diz[nod]:
        gen(diz,dizio,ramo)
    return dizio

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    f = open(fnome)
    diz = json.load(f)
    dizio = {}
    dizio = gen(diz,dizio,x)
    F = open(fout,'w')
    json.dump(dizio,F)
    f.close()
    F.close()



def canc(diz,nod):
    for ramo in diz[nod]:
        canc(diz,ramo)
    diz.pop(nod)
    return diz

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    f = open(fnome)
    diz = json.load(f)
    dizio = {}
    dizio = canc(diz,x)
    for i in dizio.keys():
        for j in range(0,len(dizio[i])):
            if x == dizio[i][j]:
                dizio[i].pop(j)
                break
    F = open(fout,'w')
    json.dump(dizio,F)
    f.close()
    F.close()




def liv(diz,l,nod,fin):
    if l not in fin.keys():
        fin[l] = []
        fin[l].append(nod)
    else:
        fin[l].append(nod)
    l+=1
    for ramo in diz[nod]:
        liv(diz,l,ramo,fin)
    return fin


def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    f = open(fnome)
    diz = json.load(f)
    nod = ""
    for i in diz.keys():
        if i not in diz.values():
            nod = i
            break
    
    dizio = {}
    dizio = liv(diz,0,nod,dizio)
    for i in dizio.keys():
        dizio[i].sort()
    F = open(fout,'w')
    json.dump(dizio,F)
    f.close()
    F.close()




def grad(diz,C,nod,n = 0):
    if len(diz[nod]) == C:
        n += 1
    for ramo in diz[nod]:
        diz = grad(diz,C,ramo,n)
    if len(diz[nod]) == C:
        diz[nod] = n-1
    else:
        diz[nod] = n
    return diz
    

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    f = open(fnome)
    diz = json.load(f)
    nod = ""
    for i in diz.keys():
        if i not in diz.values():
            nod = i
            break
    diz = grad(diz,y,nod)
    F = open(fout,'w')
    json.dump(diz,F)
    f.close()
    F.close()

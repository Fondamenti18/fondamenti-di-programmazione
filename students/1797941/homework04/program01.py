'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista 
(eventualmente vuota) degli identificativi dei  figli del nodo. Gli identificativi dei nodi 





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
                _____________'b'_______     
               |                       |            
              'c'                  ___'d'__
               |                  |        |  
              'i'              __'e'__    'l'
                              |   |   |               
                             'f' 'g' 'h'
                                  


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



import sys
import json

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    res_albero = {}
    diz_alb = leggi_file(fnome)
    if x in diz_alb.keys():
        res_albero[x] = cerca_succ(diz_alb[x],diz_alb,res_albero)
    scrivi_file(res_albero,fout)

def leggi_file(fnome):
    with open(fnome) as f:
        return json.load(f)

def scrivi_file(s,fout):
    with open(fout,mode='w') as f:
        json.dump(s, f)

def cerca_succ(ls,diz_albero,res_albero):
    for nodo in ls:
        res_albero[nodo] = cerca_succ(diz_albero[nodo],diz_albero,res_albero)
    return ls

def del_succ(ls,diz_albero,res_albero):
    for nodo in ls:
        del_succ(diz_albero[nodo],diz_albero,res_albero)
        diz_albero.pop(nodo)
    return ls

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    res_albero = {}
    diz_alb = leggi_file(fnome)
    if x in diz_alb.keys():
        del_succ(diz_alb[x],diz_alb,res_albero)
        diz_alb.pop(x)
    for it in diz_alb:
        if x in diz_alb[it]: diz_alb[it].remove(x)
    scrivi_file(diz_alb,fout)
            
def conta_livelli(ls,diz_albero,res_albero,livello):
    for nodo in ls:
        if diz_albero[nodo] != []:
            if livello+1 not in res_albero.keys():
                res_albero[livello+1] = []
            res_albero[livello+1].extend(conta_livelli(diz_albero[nodo],diz_albero,res_albero,livello+1))
            res_albero[livello+1]=sorted(res_albero[livello+1])
    return ls

def trova_primo(diz_albero):
    values = set()
    keys = set(diz_albero.keys())
    [values.update(set(el)) for el in diz_albero.values()]
    return keys.symmetric_difference(values).pop()
    
    
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    res_albero = {}
    diz_albero = leggi_file(fnome)
    primo = trova_primo(diz_albero)
    res_albero[0] = [primo]
    res_albero[1] = sorted(conta_livelli(diz_albero[primo],diz_albero,res_albero,1))
    scrivi_file(res_albero,fout)
    
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    diz_albero = leggi_file(fnome)
    diz_antenati = {}
    primo = trova_primo(diz_albero)
    diz_padri = {primo:None}
    diz_padri = trova_padre(diz_albero[primo],primo,diz_albero,diz_padri)
    for nodo in diz_albero.keys():
        if nodo == primo: diz_antenati[nodo]=0
        else: diz_antenati[nodo]=contr_antenato(nodo,2,diz_albero,diz_padri,diz_antenati)
    scrivi_file(diz_antenati,fout)
    


def contr_antenato(x,y,diz_albero,diz_padri,diz_antenati):
    if diz_padri[x] == None: return 0
    if x not in diz_antenati.keys():
        if len(diz_albero[diz_padri[x]]) == y:
#            print("   ",diz_padri[x],"==",y)
            diz_antenati[x] = contr_antenato(diz_padri[x],y,diz_albero,diz_padri,diz_antenati)
            return diz_antenati[x]+1
        else:
#            print("   ",diz_padri[x],"!=",y)
            diz_antenati[x] = contr_antenato(diz_padri[x],y,diz_albero,diz_padri,diz_antenati)
            return diz_antenati[x]
    else:
        return diz_antenati[x]
        
def trova_padre(ls,padre,diz_albero,diz_padri):
    for el in ls:
        diz_padri[el] = padre  
        diz_padri = trova_padre(diz_albero[el],el,diz_albero,diz_padri)
    return diz_padri
    

#genera_sottoalbero('Alb10.json','d','tAlb10_1.json')
#cancella_sottoalbero('Alb10.json','d','tAlb10_1.json')
#dizionario_livelli('Alb50000.json','Fail.json')
#dizionario_gradi_antenati('Alb10.json',2,'tAlb10_1.json')
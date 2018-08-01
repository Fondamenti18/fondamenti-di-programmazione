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

def genera_sottoalbero(fnome,x,fout): 
    f=open(fnome, 'r',encoding='utf8')
    d = json.load(f)
    diz={}
    diz_f=trova_v(d,diz,x)
    f_f=open(fout,'w',encoding='utf8')
    f_f.write(json.dumps(diz_f))
    f.close
    f_f.close


def trova_v(d,diz,x):
    if x not in d :
        diz=diz
    else:
        diz[x]=d[x]
       
        for z in diz[x]:
            trova_v(d,diz,z)
    return diz

def cancella_sottoalbero(fnome,x,fout): 
    f=open(fnome, 'r',encoding='utf8')
    
    d = json.load(f)
    diz={}
    diz_f=canc_v(d,diz,x)
    f_f=open(fout,'w',encoding='utf8')
    f_f.write(json.dumps(diz_f))
    f.close
    f_f.close

    
def canc_v(d,diz,x):
    if x not in d :
        diz=diz
    else:
        
        diz[x]=d[x]
       
        for z in diz[x]:
            canc_v(d,diz,z)
    for y in diz:
        if y in d:
            d.pop(y)
    
    for w in d:
        if x in d[w]:
            d[w].remove(x)
    return d


def dizionario_livelli(fnome,fout):
    f=open(fnome, 'r',encoding='utf8')
    d = json.load(f)
    diz={}
    nodo=trovac(d)
    
    diz_f=crea_l(d,diz,nodo,0)
    dioz=ordina(diz_f)
    f_f=open(fout,'w',encoding='utf8')
    f_f.write(json.dumps(diz_f))
    f.close
    f_f.close
    return dioz


def crea_l(d,diz,nodo,x):
    if str(x) not in diz:
        diz[str(x)]=[]
    diz[str(x)].append(nodo)
    for y in d[nodo]:
        crea_l(d,diz,y,x+1)
    return diz

def trovac(d):
    ins_c=set()
    ins_v=set()
    s=''
    for x in d.keys():
        
        ins_c.add(x)
    for y in d.values():
        for z in y:
            ins_v.add(z)
    for y in ins_c.difference(ins_v):
        s+=y
    return s


def ordina(diz):
    for x in diz:
      diz[x]=sorted(diz[x])
    return diz


def dizionario_gradi_antenati(fnome,y,fout):
    f=open(fnome,'r',encoding='utf8')
    d=json.load(f)
    diz={}
    nodo=trovac(d)
    print(nodo)
    c=0
    diz_f=ant(d,diz,nodo,c,y)
    f_f=open(fout,'w',encoding='utf8')
    f_f.write(json.dumps(diz_f))
    f.close
    f_f.close
    

def ant(d,diz,nodo,c,y):
    diz[nodo]=c
    for z in d[nodo]:
        if len(d[nodo])==y:
            ant(d,diz,z,c+1,y)
        else:
            ant(d,diz,z,c,y)
    return diz



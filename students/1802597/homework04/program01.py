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
    diz_ritorno ={}
    
    with open(fnome) as pfile:
        testo =pfile.read()    
    diz = json.loads(testo)
    ritorna(x,diz_ritorno,diz)
    
    
    with open(fout, 'w') as outfile:
        json.dump(diz_ritorno, outfile)
        
        
def ritorna(x,diz_ritorno,diz):
    
    
    sotto = diz[str(x)]
    diz_ritorno[str(x)]=diz[str(x)] 
    
    for i in sotto:
        if i in diz:
        
            x = i
            ritorna(x,diz_ritorno,diz)
            
    
    
def cancella_sottoalbero(fnome,x,fout):
    
    with open(fnome) as pfile:
        testo =pfile.read()    
    diz = json.loads(testo)
    ki = list(diz.keys())
    #print(diz)
    primo = diz[x]
    
    for i in range(len(ki)):
        if x in diz[ki[i]]:
            c = 0
            for el in diz[ki[i]]:
                c += 1
                if el == x:
                    #print(el)
                    del diz[ki[i]][c-1]
    del diz[x]
    ritorna_cancella(primo,diz,x)
    
    with open(fout, 'w') as outfile:
        json.dump(diz, outfile)
    #print(diz)
    
def ritorna_cancella(primo,diz,x):
    for child in primo:
        if child in diz:
            primo = diz[child]
            del diz[child]
            ritorna_cancella(primo,diz,x)
    
    
    

def dizionario_livelli(fnome,fout):
    diz_ritorno ={}
    b = True
    with open(fnome) as pfile:
        testo =pfile.read()    
        if b == True:
            diz = json.loads(testo)
    ki = list(diz.keys())    
    value = list(diz.values())
    #print(ki[0])
    Nodo = set()
    
    nodo(ki,value,Nodo)
    #print(Nodo)
    v = ''
    num = 0
    b = True
    for i in Nodo:
        v = i
    
    ritorna3(v, num ,b ,diz_ritorno,diz)
    
    with open(fout, 'w') as outfile:
        json.dump(diz_ritorno, outfile)
        
    #print(diz_ritorno)
    
def ritorna3(v, num ,b ,diz_ritorno,diz):
    #print(v)
    diz_ritorno[num]=diz_ritorno.get(num, []) + [v]
    grow = diz_ritorno[num]
    grow.sort()
    diz_ritorno[num]=grow
    for i in diz[v]:
        ritorna3(i, num+1 ,b ,diz_ritorno,diz)

    return next(iter(diz))
    
    
    

    

def nodo(ki,value,Nodo):
    if len(ki) != 0:
        for val in value:
            if not ki[0] in val:
                Nodo.add(ki[0])
    
    
    
 

def dizionario_gradi_antenati(fnome,y,fout):
    
    with open(fnome) as pfile:
        testo =pfile.read()    
        diz = json.loads(testo)
    ki = list(diz.keys())
    ki2=ki[:]
    diz_ritorno = {}
    primo = ki2[0]
    cont = 0
    ver = False
    diz_ritorno2={}
    ric(primo,diz,ki2,ver,cont,diz_ritorno,y)
    
    for i in ki2:
        if not i in diz_ritorno:
            diz_ritorno2[i] = 0
        else:
            diz_ritorno2[i] = diz_ritorno[i]
    
    with open(fout, 'w') as outfile:
        json.dump(diz_ritorno2, outfile)
    
    
    #print(diz_ritorno2)
def ric(primo,diz,ki2,ver,cont,diz_ritorno,y):
    #ti fermi quando arrivi al primo nodo
    #print(primo,ki2[len(ki2)-1])
    if primo == ki2[len(ki2)-1]: return diz_ritorno
    #print(primo)
    if len(diz[primo]) == y:
            cont+=1
            ver = True
    for el in diz[primo]:
        if el in diz :
            ver = False
            diz_ritorno[el] = cont
            ric(el,diz,ki2,ver,cont,diz_ritorno,y)
            
        
        


    
    

    
    
    
    
    
    
    
    
    
    
    
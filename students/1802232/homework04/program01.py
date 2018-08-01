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
from json import dumps
file=json.load(open('Alb10.json'))
def chiavi(dizionario):
    chiavi = list()
    for i in dizionario.keys():
        chiavi.append(i)
    return chiavi

def valori(dizionario):
    chiavi = list()
    for i in dizionario.values():
        chiavi.append(i)
    return chiavi

def genera_sottoalbero(fnome,x,fout):
    file=json.load(open(fnome))
    risultato=provaR(file,x)
    #print(risultato)
    with open(fout,'w',encoding='utf-8') as f:
        json.dump(risultato,f)
    
('Alb10.json','d','tAlb10_1.json')
def cancella_sottoalbero(fnome,x,fout):
    file=json.load(open(fnome))
    risultato=provaR(file,x)
    for chiave in risultato:
        if chiave in file:
            del(file[chiave])
    for i in file:
        if x in file[i]:
            file[i].remove(x)
    with open(fout,'w',encoding='utf-8') as f:
        json.dump(file,f)
    

def dizionario_livelli(fnome,fout):
    file=json.load(open(fnome))
    diz = {}
    insieme = set()
    for chiave in file:
        for x in file[chiave]:
            insieme.add(x)
    for chiave in file:
        if chiave not in insieme:
            radice = chiave
    diz[0] = [radice]
    livello = 1
    dizionario = ricorsione(file,livello,diz)
    for chiave in dizionario:
        diz[chiave].sort()
    with open(fout,'w',encoding='utf-8') as f:
        json.dump(dizionario,f) 
       
 

def dizionario_gradi_antenati(fnome,y,fout):
    file=json.load(open(fnome))
    diz = {}
    insieme = set()
    for chiave in file:
        for x in file[chiave]:
            insieme.add(x)
    for chiave in file:
        if chiave not in insieme:
            radice = chiave
    diz[radice] = 0
    diz = prova22(file,diz,y,0,radice)
    with open(fout,'w',encoding='utf-8') as f:
        json.dump(diz,f)
        

def provaR(dizionario,x):
    sottoAlbero = {}
    sottoAlbero[x] = dizionario[x]
    for c in sottoAlbero[x]:
        riprova=provaR(dizionario,c)
        for l in riprova:
            sottoAlbero[l] = riprova[l]
    return sottoAlbero

def prova2(dizionario,z,lista):
    #print(l)
    for chiave in dizionario:
        if z != chiave:
            if z in dizionario[chiave]:
                
                lista.append('a')
                prova2(dizionario,chiave,lista)
    #print(l)
    return len(lista)
    
def listaListe(dizionario,chiave,y,lista):
    contatore=0
    for c in dizionario:   
        if chiave in dizionario[c]:
            lista.append(dizionario[c])
            listaListe(dizionario,c,y,lista)
    for d in lista:
        if len(d) == y:
            contatore+=1
    return contatore


  
def riprova(file,dizOut,c,lista):
    for chiave in file:
        if c in file[chiave]:
            lista.append('a')
            riprova(file,dizOut,chiave,lista)
    dizOut[len(lista)] = [c]
    
    return dizOut


def dizionario_pivelli(fnome,fout):
    dizOut = {}
    file=json.load(open('Alb10.json'))
    for chiave in file:
        dizionario = riprova(file,{},chiave,[])
        print(dizionario)
        dizOut = accorpa_dizionari(dizOut,dizionario)
        print(dizOut)
            
    with open(fout,'w',encoding='utf-8') as f:
        json.dump(dizOut,f) 
    return dizOut
        
def accorpa_dizionari(diz1,diz2):
    if len(diz2) > 0:
        for c in diz1:
            for x in diz2:
                if c == x:
                    for val in diz1[c]:
                        diz1[c].append(val)
                    for val in diz2[c]:
                        diz1[c].append(val)
                else:
                    #print(dizOut[c])
                    diz1[c].append(diz1[c])
                    diz1[x].append(diz2[x])
        return diz1
        
    else:
        return(diz1)
    

def dizionario(file):
    diz={}
    for chiave in file:
        lista = []
        l = 0
        c = prova2(file,chiave,l,lista)
        diz[c] = []
    #print(diz)
    return diz

def ricorsione(file,livello,diz):
    diz[livello] = []
    for x in diz[livello-1]:
        diz[livello] += file[x]
    livello += 1
    #print(diz)
    l = []
    for chiave in diz[livello-1]:
        for elemento in file[chiave]:
            l.append(elemento)
    if len(l) == 0:
        return diz
    else:
        diz = ricorsione(file,livello,diz)
        return diz
    
def prova22(file,dizionario,grado,antenati,radice):
    if len(file[radice]) == grado:
        for chiave in file[radice]:
                dizionario[chiave] = antenati+1
        antenati += 1
        for chiave in file[radice]:
            dizionario = prova22(file,dizionario,grado,antenati,chiave)
    else:
        for chiave in file[radice]:
            dizionario[chiave] = antenati
            dizionario = prova22(file,dizionario,grado,antenati,chiave)
    return dizionario   
        
        
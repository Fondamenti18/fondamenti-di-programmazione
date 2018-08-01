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

d={'a': ['b'], 'b': ['c', 'd'], 'c': ['i'], 'd': ['e', 'l'], 'e': ['f', 'g', 'h'], 'f': [], 'g': [], 'h': [], 'i': [], 'l': []}

                             'a'
                              |
                _____________'b'____________             
               |                            |            
              'c'                  ________'d'_______   
               |                  |                  |  
              'i'         _______'e'_______         'l'
                         |        |        |               
                        'f'      'g'      'h'
                        
OUTPUT{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}
PERCORSI={'b': 'a', 'c': 'b', 'd': 'b', 'i': 'c', 'e': 'd', 'l': 'd', 'f': 'e', 'g': 'e', 'h': 'e'}
'''
import json
import copy

def trovanodi(c,lista,lista_output):
    if lista==[]:
        return lista_output
    else:
        lista_temp=[]
        for i in lista:
            lista_temp+=c.get(i)
        lista_output+=lista_temp
        trovanodi(c,lista_temp,lista_output)
        return lista_output

def eliminasottoalbero(lista,dizionario_output):
    if lista==[]:
        return dizionario_output
    else:
        del dizionario_output[lista[0]]
        eliminasottoalbero(lista[1:],dizionario_output)
        return dizionario_output

def sottoalbero(lista,c,dizionario_output):
    if lista==[]:
        return dizionario_output
    else:
        dizionario_output[lista[0]]=c.get(lista[0])
        sottoalbero(lista[1:],c,dizionario_output)
        return dizionario_output
    

def genera_sottoalbero(fnome,x,fout):
    with open(fnome) as f:
        c=f.read()
        c=eval(c)
    lista=trovanodi(c,[x],[])
    lista.append(x)
    dizionario_output=sottoalbero(lista,c,{})
    with open(fout,"w") as j:
        json.dump(dizionario_output,j)

def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as f:
        c=f.read()
        c=eval(c)
    dizionario_output=copy.deepcopy(c)
    lista=trovanodi(c,[x],[])
    lista.append(x)
    dizionario_output=eliminasottoalbero(lista,dizionario_output)
    dizionario_output=elimina_nodo(dizionario_output,x)
    with open(fout,"w") as j:
        json.dump(dizionario_output,j)
    
def elimina_nodo(dizionario_output,cerca):
    for i in dizionario_output:
        if cerca in dizionario_output[i]:
            dizionario_output[i].remove(cerca)
            return dizionario_output
    elimina_nodo(dizionario_output,cerca)
    return dizionario_output


    
def dizionario_livelli(fnome,fout):
    with open(fnome) as f:
        c=f.read()
        c=eval(c)
    x=cerca(c)
    lista=c.get(x)
    dizionario_output={}
    dizionario_output[0]=[x]
    dizionario_output[1]=sorted(lista)
    grado=2
    dizionario_output=livello(lista,dizionario_output,grado,c)
    with open(fout,"w") as j:
        json.dump(dizionario_output,j)
    
    
def livello(lista,dizionario_output,grado,d):
    if lista==[]:
        return dizionario_output
    else:
        lista_temp=[]
        for i in lista:
            lista_temp+=d.get(i)
        if lista_temp==[]:
            return dizionario_output
        dizionario_output[grado]=sorted(lista_temp)
        grado+=1
        lista=lista_temp
        livello(lista,dizionario_output,grado,d)
    return dizionario_output


def dizionario_gradi_antenati(fnome,y,fout):
    from json import load
    d = {}
    count = 0
    with open(fnome) as f :
        a = load(f)
        i=cerca(a)
        d[i]=0
    r = percorso(a,y,count,d,i)
    data = json.dumps(r)
    with open(fout , "w") as f :
        f.write(data)
def percorso(a,y,count,d,i):
    if len(a[i]) == 2 :
        count +=  1
    v = a[i]
    variabile = 0
    while variabile < len(v) :
        x = v[variabile]
        d[x] = count
        percorso(a,y,count,d,x)
        variabile = variabile + 1
    return d

def cerca(a):
    node = list(a.keys())[0]
    found = False
    while not found:
        found = True
        for key, value in a.items():
            if node in value:
                node = key
                found = False
    return node

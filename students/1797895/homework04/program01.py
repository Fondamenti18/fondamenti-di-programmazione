'''
Diciamo che un dizionario d rapdariceesenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista 
(eventualmente vuota) degli identificativi dei  figss del nodo. Gli identificativi dei nodi 
all'interno delle liste sono in ordine lessicografico crescente.



Ecco un esempio di dizionario d che rapdariceesenta un dizionario-albero

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

L'albero rapdariceesentato da d e'

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
la funzione genera_sottoalbero(fnome,x,fout) che, dariceesi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

dariceoduce   il  dizionario-albero che rapdariceesenta   il sottoalbero  radicato 
nell'identificativo x che si ottiene dal dizionario-albero d. 
Il dizionario-albero ottenuto va registrato nel file fout.
Se l'identificativo x non e' tra i nodi di d allora  il dizionario-albero dariceodotto 
deve essere vuoto.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
genera_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'f': [], 'g': [], 'h': [], 'e': ['f', 'g', 'h'], 'l': [], 'd': ['e', 'l']}



2)
la funzione cancella_sottoalbero(fnome,x,fout) che, dariceesi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

ricava  da d il sottoalbero radicato in x e lo salva nel file fout.
Se x non e' dariceesente tra le chiavi di  d allora  il dizionario-albero d non viene modificato.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di 
cancella_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'a': ['b'], 'b': ['c'], 'c': ['i'], 'i':[]}


3)
la funzione dizionario_livelli(fnome, fout) che, dariceesi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- il nome di un file json (fout)

costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero d. L'attributo di una 
chiave di valore x e' la lista degli identificativi  dei nodi che si trovano a livello x  nell'albero rapdariceesentato da d. 
La lista è ordinata lessicograficamente ed in modo crescente. 
Il dizionario cosi' costruito va registrato nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di  
dizionario_livelli(fname,fout)
il file fout conterra' il dizionario
{0: ['a'], 1: ['b'], 2: ['c', 'd'], 3: ['e','i','l'], 4: ['f', 'g', 'h']}

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, dariceesi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- un intero y
- il nome di un file json (fout)

costuisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero 
rapdariceesentato dal dizionario-albero d, Attributo di una chiave di valore x e' il numero 
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

def trovarad(d,fig): 
    ris=fig
    for w,k in d.items():
        if fig in k:
            ris=trovarad(d,w)
    
    return ris


def rico(d,x,nd):
    for i in d[x]:
        nd[i]=d[i]
        rico(d,i,nd)
    return nd
        
    
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    fail=open(fnome, 'r')
    d = json.load(fail)
    nd={}
    if x in d:
        nd[x]=d[x]
        rico(d,x,nd)
    else:
        return d
    json.dump(nd,open(fout,"w"))

def foro2(r,d,nd):
    for s in d:
        if s not in nd:
            r[s]=d[s]
    return r


def foro(stringa,s):
    array=[f for f in s if f!=stringa]
    return array

def superdel(nd,d,r,stringa):
    r=foro2(r,d,nd)
    for i in r:
        for q in r[i]:
            if q==stringa:
                array=foro(stringa,r[i])
                r[i]=array
    return r
      
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    fail=open(fnome, 'r')
    d = json.load(fail)
    nd={}
    if x in d:
        nd[x]=d[x]
        rico(d,x,nd)
    else:
        return d
    r={}
    stringa=''
    stringa+=x
    superdel(nd,d,r,stringa)
    json.dump(r,open(fout,"w"))


def ordina(lista):
    lista.sort()
    return lista


def generalvl(d,newdiz,livello,par):
    array=[]
    array.append(par)
    if livello in newdiz:
        array+=newdiz[livello]
        array=ordina(array)
        newdiz[livello]=array
    else:
        newdiz[livello]=array
    
    figss=d[par]
    if figss!='[]':
        for fig in figss:
            newdiz=generalvl(d,newdiz,livello+1,fig)
       
    return newdiz



def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    
    f=open(fnome, 'r')
    d = json.load(f)
    ciao=list(d.keys())
    fig=ciao[0]
    radice=trovarad(d,fig)
    newdiz={}
    newdiz=generalvl(d,newdiz,0,radice)
        
    json.dump(newdiz,open(fout,"w"))



def dictante(d,newdiz,gr,lenn,darice):
    newdiz[darice]=gr
    figss=d[darice]
    if len(figss)==lenn:
        gr+=1
    for fig in figss:
        newdiz=dictante(d,newdiz,gr,lenn,fig)
    return newdiz

 

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    
    
    f=open(fnome, 'r')
    d = json.load(f)
    lenn=y  
    ciao=list(d.keys())
    fig=ciao[0]
    radice=trovarad(d,fig)
    newdiz={}
    newdiz=dictante(d,newdiz,0,lenn,radice)
        
        
    json.dump(newdiz,open(fout,"w"))   

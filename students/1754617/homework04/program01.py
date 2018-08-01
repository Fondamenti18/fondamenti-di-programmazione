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
    '''inserire qui il vostro codice'''
    with open(fnome) as t:
        albero= json.loads(t.read())
        treee=visita_in_ordine(albero,x,{})
    with open(fout,'w') as v:
        json.dump(treee,v)
        
def visita_in_ordine(albero,x,tree):
    if (len(albero[x])!=0):
        for nodo in albero[x] :
           visita_in_ordine(albero,nodo,tree)
        tree[x]=albero[x]
    else:
        tree[x]=[]
    return tree

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as t:
        albero=json.loads(t.read())
        albero2=visita_in_ordine(albero,x,{})
        lista_chiavi=list(albero)
        lista2=list(albero2)
        for chiave in lista_chiavi:
            if(chiave in lista2):
               del(albero[chiave])
            else:
                lista_elementi=albero[chiave]
                for el in lista_elementi:
                    if(el in lista2):
                        albero[chiave].remove(el)
        t.close()
        with open(fout,'w') as u:
            json.dump(albero,u)

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    t=open(fnome)
    albero=json.loads(t.read())
    radice=ritorna_radice2(albero)
    dizionario=livello_albero(albero,radice,0)
    profondita={ livello: [] for livello in dizionario.values()}
    for nodo,livello in dizionario.items():
        profondita[livello].append(nodo)
    for nodi in profondita.values():
        nodi.sort()
    
    with open(fout,'w') as t:
        json.dump(profondita,t)

def livello_albero(albero,x,livello):
    if( not albero[x] ):
        return {x: livello}
    diz = {}
    for nodo in albero[x]:
        diz.update(livello_albero(albero,nodo,livello+1))
    diz[x] = livello
    return diz

def ritorna_radice(albero):
    for x in albero:
        return x

def ritorna_radice2(albero):
    radice=ritorna_radice(albero)
    lista=[]
    for x in albero:
        lista.extend(albero[x])
    lista_chiavi=list(albero.keys())
    lungh=len(lista_chiavi)
    for x in range(lungh-1,0,-1):
        if (radice in lista):
            radice=lista_chiavi[x]
        else:
            return radice
    return radice
        
    
    
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as t:
        albero=json.load(t)
        radice=ritorna_radice2(albero)
        diz=antenati(albero,radice,y,-1,0)
    with open(fout,'w') as r:
        json.dump(diz,r)


def antenati(albero,x,y,grado_padre,antenati_padre):
    if( not albero[x] ):
        return { x: antenati_padre if grado_padre!=y else antenati_padre+1}
    numeri_antenati = antenati_padre if grado_padre!=y else antenati_padre+1
    diz={}
    for nodo in albero[x]:
        diz.update(antenati(albero,nodo,y,len(albero[x]),numeri_antenati))
    diz[x]=numeri_antenati
    return diz
        
    

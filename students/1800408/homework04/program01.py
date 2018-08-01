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
                                  |
                                 'i'


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
    json_data=open(fnome).read()
    
    diz=json.loads(json_data)
    
    diz2=estrapola(diz,x)
    with open(fout,'w') as outfile:
        json.dump(diz2,outfile)    
def estrapola(diz,v):
    valore=diz[v]
    if valore==None:
        diz2={v:[]}  #prova
    else:
        diz2={v:valore}                                
        for el in valore:
            diz3=estrapola(diz,el)
            diz2.update(diz3)
    return diz2     
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    json_data=open(fnome).read()
    diz=json.loads(json_data)
    radice=trovaradice(diz)
    diz2=elimina_albero(diz,x,radice)
    with open(fout,'w') as outfile:
        json.dump(diz2,outfile)
    
    
def trovaradice(diz):
    for chiave in diz.keys():
        radice=chiave
        break
    return radice
def elimina_albero(diz,x,nodo):
    valore=diz[nodo]
    if valore!=[]:
        diz2={nodo:valore}
        if x in valore:
            valore.remove(x)
        for el in valore:
            diz3=elimina_albero(diz,x,el)
            diz2.update(diz3)   
    elif valore==[]:
        diz2={nodo:[]}
    return diz2

       

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    lista2=[]
    
    with open(fnome,'r') as file:
        diz=json.load(file)
        #print(diz)
    radice=trovaradice(diz) #ok
    i=0
    lista=livello(diz,radice,lista2,i)
    massimo=trovamassimo(lista)
    diz2=analisi(lista,massimo)
    with open(fout,'w') as outfile:
        json.dump(diz2,outfile)
        
        
        
def livello(diz,nodo,lista2,i):
    valore=diz[nodo]
    if valore==None:
        lista2.append(i,nodo)
    else:
        
        lista2.append((i,nodo))
        i=i+1
        for figlio in valore:
            lista2=livello(diz,figlio,lista2,i)
    return lista2
def trovamassimo(lista):
    listamassimo=[]
    for a,b in lista:
        listamassimo.append(a)
    massimo=max(listamassimo)
    return massimo
        
        
def analisi(lista,massimo):
    lista1=[]
    x=0
    diz={}
    while x<=massimo:
        for el1,el2 in lista:
            if el1==x:
                lista1.append(el2)
                lista1.sort()
        diz[x]=lista1
        lista1=[]
        x+=1
    return diz        
def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    lista2=[]
    i=0
    k=0
    with open(fnome,'r') as file:
        diz=json.load(file)
    radice=trovaradice(diz)
    lista=antenati(diz,radice,lista2,i,y,k)
    diz=analisi2(lista)
    with open(fout,'w') as outfile:
        json.dump(diz,outfile)
def analisi2(lista):
    def sec_elem(lista):
        return lista[1] 
    diz={}
    lista=sorted(lista, key=sec_elem) 
    for chiave,valore in lista:
        diz[chiave]=valore
    return diz
def antenati(diz,nodo,lista2,i,y,k):
    valore=diz[nodo]
    if valore==None:
        return lista2 #prova
    else:
        lista2.append((nodo,k)) #prova
        i=i+1
        if len(valore)==y:
            k=k+1
        for figlio in valore:
            lista2=antenati(diz,figlio,lista2,i,y,k)
    return lista2    
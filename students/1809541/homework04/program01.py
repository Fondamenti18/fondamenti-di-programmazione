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

def sottalbero(diz,x,end):
    if x not in diz:
        return end
    end[x]=diz[x]
    for i in diz[x]:
        sottalbero(diz,i,end)
    return end

    
def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    file=open(fnome,'r')
    albero=json.load(file)
    end={}
    fin=sottalbero(albero,x,end)
    js=open(fout,'w')
    json.dump(fin,js)
    file.close()
    js.close()
    
    

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    file=open(fnome,'r')
    albero=json.load(file)
    end={}
    fin=sottalbero(albero,x,end)
    for i in fin:
        del albero[i]
    for i in albero:
        if x in albero[i]:
            albero[i].remove(x)
    js=open(fout,'w')
    json.dump(albero,js)
    file.close()
    js.close()



def trovaradice(diz):
    ins=set()
    for i in diz:
        for m in diz[i]:
            ins.add(m)
    for a in diz:
        if a not in ins:
            return a

def trovalivelli(tree,end,count):
    arg=[]
    for i in end[count-1]:
        arg+=tree[i]
    end[count]=sorted(arg)
    if arg != []:
        trovalivelli(tree,end,count+1)
    if arg==[]:
        del end[count]
    return end
    

        
    
    
def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    file=open(fnome,'r')
    albero=json.load(file)
    end={}
    radice=trovaradice(albero)
    end[0]=[radice]
    count=1
    livelli=trovalivelli(albero,end,count)
    js=open(fout,'w')
    json.dump(livelli,js)
    file.close()
    js.close()

def trovagradi(diz,rad,n,end):
    nextrad=[]
    for i in rad:
        nextrad+=diz[i]
        if len(diz[i])==n:
            for m in diz[i]:
                end[m]=end[i]+1
        else:
            for m in diz[i]:
                end[m]=end[i]
    if nextrad!=[]:
        trovagradi(diz,nextrad,n,end)
    return end

    

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    file=open(fnome,'r')
    albero=json.load(file)
    radice=[trovaradice(albero)]
    end=trovagradi(albero,radice,y,{i:0 for i in albero})
    js=open(fout,'w')
    json.dump(end,js)
    file.close()
    js.close()

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

json.dump(fout)

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
genera_sottoalbero('Alb10.json','d','C:/Users/john/Desktop/homework04/es1/tAlb10_1.json')

cancella_sottoalbero('Alb10.json','d','C:/Users/john/Desktop/homework04/es1/a.json')

    if x  in file.keys()==False:           #forse dizionario pieno rimane in memoria. forse
        print("arhel")
        with open(fout,'w') as out:
            json.dump(dizio,out)
    else:

    
   global dizio           #<-------- non mi toglie le values così
    del dizio[x]
    for i in file[x]:
        if i in file.keys():
            cancella(i)     


            del dizio[1][0]
            [x for v in dizio.values() for x in v]       <------- per vedere se è un values()
            dizionario_livelli('Alb10.json','d','C:/Users/john/Desktop/homework04/es1/a.json')
'''



                       #ho usato del così non ho un output ogni volta
import json
dizio={}
dizio1={}
file=0
out=0
temp=0
tempo=0
radice=0
def genera_sottoalbero(fnome,x,fout): #l'ho diviso in due funzioni, così non faccio impicci per cancellare il dizionario
    global dizio
    global file
    global out
    dizio={}
    out=open(fout,'w')
    with open (fnome) as data:
        file=json.load(data)
    
    sottoalbero(x)
    with open(fout,'w') as out:      #<----- molto più veloce qui
        json.dump(dizio,out)
def sottoalbero(x):
    global dizio
    if x not in file.keys():        #se il valore passato non è nel dizionario
        dizio={}
        json.dump(dizio,out)
    dizio[x]=file[x]
    for i in file[x]:
        if i in file.keys():
            sottoalbero(i)
def cancella_sottoalbero(fnome,x,fout):
    global dizio
    global file
    global out
    dizio={}
    with open (fnome) as data:
        file=json.load(data)
    dizio=file.copy()
    #print(dizio)
    for i in file.keys():
        if x in file[i]:        #<----- così mi cancello dove la d è presente come valore
            o=file[i].index(x)
            del dizio[i][o]

    
    
    cancella(x)
    with open(fout,'w') as out:      #<----- molto più veloce qui
        json.dump(dizio,out)    

            
def cancella(x):
    global dizio           #<-------- non mi toglie le values così
    del dizio[x]
    o=0
    for i in file[x]:
        if i in file.keys(): #cancella tutte le chiavi
            cancella(i)     

    
    


 
    
    

def dizionario_livelli(fnome,fout):
    global dizio
    global file
    global out
    dizio={}
   # dizio1={}
    a=0
    c=0
    cont=0
    lista=[]
    out=open(fout,'w')
    with open (fnome) as data:
        file=json.load(data)
    dizio1=file.copy()
    chiavi=set(file.keys())
    for x in file.values():
        for v in x:
            lista.append(v)

    lista=set(lista)
    c=chiavi-lista
    c=list(c)
    dizio[0]=[c[0]]
    livelli(c[0],0)
    for i in dizio:                   #ordinerò in modo che siano "lessicografiche" wtf
        dizio[i].sort()





        
    with open(fout,'w') as out:      #<----- molto più veloce qui          x in [x for v in dizio.values() for x in v]
        json.dump(dizio,out)
def livelli(i,tempo):
    global dizio      #impossibile slaire l'albero. non posso trovare una chiave partendo da values(), e poi già per vedere se sta in values è un casino, sono liste
    tempo=tempo+1

    for v in file[i]:
        dizio.setdefault(tempo,[]).append(v)       #questa stringa fa magie e risolve i programmi. setdefault setta la chiave TEMPO con [], append gli dà il valore
        #print(type(v))
    for v in file[i]:
        livelli(v,tempo)
        #print(v,i)

        
        
        
     
 

def dizionario_gradi_antenati(fnome,y,fout):
    global dizio
    global file
    global out
    dizio={}
    out=open(fout,'w')
    lista=[]
    with open (fnome) as data:
        file=json.load(data)    
    chiavi=set(file.keys())
    for x in file.values():
        for v in x:
            lista.append(v)
    lista=set(lista)
    c=chiavi-lista
    c=list(c)
    dizio[c[0]]=0
    gradi(c[0],y,0)




    with open(fout,'w') as out:      #<----- molto più veloce qui
        json.dump(dizio,out)

def gradi(i,y,tempo):
    global dizio     #tempo dovrebbe eessere quante diramazioni ha
    #tempo=0
    if len(file[i])==y:
        tempo=tempo+1
    for v in file[i]:
        dizio[v]=tempo
        gradi(v,y,tempo)
        
    
    
    
    
    
    
    

















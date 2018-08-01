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

def albero(dizionario, num, new):
    elemento=dizionario[num]
    new[num]=elemento
    for ok in elemento:
        albero(dizionario,ok,new)
    return new  



def cancella_contenuto(dizionario,num):
    for l in dizionario:
        for h in range(len(dizionario[l])):
            if num==dizionario[l][h]:
                del dizionario[l][h] 
                break
    return dizionario            
  

         
def trovaradice(dizionario):
    valori=[]
    for ok in dizionario:
        for num in dizionario[ok]:
            valori+=[num]
    valori=set(valori)        
    for g in dizionario:
        if not g in valori:
            return g
    

    

def livello(dizionario, new, radice, cont):
    elemento=dizionario[radice]
    if str(cont) not in list(new.keys()):
        new[str(cont)]=[]    
    new[str(cont)]+=[radice] 
    for ok in elemento:
        livello (dizionario,new,ok,cont+1)
    return    
        
        
    



def genera_sottoalbero(fnome,num,fout):
    '''inserire qui il vostro codice'''
    with open(fnome,'r') as aviaria:
        dizionario=json.load(aviaria)
        new={}
        new=albero(dizionario,num,new)
        with open(fout, 'w') as ft:
            json.dump(new, ft)
    

def cancella_sottoalbero(fnome,num,fout):
   with open(fnome,'r') as aviaria:
       dizionario=json.load(aviaria)
       new={} 
       new=albero(dizionario,num,new)
       for ok in new:
           del dizionario[ok]
       dizionario=cancella_contenuto(dizionario,num)   
       with open(fout, 'w') as ft:
           json.dump(dizionario, ft)
 

         
def sort(new):
    for ok in new:
        new[ok].sort()
    return new




def dizionario_livelli(fnome,fout):
    with open(fnome, 'r') as dizionario:
        dizionario=json.load(dizionario)
        new=dict()
        contatore=0
        radice=trovaradice(dizionario)
        livello(dizionario,new,radice,contatore)
        new= sort(new)
        with open(fout, 'w') as ft:
            json.dump(new,ft)
    
    
def antenati (dizionario,ok,radice,new,cont=0):
   new[radice]= cont
   if len(dizionario[radice])==ok:
       cont+=1
   for g in dizionario[radice]:
       antenati(dizionario,ok,g,new,cont) 
   return                
    
    
    

def dizionario_gradi_antenati(fnome,ok,fout):
    with open(fnome, 'r') as dizionario:
        dizionario=json.load(dizionario)
        radice=trovaradice(dizionario) 
        new=dict()
        antenati(dizionario,ok,radice,new)
        with open(fout, 'w') as ft:
            json.dump(new,ft)



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
def put_in_file(d,fout):
  with open(fout,'w') as fp:
    json.dump(d, fp)  

def genera_albero(fnome):
  f=open(fnome)
  s=f.read()
  d=json.loads(s)
  return d
def genera_sottoalbero(fnome,x,fout):
  '''inserire qui il vostro codice'''
  d_out={}
  d_alb=genera_albero(fnome)
  d_out=trova(d_alb[x],d_alb,d_out)
  d_out[x]=d_alb[x] 
  put_in_file(d_out,fout)
def trova(lista,d_alb,d):   
  for i in lista:
    d[i]=d_alb[i]
    trova(d_alb[i],d_alb,d)
  return d  

def cancella_sottoalbero(fnome,x,fout):
 d_alb=genera_albero(fnome)
 d_salb={}
 d_salb=trova(d_alb[x],d_alb,d_salb)
 d_salb[x]=d_alb[x]
 d_out={}
 for i in d_alb:
   if i not in d_salb.keys():  
     if x in d_alb[i]:
       appo=[]
       for j in d_alb[i]:
         if j!=x:
          appo.append(j)  
     
       d_out[i]=appo
     else:d_out[i]=d_alb[i] 
 put_in_file(d_out,fout)
   
def radice(fnome):
  l_alb=[]
  d_alb=genera_albero(fnome)
  l_alb=d_alb.keys()
  i_alb=set()
  for i in l_alb:
    if d_alb[i]!=[]: 
      for j in d_alb[i]:
        i_alb.add(j)  
  
  for i in l_alb:
    if i not in i_alb:rad=i  
  
  
  
  return rad

def livelli(lista,d_alb,d,l):
  l+=1 
  if lista!=[]:
   if l in d.keys():
     l_appo=d[l]
     l_appo=l_appo+lista
     d[l]=sorted(l_appo)
   else:d[l]=lista     
   
   for i in lista:
     livelli(d_alb[i],d_alb,d,l)
 
  return d  

def dizionario_livelli(fnome, fout): 
  rad=radice(fnome)
  d_alb=genera_albero(fnome) 
  l=0
  d_out={}
  d_out=livelli(d_alb[rad],d_alb,d_out,l)
  d_out[0]=[rad]
  put_in_file(d_out,fout)
  
def dizionario_gradi_antenati(fnome,y,fout):
  '''inserire qui il vostro codice'''
  rad=radice(fnome)
  d_alb=genera_albero(fnome)    
  d_out={}
  d_out[rad]=0
  d_out=antenati(rad,d_alb,d_out,y)   
  put_in_file(d_out,fout)

def antenati(nodo,d_alb,d,y):
  for i in d_alb[nodo]:
      if len(d_alb[nodo])!=y:d[i]=d[nodo]
      else:d[i]=d[nodo]+1
      antenati(i,d_alb,d,y)
        
  return d



   

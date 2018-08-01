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

def upload(fout, diz_out):

    with open(fout, 'w') as f: 
        f=json.dump(diz_out, f)    

def download(fnome):
    
        diz_in=json.loads(open(fnome).read())
        
        return diz_in

def genera_sottoalbero(fnome,x,fout):

    diz_albero={}
    diz_ramo={}
    lst_key=[x]
    
    diz_albero=download(fnome)
    
    ricorsiva_uno(diz_albero, diz_ramo, lst_key)
    upload(fout, diz_ramo)

    return     

def ricorsiva_uno(diz_albero, diz_ramo, lst_key):
    
    lst=[]
    
    if lst_key!=[]:
    
        for i in lst_key:
            lst+=diz_albero[i]
            diz_ramo[i]=diz_albero[i]

        return ricorsiva_uno(diz_albero, diz_ramo, lst)

    else: return

def cancella_sottoalbero(fnome,x,fout):

    diz_albero={}
    diz_ramo={}
    diz_albero_potato={}
    lst_key=[x]

    diz_albero=download(fnome)

    ricorsiva_uno(diz_albero, diz_ramo, lst_key) 
    inseme_albero_potato=set(diz_albero.keys())-set(diz_ramo.keys())

    for key in inseme_albero_potato:
        diz_albero_potato[key]=diz_albero[key]
        if x in diz_albero_potato[key]:  diz_albero_potato[key].remove(x)
        
    for key in diz_albero_potato.keys():
        if x in diz_albero_potato[key]:  diz_albero_potato[key].remove(x)

    upload(fout, diz_albero_potato)

    return

def dizionario_livelli(fnome,fout):

    diz_albero=download(fnome)

    for key in diz_albero.keys():
        if diz_albero[key]==[]: 
            leaf=key
            break 

    rad_albero=found_sqrt(diz_albero, leaf)
    lst_rad=[rad_albero]
    diz_level={'0':[rad_albero]}
    l=1

    level(lst_rad, diz_albero, diz_level, l)

    for k in diz_level.copy().keys():
        if diz_level[k]==[]: del(diz_level[k])

    upload(fout, diz_level)

    return

def found_sqrt(diz_albero, leaf):

    for key in diz_albero.keys():
        if leaf in diz_albero[key]: return found_sqrt(diz_albero, key) 
    return leaf

def level(lst_key, diz_albero, diz_level, l):

    lst=[]

    for i in lst_key:
        lst+=diz_albero[i]

    diz_level[l]=sorted(lst)
    if diz_level[l]==[]: return

    return level(lst, diz_albero, diz_level, l+1)


def dizionario_gradi_antenati(fnome, y, fout):

    diz_albero=download(fnome)
    
    for key in diz_albero.keys():
        if diz_albero[key]==[]: 
            leaf=key
            break 

    rad_albero=found_sqrt(diz_albero, leaf)
    lst_rad=[rad_albero]
    diz_ancient={rad_albero:0}
    count_grade=0
    
    ancient(diz_albero, diz_ancient, lst_rad, y, count_grade)
    upload(fout, diz_ancient)
    
    return
    
def ancient(diz_albero, diz_ancient, lst_key, grade, count):

    lst=[]
    
    if lst_key==[]: return
    
    for key in lst_key:
        
        if len(diz_albero[key])==grade:
            
            diz_ancient[key]=count
            ancient(diz_albero, diz_ancient, diz_albero[key], grade, count+1)
            
        else:
            diz_ancient[key]=count
            lst=diz_albero[key]
            ancient(diz_albero, diz_ancient, lst, grade, count)
    
if __name__=='__main__':
    genera_sottoalbero('Alb10.json','d','genera_sottoalbero.json')
    cancella_sottoalbero('Alb20000.json','felici','cancella_sottoalbero.json')
    dizionario_livelli('Alb20000.json','dizionario_livelli.json')
    dizionario_gradi_antenati('Alb100.json',2,'dizionario_gradi_antenati2.json')
    dizionario_gradi_antenati('Alb10.json',2,'dizionario_gradi_antenati.json')


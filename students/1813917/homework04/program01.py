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
    with open(fnome) as file:
        file = json.load(file)
        for nodo in file:
            if nodo == x:
                albero_out = {}
                cerca_figlio(nodo, file, albero_out)
                break
                
    with open(fout,'w') as file_out:
        json.dump(albero_out, file_out)

def cancella_sottoalbero(fnome,x,fout):
    with open(fnome) as file:
        file = json.load(file)
        for nodo in file:
            if nodo == x:
                albero_copy = file.copy()
                albero = {}
                cerca_figlio(nodo, file, albero)
                
                for nodo_x in file:
                    if x in file[nodo_x]:
                        albero_copy[nodo_x].remove(x)
                    elif nodo_x in albero:
                        del albero_copy[nodo_x]
                break
    with open(fout, 'w') as file_out:
        json.dump(albero_copy, file_out)
    

def dizionario_livelli(fnome,fout):
    with open(fnome) as file:
        file = json.load(file)
        albero = {}
        l_albero = list(file)
        padre_init = l_albero[0]
        n_padre = 0
        albero_out = conta_nodi(padre_init, file, albero, n_padre)
        for nodo in albero_out:
            albero_out[nodo].sort()
                
        
    with open(fout, 'w') as file_out:
        json.dump(albero_out, file_out)
        
    return albero_out
        
def dizionario_gradi_antenati(fnome,y,fout):
    with open(fnome) as file:
        file = json.load(file)
        alb_n_ant = {}
        l_albero = list(file)
        
        l_albero.sort()
        grado = conta_grado(file, y)
        
        for nodo in l_albero:
            padre = cerca_padre(nodo, file)             
            if padre in grado:
                alb_n_ant[nodo] = alb_n_ant[padre] + 1
            elif nodo == l_albero[0]:
                alb_n_ant[nodo] = 0
            else:
                alb_n_ant[nodo] = alb_n_ant[padre]
            
    #print(grado)
                   
            
                    
    with open(fout, 'w') as file_out:
        json.dump(alb_n_ant, file_out)
                






def cerca_figlio(padre, file, albero):
    for figlio in file[padre]:
        if len(file[figlio]) == 0:
            albero[figlio] = []
        else:
            cerca_figlio(figlio, file, albero)
    albero[padre] = file[padre]
    
def conta_nodi(padre, file, albero, n_padre):
    try:
        for figlio in file[padre]:
            if len(file[figlio]) == 0:
                albero[n_padre + 1].append(figlio)
                if padre not in albero[n_padre]:
                    albero[n_padre].append(padre)
                
            elif padre not in albero[n_padre]:
                albero[n_padre].append(padre)
                conta_nodi(figlio, file, albero, n_padre + 1)
            else:
                conta_nodi(figlio, file, albero, n_padre + 1)
        n_padre += 1
        
    except KeyError:
        if n_padre in albero:
            albero[n_padre + 1] = []
            conta_nodi(padre, file, albero, n_padre)
        else:
            albero[n_padre] = []
            conta_nodi(padre, file, albero, n_padre)

    return albero
        
def conta_grado(file, y):
    diz_grado = {}
    for nodo in file:
        lung = len(file[nodo])
        if lung == y:
            diz_grado[nodo] = lung
    return diz_grado

def cerca_padre(figlio, file):
    for padre in file:
        if figlio in file[padre]:
            return padre
            
#dizionario_gradi_antenati('Alb100.json',2,'tAlb100_4.json')

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

albero = {}

livelli = {}

alberoantenati = {}

nodoradice = ''

import json

def caricaalbero(fnome):
    
    global albero
    
    global nodoradice
    
    inputfile = open(fnome, 'r')
        
    albero = json.load(inputfile)
            
    inputfile.close
    
    tmpinsieme = set()
        
    for persona in albero:
        
        for figlio in albero[persona]:
        
            tmpinsieme.add(figlio)
  
    for persona in albero:
        
        if persona not in tmpinsieme:
            
            nodoradice = persona
            
            break
            
def creaalberoordinato(albero, nodo, dizionario):
        
    for figli in albero[nodo]:
        
        dizionario = creaalberoordinato(albero, figli, dizionario)
        
    
       
    
    
    

def scorrinodo(nodo, listanodi, nododacancellare = '', livello = 0):
    
    global albero
    
    global livelli
    
    if nodo not in albero:
        
        listanodi[nodo] = []
        
        return listanodi
        
    if albero[nodo] == 0:
        
        listanodi[nodo] = []
    
    else:

        tmplivello = []
        
        if livello in livelli:
            
            tmplivello = livelli[livello]
            
        tmplivello.append(nodo)
            
        livelli[livello] = tmplivello
            
        for subnodo in albero[nodo]:
            
            if nododacancellare != subnodo:
                
                scorrinodo(subnodo, listanodi, nododacancellare, livello  + 1)
                
                if nododacancellare in albero[subnodo]:
                    
                    newlist = list(albero[subnodo])
                    
                    newlist.remove(nododacancellare)
                                        
                    listanodi[subnodo] = newlist
                    
                else:
            
                    listanodi[subnodo] = albero[subnodo]
        
    listanodi[nodo] = albero[nodo]
    
    return listanodi

def salvaalbero(alberodasalvare, fout):

    outputfile = open(fout, 'w')
        
    json.dump(alberodasalvare, outputfile)
            
    outputfile.close

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    
    caricaalbero(fnome)
    
    salvaalbero(scorrinodo(x, {}), fout)
    
    
    
def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    
    global albero  
    
    global nodoradice
    
    caricaalbero(fnome)  
    
    #
    
    salvaalbero(scorrinodo(nodoradice, {}, x), fout)
        

def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''

    global albero  
    
    global nodoradice
    
    global livelli
    
    livelli = {}

    caricaalbero(fnome)  
    
    #scorrinodo(list(albero.keys())[0], {})
    
    scorrinodo(nodoradice, {})
    
    for tmplivello in livelli.keys():
        
        #tmplista = livelli[tmplivello]
        
        tmplista = sorted(livelli[tmplivello])
        
        livelli[tmplivello] = tmplista
    
    salvaalbero(livelli, fout)

def crealegame(elemento, Padre):

    global alberoantenati

    global albero
    
    alberoantenati[elemento] = (Padre, len(albero[elemento]))

    for figlio in albero[elemento]:
        
        crealegame(figlio, elemento)


def controllafiglipadre(elemento, numerofigli, quantisonoattualmente):
    
    global alberoantenati
    
    tmpElemento = alberoantenati[elemento]
    
    if tmpElemento[1] == numerofigli:
        
        quantisonoattualmente += 1
        
    else:
        
        if tmpelemento[0] != '':
            
            controllafiglipadre(tmpelemento[0], numerofigli, quantisonoattualmente)
            
    return quantisonoattualmente

def conta_grandi_avi(chiave, valore, numeroavitrovati, chiavechiamante):

    global alberoantenati
    
    if alberoantenati[chiave][0] != '':
    
        numeroavitrovati = conta_grandi_avi(alberoantenati[chiave][0], valore, numeroavitrovati, chiavechiamante)
        
    if alberoantenati[chiave][1] == valore and chiave != chiavechiamante:
            
        return numeroavitrovati + 1
        
    else:
            
        return numeroavitrovati

def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    
    global albero  
    
    global nodoradice

    global alberoantenati
    
    dizionario_avi = {}
    
    caricaalbero(fnome)  
    '''
    primoavo = ''
    
    for primoavo in albero:
        
        break
    ''' 
    crealegame(nodoradice, '')
    
    for familiare in alberoantenati:
        
        dizionario_avi[familiare] = conta_grandi_avi(familiare, y, 0, familiare)
    
    salvaalbero(dizionario_avi, fout)
    
    alberoantenati = {}
    
    albero = {}
    
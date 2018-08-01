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
from copy import deepcopy

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as json_data:
        dict_old = json.load(json_data)
    dizionario_nuovo={}
    dizionario_nuovo[x]=dict_old[x]
    lista_livelli=dict_old[x]
    dizionario_nuovo=dizionario01(dict_old,x,lista_livelli,dizionario_nuovo)
    with open(fout,'w') as j:
        json.dump(dizionario_nuovo,j)

def dizionario01(dict_old,x,lista_livelli,dizionario_nuovo):
    dizionario_nuovo1=dizionario_nuovo
    lista_livelli01=[]
    k=0
    for valore_della_lista in lista_livelli:
        if dict_old[valore_della_lista]==[]:
            dizionario_nuovo[valore_della_lista]=dict_old[valore_della_lista]
        else:
            dizionario_nuovo[valore_della_lista]=dict_old[valore_della_lista]
            for y in dict_old[valore_della_lista]:
                lista_livelli01+=[y]
        k+=1
    lista_livelli=lista_livelli01
    if lista_livelli==[]:
        return dizionario_nuovo
    return dizionario01(dict_old,x,lista_livelli,dizionario_nuovo)




def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as json_data:
        dict_old = json.load(json_data)
    albero_da_cancellare=cancella_sottoalbero01(x,dict_old)
    valori_da_cancellare=albero_da_cancellare.keys()
    for da_cancellare in valori_da_cancellare:
        del dict_old[da_cancellare]
    valori_da_cercare=dict_old.keys()
    for valore in valori_da_cercare:
        for contenuto_dict_old in dict_old[valore]:
            #print('for2',contenuto_dict_old)
            if contenuto_dict_old==x:
                #print(valore)
                valore_identificato=valore
                break
    lista_contenuto=[]
    for contenuto in dict_old[valore_identificato]:
        if contenuto!=x:
            lista_contenuto+=[contenuto]
            #print(lista_contenuto)
    dict_old[valore_identificato]=lista_contenuto
    #print(dict_old)
    with open(fout,'w') as j:
        json.dump(dict_old,j)

def cancella_sottoalbero01(x,dict_old):
    '''inserire qui il vostro codice'''
    dizionario_nuovo={}
    dizionario_nuovo[x]=dict_old[x]
    lista_livelli=dict_old[x]
    return cancella_sottoalbero02(dict_old,x,lista_livelli,dizionario_nuovo)
    

def cancella_sottoalbero02(dict_old,x,lista_livelli,dizionario_nuovo):
    dizionario_nuovo1=dizionario_nuovo
    lista_livelli01=[]
    k=0
    for valore_della_lista in lista_livelli:
        if dict_old[valore_della_lista]==[]:
            dizionario_nuovo[valore_della_lista]=dict_old[valore_della_lista]
        else:
            dizionario_nuovo[valore_della_lista]=dict_old[valore_della_lista]
            for y in dict_old[valore_della_lista]:
                lista_livelli01+=[y]
        k+=1
    lista_livelli=lista_livelli01
    if lista_livelli==[]:
        return dizionario_nuovo
    return cancella_sottoalbero02(dict_old,x,lista_livelli,dizionario_nuovo)




def dizionario_livelli(fnome,fout):
    '''inserire qui il vostro codice'''
    with open(fnome) as json_data:
        dict_old = json.load(json_data)
    x=trova_primo_elemento(dict_old) #x=valore_iniziale
    dizionario_livelli={}
    k=0
    dizionario_livelli[k]=[x]
    lista1=dict_old[x]
    coppia_risultato=struttura_livelli(x,dict_old,dizionario_livelli,k,lista1)
    dizionario_livelli=coppia_risultato[0]
    k=coppia_risultato[1]
    k1=0
    dizionario_livelli=risistematina(dizionario_livelli,k,k1)
    with open(fout,'w') as j:
        json.dump(dizionario_livelli,j)

def trova_primo_elemento(dict_old):
    chiavi_da_cercare=dict_old.keys()
    valori_da_cercare=dict_old.values()
    lista_valori=[]
    for valore in valori_da_cercare:
        for zio in valore:
            lista_valori+=valore
            break
    for valore in chiavi_da_cercare:
        if valore not in lista_valori:
            valore_iniziale=valore
            break
    return valore_iniziale

def struttura_livelli(x,dict_old,dizionario_livelli,k,lista1):
    lista=lista1
    lista1=[]
    k+=1
    dizionario_livelli[k]=[]
    for valore in lista:
        if dizionario_livelli[k]==[]:#se dobbiamo ancora attribuirgli un valore:
            if type(valore)==type('s'):
                if valore!=[]:
                        lista1+=dict_old[valore]
                dizionario_livelli[k]=lista
            elif type(valore)==type([]):
                dizionario_livelli[k]=[]
                for elemento in valore:
                    if elemento!=[]:
                        lista1+=dict_old[elemento]
                    dizionario_livelli[k]+=[elemento]
        else:
            lista_valute=dizionario_livelli[k]
            if type(valore)==type('s'):
                if valore!=[]:
                    lista1+=dict_old[valore]
                dizionario_livelli[k]=lista
            elif type(valore)==type([]):
                for elemento in valore:
                    if elemento!=[]:
                        lista1+=dict_old[elemento]
                    dizionario_livelli[k]+=elemento
    risultato=(dizionario_livelli,k)
    if lista1!=[]:
        return struttura_livelli(x,dict_old,dizionario_livelli,k,lista1)
    return risultato

def risistematina(dizionario_livelli,k,k1):
    for attributo in dizionario_livelli:
        if type(attributo)!=type('s'):
            dizionario_livelli[k1]=sorted(dizionario_livelli[k1])
            stringa_k1=str(k1)
    dizionario_livelli[stringa_k1]=sorted(dizionario_livelli[k1])
    del dizionario_livelli[k1]
    k1+=1
    if k+1==k1:
        return dizionario_livelli
    return risistematina(dizionario_livelli,k,k1)
 

def dizionario_gradi_antenati(fnome,y,fout):
    #y=numero di grado
    #x=numero di antenati di grado y
    '''inserire qui il vostro codice'''
    with open(fnome) as json_data:
        dict_old = json.load(json_data)
    originale_dict_old=deepcopy(dict_old)
    dizionario_figli={}
    dizionario_antenati={}
    dizionariolivelli=dizionario_livelli1(fnome)
    dizionario_figli=genera_figli(dict_old,dizionario_figli)
    x=trova_primo_elemento1(originale_dict_old)
    dizionario_antenati[x]=0
    dict_old=originale_dict_old
    chiavi=[]
    chiavi1=dict_old.keys()
    for h in chiavi1:
        chiavi+=[h]
    chiavi_complete=deepcopy(chiavi)
    chiavi=chiavi[1:]
    dizionario_antenati=analizza_dati(dict_old,dizionario_figli,dizionario_antenati,y,chiavi,x,dizionariolivelli)
    #print('FINALE DIZIONARIO_ANTENATI',dizionario_antenati)
    with open(fout,'w') as j:
        json.dump(dizionario_antenati,j)

def analizza_dati(dict_old,dizionario_figli,dizionario_antenati,y,chiavi,x,dizionariolivelli):
    percorsoalbero={}
    items=[]
    items1=dict_old.items()
    for x in items1:
        items+=[x]
    i=0
    #print('CICLO',i)
    #il ciclo for posso metterlo in una funzione ricorsiva esterna che funziona grazie alla rimozione del singolo elemento nella lista delle chiavi
    for valore in chiavi:
        #print('VALORE ANALIZZA_DATI',valore)
        valore_vero=deepcopy(valore)
        percorso_albero=[]
        percorsoalbero=percorso(dizionariolivelli,dict_old,percorsoalbero,items,chiavi,valore,x,percorso_albero)
        #print('VALORE ANALIZZA_DATI DOPO PERCORSOALBERO',valore)
        #print('PERCORSOALBERO DOPO SUA CREAZIONE',percorsoalbero)
        #print('PERCORSOALBERO[VALORE]=',percorsoalbero[valore])
        percorsoalbero2={}
        percorsoalbero2[valore]=percorsoalbero[valore]
        #print('PERCORSOALBERO2',percorsoalbero2)
        #percorsoalbero2=percorso_2(valore,percorsoalbero,x,percorsoalbero2)
        dizionario_antenati=assegnazione(dizionario_figli,dizionario_antenati,percorsoalbero,y,valore)
    #print('PERCORSOALBERO2',percorsoalbero2)
    #print('CICLO',i)
    i+=1
    #print(dizionario_antenati)
    return dizionario_antenati

def assegnazione(dizionario_figli,dizionario_antenati,percorsoalbero,y,valore):
    presenze_grado=0
    for chiave_percorso in percorsoalbero[valore]:
        if dizionario_figli[chiave_percorso]==y:
            presenze_grado+=1
    dizionario_antenati[valore]=presenze_grado
    return dizionario_antenati

def percorso(dizionariolivelli,dict_old,percorsoalbero,items,chiavi,valore,x,percorso_albero):
    chiavi2=deepcopy(chiavi)
    chiavi=deepcopy(chiavi)
    #print('INIZIO',chiavi,valore)
    valore_iniziale=deepcopy(valore)
    livelli=dizionariolivelli.items()
    percorso_albero=[]
    dict_livelli=[]
    for x in livelli:
        dict_livelli+=[x]
    for k1 in range(len(items)):
        for k in range(len(chiavi2)):
            if valore in items[k][1]:
                percorso_albero+=[items[k][0]]
                break
        valore=items[k][0]
        #print('1-=',percorso_albero)
        #mi crea e mi dice il valore 
        for k2 in range(len(livelli)):
            if valore_iniziale in dict_livelli[k2][1]:
                soluzione=dict_livelli[k2][0]
                break
        #print('DIZIONARIO PERCORSO ALBERO',percorsoalbero)
        if int(soluzione)==len(percorso_albero):
            break
        #'''
    #print('VALORE',valore,'PERCORSO ALBERO',percorso_albero)
    percorsoalbero[valore_iniziale]=percorso_albero
    #print('2-=',percorso_albero)
    return percorsoalbero
    

def genera_figli(dict_old,dizionario_figli):
    chiavi=dict_old.keys()
    chiavi1=[]
    for x in chiavi:
        chiavi1+=[x]
    chiave=chiavi1[0]
    if type(dict_old[chiave])==type('s'):
        dizionario_figli[chiave]=1
        del dict_old[chiave]
    else:
        dizionario_figli[chiave]=len(dict_old[chiave])
        del dict_old[chiave]
    if dict_old=={}:
        return dizionario_figli
    return genera_figli(dict_old,dizionario_figli)

def dizionario_livelli1(fnome):
    '''inserire qui il vostro codice'''
    with open(fnome) as json_data:
        dict_old = json.load(json_data)
    x=trova_primo_elemento(dict_old) #x=valore_iniziale
    dizionario_livelli={}
    k=0
    dizionario_livelli[k]=[x]
    lista1=dict_old[x]
    coppia_risultato=struttura_livelli1(x,dict_old,dizionario_livelli,k,lista1)
    dizionario_livelli=coppia_risultato[0]
    k=coppia_risultato[1]
    k1=0
    dizionario_livelli=risistematina1(dizionario_livelli,k,k1)
    return dizionario_livelli

def trova_primo_elemento1(dict_old):
    chiavi_da_cercare=dict_old.keys()
    valori_da_cercare=dict_old.values()
    lista_valori=[]
    for valore in valori_da_cercare:
        for zio in valore:
            lista_valori+=[valore]
            break
    for valore in chiavi_da_cercare:
        if valore not in lista_valori:
            valore_iniziale=valore
            break
    return valore_iniziale

def struttura_livelli1(x,dict_old,dizionario_livelli,k,lista1):
    lista=lista1
    lista1=[]
    k+=1
    dizionario_livelli[k]=[]
    for valore in lista:
        if dizionario_livelli[k]==[]:#se dobbiamo ancora attribuirgli un valore:
            if type(valore)==type('s'):
                if valore!=[]:
                        lista1+=dict_old[valore]
                dizionario_livelli[k]=lista
            elif type(valore)==type([]):
                dizionario_livelli[k]=[]
                for elemento in valore:
                    if elemento!=[]:
                        lista1+=dict_old[elemento]
                    dizionario_livelli[k]+=[elemento]
        else:
            lista_valute=dizionario_livelli[k]
            if type(valore)==type('s'):
                if valore!=[]:
                    lista1+=dict_old[valore]
                dizionario_livelli[k]=lista
            elif type(valore)==type([]):
                for elemento in valore:
                    if elemento!=[]:
                        lista1+=dict_old[elemento]
                    dizionario_livelli[k]+=elemento
    risultato=(dizionario_livelli,k)
    if lista1!=[]:
        return struttura_livelli(x,dict_old,dizionario_livelli,k,lista1)
    return risultato

def risistematina1(dizionario_livelli,k,k1):
    for attributo in dizionario_livelli:
        if type(attributo)!=type('s'):
            dizionario_livelli[k1]=sorted(dizionario_livelli[k1])
            stringa_k1=str(k1)
    dizionario_livelli[stringa_k1]=sorted(dizionario_livelli[k1])
    del dizionario_livelli[k1]
    k1+=1
    if k+1==k1:
        return dizionario_livelli
    return risistematina(dizionario_livelli,k,k1)
    

'''
Un  file di compiti contiene  informazioni su un insieme  di compiti da eseguire.
Esistono  due tipologie di compiti:
- compiti che possono essere eseguiti indipendentemente dagli altri.
- compiti da svolgere  solo al termine di un compito preliminare.
I compiti del primo tipo sono codificati nel file mediante una linea che contiene
in sequenza le due sottostringhe "comp" ed "N" (senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "N" e' l'ID del compito (un numero positivo).
Compiti del secondo tipo sono codificati nel file mediante due linee di codice.
-- la prima  linea,  contiene in sequenza le due sottostringhe "comp" ed "N" 
(senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "N" e' l'ID del compito (un numero positivo).
-- la seconda linea (immediatamente successiva nel file) contiene 
in sequenza le due sottostringhe "sub" ed "M" (senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "M" e' l'ID del compito preliminare.

il seguente file di compiti contiene informazioni su 4 compiti (con identificativi 1,3,7 e 9). 
I compiti con identificativi 1 e 9 possono essere svolti indipendentemente dagli altri mentre i compiti 
con identificativo 3 e 7 hanno entrambi un compito preliminare.

comp 3
 sub 9
        comp1
comp              9
    comp 7
sub3

Scrivere la funzione pianifica(fcompiti,insi,fout) che prende in input:
- il percorso di un file (fcompiti) 
- un insieme  di ID di compiti da cercare (insi)
- ed il percorso di un file (fout) 
e che salva in formato JSON nel file fout un dizionario (risultato).

Il dizionario (risultato) dovra' contenere come chiavi gli identificativi (ID) dei compiti 
presenti in fcompiti e richiesti nell'insieme insi.
Associata ad ogni ID x del dizionario deve esserci una lista contenente  gli identificativi (ID) dei compiti 
che bisogna eseguire prima di poter eseguire il compito x richiesto
(ovviamente la lista di un ID di un compito che non richie un compito preliminare risultera' vuota ). 
Gli (ID) devono comparire nella lista nell'ordine di esecuzione corretto, dal primo fino a quello precedente a quello richiesto 
(ovviamente il primo ID di una lista non vuota corripondera' sempre ad un compito che non richiede un compito preliminare). 


Si puo' assumere che:
 - se l' ID di un compito che richieda un compito preliminare e' presente  in fcompiti 
    allora anche l'ID di quest'ultimo e' presente in fcompiti
 - la sequenza da associare al compito ID del dizionario esiste sempre
 - non esistono cicli (compiti che richiedono se' stessi anche indirettamente)


Ad esempio per il file di compiti  fcompiti contenente:

comp 3
 sub 9
        comp1
comp              9
    comp 7
sub3

al termine dell'esecuzione di  pianifica(fcompiti,{'7','1','5'}, 'a.json')
il file 'a.json' deve contenere il seguente dizionario
{'7':['9','3'],'1':[]}


Per altri esempi vedere il file grade02.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''
#input: percorso file,insieme di id da ricercare,il percorso di un file
#output: dizionario        
def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    lista1=[]
    lista2=[]
    with open(fcompiti,'r') as file:
        fileenumerato=list(enumerate(file))
        for indice,riga in fileenumerato:  #ricerca è la funzione che controlla se cè  'comp' e 'N' nella riga e esamina anche la successiva per distinguere i due tipi di possibili
            ID,tupla=ricerca(indice,riga,fileenumerato) #lista1 è la lista dove ci sono gli ID finiti, lista2 invece è dove ci sono gli ID infiniti
            if tupla==() and ID=='':
                continue
            elif ID!=0 and tupla==():
                lista1.append(ID)
            
            elif ID!=0 and tupla!=():  
                lista2.append(tupla)
     
    diz=controllo(insi,lista1,lista2)  
    salvafile(diz,fout)
            
    
def ricerca(indice,stringa,fileenumerato):
    
    stringasuccessiva=''
    stringa1=''                                                                 
    indicemax=len(fileenumerato)-1  #da o a indicemax
    stringa2=stringa
    listadistringhe=stringa2.split()    
    if 'comp'in listadistringhe or len(listadistringhe)==1:     #controlla se la riga contiene 'comp' o ''sub' e tutte le possibili casistiche,eliminando la punteggiatura
        if 'comp' in listadistringhe:
            stringa=stringa.replace('comp','')
            stringaid=stringa.strip()
        elif 'comp' not in listadistringhe:
            for parola in listadistringhe:
                if parola[0]!='s':
                    for carattere in parola:
                        if carattere.isdecimal():
                            stringa1=stringa1+carattere
                            stringaid=stringa1
                            
                else:
                     stringaid=''
                     tupla=()
        if indice!=indicemax:
            rigasuccessiva=fileenumerato[indice+1][1]
            rigasuccessiva2=rigasuccessiva
            listadirigasuccessiva=rigasuccessiva2.split()
            if 'sub' in listadirigasuccessiva or len(listadirigasuccessiva)==1:
                if 'sub' in listadirigasuccessiva:
                    rigasuccessiva=rigasuccessiva.replace('sub','')
                    rigasuccessivaid=rigasuccessiva.strip()
                    tupla=stringaid,rigasuccessivaid
                elif 'sub' not in listadirigasuccessiva and len(listadirigasuccessiva)==1:
                    for parola in listadirigasuccessiva:
                        if parola[0]!='c':
                            for carattere in parola:
                                if carattere.isdecimal():
                                    stringasuccessiva=stringasuccessiva+carattere
                                    tupla=stringaid,stringasuccessiva
                        else:
                            tupla=()
                 
            else:
                tupla=()
        else:
            
            tupla=()
            
        
    else: 
        stringaid=''   
        tupla=()
    
    return stringaid,tupla       
    
    
def controllo(insieme,lista1,lista2):  
    
    listatemporanea=[]   #lista in cui inserisco i file preliminari da aprire se l'Id appartiene alla lista2
    diz={}
    for id in insieme:
        
        if id in lista1:  #controllo se id appartiene alla lista1 quindi se è finito
            diz[id]=[]
        else:
            for id1,id2 in lista2:  
                if id1==id:
                    listatemporanea.append(id2)
                    while id2 not in lista1:   #loop da fare per prendere tutti i file preliminari da aprire prima del file cercato
                        for a,b in lista2:
                            if a==id2:
                                listatemporanea.append(b)
                                id2=b
                    listatemporanea.reverse()
                    diz[id1]=listatemporanea   
        listatemporanea=[] 
    return diz        
                    
                    
                    
def salvafile(diz,fout):
    import json
    with open(fout,'w') as f:
        json.dump(diz,f)         
                   

         
            

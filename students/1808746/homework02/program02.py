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

def pianifica(fcompiti,insi,fout):
    txt=open(fcompiti)
    nuovoTxt=[]
    for riga in txt.readlines():
        #si rimuovono gli spazi dalla riga e si dividono le sottostringhe dagli id 
        riga=riga.strip().split()
        #se il risultato non è nella forma ['comp', '7'] ma ['comp10']:
        if len(riga)==1:
            miglioraRiga(riga)
        #LA RIGA E' SISTEMATA ed è nella forma ['parola','id']
        nuovoTxt.append(riga)
    parziale=dizionalo(nuovoTxt)
    risultato=funziona(insi, parziale)
    salvaJson(risultato,fout)
    
    txt.close()
 
def miglioraRiga(riga):
    '''se la riga non ha due elementi (sottostringa e id separati), si divide nei due rispettivi elementi'''
    canc=''
    while riga[0][-1].isalpha()==False:
        #aggiunge i caratteri numerici a una variabile momentanea canc
        canc+=riga[0][-1]
        #rimuove i caratteri numerici 
        riga[0]=riga[0][:-1]
    #si trasforma la lista canc in stringa, dopo aver invertito l'ordine dei numeri che la compongono (poiché sono stati aggiunti scorrendo da destra a sinistra)    
    canc=''.join(canc[::-1])
    #aggiunge la variabile momentanea canc alla lista riga (al secondo elemento)
    riga.append(canc)
    return riga

def dizionalo(nuovoTxt):
    '''rende la lista di liste nuovoTxt un dizionario in cui le chiavi sono i comp e i valori sono i sub.
    Es. [comp,7],[sub,4]---->'7':['4'] '''
    parziale={}
    for i in range(len(nuovoTxt)-1):
        if nuovoTxt[i+1][0]=='sub':
            parziale[nuovoTxt[i][1]]=nuovoTxt[i+1][1]
        elif nuovoTxt[i][0]=='comp' and nuovoTxt[i+1][0]=='comp':
            pass
        #
        elif nuovoTxt[i][1] not in parziale:
            parziale[nuovoTxt[i][1]]=[]
    return parziale

def funziona(insi, parziale):
    risultato=dict() #dizionario risultato
    #lavora su ogni elemento dato in input nell'insieme:
    for el in insi:
        if el in parziale.keys():
            temp=el
            if parziale[temp]!=[]:
                risultato[el]=[parziale[temp]]
            else:
                risultato[el]=parziale[temp]
            #esegui il ciclo che aggiunge tutti i sottocompiti e sostituisce dopo ogni ciclo il nuovo sub da cercare nelle chiavi (il ciclo finisce quando il nuovo sub non ha un sub corrispondente)
            while parziale[temp]!=[]:
                temp=''.join(parziale[temp]) #ogni ciclo, la variabile da cercare nei comp è l'ultimo sub aggiunto                   
                #trasformo l'attributo-lista in stringa assegnango il valore alla variabile tempS
                tempS=''.join(parziale[temp])
                #eseguo il controllo sul sub corrispondente
                if temp in parziale.keys() and tempS!='':
                    #aggiungi alla lista-attributo la stringa equivalente all'attributo di parziale[temp]
                    risultato[el].append(tempS)

    #inverto gli elementi delle liste-attributo per ottenere i compiti in ordine
    for chiave in risultato:
        if len(risultato[chiave])>1:
            risultato[chiave]=risultato[chiave][::-1]
    return risultato

def salvaJson(risultato,fout):
    '''salva il dizionario risultato su json'''
    from json import dump
    j=open(fout,'w')
    dump(risultato,j)
    j.close()

if __name__=='__main__':
    pianifica('file02_50000_100.txt', set([str(i) for i in range(2000,50001)]),'test5.json')
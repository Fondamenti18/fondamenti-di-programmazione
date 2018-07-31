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
'''per le re:
comp_sub=dict(re.findall(r'comp *(\d*)\s*sub *(\d*)',rd))
Ncomp=filter(lambda x: x in re.findall(r'comp\s*(\d*)',rd),insi)'''

import re, json
    
def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    dic={}#dizionario output
    with open(fcompiti,mode='r') as f:
        rd=f.read()        #leggo file
        comp_sub=make_dic(rd) #faccio un dizionario con ogni comp e il suo subcomp
        turnon=filter(lambda x: x in comp_sub,insi)
        for el in turnon: #per ogni elemento di insi controllo se è un comp
            
            ls=list(tree(el,comp_sub))
                
            dic[el]=ls[::-1]#se o è chiamo tree e appendo la lista delle dipendenze a dic
    with open(fout,mode='w') as f2:
        json.dump(dic,f2)#stampo su file json il dic ottenuto
    return  

def make_dic(rd):
    comp_sub=dict((re.findall('comp *(\d*)()',rd))) #creo un dizionario comp-niente
    comp_sub1=dict((re.findall('comp *(\d*)\s*sub *(\d*)',rd)))#creo un dizionario comp-sub
    
    for x in comp_sub:
        if x in comp_sub1:
            comp_sub[x]=comp_sub1[x] #fondo i due dizionari e ottengo un dizionario
    return comp_sub                #che per ogni comp ha il suo sub se c'è, se no vuoto
        
def tree(key,comp_sub):    
        while comp_sub[key] !='':# tree cerca il sub del comp entrato
            yield comp_sub[key]
            key=comp_sub[key]
            
    
    #gira la lista e la ritorna
    
if __name__=='__main__':
    print (pianifica('file02_10_2.txt', {'2','4','11','1','6','9','10'},'test1.json'))              
    print(pianifica('file02_50000_100.txt', set([str(i) for i in range(2000,50001)]),'test5.json'))
     
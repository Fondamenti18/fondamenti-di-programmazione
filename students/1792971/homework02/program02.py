'''Scrivere la funzione pianifica(fcompiti,insi,fout) che prende in input:
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
'''
import json
from json import*
       
def pianifica(fcompiti,insi,fout):
    file=open(fcompiti)
    testo=file.read().split("comp")
    testo.pop(0)
    file.close()
            
    compiti=trova_compiti(testo,insi)
    f=open(fout,"w")
    dump(compiti,f)
    f.close()
    
    
def trova_compiti(testo,insi):
    d=inserisci_compiti(testo)
    compiti={}
    for key in insi:
        for comp in testo:
            if "sub" in comp:
                txt=comp.split("sub")
                if key==txt[0].strip():
                    k=txt[1].strip()
                    compiti[key]=[k]+sottochiavi(k,d)
                    compiti[key].reverse()
            else:
                if key==comp.strip():
                    compiti[key]=[]
    return compiti

def inserisci_compiti(testo):
    d={}
    for comp in testo:
        if "sub" in comp:
            txt=comp.split("sub")
            key=txt[0].strip()
            d[key]=[txt[1].strip()]
        else:
            key=comp.strip()
            d[key]=[]
    return d
 
def sottochiavi(k,d):
    subkeys=[]
    if k in d and d[k]!=[]:
        subkeys+=d[k]
        subkeys+=sottochiavi(d[k][0],d)
    return subkeys
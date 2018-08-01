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
    
    import json
    import re
    import sys
    sys.setrecursionlimit(4000)
    
    
    diz1={}
    with open (fcompiti,encoding="utf-8")as o:
        
        for lista in o.readlines():
            
            if "comp" in lista :
                _ = lista.replace(" ","")
                diz1[_]=[]
                
                
            else :
                diz1[_]=lista.replace(" ","")
                                            
        x=[]
        y=[]
        for _ in diz1.keys():
           xx=re.sub('[^0-9]','',_)
           x.append(xx)
       
        for _ in diz1.values():
            if _ ==[]:
                y.append(_)
            else :            
                yy=re.sub('[^0-9]','',_)      
                y.append(yy)
        dictionary = dict(zip(x, y))
        
                
        
        dizionario_totale={}
        dizionario_funzione={}
        
        for k in dictionary:
            
            if dictionary[k]!=[]:
                dizionario_funzione[k]=dictionary[k]
        
       
        def list_maker(dictio,key,lista):
            
                if key not in dictio:
                    return [key] + lista[:-1]                                 
            
                else:
                    return list_maker(dictio, dictio[key], [key] + lista) #
        
        for el in x:
           
           if (list_maker(dizionario_funzione,el,[]))==[el] and el in insi   :
               dizionario_totale[el]=[]
           elif (list_maker(dizionario_funzione,el,[]))!=[el] and el in insi  :
               dizionario_totale[el]=(list_maker(dizionario_funzione,el,[]))
    
  

   
            
    with open(fout,"w")as j:
        json.dump(dizionario_totale,j)
   

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
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero. C:/Users/john/Desktop/homework02/es2/file02_10_2.txt
if num1!="" and num not in d.values() and num not in d:
            print(num)
            d[num]=num1
            print(d)
        elif num in d and num1!="":
            print("?")
            d.setdefault(num,[]).append(num1)
             for i in insieme:
            if i in d.keys():
                finale[i]=d[i]
                if d[i] in d.keys():
                    
'''
import json
#def pianifica(fcompiti,insi,fout):
    
    
def pianifica(fcompiti,insi,fout):                 #creazione di un dizionario per ogni compito
    d={}
    finale={}
    f=open(fcompiti)
    num1=""
    temp=""
    lista=[]
    for line in f:

        #print(line)
        i=0
        j=0
        stringa=line
        
        if "comp" in stringa:
            num=""
            #print("something")
            while i != len(stringa):
                    #print("lavoro")           #vedo gli identificativi del post
                    if stringa[i].isnumeric()==True:
                        num=num+ stringa[i]
                    i=i+1
            d.setdefault(num,"")
                
        else:
            num1=""
            while i != len(stringa):
                    #print("lavoro")           #vedo gli identificativi del post
                    if stringa[i].isnumeric()==True:
                        num1=num1+ stringa[i]
                    i=i+1
        #print(num)
                    
                    #print(line)
                    if num in d.keys() and num1!="":
                        d[num]=num1
    #print(d)
    for i in insi:
        a=False
        lista=[]
        #c=[]
        #print('i',i)
        if i in d.keys() and d[i]=="":
            finale.setdefault(i,[])
            #print(finale[i])
            a=True
        if i in d.keys() and d[i] not in d.keys() and a==False:
            #print("f")
            finale.setdefault(i,[]).append(d[i]) #<.-----importante          #finale[i]=d[i]
        #elif i not in d.keys():
            #finale.setdefault(i,[])
        elif i in d.keys() and d[i] in d.keys():
            #print(i)
            temp=i
            #77print(d[i])
            while temp in d.keys() and d[temp]!="":
                #print(i)
                #finale.setdefault(i,[]).append(d[temp])<--------   IMPORTANTE
                #print(d[temp])
                    #print(d[temp])
                lista=lista + [d[temp]]
                temp=d[temp]
                #print(lista)
                #print(temp)
                #print(d[temp])
            #finale.setdefault(i,[]).append(ricerca(d,i))
            #print(lista)
            for l in reversed(lista):
                finale.setdefault(i,[]).append(l)
    
    f.close()
    f=open(fout,'w')
    json.dump(finale,f)
    f.close()
    #return(finale)
        
        
        
        
    
        
    
            
            
            
























    
    
    

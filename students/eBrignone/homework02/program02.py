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
comp 9
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
import json
finalList=[]
def pianifica(fcompiti,insi,fout):
    diz={}
    testo=fileToString(fcompiti)
    listaTuple=testoToTupla(testo)
    for compito in insi:
        compito=int(compito)
        finalList.clear()
        cercaCompito(listaTuple,compito)
        if len(finalList)>0:
            if finalList[0]!="elimina":
                finalList.reverse()
                diz.update({compito:finalList[:-1]})
        else:
            diz.update({compito:[]})
    with open(fout, 'w') as f:
        json.dump(diz, f)

def fileToString(filename): 
    try:
        file=open(filename,'r',encoding='utf8')
        testoFile=''
        for line in file.readlines():
            testoFile+=line
        return testoFile.split("\n")
    except:
        print("errore nell'apertura del file")  
            

    
    
def testoToTupla(testo):
    comp="comp"
    sub="sub"
    tupla=[]
    for line in testo:
        indiceParola=-1
        if comp in line:
            indiceParola=line.index(comp,indiceParola+1)
            tupla.append((comp,int(line[indiceParola+len(comp):])))
        elif sub in line:
            indiceParola=line.index(sub,indiceParola+1)
            tupla.append((sub,int(line[indiceParola+len(sub):])))
    return tupla
    
def cercaCompito(lista,compito):    
    i=0
    tupla=()
    cont=0
    while i<len(lista):
        tupla=lista[i]        
        if compito in tupla and "comp" in tupla:
            cont+=1
            if i+1>=len(lista):
                return tupla[1]
            if "sub" in lista[i+1]:                
                tupla2=lista[i+1]                
                finalList.append(''+str(compito))
                
                ncompito=cercaCompito(lista,tupla2[1])
                if ncompito!=None:
                    finalList.append(''+str(ncompito))
            else:
                return tupla[1]
        i+=1
    if cont==0:
        return finalList.append("elimina")
    
    
    
    
    
    
    
    
    
    
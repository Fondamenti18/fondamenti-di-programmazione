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
import json

def pianifica(fcompiti,insi,fout):
	dizionario=trovaCompiti(fcompiti, insi)    #richiama funzione trovaCompiti e passa come argomenti il file e l'insieme
	dizionarioCompleto=dizionario.copy()   #dizionario che contiene tutte le chiavi, copia del dizionario originale prima dell'eliminazione delle chiavi non presenti nell'insieme
	dizionario=eliminaChiavi(dizionario, insi) #richiamo funzione eliminaChiavi per eliminare le chiavi non presenti nell'insieme 'insi'
	
	subCompito=[]
	for chiave, valore in dizionario.items():  #scorre chiave e valore del dizionario
	   subCompito=trovaSubCompiti(dizionarioCompleto, valore)  #richiama funzione trovaSubCompiti e passa come argomenti il dizionario che contiene tutti i compiti e il valore prelevato con il ciclo

	   dizionario[chiave]+=subCompito  #aggiunge alla chiave del dizionario il valore della lista subCompito
	   dizionario[chiave]=dizionario[chiave][::-1] #rigira la lista

			  
				  
	with open(fout, 'w') as f: #apre il file 'fout' nella modalità scrittura
	  json.dump(dizionario,f)  #scrive il dizionario nel file
	 
	
	
	
def trovaCompiti(file, insi):
    '''Funzione per trovare il numero di compito e il suo eventuale sub compito, crea un dizionario che ha come chiavi i numeri dei compiti e come valori una lista dei numeri dei compiti da svolgere
    '''
    chiaveDiz=''
    diz={}
    with open(file, mode='rt', encoding='utf-8') as f:	#apre il file in modalità lettura testo
        for linea in f:	 #scorre file
            if(linea.lower().find('comp')!=-1):	#se la linea, convertita in minuscolo, contiene la parola 'comp'
                chiaveDiz=linea.replace('comp','').strip()	#memorizza nella variabile chiave la linea, senza spazi e parola 'comp'
                diz[chiaveDiz]=[]	#aggiungi a dizionario la chiave senza valore
            elif(linea.lower().find('sub')!=-1):	#se la linea, convertita in minuscolo, contiene la parola 'sub'
                diz[chiaveDiz]+=linea.replace('sub','').strip().split()	#aggiungi al dizionario alla chiave precedentemente memorizzata il valore della linea senza spazi, senza parola 'sub' e convertita in lista   
        return(diz)



def eliminaChiavi(dizionario, insi):
    '''Funzione per eliminare le chiavi non presenti nell'insieme 'insi' e ordina le liste
    '''
    lstChiaviDaEliminare=[]
    for chiave in dizionario.keys():    #scorre le chiavi del dizionario
        if(chiave not in insi):     #se la chiave non è presente nell'insieme
            lstChiaviDaEliminare.append(chiave) #aggiungi chiave alla lista lstCHiaviDaEliminare
    for i in lstChiaviDaEliminare:  #scorri la lista
        dizionario.pop(i)    #elimina chiave
    return(dizionario)	
    
 
    
    
    
def trovaSubCompiti(dizionarioCompleto, numero):
    '''Funzione per trovare i sub compiti di un compito passato come parametro
    '''
    lista=[]
    numero=''.join(numero)  #converto lista in stringa
    while(numero!='' and numero!=None and numero!=[] and numero in dizionarioCompleto): #finché il numero è diverso da vuoto ed è presente all'interno del dizionario completo
       lista+=dizionarioCompleto[numero]    #aggiungi alla lista il valore alla chiave 'numero' del dizionario
       numero=dizionarioCompleto[numero]    #la variabile numero prende il valore della chiave 'numero' del dizionario
       numero=''.join(numero)   #converto lista in stringa
    return(lista)
        
    				
    				
if __name__=='__main__':
    print(pianifica('file02_50000_100.txt', {'1','2','3','4','5','6','7','8','9'},'test3.json'))













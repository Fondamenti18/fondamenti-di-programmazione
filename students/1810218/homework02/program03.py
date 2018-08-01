'''
Abbiamo una stringa i cui elementi sono cifre tra '0' e '9' (comprese) che rappresenta la struttura di una parola.
La parola contiene al piu' 10 lettere diverse (ma puo' essere piu' lunga di 10 lettere se alcune sono ripetute), 
e la struttura si ottiene dalla parola sostituendo ciascuna lettera con una cifra, secondo le regole:
- a lettera uguale corrisponde cifra uguale
- a lettere diverse corrispondono cifre diverse

Esempio: 'cappello' -> '93447228'
Esempio: 'cappello' -> '12334556'

Sia data una "struttura" ed un insieme di parole. 
Vogliamo ottenere il sottoinsieme delle parole date compatibili con la struttura data.

Esempio: se la struttura e' '1234' e le parole sono { 'cane', 'gatto', 'nasa', 'oca', 'pino'}
le parole dell'insieme che sono compatibili con la struttura sono {'pino', 'cane'}

Scrivere una funzione decod( pfile, struttura) che prende in input:
- il percorso di un file (pfile), contenente testo organizzato in righe ciascuna composta da una sola parola
- una stringa di almeno 1 carattere, composta solo da cifre (la struttura delle parole da cercare)

La funzione  deve restituire l'insieme delle parole di pfile che sono compatibili con la struttura data.

Per gli esempi vedere il file grade03.txt

AVVERTENZE: 
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''


def compatibili(codice,parola):
    parola=parola.replace('\n','')
    if len(codice)!=len(parola):
        return False
    d={}
    pos=0
    while pos<len(parola):
        if parola[pos] not in d.keys():
            
            d.update({parola[pos]:codice[pos]})
        else:
            if codice[pos]==d[parola[pos]]:
                pass
            else:
                return False
        pos+=1
                
    l=list(d.values())
    a=set(d.values())
    l1=[]
    for x in a:
        if l.count(x)==1:
            l1.append(1)
    if len(l1)==len(l):
        return True
    else:
        return False
    
        
        
        

        
    
    



def decod(pfile, codice):
    f=open(pfile,'r')
    lista=f.readlines()
    risultato=[]
    for x in lista:
        x=x.rstrip
    for parola in lista:
        if compatibili(codice,parola):
            risultato.append(parola)
    for pos in range(len(risultato)):
        risultato[pos]=risultato[pos].replace('\n','')
    risultato=set(risultato)
    return risultato
            
    
        
   

    






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

#pfile=r"C:\Scuola\Università\Informatica\Materie\Fondamenti di Programmazione\Programmi\homework02\es3\file03.txt"
#codice='121'

def decod(pfile, codice):
    '''inserire qui il codice'''
    
    risultato=set('')
    
    with open(pfile,"r",encoding='utf-8') as parole:
        
        codicelist=list(codice)
        
        for i in parole:                        
            i=i.strip()
            
            if len(i)==len(codicelist):  
                parolelist=list(i)
                controllo=verifica(parolelist,codicelist)                        
                if controllo: risultato.add(i)
        
    return risultato

def verifica(parolelist,codicelist):
    
    controllo=True
    dizio={}
    
    for j in range(len(parolelist)):
                    
        if codicelist[j] in dizio:
            
            if dizio[codicelist[j]]!=parolelist[j]:
                controllo=False
                break
            
        elif parolelist[j] in dizio.values():
            controllo=False
            break
        
        else: dizio.setdefault(codicelist[j],parolelist[j])
                
    return controllo
                    





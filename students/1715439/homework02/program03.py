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


def decod(pfile, codice):
    with open (pfile, 'r', encoding='utf-8') as f:
        righe=f.readlines()
        compatibili=set()
        lungheOK=[]
        for riga in righe:
            riga= riga.strip()
            if len(riga)==len(codice):
                lungheOK.append(riga)
        for riga in lungheOK:
            if strutturaWord(riga)==strutturaCodice(codice):
                    compatibili.add(riga) 
    return compatibili 
  
    
    ##############################################
        
def strutturaWord(riga):
    return len(riga), encodeWord(riga)

def strutturaCodice(codice):
    return len(codice), encodeWord(codice)
            
def encodeWord(parola):
    encoded=''
    diz={}
    numeri=['1','2','3','4','5','6','7','8','9','0']
    n=0
    for letter in parola:
        try:
            if not letter in diz.keys():
                diz[letter]=numeri[n]
                n+=1
        except:
            pass
    #così ho costruito il dizionario, ora lo uso per codificare la parola
    
    for letter in parola:
        try:
            encoded+=diz[letter]
            
        except:
            pass
        
    return encoded





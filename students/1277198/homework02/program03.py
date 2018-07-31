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

'''in caso di regex:
length='(?=(\\b[a-zA-Z]'+'{'+str(len(codice))+'}\\b))
words=re.findall(length, f.read())
if len(set(w))==types and c==w:'''

def decod(pfile, codice):
    '''inserire qui il codice'''
    bingo=set()
    L=len(codice)
    types=len(set(codice))
    
    with open(pfile,'r') as f:
        words=filter(lambda x: len(x)==L and len(set(x))==types,f.read().split('\n'))
        for w in words:			
            c=compare(w,codice)
            if c==w:
                bingo.add(w)       
    return bingo
     
def compare(w,codice):
    c=''
    dic= dict(zip(codice,w))
    for k in codice:
        c+=dic[k]
    return c

if __name__=='__main__':
    print (decod('file03.txt','121'))
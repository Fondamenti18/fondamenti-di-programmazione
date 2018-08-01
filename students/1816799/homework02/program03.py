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

def decod(pfile, struttura):
     
    #lista con le parole del file, set di output vuoto
    lst=[]
    result=set()
    
    
    with open(pfile, mode='r') as text:
        txt=text.read()
        
        txt=clean(txt)
        
        #cicla sulle parole tenendo solo quelle che, senza ripetizioni, hanno lunghezza 
        #uguale al numero di input, anch' esso senza ripetizioni
        for word in txt:
            if len(word)==len(str(struttura)):
                if len(set(word))==len(set(str(struttura))):
                    lst.append(word) 
        
        #se la parola nella lista corrisponde alla chiave e al valore del dizionario,
        #aggiungilo all' insieme
        for j in lst:
            d=diz(j, struttura)
            if d==j:
                result.add(d)
        
        return result
    
def diz(word, cript_word):
    
    #formo il dizionario
    string=''
    dic=dict(zip(cript_word, word))
    
    #ciclo sul codice criptato, aggiungendo il singolo carattere se diverso da quelli precedenti
    for i in cript_word:
        string+=dic[i]

    return string

def clean(text):
    
    #splitta il testo, riuniscilo e splitta sugli spazzi
    txt=text.split()
    txt=' '.join(txt)
    txt=txt.split(' ')
    
    return txt
    


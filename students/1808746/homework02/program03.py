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

Esempio: se la struttura e' '1234' e le parole sono {'cane', 'gatto', 'nasa', 'oca', 'pino'}
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
    '''verifica che le parole del 'pfile' sinao compatibili con la struttura 'codice' data'''
    txt=open(pfile)
    risultato=set()
    #si avvia un ciclo che lavora solo sulle parole del file la cui lunghezza (eliminando lo \n finale) risulta uguale a quella del codice dato in input. PRIMO CONTROLLO-->PRIMA CONDIZIONE IF
    #se si trasforma il codice dato in input in insieme, rimarranno solo quei numeri diversi tra loro. Analogamente, se trasformo la riga in insieme, otterrò solo le lettere diverse tra di loro. Si verifica che le due lunghezze siano uguali. SECONDO CONTROLLO-->SECONDA CONDIZIONE IF.
    for riga in txt:
        riga=riga[:-1]
        if len(riga)==len(codice) and len(set(riga))==len(set(codice)):
            if verificaCorrispondenze(riga, codice)==True:
                risultato.add(riga)
    return risultato

def verificaCorrispondenze(riga, codice):
    #si crea un dizionario in cui ciascuna chiave corrisponde ad un numero del codice e ciascun attributo alla lettera di riga che compare nella posizione corrispondente
    dizIbrido={}
    for el in range(len(riga)): 
        if el not in dizIbrido:
            dizIbrido[codice[el]]=riga[el]
        else:
            continue
    
    #si verifica che la nuovaParola creata a partire dal dizIbrido sia uguale alla originale riga
    nuovaParola=''
    for i in codice:
        nuovaParola+=dizIbrido[i]
    
    if nuovaParola==riga:
        return True
    else:
        False

if __name__=='''__main__''':
    decod('file03.txt', '121')
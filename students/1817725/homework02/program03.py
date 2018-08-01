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
    pfile = open(pfile)
    righeFile = pfile.read()
    insieme = set()
    for parola in righeFile.split(): # per ogni parola nella stringa di testo divisa in parole
        if len(parola) == len(struttura): # se la lunghezza di quella parola è uguale alla lunghezza della struttura continuo, altrimenti passo alla prossima parola
            listaIndici = []       # inizializzo due liste vuote che poi andrò a confrontare una volta riempite
            listaChar = []
            for indice1,indice2 in zip(struttura[0::2], struttura[1::2]): # controllo gli indici della struttura due a due 
                x = struttura.count(indice1)     # con x conto quante volte l'indice 1 è presente nella struttura e con y quante volte l'indice 2 è presente nella struttura
                y = struttura.count(indice2)
                if x == 2 and y == 2 and indice1 == indice2: # se l'indice 1 e 2 sono presenti due volte nella struttura e sono uguali, vuol dire che sono vicini e allora li segno con due 7
                    listaIndici.append(7)
                    listaIndici.append(7)
                if x == 2 and y == 2 and indice1 != indice2: # se invece sono presenti entrambi due volte, ma non sono uguali allora nella lista aggiungo 9 e 8
                    listaIndici.append(9)
                    listaIndici.append(8)
                else:                                       # se non sono presenti due volte, ma magari 1 o 3 o 4, allora nella lista aggiungo il numero delle volte che sono presenti
                    listaIndici.append(x) 
                    listaIndici.append(y)
                    
            for char1,char2 in zip(parola[0::2], parola[1::2]): # discorso analogo per i caratteri
                x = parola.count(char1)
                y = parola.count(char2)
                if x == 2 and y == 2 and char1 == char2:
                    listaChar.append(7)
                    listaChar.append(7)
                if x == 2 and y == 2 and char1 != char2:
                    listaChar.append(9)
                    listaChar.append(8)
                else:
                    listaChar.append(x)
                    listaChar.append(y)
                    
            if listaIndici == listaChar: # infine confronto le due liste, se sono uguali vuol dire che la parola coincide con la struttura
                
                insieme.add(parola) # e quindi all'insieme aggiungo quella parola
    return insieme
    
        
       







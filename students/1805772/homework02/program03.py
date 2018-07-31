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
    risultato = set()
    
    len2 = len(codice)
    
    #trasformo codice (la copia) in una lista
    copia_codice = []
    for l in codice:
        copia_codice.append(l)
    
    for valori_file in open(pfile).readlines():
        if len(valori_file) == len2 + 1: #+1 per via di \n
            
            #trasformo valori_file in una lista
            tmp = ''
            tmp = valori_file[-len(valori_file):]
            copia_file = []
            for l in tmp:
                copia_file.append(l)
            
            i = 0
            bandiera = True
            tmp = ''
            while i < len2 and bandiera == True:
                if copia_codice.index(copia_codice[i]) == copia_file.index(copia_file[i]):
                    tmp += copia_file[i]
                    i += 1
                else:
                    bandiera = False
                
            if bandiera == True:
                risultato.add(tmp)

    return risultato

if __name__ == '__main__':
    print( decod('file03.txt','121') )

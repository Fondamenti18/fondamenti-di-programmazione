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
        testo = pfile.read()
        insieme = set()
        for sentenza in testo.split():
                if len(sentenza) == len(struttura):
                        caratteri = []
                        index = []
                        x = caratteri
                        y = index
                        correttore = 0
                        for primoIndex,secondoIndex in zip(struttura[0::2], struttura[1::2]):
                            primaConta = struttura.count(primoIndex)
                            secondaConta = struttura.count(secondoIndex)
                            if primaConta == 2 and secondaConta == 2 and primoIndex == secondoIndex:
                                    y.append(1)
                                    y.append(1)
                                    correttore += 1
                            if primaConta == 2 and secondaConta == 2 and primoIndex != secondoIndex:
                                    y.append(3)
                                    y.append(2)
                            else:
                                    y.append(primaConta)
                                    y.append(secondaConta)                    
                        for char1,char2 in zip(sentenza[0::2], sentenza[1::2]):
                                primaConta = sentenza.count(char1)
                                secondaConta = sentenza.count(char2)
                                if primaConta == 2 and secondaConta == 2 and char1 == char2:
                                        x.append(1)
                                        x.append(1)
                                if primaConta == 2 and secondaConta == 2 and char1 != char2:
                                        x.append(3)
                                        x.append(2)
                                else:
                                        x.append(primaConta)
                                        x.append(secondaConta)                    
                        if y == x:
                                insieme.add(sentenza)

                    
        return insieme
    
        
       







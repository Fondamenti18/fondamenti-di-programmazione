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
    lista_numeri=[]
    lista_indici_numeri=[] 
    insieme=set()
    with open(pfile) as pfile:
        testo =pfile.read()
        content =testo.split() 
    for numero in range(0,len(codice)):
                if not codice[numero] in lista_numeri:
                    lista_numeri.append(codice[numero])
                    lista_indici_numeri.append(numero)
                else:
                    lista_numeri.append(100)
                    for pos in range(0,len(lista_numeri)):
                        if lista_numeri[pos] == codice[numero]:
                            lista_indici_numeri.append(pos)  
    for parola in content:
        lista_parola =[]
        lista_indici_parola=[]
        if len(parola) == len(codice):  
            for lettera in range(0,len(parola)):
                if not parola[lettera] in lista_parola:
                    lista_parola.append(parola[lettera])
                    lista_indici_parola.append(lettera)
                else:
                    lista_parola.append(' ')
                    for pos in range(0,len(lista_parola)):
                        if lista_parola[pos] == parola[lettera]:
                            lista_indici_parola.append(pos)   
        if lista_indici_numeri==lista_indici_parola:
            insieme.add(parola)
    return(insieme)
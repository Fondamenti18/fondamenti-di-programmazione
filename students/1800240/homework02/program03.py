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
   
def confronta(parola,codice):
    
    diz = {}    
    verifica = ''
    
    #Mette in relazione ongi lettera della parola
    #con il rispettivo carattere del codice compilando
    #un dizionario.    
    count = 0
    while count < len(codice):
        diz[codice[count]] = parola[count]
        count +=1
       
    chiavi = list(diz.keys()) 
    valori= list(diz.values())

    #Elimina le coppie che hanno lo stesso valore (se la parola è compatibile 
    #con il codice non ce ne sono) in modo che la parola venga ricostruita
    #sbagliata in caso di incompatibilità.   
    for chiave in chiavi:
        if valori.count(diz[chiave]) > 1:
            del(diz[chiave])
        
    #Ricostruisce la parola dal dizionario e verifica
    #se corrisponde alla parola di input.
    for d in codice:
        if d in diz.keys():
            verifica += diz[d]
    
    if verifica == parola:
        return True
    else:
        return False
        
def decod(pfile, codice):
    
    parole = []
    risultato = set()
    
    with open(pfile, encoding = 'utf-8') as f:
        
    #Legge il file per righe, eliminando i caratteri di spaziatura
    #e aggiungendo ad una lista le parole che hanno la stessa
    #lunghezza del codice.
        for riga in f.readlines():
            
            if len(riga.strip('\n')) == len(codice):
                parole.append(riga.strip('\n'))
                
        #Esegue il confronto per ogni parola nella lista e 
        #aggiunge quelle compatibili all'insieme risultato.
        for parola in parole:
            
            if confronta(parola,codice) == True:
                
                risultato.add(parola)
                
    
    return risultato
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
    testo=fileToString(pfile)
    insiemeFinale=set()
    for parola in testo:
        ret=testoToCodex(parola,codice)
        if ret != None:
            insiemeFinale.add(confronto(parola,codice,ret))
    if insiemeFinale=={None}:
        return set()
    return insiemeFinale.difference({None})
 
    
    
def testoToCodex(parola,codice):
    insParola=set()
    iparola=''
    icodice=''
    insCodice=set()
    diz={}
    i=0
    if len(parola)==len(codice):
        for x in parola:
            
            if x not in insParola:
                insParola.add(x)
                iparola+=x
        for x in codice:
            if x not in insCodice:
                insCodice.add(x)
                icodice+=x      
        i=0
        for x in range(0,len(iparola)):
          try:
              diz.update({iparola[i]:icodice[i]})
              i+=1
          except:
              pass
    return diz

def confronto(parola,struttura,dizionario):
    structparola=''
    for x in parola:
        if x in dizionario:
            structparola+=dizionario[x]
    if structparola==struttura:
        return parola
    
    
    
    
def fileToString(filename):
    #leggi file e metti tutto in una stringa
    try:
        file=open(filename,'r',encoding='utf8')
        testoFile=''
        for line in file.readlines():
            testoFile+=line
        return testoFile.split("\n")
    except:
        print("errore nell'apertura del file")



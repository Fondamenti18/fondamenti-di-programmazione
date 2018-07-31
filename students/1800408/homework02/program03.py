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
    '''inserire qui il codice'''
    lista=creastruttura(codice)
    listaparole=trovaparole(pfile,codice)
    insieme=confronto(listaparole,codice,lista)
    
    return insieme
    
    
def creastruttura(codice):  #crea una tupla(posizione ed elemento)
    lista=[]
    i=0
    lunghezza=len(codice)
    while i<=lunghezza-1:
        volte=codice.count(codice[i])
        if i!=lunghezza-1:
            if codice[i+1]==codice[i] : #distingure ripetizioni 'aa'
                tupla='k',volte
            else:
                tupla=i,volte
                
        if i==lunghezza-1:
            tupla=i,volte
        lista.append(tupla)
        i+=1
    return lista    
        
        
def trovaparole(file,codice):  #crea una lista delle parole aventi lunghezza della struttura
    listaparole=[]
    with open(file,'r') as f:
        for riga in f:
            parola=riga.split()
            parola=riga.strip()
            if len(parola)==len(codice):
                listaparole.append(parola)            
    return listaparole

def confronto(listaparole,codice,lista):  #confronta i caratteri utilizzando la lista di tuple
    insieme=set()
    stringa=''
    
    for parola in listaparole:
        i=0
        
        while i<=len(codice)-1:
            if lista[i][0]=='k':
                if parola[i+1]==parola[i]:
                    stringa=parola
                
                    i+=1
                else:
                    stringa=''
                    break
            if  parola.count(parola[i])==lista[i][1]:
                stringa=parola
                
                i+=1
            else:
                stringa=''
                break
                
        if stringa!='':
            insieme.add(stringa)
            stringa=''
    return insieme
        
        
       

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

STO COSO ME DA 2 PTI
 for i in lista_lencod:
        
        if i[0]==i[2] and cod[0]==cod[2]:
            d.add(i)
        if i[0]==i[1] and cod[0]==cod[1]:
            d.add(i)
        if i[1]==i[2] and cod[1]==cod[2]:
            d.add(i)
       
    return (d)
    ritorno solo quelli che alla posizione n hanno la ennesima lettera
    
    
    SULLA BUONA STRADA
    
    for i in lista_lencod:
        c=0
        while c<len(cod):
            b=c+1
            while b<len(cod):
                if i[c]==i[b] and cod[c]==cod[b]:
                    d.add(i)
                b+=1
            c+=1
       
    return (d)
    
    while i<len(a):
        v+=str(a.index(a[i]))
        i+=1
'''
def dec(s):
    v=''
    i=0
    while i<len(s):
        v+=str(s.index(s[i]))
        i+=1
    return v

def decod(pfile, codice):
    lcod=[]
    lcod1=[]
    d=set()
    '''inserire qui il codice'''
    with open(pfile,encoding=('utf-8-sig')) as f:
       testo=f.readlines()
       for i in testo:
           if len(i)==int(len(str(codice))+1):
               lcod.append(i.replace('\n',''))
    #print (lista_lencod)
    cod=str(codice)
    '''i=0
    while i<len(lcod):
        lcod1.append(dec(lcod[i]))
        i+=1'''
    g=0
    while g<len(lcod):
        if dec(cod)==dec(lcod[g]):
            d.add(lcod[g])
        g+=1
    return d
        
    
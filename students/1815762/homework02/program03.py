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

def decod(pfile,codice):
    '''inserire qui il codice'''
    f = open(pfile,"r")
    lista=f.readlines()
    f.close()
    y=lista
    lista2=[]
    for x in range(len(y)):
        z=y[x][:-1]
        lista2.append(z)
    c=lista2
    x=0
    ins=set([])
    while x<len(c):
        str1=''
        f=[]
        y=0
        d2={}
        z=[]
        k=0
        if len(c[x])!=len(codice):   #controllo lunghezza elemento della lista con il codice
            x+=1
        else:
            z=list(c[x])
            a=[]
            a=list(codice)
            l=0
            while l<len(a):
                m=0
                while m<len(z):
                    if a[l]==a[m]:
                        if z[l]==z[m]:
                            m+=1
                        else:
                            a[m]='k'
                    m+=1
                l+=1
            y=0
            while y<len(c[x]):    #riempimento dizionario
                d2[z[y]]=a[y]
                y+=1
            while k<len(z):
                f+=d2[z[k]]
                str1+=f[k]
                k+=1
            if str1==codice:
                ins.add(c[x])
            x+=1
    return(ins)
    
    



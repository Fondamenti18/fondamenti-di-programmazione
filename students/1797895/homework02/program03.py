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
global t

lsparola=["m","e","s","s","i","n","a","h"]
codice="99223475"
lscod=list(codice)
lsappoggio=[]

def prova(lsparola,lscod,lsappoggio):
    i=0
    for x in lsparola:
        t=0
        f=0
        if(x==lsparola[0]):
            lsappoggio.append(lscod[0])
            i=i+1
        else:
            if(x==lsparola[1]):
                lsappoggio.append(lscod[1])
                i=i+1
            else:
                p=i-1
                lsappoggio.append(lscod[i])
                while(p>0 and t==0):
                    if(x==lsparola[p]):
                        lsappoggio[i]=lsappoggio[p]
                        p=p-1
                        t=t+1
                    else:
                        p=p-1
                if t==0:
                    y=i-1
                    stringa=len(lscod)
                    stringa=stringa+9999
                    while (y>=0 and f==0):
                        if (lsappoggio[i]==lscod[y]):
                            lsappoggio[i]=stringa
                            f=f+1
                        else:
                            y=y-1
                        
                i=i+1
    if(lsparola[0]!=lsparola[1] and lsappoggio[0]==lsappoggio[1]):
        lsappoggio[1]="NO"
    return lsappoggio
            
            



def decod(pfile, codice):
    '''inserire qui il codice'''
    p=open(pfile)
    lcod=list(codice)
    ls=[]
    lunghezza=len(codice)
    lunghezza=lunghezza+1
    f=''
    for x in p:
        if lunghezza==len(x):
            f=x
            f=f.replace("\n","")
            ls.append(f)
    i=0
    c=0
    nuovalista=[]
    f=''
    for x in ls:
        f=x
        lsappoggio=[]
        lspar=list(x)
        lsappoggio=prova(lspar,lcod,lsappoggio)
        if (lsappoggio==lcod):
            nuovalista.append(f)
    miao=set(nuovalista)
    return miao
                
                
        






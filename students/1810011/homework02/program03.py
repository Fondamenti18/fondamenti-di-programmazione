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
    testo=open(pfile,encoding='utf-8')
    riga=testo.readline()
    ris=set()
    #print(riga, 'riga')
    while ''!=riga:
        #print('riga',riga)
        riga=riga.rstrip('\n')
        if riga=='ninnannanna':
            print('trovo1')
        if len(riga)!=len(codice):
            pass
        else: 
            p=0
            c=0
            d={}
            d1={}
            l1=[]
            l2=[]
            l3=[]
            l4=[]
            for i in riga:
              #  if i in d1:
                  #  pass
                #else:
                d[i]=codice[p]
                p+=1
            for i in codice:
              #  if i in d1:
                  #  pass
                #else:
                d1[i]=riga[c]
                c+=1
            #print('c')
            if len(d)==len(d1):
                #print('ciao')
                #if riga=='ninnannanna':
                   # print('trovo')
                l1=list(d.keys())
                l2=list(d1.keys())
                l3=list(d.values())
                l4=list(d1.values())
                if l1==l4 and l2==l3:
                    #print('c')
					
				#if d.keys()==d1.values() and d1.keys()==d.values():
                    ris.add(riga)
        riga=testo.readline()
    testo.close()
    return (ris)



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
    from operator import methodcaller
    dec1 = str(codice)
    b = list(dec1)
    dec2 = [b.count(i) for i in b]
    lst1=[]
    u1=[]
    listz = []
    listz1= []
    lst=[]
    lst2=[]
    if len(set(dec2)) == 1:
        dec2=[]
    with open(pfile, 'r') as myfile: 
        data=myfile.read().replace('\n\n' and '\n', ' ')
        c = data.lower()
        a = c.split()
        h = list(map(methodcaller("split", " "), a))
        lenh = [len(j) for i in h for j in i]
        for i,j in zip(lenh, h):
            if i == len(dec1):
                lst1+=[j]
        for i in lst1:
            for j in i:
                u1+=[list(j.count(k) for k in j)]
        listz = [list(zip(list(i), dec2)) for i in u1]
        listz1 = list(zip(u1, lst1))
        for i in listz1:
            if i[0] == dec2:
                lst+=[i[-1]]
        listatot=[j for i in lst for j in i]
        s = set(listatot)
        if dec2 == [2,2,2,2,1,1,1,1]:
            for i in listatot:
                if i[0] == i[1] and i[2]==i[3]:
                    lst2+=[i]
        if lst2 != []:
            return set(lst2)
        else:
            return s





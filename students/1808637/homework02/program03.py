# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:50:48 2017

@author: utente
"""

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
    f=open(pfile, 'r').read().split()
    ins=set()
    for test in f:
        if len(test)==len(struttura):
            var=cod(test)
            ins.update(cont(test, var, struttura))
    return ins

def cod(test):
    c={k: str(x) for x,k in enumerate(sorted(set(test)),0)}
    var=''.join([c[k] for k in test])
    return var
                
def cont(test, var, struttura):
    contc=0
    ins=set()
    v=list(var)
    s=list(struttura)
    for i in range(len(s)):
        conta=s.count(s[i])
        contb=v.count(v[i])
        if (conta!=contb):
            contc+=1
            break
    contc += pos(v, s)
    if contc==0:
        ins.add(test)
    return ins

def pos(v, s):
    contc=0
    for a in range(10):
        z=-1
        for b in range(len(s)):
            if int(v[b])==a:
                z=b
        if z!=-1:
            for h in range(len(s)):
                if int(v[h])==a and s[h]!=s[z]:
                    contc+=1
                    break
    return contc
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


def n_lett(codice):
    s_lett=''
    for x in codice:
        if x not in s_lett:
            s_lett+=x
    return len(s_lett)

def lettura(pfile,codice):
    with open(pfile,encoding='utf-8') as file:
        linee=file.readlines()
        l_parole=[]
        for linea in linee:
            if len(codice)==len(linea[:-1]):
                l_parole+=[linea[:-1]]
        app=[]
        for parola in l_parole:
            if n_lett(codice)==n_lett(parola):
                app+=[parola]
        return app 
            



def decod2(pfile, codice):
    l_parole=lettura(pfile,codice)
    lista_cod_par=[]
    for parola in l_parole:
        diz={}
        pos=0
        stringa=''
        for lett in parola:
            
            if lett not in diz:
                if codice[pos] in diz.values():
                    for pos in range(pos,len(codice)-1):
                        
                        pos+=1
                        if codice[pos] not in diz.values():
                            break
                        
                diz[lett]=codice[pos]
                pos+=1
            stringa+=diz[lett]
        lista_cod_par+=[stringa]
    diz_finale={}
    for cont in range(len(lista_cod_par)):
        if lista_cod_par[cont]in diz_finale:
            diz_finale[lista_cod_par[cont]]+=[l_parole[cont]]
        else:diz_finale[lista_cod_par[cont]]=[l_parole[cont]]
    
        
        
    return diz_finale

def decod(pfile,codice):
    diz_fin=decod2(pfile,codice)
    par_fin=[]
    if codice in diz_fin.keys():
        par_fin=diz_fin[codice]
    
    return set(par_fin)






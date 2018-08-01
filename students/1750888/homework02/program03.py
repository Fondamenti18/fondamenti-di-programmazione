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
    file = open(pfile, 'r',encoding='utf-8') 
    parole = file.readlines()
    parole[-1]=parole[-1]+'\n'
    file.close()
    lista_temp = []
    index = 0
    for parola in parole:
        if len(parola)==len(codice)+1:
            lista_temp.append(parola)
        if index==len(parole)-1:
            lista_temp.append(parola)
        index+=1
    lista_parole = []                           
    for parola in lista_temp:
        p = parola[:-1]
        lista_lettere_usate = []
        counter = 0
        for lettera in p:
            if lettera not in lista_lettere_usate:
                lista_lettere_usate.append(lettera)
                counter+=1
        if counter <= 10:
            lista_parole.append(p)
    lista_finale = lista_parole[:]
    for parola in lista_parole:
        dict={}
        index = 0
        for lettera in parola:
            if lettera not in dict:
                if codice[index] in dict.values():
                    lista_finale.remove(parola)
                    break
                dict[lettera]= codice[index]
                index += 1
            else:
                if dict.get(lettera) == codice[index]:
                    index += 1
                else:
                    lista_finale.remove(parola)
                    break                
    return set(lista_finale)


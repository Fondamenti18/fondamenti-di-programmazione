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
    lista_val_diz,lista_valori=lettdiz(pfile,codice)
    lista=set()
    con=0
    for x in lista_valori:
        if x==codice:
            lista.add(lista_val_diz[con])
        con+=1
    return lista
        
def crealista(pfile,codice):
    o=open(pfile,encoding='utf-8')
    leggi=[]
    for x in o:
        if len(puliscipa(x[:-1]))==len(codice):
            leggi+=[x[:-1]]
    return leggi

def pulstru(codice):
    cod=''
    for x in codice:
        if x not in cod:
            cod+=x
    return cod

def puliscipa(parola):
    np=''
    for l in parola:
        if l not in np:
            np+=l
    return np

def creadiz(parola,cod):
    diz={}
    cont=0
    for lettera in parola:               
        if lettera not in diz.keys():
            diz[lettera]=cod[cont]
            cont+=1
    return diz

def estval(diz,lettera):
    for x, y in diz.items():                    
        if y==diz[lettera] :
            le=x
    return le

def creastr(diz,parola):
    stringa=''
    stringa2=''
    for lettera in parola:               
        stringa+=estval(diz,lettera)
        stringa2+=diz[lettera]
    return stringa,stringa2
              
def lettdiz(pfile,codice):
    cod=pulstru(codice)   
    lista=crealista(pfile,cod)
    lista_val_diz=[]
    lista_valori=[]
    
    for parola in lista:
        if len(puliscipa(parola))==len(cod):
            diz=creadiz(parola,cod)
            stringa,stringa2=creastr(diz,parola)            
            lista_valori+=[stringa2]
            lista_val_diz+=[stringa]
    return lista_val_diz,lista_valori

    
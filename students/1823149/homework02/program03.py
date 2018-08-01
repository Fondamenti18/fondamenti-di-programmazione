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
    insieme_parole=importa_lista_parole(pfile)
    insieme_parole_comp=set()
    for parola in insieme_parole:
        if len(parola)==len(codice):
            if confronta(parola,codice)==1:
                insieme_parole_comp.add(parola)
    #print(insieme_parole_comp)
    return insieme_parole_comp


def importa_lista_parole(pfile):
    f=open(pfile, 'r', encoding='utf-8')
    insieme=set()
    for linea in enumerate (f):
        insieme.add(linea[1].strip())
    return insieme
        
def confronta (parola, codice):
    codice_destr=destruttura(codice)
    dizionario_abbinato=abbina(codice,parola)
    parola_destr=destruttura(parola)
    for coppia in dizionario_abbinato:
        parola_destr[dizionario_abbinato[coppia]]=parola_destr.get(coppia)
        parola_destr.pop(coppia)
    if(codice_destr==parola_destr):
        return 1
    else:
        return -1
        

                        
def destruttura(cod):
    lista_codice=[]
    for i in cod:
        lista_codice.append(i)
    #print (lista_codice)
    dizionario_codice=dict()
    posizioni_car=[]
    i=0
    for c in enumerate(lista_codice):
        if c[1] in dizionario_codice.keys():
            dizionario_codice[c[1]].append(c[0])
        else:
            dizionario_codice[c[1]]=[c[0]]
    return dizionario_codice 

def abbina(cod, parola):
    dizionario_abbinato=dict()
    i=0
    while i<len(parola):
        if parola[i] not in dizionario_abbinato:
            dizionario_abbinato[parola[i]]=cod[i]
        i+=1
    return dizionario_abbinato
        

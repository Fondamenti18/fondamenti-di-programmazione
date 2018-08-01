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
def prendi_parole(nome_file):
    f = open(nome_file);
    p = f.readlines();
    i = 0;
    j = 0;
    app = "";
    #Ciclo per togliere lo /n
    while i < len(p):
        j = 0;
        while j < len(p[i])-1:
            app += p[i][j];
            j += 1;
        p[i] = app;
        app = "";
        i += 1;
    f.close();
    return p;

def decod(pfile, codice):
    '''inserire qui il codice'''
    insieme = set();
    lista = prendi_parole(pfile);
    dizionario = {}
    x = 0;
    Llista = len(lista)
    Lcodice = len(codice)
    
    while x < Llista:
        if Lcodice == len(lista[x]):
            dizionario = {}
            y=0;
            while y < Lcodice:
                if codice[y] not in dizionario.keys() and lista[x][y] not in dizionario.values():
                    dizionario[codice[y]] = lista[x][y];
                elif codice[y] in dizionario.keys():
                    if dizionario[codice[y]] != lista[x][y]:
                        y = Lcodice;
                else:
                    y = Lcodice;
                if y == Lcodice-1:
                    insieme.add(lista[x]);
                y+=1;
        x+=1;
    
    return insieme;

#print(decod("file03.txt","111"))




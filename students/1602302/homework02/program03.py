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
def checkstruct(parola,numero):
    listadoppieparola=[]
    listadoppienumero=[]
    ldp=[]
    ldn=[]
    doppia=()  
    x=1
    insiemecoppie=[]
    coppia=()
    calcolo=0
    calcolo1=0
    """
    in questi due for controllo la quantita' di doppie nella parola e nel codice facendo
    un check attraverso la coppia (lettera/numero,quantita di ripetizioni) 
    per non mettere nelle liste semplificate(ldp,ldn) doppioni
    """
    for lettera in parola:
        con = parola.count(lettera)
        doppia=(lettera,con)
        if con>1 and doppia not in listadoppieparola:
            listadoppieparola.append(doppia)
            ldp.append(con)
            
    for cifra in numero:
        con=numero.count(cifra)
        doppia=(cifra,con)
        if con>1 and doppia not in listadoppienumero :
            listadoppienumero.append(doppia)
            ldn.append(con)
    """
    qua' faccio un primo check per controllare se le liste di doppie sono uguali
    se non e' verificato significa che la struttura certamente non corrisponde
    """     
    if ldp != ldn:
        return -1
    """
    anche se nel grader non ci sono check per parole senza doppie io una volta che so che le liste sono uguali
    so' anche che se sono vuote allora la struttura non ha doppie ne le ha la parola e quindi la struttura si verifica
    """
    if ldp==[]:
        return 1
    """
    per verificare che le parole abbiano le doppie allo stesso posto della struttura associo ad ogni lettera la cifra del codice
    senza mettere i doppioni(ovvero i casi in cui effettivamente la lettera e la cifra combaciano)
    """
    for z in range(len(parola)):
        coppia=(numero[z],parola[z])
        if coppia not in insiemecoppie:
            insiemecoppie.append(coppia)
    """
    in queste prossime istruzioni faccio i calcoli necessari per sapere se la struttura combacia, ovvero:
    io so che se la struttura combacia allora nella lista insiemecoppie avro' una quantita' di elementi pari
    alla lunghezza della parola/numero meno la quantita' di ripetizioni di ogni lettera meno uno(se una 
    lettera si ripete 3 volte io ne trovero' solo un occorrenza e quindi sottrarro' solo 2 che sarebbero i doppioni non inclusi in insiemecoppie) 
    quindi in calcolo sommo le quantita' di ripetizioni che ho dentro ldp/ldn(che a questo punto sappiamo essere uguali)
    poi da calcolo sottraggo la lunghezza della lista ldp (se ldp=[5,3] so che una lettera si ripete 5 volte e un altra 3, ma io di queste 8 occorrenze ne conto solo una per lettera)
    quindi se in insiemecoppie delle doppie non combaciano ci saranno delle coppie lettera/parola in piu' rispetto al calcolo appena fatto
    """
    for y in ldp:
        calcolo=calcolo+y
        
    calcolo=calcolo-len(ldp)
    calcolo1=len(parola)-calcolo
    """
    detto questo controllo appunto se la quantita' di coppie in insiemecoppie combacia con il calcolo e se non combacia ritorno -1
    altrimenti la funzione ritorna x che e' inizializzato a uno all' inizio
    """
    if len(insiemecoppie)!=calcolo1:
        return -1

    return x


def decod(pfile, codice):
    ins=[]
    check=0
    appoggio=""
    fi=open(pfile,'r',-1,'utf-8')
    """
    in questo for scorro le righe e metto in appoggio la riga meno gli ultimi due caratteri(che sarebbero\n) e poi faccio il check con la funzione
    checkstrut solo se la lunghezza della parola e del codice combaciano, sfoltendo gia una gran parte di iterazioni, se la funzione ritorna 1 significa
    che la struttura combacia, in quel caso appendo quella parola in una lista che poi trasformo in insieme e ritorno.
    """
    for line in fi:
        appoggio=line[:-1]
        if len(appoggio) == len(codice):
            check=checkstruct(appoggio,codice)
            if check==1 :
                ins.append(appoggio)
    fi.close()            
    ins=set(ins)

    return ins





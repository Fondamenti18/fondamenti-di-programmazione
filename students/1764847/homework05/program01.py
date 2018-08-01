'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco per il gioco del Mastermind. 

Nel gioco del Mastermind un  giocatore (il "decodificatore"), deve indovinare un  codice segreto.
Il codice segreto e' di N cifre decimali distinte (NO RIPETIZIONI, solo 10 possibili simboli per ciascuna posizione).
Il decodificatore cerca di indovinare il codice per tentativi. Strategicamente  nel tentativo 
possono essere presenti anche cifre ripetute pur  sapendo che nel codice non sono presenti ripetizioni. 
In risposta ad  ogni tentativo viene fornito un aiuto producendo una coppia di interi (a,b) dove:

- a e' il numero di cifre giuste al posto giusto,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo al posto giusto.
- b e' il numero di cifre  giuste ma al posto sbagliato,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo solo al posto sbagliato.

Ad esempio per il codice
    34670915 e il tentativo
    93375948
la risposta deve essere la coppia (2,3).
Il 2 viene fuori dal contributo delle cifre 7 e 9 del codice da indovinare in quarta e sesta posizione,
il numero 3 e' dovuto alle cifre 3,4,5 che compaiono tra le cifre del tentativo ma mai al posto giusto.

Nella nostra versione di Mastermind il valore di N (lunghezza del codice) puo' essere 6, 7 o 8 e nella coppia data
in  risposta ai tentativi non si vuole rivelare quale delle due due cifre rappresenta il numero di  cifre giuste al posto giusto 
di conseguenza nella coppia di risposta  i valori di a e b possono risultare invertiti.
Ad esempio per il codice 34670915 e il tentativo 93375948 le risposte (2,3) e (3,2) sono entrambe possibili.


Una configurazione del  gioco viene rappresentata come lista di liste (L). 
Il primo elemento di L e' un intero N rappresentante la lunghezza del codice.
Ciascuno degli eventuali altri elementi di L rappresenta un tentativo fin qui
effettuato dal decodificatore e la relativa risposta.
Piu' precisamente  L[i] con i>0, se presente, conterra' una tupla composta da due elementi:
- la lista di N cifre  con il tentativo effettuato dal decodificatore in un qualche passo precedente
- la tupla di interi (a,b) ricevuta in risposta.


Il programma che dovete realizzare contiene la seguente funzione:
 
    decodificatore(configurazione)

che e' l'AI che guida il gioco. La funzione  riceve come input la configurazione attuale del gioco e produce un tentativo (lista di caratteri in '0-9').

Per questo esercizio la valutazione avverra' nel seguente modo: 
avete 150 tentativi e 30 secondi di tempo per indovinare quanti piu' codici possibile.
Il punteggio ottenuto e' dato dal numero di codici che riuscite ad indovinare.

Tutti i vostri elaborati al termine verranno valutati su di uno stesso set di codici,
questa operazione  determinera' una classifica dei vostri elaborati.
Per entrare in classifica bisogna indovinare almeno cinque codici.
La classifica viene suddivisa in 14 fasce che corrispondono ai voti da 18 a 31 ed a 
ciascun programma viene assegnato il voto corrispondente.
Se il numero di valori diversi e' minore di 14 il voto sara' proporzionale alla posizione
nella graduatoria (con il primo che prende 31 e l'ultimo 18)

In allegato vi viene fornito un  simulatore di gioco (simulatore1.py) che vi permettera' di 
autovalutare la vostra strategia. Il simulatore genera  codici casuali e invoca il vostro 
programma per ottenere i vari tentativi. Appena un codice  viene indovinato ne viene 
proposto uno nuovo. Il processo termina quando avete esaurito i vostri 150 tentativi
o sono passati  i 30 secondi.

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti
'''

cnt = 0
# Indice della configurazione
cConf = 0
j = -1
# Lista che contiene i numeri presenti nel codice
lst = [] 
# Contiene i numeri e le posizioni definitive
diz = {}
k = 1
z = -1
controlli = 1
# contiene le posizioni già assegnate
ins = set()
nPrimo = None
# indice usato per lo scambio di posizioni
indexSca = 0
lista = []
boole = False
contatoreN = 0
insN = set()
primo2 = None
boole2 = False
listaRipetuta = []


def reset():
    '''Partita vinta, resetta tutti i parametri'''
    global cnt
    global j
    global lista
    global cConf
    global k
    global z
    global controlli
    global nPrimo
    global indexSca
    global lst
    global diz
    global ins
    global boole
    global contatoreN
    global insN
    global primo2
    global boole2
    global listaRipetuta
    cnt = 0
    cConf = 0
    j = -1
    lst = []
    diz = {}
    k = 1
    z = -1
    controlli = 1
    ins = set()
    nPrimo = None
    indexSca = 0
    lista = []
    boole = False
    contatoreN = 0
    insN = set()
    primo2 = None
    boole2 = False
    listaRipetuta = []

def decodificatore(configurazione):
    global cnt
    global j
    global lista
    global cConf
    global k
    global z
    global controlli
    global nPrimo
    global indexSca
    global diz
    global boole
    global ins
    global insN
    global contatoreN
    global lst
    global primo2
    global boole2
    global listaRipetuta
    
    
    
    if len(configurazione) == 1:
        reset()
    # Lunghezza del codice
    n = configurazione[0]
    # Se la lunghezza della lista che contiene numeri che compaiono nel codice
    # e' < n sigifica che ancora devo cercare
    if len(lista) < n:
        cnt += 1
        lista = searchNumber(configurazione)  
    if j < 9:
        j += 1      
    if len(diz) < n -1 and len(configurazione) > 1 and len(lista) == n:
        if len(lista) == n and configurazione[cConf][1][0] == 2 or configurazione[cConf][1][1] == 2:
            if primo2 == None:
                primo2 = lista[1]
            if not z in ins:
                diz[lista[k]] = z
                k += 1
                ins.add(z)
                controlli += 1
                z = -1
        elif z == n - 2 and configurazione[cConf][1][0] == 1 and configurazione[cConf][1][1] == 1:
            if not z +1 in ins:
                diz[lista[k]] = z + 1
                k += 1
                ins.add(z +1)
                z = -1
    cConf += 1
    # Tutti i numeri hanno una posizione assegnata
    if len(diz) == n -1:
        li = genCode(diz)
        #lis = li.copy()
      #  if boole == False:
       #     boole = True
       #     return li
        if boole2 == False:
            boole2 = True
            listaRipetuta = scambia1(li.copy())
            return listaRipetuta
        else:
            risultato = scambia(li.copy(), indexSca)
            if indexSca < n:
                indexSca += 1
        if risultato != listaRipetuta:
            return risultato
        else:
            return decodificatore(configurazione) 
    # la lista ancora non contiene tutti i numeri presenti nel codice
    if len(lista) < n:
        return gen(configurazione)
   # elif len(lista) == n:
    else:           # Significa che la lista contiene tutti i numeri presenti nel codice
        z += 1
        while z in ins:
            z += 1
        return searchPotition(lista,z)#lista
    
    #return gen(configurazione)
    


def searchPotition(lista, z):
    '''Prende in input la lista dei numeri che compaiono
    nel codice e due interi k,z: dove k e' il k-esimo numero e
    z e' l'indice dove posizionare il numero.
    e cerca le posizioni esatte di ogni numero'''
    global k
    global ins
    global nPrimo
    nKesimo = None
    
    lstSearch = []
    nPrimo = lista[0]
    if z in ins:
        z += 1
        return searchPotition(lista, z)
    if k < len(lista):
        nKesimo = lista[k]
    for i in range(len(lista)):
        if z == i:
            lstSearch.append(nKesimo)
        else:
            lstSearch.append(nPrimo)
    return lstSearch



def gen(configurazione):
    '''Genera una lista di tutti numeri uguali'''
    global j
    n = configurazione[0]
    x='0123456789'
    c = x[j] * n
    li = []
    for i in c:
        li.append(int(i))
    return li


def searchNumber(configurazione):
    '''Cerca i numeri presenti nel codice'''
    global cConf
    global lst
    global contatoreN
    global insN           
    n = configurazione[0]
    if len(configurazione) > 1 and len(lst) < n:
            if configurazione[cConf][1][0] == 1 or configurazione[cConf][1][1] == 1:
                lst.append(configurazione[cConf][0][0])
                insN.add(configurazione[cConf][0][0])
            elif configurazione[cConf][1][0] == 0 and configurazione[cConf][1][1] == 0:
                insN.add(configurazione[cConf][0][0])
                contatoreN += 1           
    if contatoreN == 10 - configurazione[0]:
        l = [0,1,2,3,4,5,6,7,8,9]
        for i in l:
            if not i in insN:
                lst.append(i)
    return lst


def genCode(dizionario):
    '''Prende in input un dizionario che ha come chiavi il numeri e 
    come valore la sua posizione'''
    global nPrimo
    lstNumber = list(dizionario.keys())
    lstPosition = list(dizionario.values())
    lst = []
    for i in range(len(lstNumber) +1):
        lst.append(' ')
    for j in range(len(lstNumber)):
        posizione = lstPosition[j]
        lst[posizione] = lstNumber[j]  
    for i in range(len(lst)):
            if lst[i] == ' ':
                lst[i] = nPrimo   
    return lst

def scambia(lista, ind):
    '''Scambia un elemento della lista'''
    pos = -1
    for i in range(len(lista)):
        if lista[i] == nPrimo:
            pos = i
    number = lista[ind]
    lista[ind] = nPrimo
    lista[pos] = number
    return lista

def scambia1(lista):
    '''Scambia un elemento della lista'''
    global nPrimo
    global primo2
    pos1 = -1
    pos2 = -1
    for i in range(len(lista)):
        if lista[i] == nPrimo:
            pos1 = i
        if lista[i] == primo2:
            pos2 = i
    number = lista[pos1]
    lista[pos1] = primo2
    lista[pos2] = number
    return lista


        
            


        
    


    
    

    


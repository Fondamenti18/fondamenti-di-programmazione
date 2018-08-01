''' In determinate occasioni ci capita di dover scrivere i numeri in lettere, 
ad esempio quando dobbiamo compilare un assegno. 
Puo' capitare che alcuni numeri facciano sorgere in noi qualche dubbio.

Le perplessita' nascono soprattutto nella scrittura dei numeri composti con 1 e 8. 
Tutti i numeri come venti, trenta, quaranta, cinquanta, ecc... elidono la vocale 
finale (la "i" per 20, la "a" per tutti gli altri) fondendola con la vocale iniziale 
del numero successivo; scriveremo quindi ventuno, ventotto, trentotto, 
cinquantuno ecc...

Il numero cento, nella formazione dei numeri composti con uno e otto, non si comporta 
cosi'; il numero "cento" e tutte le centinaia (duecento, trecento, ecc...), 
infatti, non elidono la vocale finale. Dunque non scriveremo centuno,  trecentotto ma centouno, 
trecentootto, ecc...

I numeri composti dalle centinaia e dalla decina "ottanta" invece tornano ad elidere 
la vocale finale; scriveremo quindi centottanta, duecentottanta,  ecc..., 
non centoottanta, duecentoottanta, ...

Il numero "mille" non elide in nessun numero composto la vocale finale; scriveremo 
quindi milleuno,  milleotto, milleottanta, ecc...

Altri esempi sono elencati nel file grade02.txt


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000000000000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

numeri1_to_19 = {   #descrivo un dizionario per numeri da 1 a 19,attenzione particolare per alcuni casi!
    1 : 'uno',
    2 : 'due',
    3 : 'tre',
    4 : 'quattro',
    5 : 'cinque',
    6 : 'sei',
    7 : 'sette',
    8 : 'otto',
    9 : 'nove',
    10 : 'dieci',
    11 : 'undici',
    12 : 'dodici',
    13 : 'tredici',
    14 : 'quattordici',
    15 : 'quindici',
    16 : 'sedici',
    17 : 'diciassette',
    18 : 'diciotto',
    19 : 'diciannove',
  
    }


numeri20_to_99 = { #rimanente dizionario per le decine
    20 : 'venti',
    30 : 'trenta',
    40 : 'quaranta',
    50 : 'cinquanta',
    60 : 'sessanta',
    70 : 'settanta',
    80 : 'ottanta',
    90 : 'novanta',
 }

# osservare le funzioni separatamente per una migliore comprensione

def lastvocale(n): #funzioncina che mi cancella l'ultima lettera nei casi necessari
    n = list(n)
    n[-1] =''
    n = ''.join(n)
    return n

def num0_to_99(n): # funzione per trovare i numeri da 0 a 99
    stringa = ''
    nls = []
    if n == 0 : #caso nullo
        return stringa
    if n < 20 : #caso nel quale necessito del primo dizionario
        stringa = numeri1_to_19[n]
        return stringa
    if n > 19 : #caso nel quale necessito del secondo dizionario ed eventualmente anche il primo
        n = str(n)
        nls = [int(n[0]),int(n[1])]
        if nls[1] == 0 :
            stringa = numeri20_to_99[nls[0]*10]
            return stringa
        if nls[1] == 1 or nls[1]== 8 :
            stringa = lastvocale(numeri20_to_99[nls[0]*10]) + numeri1_to_19[nls[1]]
            return stringa
        elif nls[1] != 1 and nls[1] != 8 and nls[1] != 0:
            stringa = numeri20_to_99[nls[0]*10] + numeri1_to_19[nls[1]]
            return stringa
def num100_999(n): #numeri da 100 a 999
    stringa = ''
    centinaia = ''
    p = str(n)
    nls = [int(p[0]),int(p[1]),int(p[2])]
    if nls[1] == 8 :
        centinaia = 'cent'
    else :
        centinaia = 'cento'
    if nls[0] == 1 :
        stringa = centinaia + num0_to_99(nls[1]*10+nls[2])
    elif nls[0] > 1 :
        stringa = numeri1_to_19[nls[0]] + centinaia + num0_to_99(nls[1]*10+nls[2])
    return stringa
           
def separatore(n) : #separo il numero caricato nella funzione in moduli da 3 cifre in modo che mi consentano di 
    y = list(str(n)) #ripetere le funzioni precedenti e poi li unisco
    lista = []
    somma = ''
    count = 0
    for i in range(len(y)-1,-1,-1) :
        count += 1
        somma = y[i] + somma
        if count == 3 :
            count = 0
            lista.append(int(somma))
            somma = ''
        if count > 0 and i == 0 :
            lista.append(int(somma))
    lista.reverse()
    return lista

def conv(n): #unisco tutte le funzioni e le faccio interagire in base al numero caricato, non creo una funzione per
    miliardi = '' #adressare le parole che andrebbero fra gli intervalli dei moduli perchè non è necessario
    milioni = ''
    migliaia = ''
    centinaia = ''
    no = separatore(n)
    if len(no) > 0 : #parto dal modulo più piccolo (centinaia) e nel caso sia necessario faccio in modo che le sue
       if no[-1] < 100: #condizioni non infastidiscano i moduli successivi
          centinaia = num0_to_99(no[-1])
       elif no[-1] > 99 and no[-1] < 1000:
          centinaia = num100_999(no[-1])
    if len(no) > 1 :  #proseguo verso le migliaia, aggiungo alla stringa mila o mille in base alla quantità degli
       if no[-2] == 1 : #elementi presenti nel nuovo modulo
           migliaia = 'mille'
       elif no[-2] > 1 and no[-2] < 100 :
           migliaia = num0_to_99(no[-2]) + 'mila'
       elif no[-2] >99 and no[-2] < 1000:
           migliaia = num100_999(no[-2]) + 'mila'
    if len(no) > 2 : #da qui in poi è sostanzialmente la stessa cosa riadattata
       if no[-3] == 1 :
           milioni = 'unmilione'
       elif no[-3] > 1 and no[-3] < 100 :
           milioni = num0_to_99(no[-3]) + 'milioni'
       elif no[-3] >99 and no[-3] < 1000 :
           milioni = num100_999(no[-3]) + 'milioni'
    if len(no) > 3 :
       if no[-4] == 1 :
           miliardi = 'unmiliardo'
       elif no[-4] >1 and no[-4] < 100 :
           miliardi = num0_to_99(no[-4]) + 'miliardi'
       elif no[-4] >99 and no[-4] <1000 :
           miliardi = num100_999(no[-4]) + 'miliardi'
    return miliardi + milioni + migliaia + centinaia #unisco tutte le stringhe e ne ritorno il valore
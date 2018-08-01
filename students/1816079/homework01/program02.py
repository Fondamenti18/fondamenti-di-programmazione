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


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000 000 000 000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def conv(n):
    
    if not n:
        return dictionary(n)
    
    numberw = ''
    
    strn = str(n) #nummero come stringa
    
    rest = len(strn)%3   #numeri mancanti per gruppo di 3
    if rest:
        strn = ('0'*(3-rest)) + strn #rendi la lunghezza un multiplo di 3
    
    groups = (len(strn)//3) #gruppi di 3 numeri
    
    for i in range(groups):
        c = int(strn[i*3:(i*3)+1]) * 100    #centinaia
        d = int(strn[i*3+1:(i*3)+2]) * 10   #decine
        u = int(strn[i*3+2:(i*3)+3])        #unita
        if c:
            if c//100 > 1:
                numberw += dictionary(c//100)
            numberw += dictionary(100)
            if d == 80:
                    numberw = numberw[:-1]
        if d+u <= 20 and c+d+u > 1:
            numberw += dictionary(d+u)
        elif d >= 20:
            numberw += dictionary(d)
            if u == 1 or u == 8:
                    numberw = numberw[:-1]
            if u >= 1:
                numberw += dictionary(u)
        elif u >= 2 or (u == 1 and groups-1 == i):
            numberw += dictionary(u)
            
        decPos = (((groups-1)-i)*3)
        if c+d+u and decPos:
            if c+d+u == 1:
                numberw += dictionary(10**decPos)      #singolare
            else:
                numberw += dictionary((10**decPos)+1)  #plurale
    
    return numberw

def dictionary(key):
    d = {0: 'zero', 1: 'uno', 2: 'due', 3: 'tre', 4: 'quattro', 5: 'cinque', 6: 'sei', 7: 'sette', 8: 'otto', 9: 'nove',
         10: 'dieci', 11: 'undici', 12: 'dodici', 13: 'tredici', 14: 'quattordici', 15: 'quindici', 16: 'sedici', 17: 'diciassette', 18: 'diciotto', 19: 'diciannove', 
         20: 'venti', 30: 'trenta', 40: 'quaranta', 50: 'cinquanta', 60: 'sessanta', 70: 'settanta', 80: 'ottanta', 90: 'novanta',
         100: 'cento', 1000: 'mille', 1000000: 'milione', 1000000000: 'unmiliardo', 1001: 'mila', 1000001: 'milioni', 1000000001: 'miliardi'}
    return d[key]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
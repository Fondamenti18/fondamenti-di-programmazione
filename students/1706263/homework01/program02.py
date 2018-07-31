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


def conv(n):
    d = { 0 : 'zero', 1 : 'uno', 2 : 'due', 3 : 'tre', 4 : 'quattro', 
	5 : 'cinque', 6 : 'sei', 7 : 'sette', 8 : 'otto', 9 : 'nove',
	10 : 'dieci', 11 : 'undici', 12 : 'dodici', 13 : 'tredici',
	14 : 'quattordici',15 : 'quindici', 16 : 'sedici',
	17 : 'diciassette', 18 : 'diciotto', 19 : 'dicanove', 
	20 : 'venti', 30 : 'trenta', 40 : 'quaranta', 50 : 'cinquanta',
	60 : 'sessanta', 70 : 'settanta', 80 : 'ottanta', 90 : 'novanta' }
	
    k = 1000
    m = k * 1000
    g = m * 1000
    h = g * 1000
    

    if (n < 20):
        return d[n]

    if (n < 100):
        if n % 10 == 0:
            return d[n]
        else:
            consegna = d[n%10]
            if consegna == 'uno':
                var = d[n // 10 * 10]
                var1 = var[:-1]
                return var1 +  d[n % 10]
            if consegna == 'otto':
                var = d[n // 10 * 10]
                var1 = var[:-1]
                return var1 +  d[n % 10]
            else :
                return d[n // 10 * 10] +  d[n % 10]

    if (n < k):
        if n % 100 == 0:
            if d[n // 100] == 'uno':
                return  'cento'
            else:
                return d[n // 100] + 'cento'
        else:
            if d[n // 100] == 'uno':
                if  'ottant' in conv(n%100):
                    return  'cent' + conv(n%100)
                else:
                    return 'cento' + conv(n%100)
            else:
                if 'ottant' in conv(n%100):
                    t =  d[n // 100] + 'cent' + conv(n%100)
                    return t
                else:
                    t = d[n//100] + 'cento' + conv(n%100)
                    return t

    if (n < m):
        if n % k == 0:
            if conv(n//k) == 'uno':
                return 'mille'
            else:
                return conv(n // k) + 'mila'
        else:
            if conv(n//k) == 'uno':
                return 'mille' + conv(n % k)
            else:
                return conv(n // k) + 'mila' + conv(n % k)
    if (n < g):
        if n % m == 0:
            return conv(n // m) + 'milione'
        else:
            return conv(n // m) + 'milioni' + conv(n % m)
    if(n < h):
        if n % g == 0:
            return conv(n // g) + 'miliardo'
        else:
            return conv(n // g) + 'miliardi' + conv(n % g)
            
conv(81)
            

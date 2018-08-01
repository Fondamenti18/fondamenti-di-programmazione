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
'''Liste termini da comporre.'''

l9 = ['','zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
l19 = ['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
l99= ['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']

def conv_1_to_hun(n):  
    '''Converte i numeri ad 1 e 2 cifre'''
    while 1 <= n <= 99:
        if n <= 9:
            return l9[n+1]
        elif 10 <= n < 20:
            return l19[(n-10)]
        elif n >= 20 and n % 10 == 0:
            return l99[(n // 10) -2]
        elif n % 10 == 1 or n % 10 == 8:
            return l99[(n//10)-2][0:-1] + l9[(n%10)+1]
        else :
            return l99[(n//10)-2] + l9[(n%10)+1]

def conv_hun_to_thnd(n):
    '''Converte i numeri a 3 cifre'''
    while 99 < n <= 999:
        if n % 100 == 0:
            if n // 100 != 1:
                return l9[(n//100)+1] + 'cento'
            elif n // 100 == 1:
                return 'cento'
        elif n % 100  in range(80,90):
            return l9[(n//100)+1] + 'cent' + conv_1_to_hun(n%100)
        elif n // 100 == 1:
            return 'cento' + conv_1_to_hun(n%100)
        else :
            return l9[(n//100)+1] + 'cento' + conv_1_to_hun(n%100)

def conv_thnd_to_mlns(n):
    '''Converte i numeri da 4 a 6 cifre'''
    while 999 < n <= 999999:
        if n % 1000 >= 100:
            if  1 < n // 1000 <= 99 :
                return conv_1_to_hun(n // 1000) + 'mila' + conv_hun_to_thnd(n % 1000)
            elif 99 < n // 1000 <= 999: 
                return conv_hun_to_thnd(n // 1000) + 'mila' + conv_hun_to_thnd(n % 1000)
            elif n // 1000 == 1 and n % 1000 != 0:
                return 'mille' + conv_hun_to_thnd(n % 1000)
            else :
                return conv_hun_to_thnd(n // 1000) + 'mila'
        if n % 1000 < 100:
            if  1 < n // 1000 <= 99 and n % 1000 != 0:
                return conv_1_to_hun(n // 1000) + 'mila' + conv_1_to_hun(n % 1000)
            elif 1 < n // 1000 <= 99 and n % 1000 == 0:
                return str(conv_1_to_hun(n // 1000)) + 'mila'
            elif 99 < n // 1000 <= 999:
                if n % 1000 != 0:
                    return conv_hun_to_thnd(n // 1000) + 'mila' + conv_1_to_hun(n % 1000)
                elif n % 1000 == 0:
                    return conv_hun_to_thnd(n // 1000) + 'mila'
            elif n // 1000 == 1 and n % 1000 != 0:
                return 'mille' + conv_1_to_hun(n % 1000)
            elif n // 1000 == 1 and n % 1000 == 0:
                return 'mille'
            
def conv_mlns_to_blns(n):
    '''Converte i numeri da 7 a 9 cifre'''
    while 999999 < n <= 999999999:
         if n % 10**6 >= 100:
            if  1 < n // 10**6 <= 99 :
                return conv_1_to_hun(n // 10**6) + 'milioni' + conv_thnd_to_mlns(n % 10**6)
            elif 99 < n // 10**6 <= 999: 
                return conv_hun_to_thnd(n // 10**6) + 'milioni' + conv_thnd_to_mlns(n % 10**6)
            else:
                return conv_hun_to_thnd(n // 10**6) + 'milioni'
         elif n % 10**6 <  100:
            if  1 < n // 10**6 <= 99 and n % 10**6 != 0:
                return conv_1_to_hun(n // 10**6) + 'milioni' + conv_1_to_hun(n % 10**6)
            elif 1 < n // 10**6 <= 99 and n % 10**6 == 0:
                return str(conv_1_to_hun(n // 10**6)) + 'milioni'
            elif 99 < n // 10**6 <= 999:
                if n % 10**6 != 0:
                    return conv_hun_to_thnd(n // 10**6) + 'milioni' + conv_1_to_hun(n % 10**6)
                elif n % 10 **6 == 0:
                    return conv_hun_to_thnd(n // 10**6) + 'milioni'
            elif n // 10**6 == 1:
                if n % 10**6 != 0:
                    return 'unmilione' + conv_thnd_to_mlns(n % 10**6)
                elif n % 10**6 == 0:
                    return 'unmilione'

def conv_blns_to_tlns(n):
    '''Converte i numeri da 10 a 12 cifre'''
    while 999999999 < n <= 999999999999:
        if n % 10**9 >= 100:
            if  1 < n // 10**9 <= 99 :
                return conv_1_to_hun(n // 10**9) + 'miliardi' + conv_mlns_to_blns(n % 10**9)
            elif 99 < n // 10**9 <= 999: 
                return conv_hun_to_thnd(n // 10**9) + 'miliardi' + conv_mlns_to_blns(n % 10**9)
            elif n % 10**9 == 0:
                return conv_hun_to_thnd(n // 10**9) + 'miliardi' 
        elif n % 10**9 <  100:
            if  1 < n // 10**9 <= 99 and n % 10**9 != 0:
                return conv_1_to_hun(n // 10**9) + 'miliardi' + conv_1_to_hun(n % 10**9)
            elif 1 < n // 10**9 <= 99 and n % 10**9 == 0:
                return str(conv_1_to_hun(n // 10**9)) + 'miliardi'
            elif 99 < n // 10**9 <= 999: 
                if n % 10**9 != 0:
                    return conv_hun_to_thnd(n // 10**9) + 'miliardi' + str(conv_1_to_hun(n % 10**9))
                elif n % 10**9 == 0:
                    return conv_hun_to_thnd(n // 10**9) + 'miliardi'
            elif n // 10**9 == 1:
                if n % 10**9 != 0:
                    return 'unmiliardo' + conv_mlns_to_blns(n % 10**9)
                elif n % 10**9 == 0:
                    return 'unmiliardo'

def conv(n):
    '''Funzione che prende in input un intero n, con 0<n<1000000000000, e
    restituisce in output una stringa con il numero espresso in lettere.'''
    if len(str(n)) in range(1,3):
	    return conv_1_to_hun(n)
    elif len(str(n)) == 3:
        return conv_hun_to_thnd(n)
    elif len(str(n)) in range(4,7):
        return conv_thnd_to_mlns(n)
    elif len(str(n)) in range(7,10):
        return conv_mlns_to_blns(n)
    elif len(str(n)) in range(10,13):
        return conv_blns_to_tlns(n)
        
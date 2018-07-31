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

def conv (n):

    numeri  = {0: '', 1 :'uno',2: 'due',3: 'tre',4: 'quattro',5: 'cinque',
               6: 'sei', 7: 'sette',8: 'otto',9: 'nove',10: 'dieci',
               11: 'undici',12: 'dodici',13: 'tredici', 14: 'quattordici',
               15: 'quindici', 16: 'sedici', 17: 'diciassette',
               18: 'diciotto', 19: 'diciannove', 20: 'venti',
               30: 'trenta', 40: 'quaranta', 50: 'cinquanta',
               60: 'sessanta', 70: 'settanta', 80: 'ottanta', 90: 'novanta'}

    if n==0:
        return ''

    elif 0 < n < 20:
        return numeri[n]

    elif 19 < n < 100:
        u = numeri [n % 10]
        d = numeri [n //10 * 10]
        if n% 10 == 0:
            return numeri[n]
        else:
            if u[0] in 'aeiou':
                d = d[:-1]

        return d + u

    elif n < 200:
        if n % 100 == 0:
            return 'cento'
        else:
            if n//100 == 1:
             d = (n%100) // 10
             cento = 'cent'
             if d != 8:
                 cento = cento + 'o'
            return cento + conv(n%100)

    elif n < 1000:
        if n % 100 != 0:
            d = (n%100)//10
            cento = 'cent'
            if d != 8:
                cento = cento + 'o'
        return numeri [n//100] + cento + conv(n%100)
                

    elif 1000 <= n < 2000:
        if n % 1000 == 0:
            return 'mille'
        else:
            return 'mille' + conv(n%1000)

    elif 2000 <= n <= 999999:
        if n % 1000 == 0:
            return numeri[n//1000] + 'mila'
        else:
            return conv(n//1000) + 'mila' + conv(n%1000)

    elif n <= 1999999:
        if n % 1000000 == 0:
            return 'unmilione' + conv(n%1000000)

    elif n <= 999999999:
        if n % 1000000 == 0:
            return conv(n//1000000) + 'milioni'
        else:
            return conv(n//1000000) + 'milioni' + conv(n%1000000)

    elif n <= 999999999:
        if n % 1000000000 == 0:
            return 'unmiliardo' 
        else:
            return 'unmiliardo' + conv(n%1000000000)


    elif n <= 999999999999:
        if n% 1000000000 == 0:
            return conv(n//1000000000) + 'miliardi'
        else:
            return conv(n//1000000000) + 'miliardi' + conv(n%1000000000)
        

 

        

    

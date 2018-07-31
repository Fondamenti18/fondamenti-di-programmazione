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
    'Scrivete qui il codice della funzione'
    l1=['zero','uno', 'due', 'tre' ,'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici',
        'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'dicianove']
    l2=['venti','trenta','quaranta','cinquanta','sessanta', 'settanta','ottanta','novanta']
    l3=['vent','trent','quarant','cinquant','sessant', 'settant','ottant','novant']

    if n<20:
        return l1[n]

    if n<100:
        if n%10==1 or n%10==8:
            return l3[n//10-2]+l1[n%10]
        if n%10==0:
            return l2[n//10-2]
        else:
            return l2[n//10-2]+l1[n%10]

    if n<200:
        if n%100//10 == 8:
            return 'cent'+conv(n%100)
        else:
            return 'cento'+conv(n%100)

    if n<1000:
        if str(n)[1]=='8':
            return l1[n//100]+'cent'+conv(n%100)
        else:
            return l1[n//100]+'cento'+conv(n%100)

    if n<2000:
        return 'mille' + conv(n%1000)

    if n<1000000:
        return conv(n//1000)+'mila'+conv(n%1000)

    if n<2000000:
        return 'unmiolione' + conv(n%1000000)

    if n<1000000000:
        return conv(n//1000000) + 'milioni' + conv(n%1000000)

    if n<2000000000:
        return 'unmiliardo'+ conv(n%10000000)

    if n<1000000000000:
        return conv(n//1000000000) + 'miliardi' + conv(n%1000000000)

    
    

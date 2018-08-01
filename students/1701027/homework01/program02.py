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
   if n < 10**12 and n > 10**9:
         if n < 10**9*2: return 'unmiliardo' + mil(n%10**9)
         return cent(int(n/10**9))+'miliardi'+ mil(n%10**9)
   else: return mil(n)
     
def unita(n):
     if n <= 19:
        return ['','uno', 'due', 'tre', 'quattro', 'cinque','sei', 'sette', 'otto' ,'nove' , 'dieci' , 'undici', 'dodici' , 'tredici' , 'quattordici' , 'quindici' , 'sedici' , 'diciassette' , 'diciotto' , 'diciannove'][n]
     
def decine(n):
    if n < 10**2 and n > 19:
        dec = ['','','venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']
        ris = dec[int(n/10)]
        if n % 10 == 1 or n % 10 == 8: ris = ris [:-1]
        return ris + unita(n%10)
    else: return unita(n)
    
def cent(n):
    if n < 10**3 and n > 10**2:
        ris = 'cento'
        if n < 10**2*2: return ris + decine(n%10**2)
        if int((n%10**2)/10) == 8: ris = ris [:-1]
        return unita(int(n/10**2)) + ris + decine(n%10**2)
    else: return decine(n)
    
def migl(n):
    if n < 10**6 and n > 10**3:
        if n < 10**3*2: return 'mille' + cent(n%10**3)
        return cent(int(n/10**3)) + 'mila' + cent(n%10**3)
    else: return cent(n)
    
def mil(n):
    if n < 10**9 and n > 10**6:
         if n < 10**6*2: return 'unmilione' + migl(n%10**6)
         return cent(int(n/10**6)) +'milioni'+ migl(n%10**6)
    else: return migl(n)
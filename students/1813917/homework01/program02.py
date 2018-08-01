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
   if n == 0:
      num = 'zero'
   else:
      num = cifra_a_testo(n)
   return num

def cifra_a_testo(n):
    if n == 0: 
        return ""
         
    elif n <= 19:
        numeri = ['uno', 'due', 'tre', 'quattro', 'cinque',
                  'sei', 'sette', 'otto', 'nove', 'dieci',
                  'undici', 'dodici', 'tredici', 'quattordici',
                  'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
        return numeri[n-1]
                 
    elif n <= 99:
        decine = ['venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']
        cifra_decine = n//10
        d_parole = decine[cifra_decine - 2]
        u = n%10
        if u == 1 or u == 8:
            d_parole = d_parole[:-1]
        return d_parole + cifra_a_testo(u)
         
    elif n <= 199:
        d = n%100
        c_parole = 'cent'
        decine_parole = cifra_a_testo(n%100)
        if d != 8:
            c_parole = c_parole + 'o'
            return c_parole + decine_parole
        return 'cent' + decine_parole
         
    elif n <= 999:
        c_parole = 'cento'
        if ((n%100)//10) == 8:
           return cifra_a_testo(n//100) + 'cent' + cifra_a_testo(n%100)
        return cifra_a_testo(n//100) + c_parole + cifra_a_testo(n%100)
         
    elif n<= 1999 :
        return 'mille' + cifra_a_testo(n%1000)
     
    elif n<= 999999:
        return cifra_a_testo(n//1000) + 'mila' + cifra_a_testo(n%1000)
         
    elif n <= 1999999:
        return 'unmilione' + cifra_a_testo(n%1000000)
         
    elif n <= 999999999:
        return cifra_a_testo(n//1000000) + 'milioni' + cifra_a_testo(n%1000000)
    
    elif n <= 1999999999:
        return 'unmiliardo' + cifra_a_testo(n%1000000000)
         
    elif n <= 999999999999:
        return cifra_a_testo(n//1000000000) + 'miliardi' + cifra_a_testo(n%1000000000)
    else:
        return 'unbilione'
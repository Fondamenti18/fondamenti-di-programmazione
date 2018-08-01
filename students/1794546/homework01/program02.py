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
   
    lol={0:'', 1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque', 6:'sei', 7:'sette', 8:'otto', 9:'nove', 10:'dieci', 11:'undici', 12:'dodici', 13:'tredici', 14:'quattordici', 15:'quindici', 16:'sedici', 17:'diciassette', 18:'diciotto', 19:'diciannove'}
    lel={2:'venti', 3:'trenta', 4:'quaranta', 5:'cinquanta', 6:'sessanta', 7:'settanta', 8:'ottanta', 9:'novanta'}
   
    a=n%10 #unita
    b=(n%100)//10 #decine
    
    if n==0: 
        return ""
    
    if 0<n<20:
        return lol[n]
    
    if 19<n<100:
        if a in (1,8):
            lel[b]=lel[b][:-1]
        return lel[b] + conv(n%10)
    
    cento='cento'
    if 99<n<200:
        return cento + conv(n%100)
        
    if 199<n<1000:
        if b==8:
            cento=cento[:-1]
        return conv(n//100) + cento + conv(n%100)
    
    if 999<n<2000:
        return 'mille' + conv(n%1000)
    
    if 1999<n<1000000:
        return conv(n//1000) + 'mila' + conv(n%1000) 
    
    if 999999<n<2000000:
        return 'unmilione' + conv(n%1000000)
    
    if 1999999<n<1000000000:
        return conv(n//1000000) + 'milioni' + conv(n%1000000)
    
    if 999999999<n<2000000000:
        return 'unmiliardo' + conv(n%1000000000)
    
    if 1999999999<n<1000000000000:
        return conv(n//1000000000) + 'miliardi' + conv(n%1000000000)
    
    if n==1000000000000:
        return 'unbilione'
    
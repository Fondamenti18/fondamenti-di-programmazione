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
    l= {28:'ventotto', 38:'trentotto', 48:'quarantotto', 58:'cinquantotto', 68:'sessantotto', 78:'settantotto', 88:'ottantotto', 98:'novantotto', 99:'novantanove', 1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque', 6:'sei', 7:'sette', 8:'otto', 9:'nove', 10:'dieci', 11:'undici', 12:'dodici', 13:'tredici', 14:'quattordici', 15:'quindici', 16:'sedici', 17:'diciassette', 18:'diciotto', 19:'diciannove', 20:'venti', 30:'trenta', 40:'quaranta', 50:'cinquanta', 60:'sessanta', 70:'settanta', 80:'ottanta', 90:'novanta', 100:'cento', 0:'zero', 21:'ventuno', 31:'trentuno', 41:'quarantuno', 51:'cinquantuno', 61:'sessantuno', 71:'settantuno', 81:'ottantuno', 91:'novantuno', 1000:'mille'}
    assert (0<= n)
    if(n<=20):
        return l[n]
    if (n<=100):
        if n%10 == 0 or n%10==1:
            return l[n]
        elif n%10==8:
            return l[n]
        else:
            return l[n//10*10]+l[n%10]
    if (n<200):
        if n==181:
            return 'centottantuno'
        else:
            return 'cento'+ conv(n%100)
    if (n<=1000):
        if n==1000:
            return l[n]
        elif n%100==81:
            return l[n//100]+'centottantuno'
        elif n%100 == 0:
            return l[n/100]+l[100]
        else:
            return l[n//100]+l[100]+ conv(n%100)
    if (n<10000):
        if n%1000==0:
            return l[n/1000]+'mila'
        else:
            return conv((n//1000)*1000)+ conv(n%1000)
    if (n<100000):
        if n%1000==0:
            return l[n/1000]+'mila'
        else:
            return conv(n//1000)+'mila'+conv(n%1000)
    if (n<=1000000):
        if n==1000000:
            return 'un milione'
        elif n%100000==0:
            return conv(n/1000)+'mila'
        else:
            return conv((n//100000)*100)+conv(n%100000)
    if(n<10000000):
        if n%1000000==0:
            return l[n/1000000]+' milioni'
        else:
            return l[n//1000000]+' milioni'+conv(n%1000000)
    if(n<100000000):
        if n%10000000==0:
            return l[n/10000000]+' milioni'
        else:
            return l[n//10000000]+' milioni'+conv(n%10000000)
    if(n<1000000000):
        if n==1000000000:
            return 'un miliardo'
        elif n%100000000==0:
            return l[n/1000000]+'milioni'
        else:
            return conv(n//1000000)+'milioni'+conv(n%1000000)
    if(n<10000000000):
        if n%1000000000==0:
            return l[n/100000000]+'miliardi'
        else:
            return l[n/100000000]+'miliardi'+ conv(n%1000000000)
    if(n<=100000000000):
        if n== 100000000000:
            return 'cento miliardi'
        elif n%10000000000==0:
            return conv(n/10000000000)+'miliardi'
        else:
            return conv(n/10000000000)+'miliardi'+conv(n%10000000000)
    

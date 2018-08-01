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
    numeri={0:'zero', 1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque', 
            6:'sei', 7:'sette', 8:'otto', 9:'nove', 10:'dieci', 11:'undici', 
            12:'dodici', 13:'tredici', 14:'quattordici', 15:'quindici', 
            16:'sedici', 17:'diciassette', 18:'diciotto', 19:'dicianove', 
            20:'venti', 30:'trenta', 40:'quaranta', 50:'cinquanta', 
            60:'sessanta', 70:'settanta', 80:'ottanta', 90:'novanta'}
    
    k=1000
    milione=k*1000
    miliardo=milione*1000
    bilione=miliardo*1000
            
    if n<20:
        return numeri[n]
    elif n<100:
        if n==28:return 'ventotto'
        elif n==38:return 'trentotto'
        elif n==48:return 'quarantotto'
        elif n==58:return 'cinquantotto'
        elif n==68:return 'sessantotto'
        elif n==78:return 'settantotto'
        elif n==88:return 'ottantotto'
        elif n==98:return 'novantotto'
        elif n==21:return 'ventuno'
        elif n==31:return 'trentuno'
        elif n==41:return 'quarantuno'
        elif n==51:return 'cinquantuno'
        elif n==61:return 'sessantuno'
        elif n==71:return 'settantuno'
        elif n==81:return 'ottantuno'
        elif n==91:return 'novantuno'
        elif n%10==0:return numeri[n]
        else:return numeri[n//10*10]+numeri[n%10]
    elif n<k:
        if 100<n<200:return 'cento'+conv(n%100)
        elif n==180:return 'centottanta'
        elif n==181:return 'centottantuno'
        elif n==280:return 'duecentottanta'
        elif n==281:return 'duecentottantuno'
        elif n==380:return 'trecentottanta'
        elif n==381:return 'trecentottantuno'
        elif n==480:return 'quattrocentottanta'
        elif n==481:return 'quattrocentottantuno'
        elif n==580:return 'cinquecentottanta'
        elif n==581:return 'cinquecentottantuno'
        elif n==680:return 'seicentottanta'
        elif n==681:return 'seicentottantuno'
        elif n==780:return 'settecentottanta'
        elif n==781:return 'settecentottantuno'
        elif n==880:return 'ottocentottanta'
        elif n==881:return 'ottocentottantuno'
        elif n==888:return 'ottocentottantotto'
        elif n==980:return 'novecentottanta'
        elif n==981:return 'novecentottantuno'
        elif n%100==0:return numeri[n//100]+'cento'
        else:return numeri[n//100]+'cento'+conv(n%100)
    elif n<milione:
        if k<n<2000:return 'mille'+conv(n%k)
        elif n%k==0:return conv(n//1000)+'mila'
        else:return conv(n//k)+'mila'+conv(n%k)
    elif n<miliardo:
        if 1*milione<n<2*milione:return 'un milione'+conv(n%milione)
        elif n%milione==0:return conv(n//1000000)+'milioni'
        else:return conv(n//milione)+'milioni'+conv(n%milione)
    elif n<bilione:
        if 1*miliardo<n<2*miliardo:return 'un miliardo'+conv(n%miliardo)
        elif n%miliardo==0:return conv(n//1000000000)+'miliardi'
        else:return conv(n//miliardo)+'miliardi'+conv(n%miliardo)
        

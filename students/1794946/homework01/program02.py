
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
    if n==0:
        return ''
    elif n<=19:
        diciannove={1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque' ,6:'sei',7:'sette', 8:'otto', 9:'nove', 10:'dieci',
           11:'undici', 12:'dodici', 13:'tredici',14:'quattordici', 15:'quindici', 16:'sedici', 17:'diciassette', 18:'diciotto', 19:'diciannove'}
        return (diciannove[n])

    elif n<=99:
        u=n%10
        d=n//10
        novantanove={2:'venti', 3:'trenta', 4:'quaranta', 5:'cinquanta' ,6:'sessanta',7:'settanta', 8:'ottanta', 9:'novanta'}
        decine=novantanove[d]
        if u==1 or u==8:
            decine=decine [:-1]         
        return decine+conv(u)
        

    elif n<=999:
        d=n%100
        d1=(n%100)//10
        c=n//100
        novecentonovantanove={1:'cento', 2:'duecento', 3:'trecento', 4:'quattrocento', 5:'cinquecento' ,6:'seicento',7:'settecento', 8:'ottocento', 9:'novecento'}
        centinaia=novecentonovantanove[c]
        if d1==8:
            centinaia=centinaia[:-1]
        return centinaia+conv(d)
    
  
    elif n<=1999:
        c=n%1000
        return 'mille'+conv(c)

    elif n<=999999:
        c=n%1000
        c1=(n-c)//1000
        return conv(c1)+'mila'+conv(c)

    elif n<=1999999:
        m=n%1000000
        return 'unmilione'+conv(m)

    elif n<=999999999:
        m=n%1000000
        m1=(n-m)//1000000
        return conv(m1)+'milioni'+conv(m)

    elif n<=1999999999:
        k=n%1000000000
        return 'unmiliardo'+conv(k)

    elif n<1000000000000:
        k=n%1000000000
        k1=(n-k)//1000000000
        return conv(k1)+'miliardi'+conv(k)

    

   



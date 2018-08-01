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

diz = {1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque', 6:'sei', 7:'sette', 8:'otto', 9:'nove', 10:'dieci', 
         11:'undici', 12:'dodici', 13:'tredici', 14:'quattordici', 15:'quindici', 16:'sedici', 17:'diciassette', 
         18:'diciotto', 19:'diciannove', 20:'venti', 30:'trenta', 40:'quaranta', 50:'cinquanta', 60:'sessanta',
         70:'settanta', 80:'ottanta', 90:'novanta', 100:'cento'}

def num(n):
    return diz[n]


def parole(n):
    ctx = ''
    utx = ''
    dtx = ''
    u = (n % 10)
    d = (((n//10)% 100)% 10)*10
    if n != 0:
        if n in diz:
            return diz[n]
        else:
            if n > 100:
                if n // 100 != 1:
                    ctx = num(n // 100) + 'cento'
                else:
                    ctx = 'cento'
                if d == 80:
                    ctx = ctx[:-1]
            if (n % 100) in diz:
                dtx = diz[n % 100]
            else:
                if (n % 100) % 10 != 0:
                    if d != 0:
                        dtx = num(d)
                        if u == 1 or u == 8:
                            dtx = dtx[:-1]
                            utx = num(u)
                        else:
                            utx = num(u)
                    else:
                        utx = num(u)
                else:
                    dtx = num(n % 100)
    else:
        return ''
    return ctx + dtx + utx


        



def conv(n):
    miliardi = (n //10**9)
    if miliardi > 1:
        mlrdtx = parole(miliardi) + 'miliardi'
    elif miliardi == 1:
        mlrdtx = 'unmiliardo'
    elif miliardi == 0:
        mlrdtx = ''
        
    milioni = (((n %10**9) % 10**9) //10**6)
    if milioni > 1:
        mlntx = parole(milioni) + 'milioni'
    elif milioni == 1:
        mlntx = 'unmilione'
    elif milioni == 0:
        mlntx = ''
        
    mille = ((((n %10**9) % 10**6) % 10**6) //10**3)
    if mille > 1:
        milletx = parole(mille) + 'mila'
    elif mille == 1:
        milletx = 'mille'
    elif mille == 0:
        milletx = ''
        
    cent = ((((((n %10**9) % 10**6) % 10**6)%10**3) %1000))
    centx = parole(cent)
    return  mlrdtx + mlntx + milletx + centx



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

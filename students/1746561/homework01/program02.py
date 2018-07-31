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

#Prova a rendere tutto più asciutto
def scomposizione(n): #Scompone un naturale in u,d,c,k...
    ls = []
    for i in range(len(str(n))-1, -1, -1):
        e = 10**i
        c = n//e
        n %= e
        ls += [c]
    return ls


def conv(n): 
    ls = scomposizione(n)
    
    unita = {1:'uno',2:'due',3:'tre',4:'quattro',\
            5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove'}
    
    decine_dieci = {0: 'dieci',1:'undici',2:'dodici',3:'tredici',4:'quattordici',\
                    5:'quindici',6:'sedici',7:'diciassette',\
                    8:'diciotto',9:'diciannove'}
    decine_zeri = {2:'venti',3:'trenta',4:'quaranta',5:'cinquanta',\
                    6:'sessanta',7:'settanta',8:'ottanta',9:'novanta'}
    
    if len(ls) == 1:
        try : return unita[ls[0]] #unita
        except KeyError: return '' 
        
    elif len(ls) == 2: #decine
        if ls[0] == 1: return decine_dieci[ls[1]]
        elif ls[0] != 1:
            if ls[1] == 1 or ls[1] == 8: 
                return decine_zeri[ls[0]][:-1]+conv(n%10)
            return decine_zeri[ls[0]]+conv(n%10)
        
    elif len(ls) == 3: #centinaia
        if ls[0] == 1: return 'cento'+conv(n%100)
        elif ls[1] == 8: return unita[ls[0]]+'cent'+conv(n%100)
        return unita[ls[0]]+'cento'+conv(n%100)
    
    elif len(ls) == 4: #migliaia
        if ls[0] == 1: return 'mille'+conv(n%1000)
        return unita[ls[0]]+'mila'+conv(n%1000)
    elif len(ls) <= 6: #migliaia*10
        return conv(n//1000)+'mila'+conv(n%1000)
    
    elif len(ls) == 7: #milioni
        if ls[0] == 1: return 'unmilione'+conv(n%1000000)
        return unita[ls[0]]+'milioni'+conv(n%1000000)
    elif len(ls) <= 9: #migliaia*10
        return conv(n//1000000)+'milioni'+conv(n%1000000)
    
    elif len(ls) == 10: #miliardi
        if ls[0] == 1: return 'unmiliardo'+conv(n%1000000000)
        return unita[ls[0]]+'miliardi'+conv(n%1000000000)
    elif len(ls) <= 12: #migliaia*10
        return conv(n//1000000000)+'miliardi'+conv(n%1000000000)
    
    
        
    
        
         
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
    if n<20:
        return unit(n)
    elif n<100:
        return decine(n)
    elif n<1000:
        return centinaia(n)
    elif n<1000000:
        return migliaia(n)
    elif n<1000000000:
        return milioni(n)
    elif n<1000000000000:
        return miliardi(n)
            

def unit(x):
    zero_19=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove',\
             'dieci','undici','dodici','tredici','quattordici','quindici','sedici',\
             'diciassette','diciotto','diciannove']
    return zero_19[x]

def decine(x):
    if x>19:
        dec=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
        cifre=list(str(x))
        if cifre[1]=='1' or cifre[1]=='8':
            return dec[int(cifre[0])-2][:-1]+unit(int(cifre[1]))
        else:
            return dec[int(cifre[0])-2]+unit(int(cifre[1]))
    else:
        return unit(x)

def centinaia(x):
    cifre=list(str(x))
    if len(cifre)==3:
        c='cento'
        if cifre[0]=='1':
            if cifre[1]=='0':
                return c+unit(int(cifre[2]))
            elif cifre[1]=='8':
                return c[:-1]+decine(int(''.join(cifre[1:])))
            else:
                return c+decine(int(''.join(cifre[1:])))
        else:
            if cifre[1]=='0':
                return unit(int(cifre[0]))+c+unit(int(cifre[2]))
            elif cifre[1]=='8':
                return unit(int(cifre[0]))+c[:-1]+decine(int(''.join(cifre[1:])))
            else:
                return unit(int(cifre[0]))+c+decine(int(''.join(cifre[1:])))
    else:
        return decine(x)

def migliaia(x):
    cifre=list(str(x))
    if len(cifre)==4:
        if cifre[0]=='1':
            return 'mille'+centinaia(int(''.join(cifre[1:])))
        else:
            return unit(int(cifre[0]))+'mila'+centinaia(int(''.join(cifre[1:])))
    elif len(cifre)==5:
        return decine(int(''.join(cifre[:2])))+'mila'+centinaia(int(''.join(cifre[2:])))        
    else:
        return centinaia(int(''.join(cifre[:3])))+'mila'+centinaia(int(''.join(cifre[3:])))

def milioni(x):
    cifre=list(str(x))
    if len(cifre)==7:
        if cifre[0]=='1':
            return 'unmilione'+migliaia(int(''.join(cifre[1:])))
        else:
            return unit(int(cifre[0]))+'milioni'+migliaia(int(''.join(cifre[1:])))
    elif len(cifre)==8:
        return decine(int(''.join(cifre[:2])))+'milioni'+migliaia(int(''.join(cifre[2:])))        
    else:
        return centinaia(int(''.join(cifre[:3])))+'milioni'+migliaia(int(''.join(cifre[3:])))

def miliardi(x):
    cifre=list(str(x))
    if len(cifre)==10:
        if cifre[0]=='1':
            return 'unmiliardo'+milioni(int(''.join(cifre[1:])))
        else:
            return unit(int(cifre[0]))+'miliardi'+milioni(int(''.join(cifre[1:])))
    elif len(cifre)==11:
        return decine(int(''.join(cifre[:2])))+'miliardi'+milioni(int(''.join(cifre[2:])))        
    else:
        return centinaia(int(''.join(cifre[:3])))+'miliardi'+milioni(int(''.join(cifre[3:])))
        
    
        
    










    

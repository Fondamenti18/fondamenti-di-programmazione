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

def startVocale(x):
    flag=False
    lista=['a','e','i','o','u']
    for let in lista:
        if x[0]==let:
            flag=True
    return flag

def unita(x):
    r=''
    if x=='1':
        r+='uno'
    elif x=='2':
        r+='due'
    elif x=='3':
        r+='tre'
    elif x=='4':
        r+='quattro'
    elif x=='5':
        r+='cinque'
    elif x=='6':
        r+='sei'
    elif x=='7':
        r+='sette'
    elif x=='8':
        r+='otto'
    else:
        r+='nove'
    return r

def decina(x):
    r=''
    if x[0]=='0':
        r= unita(x[1])
    else:
        if x[0]=='1':
            if x=='10':
                r+='dieci'
            elif x=='11':
                r+='undici'
            elif x=='12':
                r+='dodici'
            elif x=='13':
                r+='tredici'
            elif x=='14':
                r+='quattordici'
            elif x=='15':
                r+='quindici'
            elif x=='16':
                r+='sedici'
            elif x=='17':
                r+='diciassette'
            elif x=='18':
                r+='diciotto'
            else:
                r+='diciannove'
        elif x[0]=='2':
            if x[1]=='0':
                r='venti'
            elif startVocale(unita(x[1])):
                r= 'vent' + unita(x[1])
            else:
                r= 'venti' + unita(x[1])
        elif x[0]=='3':
            if x[1]=='0':
                r='trenta'
            elif startVocale(unita(x[1])):
                r= 'trent' + unita(x[1])
            else:
                r= 'trenta' + unita(x[1])
        elif x[0]=='4':
            if x[1]=='0':
                r='quaranta'
            elif startVocale(unita(x[1])):
                r= 'quarant' + unita(x[1])
            else:
                r= 'quaranta' + unita(x[1])
        elif x[0]=='5':
            if x[1]=='0':
                r='cinquanta'
            elif startVocale(unita(x[1])):
                r= 'cinquant' + unita(x[1])
            else:
                r= 'cinquanta' + unita(x[1])
        elif x[0]=='6':
            if x[1]=='0':
                r='sessanta'
            elif startVocale(unita(x[1])):
                r= 'sessant' + unita(x[1])
            else:
                r= 'sessanta' + unita(x[1])
        elif x[0]=='7':
            if x[1]=='0':
                r='settanta'
            elif startVocale(unita(x[1])):
                r= 'settant' + unita(x[1])
            else:
                r= 'settanta' + unita(x[1])
        elif x[0]=='8':
            if x[1]=='0':
                r='ottanta'
            elif startVocale(unita(x[1])):
                r= 'ottant' + unita(x[1])
            else:
                r= 'ottanta' + unita(x[1])
        elif x[0]=='9':
            if x[1]=='0':
                r='novanta'
            elif startVocale(unita(x[1])):
                r= 'novant' + unita(x[1])
            else:
                r= 'novanta' + unita(x[1])
    return r

def centinaia(x):
    r=''
    if x[0]=='0':
        if x[1]=='0':
            r= unita(x[2])
        else:
            r= decina(x[1:])
    else:
        if x[0]=='1':
            if x[1]!='8':
                r= 'cento' + decina(x[1:])
            else:
                r= 'cent' + decina(x[1:])
        elif x[0]=='2':
            if x[1]!='8':
                r= 'duecento' + decina(x[1:])
            else:
                r= 'duecent' + decina(x[1:])
        elif x[0]=='3':
            if x[1]!='8':
                r= 'trecento' + decina(x[1:])
            else:
                r= 'trecent' + decina(x[1:])
        elif x[0]=='4':
            if x[1]!='8':
                r= 'quattrocento' + decina(x[1:])
            else:
                r= 'quattrocent' + decina(x[1:])
        elif x[0]=='5':
            if x[1]!='8':
                r= 'cinquecento' + decina(x[1:])
            else:
                r= 'cinquecent' + decina(x[1:])
        elif x[0]=='6':
            if x[1]!='8':
                r= 'seicento' + decina(x[1:])
            else:
                r= 'seicent' + decina(x[1:])
        elif x[0]=='7':
            if x[1]!='8':
                r= 'settecento' + decina(x[1:])
            else:
                r= 'settecent' + decina(x[1:])
        elif x[0]=='8':
            if x[1]!='8':
                r= 'ottocento' + decina(x[1:])
            else:
                r= 'ottocent' + decina(x[1:])
        else:
            if x[1]!='8':
                r= 'novecento' + decina(x[1:])
            else:
                r= 'novecent' + decina(x[1:])
    return r
    
def conv(n):
    x=str(n)
    if len(x)==1:
        return unita(x)
    elif len(x)==2:
        return decina(x)
    elif len(x)==3:
        return centinaia(x)
    elif len(x)==4:
        if x [0]=='1':
            return 'mille' + centinaia(x[1:])
        else:
            return unita(x[0]) + 'mila' + centinaia(x[1:])
    elif len(x)==5:
        return decina(x[0:2]) + 'mila' + centinaia(x[2:])
    elif len(x)==6:
        return centinaia(x[:3]) + 'mila' + centinaia(x[3:])
    elif len(x)==7:
        if x [0]=='1':
            return 'unmilione' + centinaia(x[1:4]) + 'mila' + centinaia(x[4:])
        else:
            return unita(x[0]) + 'milioni' + centinaia(x[1:4])+ 'mila' + centinaia(x[4:])
    elif len(x)==8:
        return decina(x[0:2]) + 'milioni' + centinaia(x[2:5])+ 'mila' + centinaia(x[5:])
    elif len(x)==9:
        return centinaia(x[0:3]) + 'milioni' + centinaia(x[3:6])+ 'mila' + centinaia(x[6:])
    elif len(x)==10:
        if x [0]=='1':
            return 'unmiliardo' + centinaia(x[1:4]) + 'milioni' + centinaia(x[4:7]) + 'mila'+ centinaia(x[7:])
        else:
            return unita(x[0]) + 'miliardi' + centinaia(x[1:4]) + 'milioni' + centinaia(x[4:7]) + 'mila'+ centinaia(x[7:])
    elif len(x)==11:
        return decina(x[0:2]) + 'miliardi' + centinaia(x[2:5]) + 'milioni' + centinaia(x[5:8]) + 'mila'+ centinaia(x[8:])
    else:
        return centinaia(x[0:3]) + 'miliardi' + centinaia(x[3:6]) + 'milioni' + centinaia(x[6:9]) + 'mila'+ centinaia(x[9:])
    
    
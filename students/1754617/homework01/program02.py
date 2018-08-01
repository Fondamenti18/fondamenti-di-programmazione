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

    if(lunghezza(n)==1):
        x=traduci3(n)
        return x
    elif(lunghezza(n)==2):
        x=traduci3(n)
        return x
    elif(lunghezza(n)==3):
        x=traduci3(n)         #scoorro per la lunghezza e vedo di che cifra
        return x
    elif(lunghezza(n)==4):
        stringa=str(n)
        primaCifra=int(stringa[0])
        treCifre=int(stringa[1:4])
        x=traduci3(primaCifra)
        y=traduci3(treCifre)
        if(x=='uno' and y!='zero'):
            return 'mille'+y
        elif(x=='uno' and y=='zero'):
            return 'mille'
        elif( x!='uno' and y=='zero'):
            return x+'mila'    #controllo
        elif(treCifre==0):
            return x+'mila'
        else:
            return x+'mila'+y
    elif(lunghezza(n)==5):
        stringa=str(n)
        primeDue=int(stringa[0:2])
        treCifre=int(stringa[2:])
        x=traduci3(primeDue)
        y=traduci3(treCifre)
        if(x=='dieci' and y!='zero'):
            return 'decimila'+y
        elif(y=='zero'):
            return x+'mila'
        else:
            return x+'mila'+y
    elif(lunghezza(n)==6):
        stringa=str(n)
        primeTre=int(stringa[0:3])
        treCifre=int(stringa[3:6])
        x=traduci3(primeTre)
        y=traduci3(treCifre)     #controllo
        if(y=='zero'):
            return x+'mila'
        else:
            return x+'mila'+y
    elif(lunghezza(n)==7):
        stringa=str(n)
        primaCifra=int(stringa[0])
        treCifre=int(stringa[1:4])
        treCifre2=int(stringa[4:])
        x=traduci3(primaCifra)
        y=traduci3(treCifre)
        z=traduci3(treCifre2)
        if(y=='zero' and z=='zero' and x=='uno'):
            return 'unmilione'
        elif(y=='zero' and z=='zero' and x!='uno'):
            return x+'milioni'
        elif(y=='zero'):
            return x+'milioni'+z
        elif(z=='zero' and x=='uno'):
            return 'unmilione'+y
        elif(z=='zero' and x!='uno'):
            return x+'milioni'+y+'mila'
        else:
            return x+'milioni'+y+'mila'+z
    elif(lunghezza(n)==8):
        stringa=str(n)
        primaDue=int(stringa[0:2])
        treCifre=int(stringa[2:5])    #sempre lunghezza
        treCifre2=int(stringa[5:])
        x=traduci3(primaDue)
        y=traduci3(treCifre)
        z=traduci3(treCifre2)
        if(y=='zero' and z=='zero' and x=='dieci'):
            return 'diecimilioni'
        elif(y=='zero' and z=='zero' and x!='dieci'):
            return x+'milioni'
        elif(y=='zero'):
            return x+'milioni'+z
        elif(z=='zero' and x=='dieci'):
            return 'diecimilioni'+y
        elif(z=='zero' and x!='dieci'):
            return x+'milioni'+y+'mila'
        else:
            return x+'milioni'+y+'mila'+z
    elif(lunghezza(n)==9):
        stringa=str(n)
        primaTre=int(stringa[0:3])
        treCifre2=int(stringa[3:6])
        treCifre3=int(stringa[6:])
        x=traduci3(primaTre)
        y=traduci3(treCifre2)
        z=traduci3(treCifre3)
        if(y=='zero' and z=='zero' and x=='cento'):
            return 'centomilioni'
        elif(z=='zero' and y=='zero' and x!='cento'):
            return x+'milioni'
        elif(y=='zero'):
            return x+'milioni'+z
        elif(z=='zero' and x=='cento'):
            return 'centoimilioni'+y
        elif(z=='zero' and x!='dieci'):
            return x+'milioni'+y+'mila'
        else:
            return x+'milioni'+y+'mila'+z
    elif(lunghezza(n)==10):
        stringa=str(n)
        primaCifra=int(stringa[0:1])
        treCifre=int(stringa[1:4])
        treCifre2=int(stringa[4:7])
        treCifre3=int(stringa[7:])
        x=traduci3(primaCifra)
        w=traduci3(treCifre)
        y=traduci3(treCifre2)
        z=traduci3(treCifre3)
        if(y=='zero' and z=='zero' and w=='zero' and x=='uno'):
            return 'unmiliardo'
        elif(y=='zero' and z=='zero' and w=='zero' and x!='uno'):
            return x+'miliardi'
        elif(x!='uno' and y!='zero' and z!='zero' and w!='zero'):
            return x+'miliardi'+w+'milioni'+y+'mila'+z
        elif(x=='uno' and y!='zero' and z!='zero' and w!='zero'):
            return 'unmiliardo'+w+'milioni'+y+'mila'+z
        elif(y=='zero' and w!='zero' and z!='zero' and x!='uno'):
            return x+'miliardi'+z
        elif(x!='uno' and w=='zero' and y!='zero' and z=='zero'):
            return x+'milardi'+y+'mila'
        elif(y=='zero' and w!='zero' and z!='zero' and x=='uno'):
            return 'unmiliardo'+z
        elif(x!='uno' and w!='zero' and y=='zero' and z=='zero'):
            return x+'milardi'+w+'milioni'
        elif(z=='zero' and x=='uno'):
            return 'unmiliardo'+y
        elif(z=='zero' and x!='uno' and w!='zero'):
            return x+'miliardi'+w+'milioni'+ y +'mila'
        elif(w=='zero' and y=='zero'):
            return x+'milardi'+ z
        else:
            return x+'miliardi'+w+'milioni'+y+'mila'+z
    elif(lunghezza(n)==11):
        stringa=str(n)
        primeDue=int(stringa[0:2])
        treCifre=int(stringa[2:5])
        treCifre2=int(stringa[5:8])
        treCifre3=int(stringa[8:])
        x=traduci3(primeDue)
        w=traduci3(treCifre)
        y=traduci3(treCifre2)
        z=traduci3(treCifre3)
        if(y=='zero' and z=='zero' and w=='zero' and x=='deci'):
            return 'diecimiliardi'
        elif(y=='zero' and z=='zero' and w=='zero' and x!='dieci'):
            return x+'miliardi'
        elif(x!='dieci' and y!='zero' and z!='zero' and w!='zero'):
            return x+'miliardi'+w+'milioni'+y+'mila'+z
        elif(x=='dieci' and y!='zero' and z!='zero' and w!='zero'):
            return 'diecimiliardo'+w+'milioni'+y+'mila'+z
        elif(y=='zero' and w!='zero' and z!='zero' and x!='dieci'):
            return x+'miliardi'+z
        elif(x!='dieci' and w=='zero' and y!='zero' and z=='zero'):
            return x+'milardi'+y+'mila'
        elif(y=='zero' and w!='zero' and z!='zero' and x=='dieci'):
            return 'diecimiliardo'+z
        elif(x!='dieci' and w!='zero' and y=='zero' and z=='zero'):
            return x+'milardi'+w+'milioni'
        elif(z=='zero' and x=='dieci'):
            return 'diecimiliardi'+y
        elif(z=='zero' and x!='dieci' and w!='zero'):
            return x+'miliardi'+w+'milioni'+ y +'mila'
        elif(w=='zero' and y=='zero'):
            return x+'milardi'+ z
        else:
            return x+'miliardi'+w+'milioni'+y+'mila'+z
    elif(lunghezza(n)==12):
        stringa=str(n)
        primeTre=int(stringa[0:3])
        treCifre=int(stringa[3:6])
        treCifre2=int(stringa[6:9])
        treCifre3=int(stringa[9:])
        x=traduci3(primeTre)
        w=traduci3(treCifre)
        y=traduci3(treCifre2)
        z=traduci3(treCifre3)
        if(y=='zero' and z=='zero' and w=='zero' and x=='cento'):
            return 'centomiliardi'
        elif(y=='zero' and z=='zero' and w=='zero' and x!='cento'):
            return x+'miliardi'
        elif(x!='cento' and y!='zero' and z!='zero' and w!='zero'):
            return x+'miliardi'+w+'milioni'+y+'mila'+z
        elif(x=='cento' and y!='zero' and z!='zero' and w!='zero'):
            return 'centomiliardi'+w+'milioni'+y+'mila'+z
        elif(y=='zero' and w!='zero' and z!='zero' and x!='dieci'):
            return x+'miliardi'+z
        elif(x!='dieci' and w=='zero' and y!='zero' and z=='zero'):
            return x+'milardi'+y+'mila'
        elif(y=='zero' and w!='zero' and z!='zero' and x=='cento'):
            return 'centomiliardi'+z
        elif(x!='cento' and w!='zero' and y=='zero' and z=='zero'):
            return x+'milardi'+w+'milioni'
        elif(z=='zero' and x=='cento'):
            return 'centoimiliardi'+y
        elif(z=='zero' and x!='dieci' and w!='zero'):
            return x+'miliardi'+w+'milioni'+ y +'mila'
        elif(w=='zero' and y=='zero'):
            return x+'milardi'+ z
        else:
            return x+'miliardi'+w+'milioni'+y+'mila'+z
    

def lunghezza(n):
    stringa=str(n)
    return len(stringa)

def traduci3(n):
    listaUnita=["zero", "uno", "due", "tre", "quattro", "cinque", "sei", "sette",'otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici',
                'diciassette','diciotto',"diciannove","venti","ventuno", "ventidue", "ventitre","ventiquattro", "venticinque", "ventisei", "ventisette",
                "ventotto", "ventinove","trenta", "trentuno", "trentadue", "trentatre", "trentaquattro", "trentacinque","trentasei","trentasette","trentotto",
                "trentanove", "quaranta", "quarantuno", "quarantadue", "quarantatre", "quarantaquattro","quarantacinque", "quarantasei", "quarantasette",
                "quarantotto", "quarantanove", "cinquanta", "cinquantuno","cinquantadue", "cinquantatre", "cinquantaquattro", "cinquantacinque", "cinquantasei",
                "cinquantasette","cinquantotto", "cinquantanove", "sessanta", "sessantuno", "sessantadue", "sessantatre","sessantaquattro", "sessantacinque",
                "sessantasei", "sessantasette", "sessantotto", "sessantanove", "settanta", "settantuno", "settantadue", "settantatre","settantaquattro",
                 "settantacinque","settantasei", "settantasette", "settantotto", "settantanove", "ottanta", "ottantuno","ottantadue","ottantatre","ottantaquattro",
                "ottantacinque", "ottantasei", "ottantasette", "ottantotto", "ottantanove", "novanta", "novantuno", "novantadue", "novantatre","novantaquattro",
                "novantacinque","novantasei", "novantasette", "novantotto","novantanove"]
    
    lista100 = ['zero','cento','duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento']
    lista100modificata=['zero','cent','duecent','trecent','quattrocent','cinquecent','seicent','settecent','ottocent','novecent']
    stringa=str(n)
    primaCifra=int(stringa[0])
    secondaCifra=int(((n%100)-(n%10))/10)      #vedo le cifre con i moduli poche con stringhe errore
    terzaCifra=n%10
    secondaTerza=n%100
    if(len(stringa)==3 and primaCifra==0 and secondaCifra==0):
        return listaUnita[terzaCifra]
    elif(len(stringa)==2 and primaCifra==0):
        return listaUnita[secondaTerza]
    elif(len(stringa)==1):
        return listaUnita[primaCifra]
    elif(len(stringa)==2):
        return listaUnita[secondaTerza]
    elif(len(stringa)==3 and secondaTerza==0):
        return lista100[primaCifra]
    elif(len(stringa)==3 and secondaCifra==8):
        return lista100modificata[primaCifra]+listaUnita[secondaTerza]
    elif(len(stringa)==3 and secondaCifra==0):
        return lista100[primaCifra]+listaUnita[terzaCifra]
    else:
        return lista100[primaCifra]+listaUnita[secondaTerza]
    

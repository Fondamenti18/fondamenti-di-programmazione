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
    '''prende in input un intero e lo trsfroma nel corrispettivo numero a letter'''
    s=str(n)
    l=[]
    for char in s:
        l.append(int(char)) #appendo ogni singolo carattere che compone il numero ad una lista
    if len(l)==12:  #se ha 12 cifre
        miliardo=centi(l[0],l[1],l[2])+'miliardi'
        milione=milioni(l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11])
        return miliardo+milione
    elif len(l)==11: #se ha 11 cifre
        miliardo=decine(l[0],l[1])+'miliardi'
        milione=milioni(l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10])
        return miliardo+milione
    elif len(l)==10:#se ha 10 cifre
        if l[0]==1:
            return 'un miliardo'+milioni(l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9])
        else:
            miliardo=unita(l[0])+'miliardi'
            milione=milioni(l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9])
            return miliardo+milione
    elif len(l)==9:
        milione=centi(l[0],l[1],l[2])+'milioni' #il miione sarà a tre cifre
        #print(milione)
        migliaia=miglia(l[3],l[4],l[5],l[6],l[7],l[8])
        #print(migliaia)
        return milione+migliaia
    elif len(l)==8:
        milione=decine(l[0],l[1])+'milioni' #il milione è a due cifre
        migliaia=miglia(l[2],l[3],l[4],l[5],l[6],l[7])
        return milione+migliaia
    elif len(l)==7:
        if l[0]==1:  #il milione è ad una cifra fra 1 e 9
            migliaia=miglia(l[1],l[2],l[3],l[4],l[5],l[6])
            return 'un milione'+migliaia
        else:
            milione=unita(l[0])+'mila'
            migliaia=miglia(l[1],l[2],l[3],l[4],l[5],l[6])
            return milione+migliaia
    elif len(l)==6: #la cifra arriva a tre migliaia
        migliaia=centi(l[0],l[1],l[2])+'mila' 
        centinaia=centi(l[3],l[4],l[5])
        return migliaia+centinaia        
    elif len(l)==5:
        migliaia=decine(l[0],l[1])+'mila' #le migliaia sono a due cifre
        centina=centi(l[2],l[3],l[4])
        return migliaia+centina
    elif len(l)==4:#le migliaia hanno un'unica cifra compresa fra 1 e 9
        if l[0]==1: 
            migliaia='mille'+centi(l[1],l[2],l[3])
            return migliaia
        else:
            migliaia=unita(l[0])+'mila'
            centina=centi(l[1],l[2],l[3])
            return migliaia+centina
    elif len(l)==3: #abbiamo le centinaia
        if l[0]==1:
            centinaia='cento'+decine(l[1],l[2])
            return centinaia
        else:
            centinaia=unita(l[0])+'cento'
            decina=decine(l[1],l[2])
            return centinaia+decina
    elif len(l)==2: #abbiamo le decine
        return decine(l[0],l[1])
    elif len(l)==1: # la cifra è compresa fra 0 e 9
        return unita(l[0])

def miglia(n,n2,n3,n4,n5,n6):
    '''prende in input 6 numeri che,uno dopo l'altro formano un'unica cifra e li decodifica scrivendo la cifra che rappresentano in lettere'''
    if n==0: #se la prima cifra è 0
        if n2==0: #se anche la seconda è 0 allora le migliaia hanno solo le unità
            migliaia=unita(n3)+'mila'
        else:
            migliaia=decine(n2,n3)+'mila' #altrimenti sono composte da decine
    else:
        migliaia=centi(n,n2,n3)+'mila'
    centinaia=centi(n4,n5,n6)
    return migliaia+centinaia        
        
def milioni(n,n2,n3,n4,n5,n6,n7,n8,n9):
    '''ritorna il numero di milioni, migliaia, centinaia, decine e unità in lettere'''
    if n==0:
        if n2==0:
            milione=unita(n3)+'milioni'
        else:
            milione=decine(n2,n3)+'milioni'
    else:
        milione=centi(n,n2,n3)+'milioni'
    migliaia=miglia(n4,n5,n6,n7,n8,n9)
    return milione+migliaia        
    
def centi(n,n1,n2):
    ''' ritorna il numero delle centinaia,decine e unità in lettere con elisione nel caso dell'8'''
    if n==0:
        return decine(n1,n2)
    elif n==1:
        decina=decine(n1,n2)
        centinaia='cento'
        return centinaia+decina
    else:
        centinaia=unita(n)+'cento'
        decina=decine(n1,n2)
        if n1==8:
            centinaia=elidi(decina,centinaia)
        return centinaia + decina
        
def unita(n):
    '''fa corrispondere ad ogni numero rappresentante un'unità, ossia un numero compreso fra 0 e 9, il corrispettivo numero in lettere'''
    if n==0:
        return '' # se n=0 non viene preso in considerazione
    elif n==1:
        return 'uno'
    elif n==2:
        return 'due'
    elif n==3:
        return 'tre'
    elif n==4:
        return 'quattro'
    elif n==5:
        return 'cinque'
    elif n==6:
        return 'sei'
    elif n==7:
        return 'sette'
    elif n==8:
        return 'otto'
    elif n==9:
        return 'nove'

def decine(n,n2):
    '''ritorna il corrispettivo numero d'input tradotto in lettere. se il valore delle decine è 1 segue un determinato percorso, altrimenti segue un altro percorso utilizzando il metodo unita e il metodo elidi'''
    if n==0:
        return unita(n2)
    elif n==1:
        if n2==0:
            return 'dieci'
        elif n2==1:
            return 'undici'
        elif n2==2:
             return 'dodici'
        elif n2==3:
            return  'tredici'
        elif n2==4:
            return 'quattordici'
        elif n2==5:
            return 'quindici'
        elif n2==6:
            return 'sedici'
        elif n2==7:
            return 'diciassette'
        elif n2==8:
            return 'diciotto'
        elif n2==9:
            return 'diciannove'
    elif n==2:
        stringa='venti'
        unit=unita(n2)
        if unit!='':
            stringa=elidi(unit,stringa)
        return stringa+unit
    elif n==3:
        stringa='trenta'
        unit=unita(n2)
        if unit!='':
            stringa=elidi(unit,stringa)
        return stringa+unit
    elif n==4:
        stringa='quaranta'
        unit=unita(n2)
        if unit!='':
            stringa=elidi(unit,stringa)
        return stringa+unit
    elif n==5:
        stringa='cinquanta'
        unit=unita(n2)
        if unit!='':
            stringa=elidi(unit,stringa)
        return stringa+unit
    elif n==6:
        stringa='sessanta'
        unit=unita(n2)
        if unit!='':
            stringa=elidi(unit,stringa)
        return stringa+unit
    elif n==7:
        stringa='settanta'
        unit=unita(n2)
        if unit!='':
            stringa=elidi(unit,stringa)
        return stringa+unit
    elif n==8:
        stringa='ottanta'
        unit=unita(n2)
        if unit!='':
            stringa=elidi(unit,stringa)
        return stringa+unit
    elif n==9:
        stringa='novanta'
        unit=unita(n2)
        if unit!='':
            stringa=elidi(unit,stringa)
        return stringa+unit
    
def elidi(string,string1):
    '''elide la lettera finale di una stringa contenente un numero che termina per vocale qualora debba essere concatenata ad un'altra stringa contenente un numero che inizia per vocale'''
    vocali=['a','e','i','o','u']
    for vocale in vocali:
        if string[0]==vocale:
            string1=string1[:-1]
    return string1
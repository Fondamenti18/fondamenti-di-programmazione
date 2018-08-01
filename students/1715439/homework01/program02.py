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
    lista=str(n)
    decine={'0':'','2':'venti', '3':'trenta', '4':'quaranta', '5':'cinquanta', '6':'sessanta', '7':'settanta', '8':'ottanta', '9':'novanta'}
    diecine={'10':'dieci','11':'undici','12':'dodici','13':'tredici','14':'quattordici','15':'quindici','16':'sedici','17':'diciassette','18':'diciotto','19':'diciannove'}
    unita={'0':'','1':'uno','2':'due','3':'tre','4':'quattro','5':'cinque','6':'sei','7':'sette','8':'otto','9':'nove'}
    decin={'0':'', '2':'vent', '3':'trent', '4':'quarant', '5':'cinquant', '6':'sessant', '7':'settant', '8':'ottant', '9':'novant'}
    #in lettere l'unità
    A=unita[lista[-1]]
    B=''
    C=''
    D=''
    E=''
    F=''
    G=''
    H='' 
    I=''
    L=''
    M=''
    N=''
    x=2
    while x<=len(lista):
    #in lettere le decine
        if x==2:
            if lista[-2]=='1':
                A=diecine[lista[-2:]]
            else:
                if lista[-1]=='1' or lista[-1]=='8':
                    B=decin[lista[-2]]
                else:
                    B=decine[lista[-2]]
    #in lettere le centinaia
        if x==3:
            if lista[-3]=='1':
                C='cento'
            elif lista[-3]=='0':
                C=''
            elif lista[-2]=='8':
                C=unita[lista[-3]]+'cent'
            else:
                C=unita[lista[-3]]+'cento'
    #in lettere le unità e decine di migliaia
        if x==4:
            if lista[-4]=='1':
                D='mille'
            else:
                D=unita[lista[-4]]+'mila'
        if x==5:
            D=unita[lista[-4]]
            if lista[-5]=='1':
                D=diecine[lista[-5:-3]]
            else:
                if lista[-4]=='1' or lista[-4]=='8':
                    E=decin[lista[-5]]
                else:
                    E=decine[lista[-5]]
            D=D+'mila'
    #centinaia di migliaia
        if x==6:  
            if lista[-6]=='1':
                F='cento'
            elif lista[-6]=='0':
                F=''
            elif lista[-5]=='8':
                F=unita[lista[-6]]+'cent'
            else:
                F=unita[lista[-6]]+'cento'
            if lista[-6:-3]=='000':
                D=''
            if lista[-6:-3]=='001':
                D='mille'

    #uni milioni e decine
        if x==7:
            if lista[-7]=='1':
                G='un milione'
            else:
                G=unita[lista[-7]]+'milioni'
        if x==8:
            G=unita[lista[-7]]
            if lista[-8]=='1':
                G=diecine[lista[-8:-6]]
            else:
                if lista[-7]=='1' or lista[-7]=='8':
                    H=decin[lista[-8]]
                else:
                    H=decine[lista[-8]]
            G=G+'milioni'
    #centinaia di milioni
        if x==9:
            if lista[-9]=='1':
                I='cento'
            elif lista[-9]=='0':
                I=''
            elif lista[-8]=='8':
                I=unita[lista[-9]]+'cent'
            else: 
                I=unita[lista[-9]]+'cento'
            if lista[-9:-6]=='000':
                G=''
            if lista[-9:-6]=='001':
                G='un milione'
    #uni e deca miliardi
        if x==10:
            if lista[-10]=='1':
                L='un miliardo'
            else:
                L=unita[lista[-10]]+'miliardi'
        if x==11:
            L=unita[lista[-10]]
            if lista[-11]=='1':
                L=diecine[lista[-11:-9]]
            else:
                if lista[-10]=='1' or lista[-10]=='8':
                    M=decin[lista[-11]]
                else:
                    M=decine[lista[-11]]
            L=L+'miliardi'
    #centinaia di miliardi
        if x==12:
            if lista[-12]=='1':
                N='cento'
            elif lista[-12]=='0':
                N=''
            elif lista[-11]=='8':
                N=unita[lista[-12]]+'cent'
            else:
                N=unita[lista[-12]]+'cento'
            if lista[-12:-9]=='000':
                L=''
            if lista[-12:-9]=='001':
                L='un miliardo'
        x=x+1
    return N+M+L+I+H+G+F+E+D+C+B+A
    





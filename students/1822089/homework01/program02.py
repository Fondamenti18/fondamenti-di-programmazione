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
    str=""
    if(n==0):
        str="zero"
    elif(n<10):
        str=strU(n)
    elif(n<20):
        str=str1D(n)
    elif(n<100):
        str=strDec(n)
    elif(n<1000):
        str=strCent(n)
    elif(n<10000):
        str=strMil(n) #migliaia
    elif(n<100000):
        str=strDecMil(n) #decine di migliaia
    elif(n<1000000):
        str=strCentMil(n) #centinaia di migliaia
    elif(n<10000000):
        str=strMilion(n) #milioni
    elif(n<100000000):
        str=strDecMilion(n) #decine di milioni
    elif(n<1000000000):
        str=strCentMilion(n) #centinaia di milioni
    elif(n<10000000000):
        str=strBillion(n) #miliardi
    elif(n<100000000000):
        str=strDecBillion(n) #decine di miliardi
    elif(n<1000000000000):
        str=strCentBillion(n) #centinaia di miliardi
    return str

#Unità
def strU(n):
    str_u=""
    if(n==1):
        str_u="uno"
    if(n==2):
        str_u="due"
    if(n==3):
        str_u="tre"
    if(n==4):
        str_u="quattro"
    if(n==5):
        str_u="cinque"
    if(n==6):
        str_u="sei"
    if(n==7):
        str_u="sette"
    if(n==8):
        str_u="otto"
    if(n==9):
        str_u="nove"
    
    return str_u

#Prima decina
def str1D(n):
    str_1d=""
    dici="dici"
    
    #Mi servirà per i numeri con più di 3 cifre
    if(n>=1 and n<10):
        str_1d=strU(n)
    else:
        if(n==10):
            str_1d="dieci"
        if(n==11):
            str_1d="un"+dici
        if(n==12):
            str_1d="do"+dici
        if(n==13):
            str_1d="tre"+dici
        if(n==14):
            str_1d="quattor"+dici
        if(n==15):
            str_1d="quin"+dici
        if(n==16):
            str_1d="se"+dici
        if(n==17):
            str_1d=dici+"assette"
        if(n==18):
            str_1d=dici+"otto"
        if(n==19):
            str_1d=dici+"annove"
    return str_1d

#Altre decine
def strDec(n):
    str_dec=""
    dec=""
    
    #Mi servirà per i numeri con più di 3 cifre
    if(n<20):
        str_dec=str1D(n)
    else:
        unit=int(str(n)[-1])#get unità
        
        if(n>=20 and n<30):#20
            dec="venti"
            if(n==20):
                str_dec=dec
            else:
                if(unit==1 or unit==8):
                    str_dec=dec[:4]+strU(unit)
                else:
                    str_dec=dec+strU(unit)
                    
        elif(n>=30 and n<40):#30
            dec="trenta"
            if(n==30):
                str_dec=dec
            else:
                if(unit==1 or unit==8):
                    str_dec=dec[:5]+strU(unit)
                else:
                    str_dec=dec+strU(unit)
            
        elif(n>=40 and n<50):#40
            dec="quaranta"
            if(n==40):
                str_dec=dec
            else:
                if(unit==1 or unit==8):
                    str_dec=dec[:7]+strU(unit)
                else:
                    str_dec=dec+strU(unit)
                    
        elif(n>=50 and n<60):#50
            dec="cinquanta"
            if(n==50):
                str_dec=dec
            else:
                if(unit==1 or unit==8):
                    str_dec=dec[:8]+strU(unit)
                else:
                    str_dec=dec+strU(unit)
                    
        elif(n>=60 and n<70):#60
            dec="sessanta"
            if(n==60):
                str_dec=dec
            else:
                if(unit==1 or unit==8):
                    str_dec=dec[:7]+strU(unit)
                else:
                    str_dec=dec+strU(unit)
                    
        elif(n>=70 and n<80):#70
            dec="settanta"
            if(n==70):
                str_dec=dec
            else:
                if(unit==1 or unit==8):
                    str_dec=dec[:7]+strU(unit)
                else:
                    str_dec=dec+strU(unit)
                    
        elif(n>=80 and n<90):#80
            dec="ottanta"
            if(n==80):
                str_dec=dec
            else:
                if(unit==1 or unit==8):
                    str_dec=dec[:6]+strU(unit)
                else:
                    str_dec=dec+strU(unit)
                    
        elif(n>=90 and n<100):#90
            dec="novanta"
            if(n==90):
                str_dec=dec
            else:
                if(unit==1 or unit==8):
                    str_dec=dec[:6]+strU(unit)
                else:
                    str_dec=dec+strU(unit)
                
    return str_dec

#Centinaia
def strCent(n):
    str_cent=""
    cent="cento"
    
    if(n<100):
        str_cent=strDec(n)
    else:
        dec=int(str(n)[-2:])#get decine-unità
        
        if(int(str(n)[-2])==8):#case: centinaia + decina 80
            cent="cent"
        
        if(n<200):#100
            str_cent=cent+strDec(dec)
        else:#200-999
            c=int(str(n)[-3])
            str_cent=strU(c)+cent+strDec(dec)
    
    return str_cent

#Migliaia
def strMil(n):
    str_mil=""
    mil=""
    
    if(n<1000):
        str_mil=strCent(n)
    else:
        cent=int(str(n)[-3:])#get centinaia-decine-unità
        
        if(int(str(n)[-4])==1):
            mil="mille"
            str_mil=mil+strCent(cent)
        else:
            mil="mila"
            str_mil=strU(int(str(n)[-4]))+mil+strCent(cent)
    
    
    return str_mil

#Decine di Migliaia
def strDecMil(n):
    str_decmil=""
    mil=""
    
    if(n<10000):
        str_decmil=strMil(n)
    else:
        cent=int(str(n)[-3:])#get centinaia-decine-unità
        decMil=int(str(n)[-5:-3])#get decine di migliaia
        mil="mila"
        
        str_decmil=strDec(decMil)+mil+strCent(cent)
        
    return str_decmil

#Centinaia di Migliaia
def strCentMil(n):
    str_centmil=""
    mil=""
    
    if(n<100000):
        str_centmil=strDecMil(n)
    else:
        cent=int(str(n)[-3:])#get centinaia-decine-unità
        centMil=int(str(n)[-6:-3])# get centinaia di migliaia
        mil="mila"
        
        str_centmil=strCent(centMil)+mil+strCent(cent)
    
    return str_centmil

#Milioni
def strMilion(n):
    str_milion=""
    mil=""
    
    if(n<1000000):
        str_milion=strCentMil(n)
    else:
        milion=int(str(n)[-7])#get milioni
        centMil=int(str(n)[-6:])#get centinaia di migliaia-decMigl-....unità
        
        if(milion==1):  
            mil="unmilione"
            str_milion=mil+strCentMil(centMil)
        else:
            mil="milioni"
            str_milion=strU(milion)+mil+strCentMil(centMil)
    
    return str_milion

#Decine di Milioni
def strDecMilion(n):
    str_decmilion=""
    
    if(n<10000000):
        str_decmilion=strMilion(n)
    else:
        decMilioni=int(str(n)[-8:-6])
        centMil=int(str(n)[-6:])
        str_decmilion=strDec(decMilioni)+"milioni"+strCentMil(centMil)
    return str_decmilion

#Centinaia di Milioni
def strCentMilion(n):
    str_centmilion=""
    
    if(n<100000000):
        str_centmilion=strDecMilion(n)
    else:
        centMilion=int(str(n)[-9:-6])
        centMil=int(str(n)[-6:])
        str_centmilion=strCent(centMilion)+"milioni"+strCentMil(centMil)
    
    return str_centmilion

#Miliardo
def strBillion(n):
    str_billion=""
    
    if(n<1000000000):
        str_billion=strCentMilion(n)
    else:
        billion=int(str(n)[-10])
        centMilion=int(str(n)[-9:])
        mil=""
        
        if(billion==1):
            mil="unmiliardo"
            str_billion=mil+strCentMilion(centMilion)
        else:
            mil="miliardi"
            str_billion=strU(billion)+mil+strCentMilion(centMilion)
            
    return str_billion

#Decine di Miliardi
def strDecBillion(n):
    str_decbillion=""
    
    if(n<10000000000):
        str_decbillion=strBillion(n)
    else:
        decBillion=int(str(n)[-11:-9])
        centMilion=int(str(n)[-9:])
        
        str_decbillion=strDec(decBillion)+"miliardi"+strCentMilion(centMilion)
        
    return str_decbillion

#Centinaia di Miliardi
def strCentBillion(n):
    str_centbillion=""
    
    if(n<100000000000):
        str_centbillion=strDecBillion(n)
    else:
        centBillion=int(str(n)[-12:-9])
        centMilion=int(str(n)[-9:])
        
        str_centbillion=strCent(centBillion)+"miliardi"+strCentMilion(centMilion)
    
    return str_centbillion

print(conv(508))



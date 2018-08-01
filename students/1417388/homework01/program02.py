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
    stl=""
    if(n <=20):
        stl=st2(n)
    elif n <100:
        stl=st3(n)
    elif n < 1000:
        stl=st4(n)
    elif n < 10000:
        stl=st5(n)
    elif n < 100000:
        stl=st6(n)
    elif n < 1000000:
        stl=st7(n)
    elif n < 10000000:
        stl=st8(n)
    elif n < 100000000:
        stl=st9(n)
    elif n < 1000000000:
       stl=st10(n)
    return stl

def st1(n1):
    stl=""
    if n1 == 1:
        stl+= "uno"
    if n1 == 2:
        stl+= "due"
    if n1 == 3:
        stl+= "tre"
    if n1 == 4:
        stl+= "quattro"
    if n1 == 5:
        stl+= "cinque"
    if n1 == 6:
        stl+= "sei"
    if n1 == 7:
        stl+= "sette"
    if n1 == 8:
        stl+= "otto"
    if n1 == 9:
        stl+= "nove"
    return stl

def st2(n2):
    stl=""
    if(n2 >=1 and n2 <= 10):
        stl+=st1(n2)
    if(n2>=10 and n2 <20):
        d="dici"
        if n2 == 10:
            stl+= "dieci"
        if n2==11:
            stl+="un" + d
        if n2==12:
            stl+="do" + d
        if n2==13:
            stl+="tre" + d
        if n2==14:
            stl+="quattor" + d
        if n2==15:
            stl+="quin" + d
        if n2==16:
            stl+="se" + d
        if n2==17:
            stl+= d + "assette"
        if n2==18:
            stl+= d + "otto"
        if n2==19:
            stl+= d + "annove"
    return stl

def st3(n3):
    stl=""
    if(n3 < 20):
        stl+=st2(n3)
    else:   
        if(n3 >= 20 and n3 < 30 ):
            n0=int(str(n3)[1:])
            v="venti"
            if(n3==20):
                stl+=v
            elif n0 == 1 or n0==8:
                stl+="vent" + st1(n0)
            else:
                stl+= v + st1(n0)
        if(n3 >= 30 and n3 < 40 ):
            n0=int(str(n3)[1:])
            t="trenta"
            if(n3==30):
                stl+=t
            elif n0 == 1 or n0==8:
                stl+="trent" + st1(n0)
            else:
                stl+= t + st1(n0)
        if(n3 >= 40 and n3 < 50 ):
            n0=int(str(n3)[1:])
            t="quaranta"
            if(n3==40):
                stl+=t
            elif n0 == 1 or n0==8:
                stl+="quarant" + st1(n0)
            else:
                stl+=t + st1(n0)
        if(n3 >= 50 and n3 < 60 ):
            n0=int(str(n3)[1:])
            t="cinquanta"
            if(n3==50):
                stl+=t
            elif n0 == 1 or n0==8:
                stl+="cinquant" + st1(n0)
            else:
                stl+=t+ st1(n0)
        if(n3 >= 60 and n3 < 70 ):
            n0=int(str(n3)[1:])
            t="sessanta"
            if(n3==60):
                stl+=t
            elif n0 == 1 or n0==8:
                stl+="sessant" + st1(n0)
            else:
                stl+=t+ st1(n0)
        if(n3 >= 70 and n3 < 80 ):
            n0=int(str(n3)[1:])
            t="settanta"
            if(n3==70):
                stl+=t
            elif n0 == 1 or n0==8:
                stl+="settant" + st1(n0)
            else:
                stl+=t+ st1(n0)
        if(n3 >= 80 and n3 < 90 ):
            n0=int(str(n3)[1:])
            t="ottanta"
            if(n3==80):
                stl+=t
            elif n0 == 1 or n0==8:
                stl+="ottant" + st1(n0)
            else:
                stl+=t+ st1(n0)
        if(n3 >= 90 and n3 < 100 ):
            n0=int(str(n3)[1:])
            t="novanta"
            if(n3==90):
                stl+=t
            elif n0 == 1 or n0==8:
                stl+="novant" + st1(n0)
            else:
                stl+=t+ st1(n0)
    return stl 

def st4(n4):
    stl=""
    s1=""
    s2=""
    c="cento"
    if(n4<100):
        stl+=st3(n4)
    else:
        if(n4 <=199):
            s2=int(str(n4)[1:3])
            stl+=c + st3(s2)
        else:
            s1=int(str(n4)[:1])
    
            s2=int(str(n4)[1:3])
            
            s3=int(str(s2)[:2])
            if(s3>=80 and s3<90):
                
                stl=st1(s1) + "cent" + st3(s2)
            else:
                 stl=st1(s1) + c + st3(s2)

    return stl

def st5(n5):
    stl=""
    s1=int(str(n5)[:1])
    s2=int(str(n5)[1:4])
    if(n5<1000): 
        stl+=st4(n5)
    else:
        if(s1==1):
            stl+="mille" + st4(s2)
        else:
            stl+= st1(s1) + "mila" + st4(s2)
    return stl

def st6(n6):
    stl=""
    s1=int(str(n6)[:2])
    s2=int(str(n6)[2:5])
    if(n6<10000): 
        stl+=st5(n6)
    else:   
        stl+= st3(s1) + "mila" + st4(s2)
    return stl

def st7(n7):
    stl=""
    s1=int(str(n7)[:3])
    s2=int(str(n7)[3:6])
    if(n7<100000): 
        stl+=st6(n7)
    else:
        stl+= st4(s1) + "mila" + st4(s2)
    return stl

def st8(n8):
    stl=""
    s1=int(str(n8)[:1])
    s2=int(str(n8)[1:7])
    if(n8<1000000):
        stl+=st7(n8)
    else:
        if(s1==1):
            stl+="un milione" + st7(s2)
        else:
            stl+= st1(s1) + "milioni" + st7(s2)
    return stl

def st9(n9):
    stl=""
    if(n9<10000000):
        stl+=st8(n9)
    else:
        s1=int(str(n9)[:2])
        s2=int(str(n9)[2:8])
        stl+= st3(s1) + "milioni" + st7(s2)
    return stl

def st10(n10):
    stl=""
    s1=int(str(n10)[:3])
    s2=int(str(n10)[3:9])
    if(n10<100000000):
        stl+=st9(n10)
    else:
        stl+= st4(s1) + "milioni" + st7(s2)
    return stl
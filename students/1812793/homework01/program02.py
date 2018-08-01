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
    numeri=["","uno","due","tre","quattro","cinque","sei","sette","otto","nove"]
    decine=["venti","trenta","quaranta","cinquanta","sessanta","settanta","ottanta","novanta"]
    
    num=str(n)
    l=len(num)
    if l==1:
        x=numeri[n]
    elif l==2:
        x=duecifre(numeri,decine,num,l)
    elif l==3:
        x=cento(num,l,numeri,decine)
    elif l>3 and l<7:
        x=mille(num,l,numeri,decine)
    elif l>6 and l<10:
        x=milione(num,l,numeri,decine)
    else:
        x=miliardo(num,l,numeri,decine)
    return x
    

def duecifre(numeri,decine,num,l):
    dieci=["dieci","undici","dodici","tredici","quattordici","quindici","sedici","diciassette","diciotto","diciannove"]
    if num[l-2]=="0":
        return numeri[int(num[l-1])]
    if num[l-2]=="1":
        return dieci[int(num[-2:])-10]
    else:
        x=int(num[l-2])
        y=int(num[l-1])
        a=decine[x-2]
        if y==1 or y==8:
            return a[0:len(a)-1]+numeri[y]
        else:
            return a+numeri[y]
        
def cento(num,l,numeri,decine):
    if num[l-2]=="8":
        if num[l-3]=="1":
            s="cent"+duecifre(numeri,decine,num,l)
        elif num[l-3]=="0":
            s=numeri[int(num[l-3])]+duecifre(numeri,decine,num,l)
        else:
            s=numeri[int(num[l-3])]+"cent"+duecifre(numeri,decine,num,l)
    else:
        if num[l-3]=="1":
            s="cento"+duecifre(numeri,decine,num,l)
        elif num[l-3]=="0":
            s=numeri[int(num[l-3])]+duecifre(numeri,decine,num,l)
        else:
            s=numeri[int(num[l-3])]+"cento"+duecifre(numeri,decine,num,l)
    return s

def mille(num,l,numeri,decine):
    if l==4:
        if num[l-4]=="1":
            s="mille"+cento(num,l,numeri,decine)
        else:
            s=numeri[int(num[l-4])]+"mila"+cento(num,l,numeri,decine)
    elif l==5:
        s=duecifre(numeri,decine,num[l-5:l-3],len(num[l-5:l-3]))+"mila"+cento(num,l,numeri,decine)
    else:
        if num[l-6:l-3]=="000":
            s=cento(num,l,numeri,decine)
        else:
            s=cento(num[l-6:l-3],len(num[l-6:l-3]),numeri,decine)+"mila"+cento(num,l,numeri,decine)
    return s

def milione(num,l,numeri,decine):
    if l==7:
        if num[l-7]=="1":
            s="unmilione"+mille(num[l-6:l],len(num[l-6:l]),numeri,decine)
        else:
            s=numeri[int(num[l-7])]+"milioni"+mille(num[l-6:l],len(num[l-6:l]),numeri,decine)
    elif l==8:
        s=duecifre(numeri,decine,num[l-8:l-6],len(num[l-8:l-6]))+"milioni"+mille(num[l-6:l],len(num[l-6:l]),numeri,decine)
    else:
        if num[l-9:l-6]=="000":
            s=mille(num,l,numeri,decine)
        else:
            s=cento(num[l-9:l-6],len(num[l-9:l-6]),numeri,decine)+"milioni"+mille(num[l-6:l],len(num[l-6:l]),numeri,decine)
    return s

def miliardo(num,l,numeri,decine):
    num1=num[1:].strip("0")
    if l==10:
        if num[l-10]=="1":
            if num1[0]=="8":
                s="unmiliard"+milione(num[l-9:l],len(num[l-9:l]),numeri,decine)
            else:
                s="unmiliardo"+milione(num[l-9:l],len(num[l-9:l]),numeri,decine)
        else:
            s=numeri[int(num[l-10])]+"miliardi"+milione(num[l-9:l],len(num[l-9:l]),numeri,decine)
    elif l==11:
        s=duecifre(numeri,decine,num[l-11:l-9],len(num[l-11:l-9]))+"miliardi"+milione(num[l-9:l],len(num[l-9:l]),numeri,decine)
    else:
        s=cento(num[l-12:l-9],len(num[l-12:l-9]),numeri,decine)+"miliardi"+milione(num[l-9:l],len(num[l-9:l]),numeri,decine)
    return s
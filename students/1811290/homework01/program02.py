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

y=''
f=''
unita_numeri=[0,1,2,3,4,5,6,7,8,9]
unitanozero=[1,2,3,4,5,6,7,8,9]
numeri1019=[10,11,12,13,14,15,16,17,18,19]
decineintere=[20,30,40,50,60,70,80,90]
decine_primo=[2,3,4,5,6,7,8,9]
centinaioelisione=[1,2,3,4,5,6,7,8,9]
unita_scritte=['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
unita_nozero=['uno','due','tre','quattro','cinque','sei','sette','otto','nove']
numeri_1019=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
decine_intere=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
decine_scritte=['vent','trent','quarant','cinquant','sessant','settant','ottant','novant']

def conv(n):
    a=len(str(n))
    b=a//3
    c=a%3
    f=''
    global s
    if verifica(n)==True:
        if a<=3:
            f+=blocco(n)
        elif a<=6:
            f+=blocco2(n)
            f+=blocco21(n)
        elif a<=9:
            f+=blocco3(n)
            f+=blocco31(n)
            f+=blocco32(n)
        elif a<=12:
            f+=blocco4(n)
            f+=blocco41(n)
            f+=blocco42(n)
            f+=blocco43(n)
    return f
    
    

    




def blocco(n):
    a=str(n)
    b=len(a)
    c=int(a)
    s=''
    if c<=19:
        s=''
        s+=da0a19(c)
    elif c<=99:
        s=''
        s+=decine(c)
        s+=unita(c)
    elif c<=199:
        s=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
    elif c<=999:
        s=''
        s+=contatore3(c)
        s+=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
    return s

def blocco2(n):
    a=str(n)
    b=len(a)
    d=b//3
    h=b%3
    t=0
    T=b-3
    c=a[t:T]
    c=int(c)
    if c==1:
        s=mila(c)
    elif c<=19:
        s=''
        s+=da0a19(c)#da modificare: levare 0 e 1 farla partire da 2
        s+=mila(c)
    elif c<=99:
        s=''
        s+=decine(c)
        s+=unita(c)
        s+=mila(c)
    elif c<=199:
        s=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=mila(c)
    elif c<=999:
        s=''
        s+=contatore3(c)
        s+=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=mila(c)
    return s

def blocco21(n):
    a=str(n)
    b=len(a)
    t=b-3
    T=b
    c=a[t:T]
    c=int(c)
    if c<=19:
        s=''
        s+=da0a19(c)
    elif c<=99:
        s=''
        s+=decine(c)
        s+=unita(c)
    elif c<=199:
        s=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
    elif c<=999:
        s=''
        s+=contatore3(c)
        s+=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
    return s
    

def blocco3(n):
    a=str(n)
    b=len(a)
    d=b//3
    h=b%3
    t=0
    T=b-6
    c=a[t:T]
    c=int(c)
    if c==1:
        s=milioni(c)
    elif c<=19:
        s=''
        s+=da0a19(c)#da modificare: levare 0 e 1 farla partire da 2
        s+=milioni(c)
    elif c<=99:
        s=''
        s+=decine(c)
        s+=unita(c)
        s+=milioni(c)
    elif c<=199:
        s=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=milioni(c)
    elif c<=999:
        s=''
        s+=contatore3(c)
        s+=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=milioni(c)
    return s

def blocco31(n):
    a=str(n)
    b=len(a)
    d=b//3
    h=b%3
    t=b-6
    T=b-3
    c=a[t:T]
    c=int(c)
    if c==1:
        s=mila(c)
    elif c<=19:
        s=''
        s+=da0a19(c)#da modificare: levare 0 e 1 farla partire da 2
        s+=mila(c)
    elif c<=99:
        s=''
        s+=decine(c)
        s+=unita(c)
        s+=mila(c)
    elif c<=199:
        s=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=mila(c)
    elif c<=999:
        s=''
        s+=contatore3(c)
        s+=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=mila(c)
    return s

def blocco32(n):
    a=str(n)
    b=len(a)
    t=b-3
    T=b
    c=a[t:T]
    c=int(c)
    if c<=19:
        s=''
        s+=da0a19(c)
    elif c<=99:
        s=''
        s+=decine(c)
        s+=unita(c)
    elif c<=199:
        s=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
    elif c<=999:
        s=''
        s+=contatore3(c)
        s+=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
    return s


def blocco4(n):
    a=str(n)
    b=len(a)
    d=b//3
    h=b%3
    t=0
    T=b-9
    c=a[t:T]
    c=int(c)
    if c==1:
        s=miliardi(c)
    elif c<=19:
        s=''
        s+=da0a19(c)#da modificare: levare 0 e 1 farla partire da 2
        s+=miliardi(c)
    elif c<=99:
        s=''
        s+=decine(c)
        s+=unita(c)
        s+=miliardi(c)
    elif c<=199:
        s=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=miliardi(c)
    elif c<=999:
        s=''
        s+=contatore3(c)
        s+=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=miliardi(c)
    return s

def blocco41(n):
    a=str(n)
    b=len(a)
    d=b//3
    h=b%3
    t=b-9
    T=b-6
    c=a[t:T]
    c=int(c)
    if c==1:
        s=milioni(c)
    elif c<=19:
        s=''
        s+=da0a19(c)#da modificare: levare 0 e 1 farla partire da 2
        s+=milioni(c)
    elif c<=99:
        s=''
        s+=decine(c)
        s+=unita(c)
        s+=milioni(c)
    elif c<=199:
        s=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=milioni(c)
    elif c<=999:
        s=''
        s+=contatore3(c)
        s+=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=milioni(c)
    return s

def blocco42(n):
    a=str(n)
    b=len(a)
    d=b//3
    h=b%3
    t=b-6
    T=b-3
    c=a[t:T]
    c=int(c)
    if c==1:
        s=mila(c)
    elif c<=19:
        s=''
        s+=da0a19(c)#da modificare: levare 0 e 1 farla partire da 2
        s+=mila(c)
    elif c<=99:
        s=''
        s+=decine(c)
        s+=unita(c)
        s+=mila(c)
    elif c<=199:
        s=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=mila(c)
    elif c<=999:
        s=''
        s+=contatore3(c)
        s+=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
        s+=mila(c)
    return s

def blocco43(n):
    a=str(n)
    b=len(a)
    t=b-3
    T=b
    c=a[t:T]
    c=int(c)
    if c<=19:
        s=''
        s+=da0a19(c)
    elif c<=99:
        s=''
        s+=decine(c)
        s+=unita(c)
    elif c<=199:
        s=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
    elif c<=999:
        s=''
        s+=contatore3(c)
        s+=centinaio(c)
        s+=decine3(c)
        s+=unita3(c)
    return s


#verifica

def verifica(n):
    if 0<n<1000000000000:
        return True
        print(true)
    return False
    
#nomi valori

def centinaio(c):
    s=''
    f=str(c)
    t=f[0]
    t=int(t)
    if t in centinaioelisione:
        f=f[1:3]
        if int(f[0])==8:
            s+='cent'
        else:
            s+='cento'
    return s

def mila(c):
    s=''
    if c==0:
        pass
    elif c==1:
        s+='mille'
    elif c>1:
        s+='mila'
    return s

def milioni(c):
    s=''
    if c==0:
        pass
    elif c==1:
        s+='unmilione'
    elif c>1:
        s+='milioni'
    return s

def miliardi(c):
    s=''
    if c==0:
        pass
    elif c==1:
        s+='unmiliardo'
    elif c>1:
        s+='miliardi'
    return s

#calcolatori 3

def decine3(c):
    s=''
    c=str(c)
    c=c[1:3]
    c=int(c)
    if c in numeri1019:
        i=0
        for x in numeri1019:
            if x==c:
                s+=numeri_1019[i]
                break
            i+=1
    elif 20<=c<=99:
        if c in decineintere:
            i=0
            for x in decineintere:
                if c==x: #se x [numeri3] uguale a n
                    y=decine_intere[i]
                    s+=y
                    break
                i+=1
        else:
            t=str(c)
            if int(t[0]) in decine_primo:
                if int(t[1])==1 or int(t[1])==8:
                    i=0
                    for x in decine_primo:
                        if x==int(t[0]):
                            s+=decine_scritte[i]
                            break
                        
                        i+=1
                else:
                    i=0
                    for x in decine_primo:
                        if x==int(t[0]):
                            s+=decine_intere[i]
                            break
                        i+=1
    return s

def unita3(c):
    s=''
    t=str(c)
    t=t[1:3]
    if int(t) in numeri1019:
        pass
    elif int(t[1]) in unita_numeri:
        if int(t) in decineintere:
            pass
        elif int(t[1])!=0:
                i=0
                for x in unitanozero:
                    if x==int(t[1]):
                        s+=unita_nozero[i]
                        break
                    i+=1
    return s

def contatore3(c):
    t=str(c)
    t=t[0:1]
    i=0
    s=''
    t=int(t)
    for x in unita_numeri:
        if x==t:
            s+=unita_scritte[i]
            break
        i+=1
    return s
    
#calcolatori 2 


def decine(c):
    s=''
    if 20<=c<=99:
        if c in decineintere:
            i=0
            for x in decineintere:
                if c==x: #se x [numeri3] uguale a n
                    y=decine_intere[i]
                    s+=y
                    break
                i+=1
        else:
            t=str(c)
            if int(t[0]) in decine_primo:
                if int(t[1])==1 or int(t[1])==8:
                    i=0
                    for x in decine_primo:
                        if x==int(t[0]):
                            s+=decine_scritte[i]
                            break
                        i+=1
                else:
                    i=0
                    for x in decine_primo:
                        if x==int(t[0]):
                            s+=decine_intere[i]
                            break
                        i+=1
    return s


def unita(c):
    s=''
    t=str(c)
    if c==0:
        pass
    elif int(t[1]) in unita_numeri:
        if int(t) in decineintere:
            pass
        elif int(t[1])!=0:
                i=0
                for x in unitanozero:
                    if x==int(t[1]):
                        s+=unita_nozero[i]
                        break
                    i+=1
    return s


def da0a19(c):
    s=''
    if verifica(c)==True:
        if 1<=c<=19:
            if c in unita_numeri:
                i=0
                for x in unita_numeri:
                    if c==x:
                       s+=unita_scritte[i]
                       break
                    i+=1
            elif c in numeri1019:
                i=0
                for x in numeri1019:
                    if c==x: #se x [numeri1019] uguale a n
                        s+=numeri_1019[i]
                        break
                    i+=1
    return s


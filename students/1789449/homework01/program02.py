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

if(m == "uno"):
        if(10<=mm<=19):
            mm=from10to19(mm)
            if(10<=du<=19):
                du=from10to19(du)
                return m6+m5+m4+m3+mm+"mila"+c+du
            else:        
                if(d=="ottanta")or(d=="ottant"):
                    c=c[:-1]
                    return m6+m5+m4+m3+mm+"mila"+c+d+u
                else:
                    return m6+m5+m4+m3+mm+"mila"+c+d+u
        else:
            if(10<=du<=19):
                du=from10to19(du)
                return m6+m5+m4+m3+m2+"mila"+c+du
            else:        
                if(d=="ottanta")or(d=="ottant"):
                    c=c[:-1]
                    print(m2)
                    return m6+m5+m4+m3+m2+"mille"+c+d+u
                else:
                    print(m2)
                    return m6+m5+m4+m3+m2+"mille"+c+d+u
        
    else:
        if(10<=du<=19):
            du=from10to19(du)
            return m6+m5+m4+m3+m2+m+"mila"+c+du
        else:        
            if(d=="ottanta")or(d=="ottant"):
                c=c[:-1]
                if(10<=mm<=19):
                    mm=from10to19(mm)
                    return m6+m5+m4+m3+mm+"mila"+c+d+u
                else:
                    return m6+m5+m4+m3+m2+m+"mila"+c+d+u
            else:
                if(10<=mm<=19):
                    mm=from10to19(mm)
                    return m6+m5+m4+m3+mm+"mila"+c+d+u
                else:
                    return m6+m5+m4+m3+m2+m+"mila"+c+d+u
ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def from0to9(n):
    switch = {
        0:  "",
        1:  "uno",
        2:  "due",
        3:  "tre",
        4:  "quattro",
        5:  "cinque",
        6:  "sei",
        7:  "sette",
        8:  "otto",
        9:  "nove"
    }
    return switch.get(n)

def ten(n):
    switch = {
        0: "",
        1: "uno",
        2: "venti",
        3: "trenta",
        4: "quaranta",
        5: "cinquanta",
        6: "sessanta",
        7: "settanta",
        8: "ottanta",
        9: "novanta"
    }
    return switch.get(n)

def hundreds(n):
    switch = {
        0: "",
        1: "cento",
        2: "duecento",
        3: "trecento",
        4: "quattrocento",
        5: "cinquecento",
        6: "seicento",
        7: "settecente",
        8: "ottocento",
        9: "novecento"
    }
    return switch.get(n)

def from10to19(n):
    switch = {
        0: "",
        10: "dieci",
        11: "undici",
        12: "dodici",
        13: "tredici",
        14: "quattordici",
        15: "quindici",
        16: "sedici",
        17: "diciassette",
        18: "diciotto",
        19: "diciannove"
    }
    return switch.get(n)

def decine(n):
    d = int(n/10)
    u = int(n%10)
    #print(n)
    d = ten(d)
    if(u == 1) or (u == 8):
        d = d[:-1]
        #print(d)
    u = from0to9(u)
    if(u == "zero"):
        u = ""
        
    return d         

def centinaia(n):
    um=n//10**2
    den=""
    if(n//10**2==1):
        return "cento"
    elif 9>=um >=2 :
        if(89>=n%100 >= 80):
            den+= from0to9(um)+"cent"
            um=n%(100*um)
        else:
            #print(n%100)
            den+= from0to9(um)+"cento"
            #print(den)
            um=n%(100)
            #print(um)
        #if(20<=um<=99):
            #den+=decine(um)
            #print(um)
            #um=um%10
            #print(um)
        #elif 19<=um<=10:
            #den+=from10to19(um)
            #um=um%10
            #print(um)
        
    return den
        
    
    
    
    
def migliaia(n):
    
    den=""
    um=n//10**3
    if(n//10**3==1):
        return "mille"
    if 999>= um >=100:
        den+= centinaia(um)
        um=um%100
    if 99>= um >=20:
        den+= decine(um)
        um=um%10
        #☺print(den)
    elif 19>= um >=10:
        den+= from10to19(um)
        #print(um)
        
        
    if 9>=um >=1 :
        den+= from0to9(um)
    #print(den)
    return den+"mila"
    
    

def milioni(n):
    den=""
    #print(n//10**6)
    um=n//10**6
    #print(um)
    if(n//10**6==1):
        return "unmilione"
    if 999>= um >=100:
        #print(um)
        den+= centinaia(um)
        um=um%100

    if 99>= um >=20:
        den+= decine(um)
        um=um%10
    elif 19>= um >=10:
        den+= from10to19(um)
        
    #print(um)
    if 9>=um >=1 :
        den+= from0to9(um)
    return den+"milioni"
def miliardi(n):
    den=""
    #print(n//10**6)
    um=n//10**9
    #print(um)
    if(n//10**9==1):
        return "unmiliardo"
    if 999>= um >=100:
        #print(um)
        den+= centinaia(um)
        um=um%100

    if 99>= um >=20:
        den+= decine(um)
        um=um%10
    elif 19>= um >=10:
        den+= from10to19(um)
        
    #print(um)
    if 9>=um >=1 :
        den+= from0to9(um)
    return den+"miliardi"        
    
    

def conv(n):
    'Scrivete qui il codice della funzione'
    denominazione=""
    n1=n
    if(type(n)==int):
        if(0<n<1000000000000):
            if(1000000000<=n1<=999999999999):
                denominazione+=(miliardi(n1))
                n1=n%10**9
            if(1000000<=n1<=999999999):
                denominazione+=(milioni(n1))
                #print(n1)
                n1=n%10**6
            if(1000<=n1<=999999):
                #print(n1)
                denominazione+=(migliaia(n1))
                n1=n%10**3
                #print(n1)
            if(100<=n1<=999):
                #print(n1)
                denominazione+=(centinaia(n1))
                n1=n%10**2
                #print(n1)
            if(20<=n1<=99):
                denominazione+=(decine(n1))
                n1=n%10
                #print(n1)
            if(10<=n1<=19):
                denominazione+=(from10to19(n1))
            
            if(0<n1<=9):
                denominazione+=(from0to9(n1))
            
            
    return denominazione
            
          
            
print(conv(68258148238))
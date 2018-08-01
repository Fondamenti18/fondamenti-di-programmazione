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
def decimals(n):
    num=""
    if n == 1 :
        num = "uno"
    elif n == 2 :
        num = "due"
    elif n == 3 :
        num = "tre"
    elif n == 4 :
        num = "quattro"
    elif n == 5 :
        num = "cinque"
    elif n == 6 :
        num = "sei"
    elif n == 7 :
        num = "sette"
    elif n == 8 :
        num = "otto"
    elif n == 9 :
        num = "nove"
    elif n == 10 :
        num = "dieci"
    elif n == 11 :
        num = "undici"
    elif n == 12 :
        num = "dodici"
    elif n == 13 :
        num = "tredici"
    elif n == 14 :
        num = "quattordici"
    elif n == 15 :
        num = "quindici"
    elif n == 16 :
        num = "sedici"
    elif n == 17 :
        num = "diciassette"
    elif n == 18 :
        num = "diciotto"
    elif n == 19 :
        num = "diciannove"
    return num


def decimalsup20(n):
    word = ""
    n=str(n)
    dec=int(n[0])*10+int(n[1])
     
    if dec>19 and dec<30:
        if int(n[1])==0:
            word=word+"venti"
            return word
        elif int(n[1])==1 or int(n[1])==8:
            word=word+"vent"+decimals(int(n[1]))
            return word
        else:
            word=word+"venti"+decimals(int(n[1]))
            return word
        
    elif dec>29 and dec<40:
        if int(n[1])==0:
            word=word+"trenta"
            return word
        elif int(n[1])==1 or int(n[1])==8:
            word=word+"trent"+decimals(int(n[1]))
            return word
        else:
            word=word+"trenta"+decimals(int(n[1]))
            return word
        
    elif dec>39 and dec<50:
        if int(n[1])==0:
            word=word+"quaranta"
            return word
        elif int(n[1])==1 or int(n[1])==8:
            word=word+"quarant"+decimals(int(n[1]))
            return word
        else:
            word=word+"quaranta"+decimals(int(n[1]))
            return word
        
    elif dec>49 and dec<60:   
        if int(n[1])==0:
            word=word+"cinquanta"
            return word
        elif int(n[1])==1 or int(n[1])==8:
            word=word+"cinquant"+decimals(int(n[1]))
            return word
        else:
            word=word+"cinquanta"+decimals(int(n[1]))
            return word
        
    elif dec>59 and dec<70: 
        if int(n[1])==0:
            word=word+"sessanta"
            return word
        elif int(n[1])==1 or int(n[1])==8:
            word=word+"sessant"+decimals(int(n[1]))
            return word
        else:
            word=word+"sessanta"+decimals(int(n[1]))
            return word
        
    elif dec>69 and dec<80:
        if int(n[1])==0:
            word=word+"settanta"
            return word
        elif int(n[1])==1 or int(n[1])==8:
            word=word+"settant"+decimals(int(n[1]))
            return word
        else:
            word=word+"settanta"+decimals(int(n[1]))
            return word
        
    elif dec>79 and dec<90:
        if int(n[1])==0:
            word=word+"ottanta"
            return word
        elif int(n[1])==1 or int(n[1])==8:
            word=word+"ottant"+decimals(int(n[1]))
            return word
        else:
            word=word+"ottanta"+decimals(int(n[1]))
            return word
        
    elif dec>89 and dec<100:
        if int(n[1])==0:
            word=word+"novanta"
            return word
        elif int(n[1])==1 or int(n[1])==8:
            word=word+"novant"+decimals(int(n[1]))
            return word
        else:
            word=word+"novanta"+decimals(int(n[1]))
            return word    



def figurestoword(n):
    word=""
    
    #decine e unita'
    if n<20:
        word=word+decimals(n)
        return word
    if n<100:
        word=word+decimalsup20(n)
        return word
    #centinaia
    n=str(n)
    dec=int(n[1])*10+int(n[2])
    
    if int(n[0])>0:
        if int(n[0])==1:
            if int(n[1])==8:
                word=word+"cent"
            else:
                word=word+"cento"
        elif int(n[0])>1:
            if int(n[1])==8:
                word=word+decimals(int(n[0]))+"cent"
            else:
                word=word+decimals(int(n[0]))+"cento"
    #decine in centinaia
    if dec<20:
        word=word+decimals(dec)
        return word
    elif dec>19:
        word=word+decimalsup20(dec)
        return word
    return word



def conv(n):
    word=""
    cento=""
    mille=""
    milione=""
    miliardo=""
    #init divisore di numero in gruppi di 3 cifre
    c=0
    c2=0
    z=""
    lis=[]
    n=str(n)
    n=n[::-1]
    for x in n:
        z=z+x
        c+=1
        c2+=1
        if c==3:
            z=z[::-1]
            lis.append(int(z))
            z= ""
            c=0
        elif c2==len(str(n)):
            z=z[::-1]
            lis.append(int(z))
            
    
    if len(lis)>3:
        if lis[3]==1:
            miliardo="unmiliardo"
        elif lis[3]>1:
            miliardo= figurestoword(lis[3]) + "miliardi"
    if len(lis)>2:
        if lis[2]==1:
            milione="unmilione"
        elif lis[2]>1:
            milione = figurestoword(lis[2]) + "milioni" 
    if len(lis)>1:
        if lis[1]==1:
            mille="mille"
        elif lis[1]>1:
            mille= figurestoword(lis[1]) + "mila"
    
    cento=figurestoword(lis[0])
    word=miliardo+milione+mille+cento
    return word
    
    
    
    

    
    
    
    
    
    
    
    
    
    

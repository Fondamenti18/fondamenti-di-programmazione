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
    if n==0:
        return('')
    elif n<=19:
        return ('uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','dicianove')[n-1]
   
    elif n<=99:
        if n%10==0:
            if n==20:
                return('venti')
            elif n==30:
                return('trenta')
            elif n==40:
                return('quaranta')
            elif n==50:
                return('cinquanta')
            elif n==60:
                return('sessanta')
            elif n==70:
                return('settanta')
            elif n==80:
                return('ottanta')
            elif n==90:
                return('novanta')
                
        elif n%10!=0 and n<100:
            t=conv(n%10)
            e=n-(n%10)
          
            if conv(e)=='venti':
                if t=='uno' or t=='otto':
                    e='venti'[:-1]
                    return(e+t)
                else:
                    return(conv(e)+t)
                    
            elif conv(e)=='trenta':
                if t=='uno' or t=='otto':
                    e='trenta'[:-1]
                    return(e+t)
                else:
                    return(conv(e)+t)
                    
            elif conv(e)=='quaranta':
                if t=='uno' or t=='otto':
                    e='quaranta'[:-1]
                    return(e+t)
                else:
                    return(conv(e)+t)
                    
            elif conv(e)=='cinquanta':
                if t=='uno' or t=='otto':
                    e='cinquanta'[:-1]
                    return(e+t)
                else:
                    return(conv(e)+t)
                    
            elif conv(e)=='sessanta':
                if t=='uno' or t=='otto':
                    e='sessanta'[:-1]
                    return(e+t)
                else:
                    return(conv(e)+t)
                    
            elif conv(e)=='settanta':
                if t=='uno' or t=='otto':
                    e='settanta'[:-1]
                    return(e+t)
                else:
                    return(conv(e)+t) 
             
            elif conv(e)=='ottanta':
                if t=='uno' or t=='otto':
                    e='ottanta'[:-1]
                    return(e+t)
                else:
                    return(conv(e)+t)
                    
            elif conv(e)=='novanta':
                if t=='uno' or t=='otto':
                    e='novanta'[:-1]
                    return(e+t)
                else:
                    return(conv(e)+t)
                    
    elif n<200:
        e=conv(n%100)
        if e==80:
            t='cento'[:-1]
            return(t+e)
        else:
            return('cento'+e)
            
            
    elif n<1000:
        t=conv(n//100)
        e=conv(n%100)
        if e=='ottanta' or e=='ottantuno' or e=='ottantadue' or e=='ottantatre':
            l='cento'[:-1]
            return(t+l+e)
        elif e=='ottantaquattro' or e=='ottantacinque' or e=='ottantasei':
            l='cento'[:-1]
            return(t+l+e)
        elif e=='ottantasette' or e=='ottantotto' or e=='ottantanove':
            l='cento'[:-1]
            return(t+l+e)
        else:
            return(t+'cento'+e)
        
    elif n<2000:
        t=conv(n%1000)
        return('mille'+t)
        
    elif n<10000:
        t=conv(n//1000)
        e=conv(n%1000)
        return(t+'mila'+e)
    
    elif n<1000000:
        t=conv(n//1000)
        e=conv(n%1000)
        return(t+'mila'+e)
    
    elif n<2000000:
        t=conv(n%1000000)
        return('un milione'+t)
        
    elif n<1000000000:
        t=conv(n//1000000)
        e=conv(n%1000000)
        return(t+'milioni'+e)
     
    elif n<2000000000:
        t=conv(n%1000000)
        return('un miliardo'+t)
    
    elif n<1000000000000:
        t=conv(n//1000000000)
        e=conv(n%1000000000)
        return(t+'miliardi'+e)
 

 

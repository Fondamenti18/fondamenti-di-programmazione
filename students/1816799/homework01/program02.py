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
    ls=[int(x) for x in str(n)] #prendi n, scompattalo e metti ogni numero in ls
    a=list(reversed(ls)) #capovolgi la lista per partire dalle unità
    
    lso=[]
    i=0
    while i<=12-len(a): #incrementa i fino al numero massimo di numeri utilizzati in n
        lso.append(0)
        i+=1
    a.extend(lso)

    suf=['','mila', 'milioni', 'miliardi']
    sufs=['', 'mille', 'unmilione', 'unmiliardo']    
    
    i=0
    x=0
    word=[]
    while i<len(a)//3:
        u=centinaia(a[x+2])+decine(a[x+1])+unita(a[x])
        
        if a[x+2]*100 + a[x+1]*10 + a[x]==1:
            u=sufs[i]
            word.append(u)
        elif a[(x+1)]*10 + a[x]<20 and decine(a[(x+1)])!='' :
            u=centinaia(a[x+2])+stronzi(a[x])
            u+=suf[i]
            word.append(u)
            print(u)
        elif  u!='':  
            u+=suf[i]
            word.append(u)
                    
        i+=1
        x+=3
        
    fword=list(reversed(word))        
    return ''.join(fword)
        
def unita(n):
    ls=['', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
    return ls[n]
    
def stronzi(n):
    ls=['', 'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    return ls[n]

def decine(n):
    ls=['','dieci','vent', 'trent', 'quarant', 'cinquant', 'sessant', 'settant', 'ottant', 'novant']
    return ls[n]         
                             
def centinaia(n):
    ls=['','cento','duecento', 'trecento', 'quattrocento', 'cinquecento', 'seicento', 'settecento', 'ottocento', 'novecento']
    return ls[n]         
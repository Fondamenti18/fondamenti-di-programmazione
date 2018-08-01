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


def letnum(n):
    letnumU = ['zero','uno', 'due', 'tre','quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
    letnumDD = ['dieci', 'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    letnumD = ['', '', 'venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']
    letnumDeli = ['', '', 'vent', 'trent', 'quarant', 'cinquant', 'sessant', 'settant', 'ottant', 'novant']
    letnumH = ['', 'cento', 'duecento', 'trecento', 'quattrocento', 'cinquecento', 'seicento', 'settecento', 'ottocento', 'novecento']
    letnumHeli = ['', 'cent', 'duecent', 'trecent', 'quattrocent', 'cinquecent', 'seicent', 'settecent', 'ottocent', 'novecent']
    st = ''
    
    u = n % 10
    n = n // 10
    d = n % 10
    n = n // 10
    h = n % 10
    
    if h!= 0:
        if d == 8:
            st += letnumHeli[h]
            
        else:
            st += letnumH[h]
        
    if d == 1:
        st += letnumDD[u]
        
    if d != 0 and d != 1:
        if u == 1 or u == 8:
            st = st + letnumDeli[d] + letnumU[u]
        else:
            st = st + letnumD[d] + letnum[u]
            
    if d == 0:
        st += letnumU[u]
        
        
    return st

def conv(n):
    
    pesi = ['','mila','milioni','miliardi', 'trilioni']
    
    u = n % 1000
    n = n // 1000
    direpesiU = letnum(u)
    if n != 0 and u == 0:
        letc = ''
    else:
        letc = direpesiU 
        
    if n != 0:
        k = n % 1000
        n = n // 1000
        direpesiK = letnum(k)
        if k == 0:
            letc = '' + letc
        else:
            if k == 1:
                letc = 'mille' + letc
            else:
                letc = direpesiK + pesi[1] + letc
        
    if n != 0:
        m = n % 1000
        n = n // 1000
        direpesiM = letnum(m)
        if m == 0:
            letc = '' + letc
        else:
            if m == 1:
                letc = 'unmilione' + letc
            else:
                letc = direpesiM + pesi[2] + letc
                
        if n != 0:
            g = n % 1000
            n = n // 1000
            direpesiG = letnum(g)
            if g == 0:
                letc = '' + letc
            else:
                if g == 1:
                    letc = 'unmiliardo' + letc
                else:
                    letc = direpesiG + pesi[3] + letc
                    
            if n != 0:
                t = n % 1000
                n = n // 1000
                direpesiT = letnum(t)
                if t == 0:
                    letc = '' + letc
                else:
                    if t == 1:
                        letc = 'untrilione' + letc
                    else:
                        letc = direpesiT + pesi[4] + letc
                        
    return letc
    print(letc)
    
   
             
        
        
            
    
        
    
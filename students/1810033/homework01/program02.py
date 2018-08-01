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



def st(n):
    s=''
    c=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    s=c[n]
    return s
def scritta(n):
    l=str(n)
    l = l.zfill(3)
    l=list(l)
    s=''
    a=['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    c=['uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','dicinnove',]

    if l[1]=='1':
       s = c[int(l[2])+9]
    if (l[1])!= '1':
        if l[2]== '8' or l[2]== '1' :
            s= a[int(l[1])][:-1] + st(int(l[2]))
        else:
          s= a[int(l[1])] + st(int(l[2]))
        
    if l[0]=='1':
        
        if l[1]=='8':
            s='cent'+s
        else:
             s='cento'+s
    if int(l[0])>1:
         if l[1]=='8':
             s=st(int(l[0])) + 'cent'+s
         else:
             s=st(int(l[0])) + 'cento'+s
    
    
    
    
    return s

def conv(n):
    t=0
    m=''
    c=''
    l=list(str(n))
    h=[]
    o=[]
    for i in range (len(l)-3,0,-3):
        l.insert(i,' ')
    for i in l :
        c = c+i
    c=c.split(' ')
    for i in range(0,len(c)) :
        c[i]=int(c[i])
    h=list(c)
    h.reverse()
    for i in h:
        
        
        if t == 1:
            if h[1]==1:
                o.append( 'mille')
                
            else:
               o.append( scritta(i) + 'mila')
            t=t+1
            continue
        if t == 2 :
            if h[2]==1:
                o.append( 'unmilione')
            o.append(scritta(i) + 'milioni' )
            t=t+1
            continue
        if t == 3 :
            if h[3]==1:
                o.append( 'unmiliardo')
            o.append(scritta(i) + 'miliardi' )
            t=t+1
            continue
        o.append( m + scritta(i))
        
        t=t+1
    o.reverse()
    m=''
    for i in o:
        m=m+i
    return m
    'Scrivete qui il codice della funzione'

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
    'Scrivete qui il codice della funzione'
    K=n%1000
    n=n//1000
    M=n%1000
    n=n//1000
    G=n%1000
    n=n//1000
    T=n%1000
    
    lsf=[]
    if T:
        lsf.append(compl_terne(T,'miliardi','unmilliardo'))

        
    if G:
        lsf.append(compl_terne(G,'milioni','unmilione'))
    
    if M:
        lsf.append(compl_terne(M,'mila','mille'))
    
    if K:
        k=mklist(K)
        lsf.append(num(k[0],k[1],k[2]))
    
    nome=''
    for el in lsf:
        for x in el:
            if x!='zero':
                nome+=x
    return nome
            

def num(c,d,u):
    unita = {'0':'zero','1':'uno','2':'due','3':'tre','4':'quattro', 
                 '5':'cinque','6':'sei','7':'sette','8':'otto','9':'nove'}
    decine = {'0':'zero','1':'dieci','2':'venti','3':'trenta','4':'quaranta',
              '5':'cinquanta','6':'sessanta', '7':'settanta', '8':'ottanta',
              '9':'novanta'}
    centinaia = {'0':'zero','1':'cento','2':'duecento','3':'trecento',
                 '4':'quattrocento','5':'cinquecento','6':'seicento',
                 '7':'settecento','8':'ottocento','9':'novecento'}
    diz_11_20={'uno':'undici','due':'dodici','tre':'tredici',
               'quattro':'quattordici','cinque':'quindici',
               'sei':'sedici','sette':'diciassette','otto':'diciotto',
               'nove':'diciannove'}
    decin = {'venti':'vent','trenta':'trent','quaranta':'quarant',
             'cinquanta':'cinquant','sessanta':'sessant',
             'settanta':'settant','ottanta':'ottant','novanta':'novant'}
    centin = {'cento':'cent','duecento':'duecent','trecento':'trecent',
              'quattrocento':'quattrocent','cinquecento':'cinquecent',
              'seicento':'seicent','settecento':'settecent',
              'ottocento':'ottocent','novecento':'novecent'}
    C=centinaia[c]
    D=decine[d]
    U=unita[u]
    if D == 'dieci' and U != 'zero':
        D = diz_11_20[U]
        U = 'zero'
    if (U == 'uno' or U == 'otto') and D != 'zero':
        D = decin[D]
    if D[0] == 'o' and C != 'zero':
        C = centin[C]
    
    return C,D,U

def mklist(Y):
    y=list(str(Y))
    if len(y)==2:
        y.reverse()
        y.append('0')
        y.reverse()
    elif len(y)==1:
        y.reverse()
        y.append('0')
        y.append('0')
        y.reverse()
    return y

def compl_terne(H,x1,xx1):
    h = mklist(H)
    l = [x for x in num(h[0],h[1],h[2])]
    if l[-1] == 'uno' and l[0] == 'zero' and l[1] == 'zero':
        l[-1] = xx1
    else:
        l.append(x1)
    return l
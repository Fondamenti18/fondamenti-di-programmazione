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


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1'000'000'000'000,
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def conv(n):

    lista_numero=list(str(n))
    tripletta=[]
    n_return=''

    for i in range(0,4):

        if lista_numero==[]:
            break

        tripletta=lista_numero[-3:]
        lista_numero=lista_numero[:-3]
        n_return=lavora_tripletta(tripletta,i)+n_return

    return n_return


def lavora_tripletta(t,i):

    stringa_return=''
    l_centinaia=['', 'cento', 'duecento', 'trecento', 'quattrocento', 'cinquecento', 'seicento', 'settecento', 'ottocento', 'novecento']
    l_decine=['','dieci','venti','trenta','quaranta','cinquanta','sessanta','settanta','ttanta','novanta']
    l_decine_1=['','dieci','vent','trent','quarant','cinquant','sessant','settant','ttant','novant']
    l_decine_unita=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    l_unita=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    l_suffissi=['','mila','milioni','miliardi']

    if len(t)==2:
        t=['0']+t
    elif len(t)==1:
        t=['0','0']+t

    if t[2]=='1' or t[2]=='8':
        stringa_return=l_centinaia[int(t[0])]+l_decine_1[int(t[1])]+l_unita[int(t[2])]
    else:
        stringa_return=l_centinaia[int(t[0])]+l_decine[int(t[1])]+l_unita[int(t[2])]

    if t[1]=='1':
        stringa_return=l_centinaia[int(t[0])]+l_decine_unita[int(t[2])]

    if t[1]=='8' and t[0]=='0':
        if t[2]!='1' and t[2]!='8':
            stringa_return='ottanta'+l_unita[int(t[2])]
        else:
            stringa_return='ottant'+l_unita[int(t[2])]

    if stringa_return!='':
        stringa_return=stringa_return+l_suffissi[i]

    if t[0]=='0' and t[1]=='0' and t[2]=='1':
        if i==0:
            stringa_return='uno'
        elif i==1:
            stringa_return='mille'
        elif i==2:
            stringa_return='unmilione'
        else:
            stringa_return='unmiliardo'

    return stringa_return

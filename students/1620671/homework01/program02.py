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
    s =''
    irregolari = [0,10,11,12,13,14,15,16,17,18,19]
    if 0 < n < 10:
        s = unita(n)
    elif n in irregolari:
        s = conv_irregolari(n)
    elif 20 <= n <= 99:
        s = conv_decine(n)
    elif 100 <= n <= 999:
        s = centinaia(n)
    elif 1000 <= n <= 999999:
        s = migliaia(n)
    elif 1000000 <= n <= 999999999:
        s = milioni(n)
    elif 1000000000 <= n <= 1000000000000:
        s = miliardi(n)
    if len(s) > 4 and s[-4:] == 'zero':
        s = s[:-4]
    return s

def unita(n):
    lista_unita = ['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    return lista_unita[n]

def conv_decine(n):
    s = ''
    decine = ['','','vent','trent','quarant','cinquant','sessant','settant','ottant','novant']
    if unita(int(str(n)[1]))== 'otto' or unita(int(str(n)[1])) == 'uno':
        s = decine[int(str(n)[0])] + unita(int(str(n)[1]))
    elif str(n)[0] == '2':
        s = 'venti' + unita(int(str(n)[1]))
    else:
        s = decine[int(str(n)[0])] +'a'+ unita(int(str(n)[1]))
    return s

def centinaia(n):
    s = ''
    if str(n)[0] == '1' and str(n)[1] == '8':
        s ='cent' + conv(int(str(n)[1:3]))
    elif str(n)[0] == '1' and str(n) != '8':
        s ='cento' + conv(int(str(n)[1:3]))
    elif str(n)[1] == '8':
        s = unita(int(str(n)[0])) + 'cent' + conv(int(str(n)[1:3]))
    else:
        s = unita(int(str(n)[0])) + 'cento' + conv(int(str(n)[1:3]))
    return s

def migliaia(n):
    s = ''
    if str(n)[0] == '1'and len(str(n)) == 4:
        s = 'mille' + conv(int(str(n)[-3:]))
    else:
        s = conv(int(str(n)[0:-3])) + 'mila' + conv(int(str(n)[-3:]))
    return s

def milioni(n):
    s = ''
    if str(n)[0] == '1'and len(str(n)) == 7:
        s = 'unmilione' + conv(int(str(n)[-6:]))
    else:
        s = conv(int(str(n)[0:-6])) + 'milioni' + conv(int(str(n)[-6:]))
    return s
def miliardi(n):
    if str(n)[0] == '1'and len(str(n)) == 10:
        s = 'unmiliardo' + conv(int(str(n)[-9:]))
    else:
        s = conv(int(str(n)[0:-9])) + 'miliardi' + conv(int(str(n)[-9:]))
    return s

def conv_irregolari(n):
    lista_irregolari = ['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    s = ''
    if n == 0:
        s = 'zero'
    else:
        s = lista_irregolari[n-10]
    return s

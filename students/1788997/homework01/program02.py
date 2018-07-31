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
units = [['',''], ['mille','mila'],['milione','milioni'],['miliardo','miliardi']]
nums = [
    ["","uno","due","tre","quattro","cinque","sei","sette","otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto","diciannove"],
    ["", "dieci", "venti","trenta","quaranta","cinquanta", "sessanta", "settanta","ottanta","novanta"],
    ["","cento", "duecento", "trecento", "quattrocento", "cinquecento", "seicento", "settecento", "ottocento", "novecento"]       
]
def f2(d, u, n, res):
    if u > 0:
        if n[2] in '18' and d > 0:            
            return res[:-1] + nums[0][u]
        res += nums[0][u]
    return res
def f1(c, d, u, n):
    res = ""
    if c > 0:
        res = nums[2][c] 
    du = int(n[1] + n[2])
    if du < 20:
        return res + nums[0][du]
    if d == 8:
        return f2(d, u, n, res[:-1] + nums[1][d])
    elif d > 0:
        res += nums[1][d]
    return f2(d, u, n, res)

def getWord(n):
    '''converte il numero nell'equivalente in stringa'''
    n = '0' * (3 % len(n)) + n
    try: return f1(int(n[0]), int(n[1]), int(n[2]), n)
    except: return nums[0][int(n)]

def getNumWithUnit(i, num):
    '''imposta la unit del numero a 3 cifre convertito in testo'''
    unit = units[i][0 if num == 'uno' else 1]
    if unit[-1:] in 'oe' and num == 'uno':
        num = '' if unit == 'mille' else num[:-1]
    return num + unit
     
def conv(n):    
    '''preso un numero in input, ritorna il corrispettivo in stringa'''
    res, nr = "", str(n)[::-1]
    divn = [nr[i : i+3][::-1] for i in range(0, len(nr), 3)]
    for i in range(len(divn) - 1, -1, -1):
        res += getNumWithUnit(i, getWord(divn[i]))   
    return res
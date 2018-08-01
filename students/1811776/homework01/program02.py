
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

def conv99(n):
    sotto_dieci=('','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci',)
    decine=('venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta') 
    if n==0:
        return ''
    if n<=9:
      return sotto_dieci[n]
    if n<=19: 
      sotto_venti=('dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove')
      return sotto_venti[n-10]
    if n<=99:
        decina=decine[n//10-2]
        unita=sotto_dieci[n%10]
        if n%10==1 or n%10==8:
            decina=decina[:-1]
        return decina+unita
 
def conv999(n):
    centinaia=conv99(n//100)+'cento'
    if centinaia=='cento':
        centinaia=''
    if 79<(n%100)<90 and n>100:
        centinaia=conv99(n//100)+'cent'
    if centinaia=='unocent':
        centinaia='cent'
    if centinaia=='unocento':
        centinaia='cento'
    return centinaia+conv99(n%100)

def conv(n):
    singolari=('unmiliardo','unmilione','mille')
    plurali=('miliardi','milioni','mila')
    megafinale=conv999(n%1000)
    for i in range (3):
        n=n//1000
        if n %1000==1:
           megafinale=singolari[-i-1]+megafinale
        if n%1000>1:
            megafinale=plurali[-i-1]+megafinale
            megafinale=conv999(n%1000)+megafinale
    return megafinale


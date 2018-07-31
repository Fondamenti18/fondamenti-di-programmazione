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
numeriElementari = ['','uno','due','tre','quatro','cinque','sei','sette','otto','nove']
numeriSpeciali = ['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
numeriDiOrdine2 = ['',0,'venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
def convOrdine1(n):  
    return numeriElementari[int(n)]
def convOrdine2(n): 
    numeroConvertito = '' 
    if n[0]=='0':
        numeroConvertito = convOrdine1(n[1])
    if n[0]=='1':
        numeroConvertito = numeriSpeciali[int(n[1])]
    elif n[0]!='1' and n[0]!='0':
        temp = numeriDiOrdine2[int(n[0])]
        if n[1]=='1' or n[1]=='8':
            numeroConvertito = temp[0:len(temp)-1]+numeriElementari[int(n[1])]
        else:
            numeroConvertito = temp+numeriElementari[int(n[1])]
    return numeroConvertito
def convOrdine3(n): 
    numeroConvertito = ''
    if n[0]=='0':
        numeroConvertito = convOrdine2(n[1:])
    if n[0]=='1':
        if n[1]=='8':
            numeroConvertito = 'cent'+convOrdine2(n[1:])
        else:
            numeroConvertito = 'cento'+convOrdine2(n[1:])
    elif n[0]!='1' and n[0]!='0':
        if n[1]=='8':
            numeroConvertito = convOrdine1(n[0])+'cent'+convOrdine2(n[1:])
        else:
            numeroConvertito = convOrdine1(n[0])+'cento'+convOrdine2(n[1:])
    return numeroConvertito
def convOrdine4(n): 
    numeroConvertito = ''
    if n[0]=='0':
        numeroConvertito = convOrdine3(n[1:])
    if n[0]=='1':
        numeroConvertito = 'mille'+convOrdine3(n[1:])
    elif n[0]!='1' and n[0]!='0':
        numeroConvertito = convOrdine1(n[0])+'mila'+convOrdine3(n[1:])
    return numeroConvertito
def convOrdine5(n): 
    numeroConvertito = ''
    if n[0]=='0':
        numeroConvertito = convOrdine4(n[1:])
    else:
        numeroConvertito = convOrdine2(n[0:2])+'mila'+convOrdine3(n[2:])
    return numeroConvertito
def convOrdine6(n): 
    numeroConvertito = ''
    if n[0]=='0':
        numeroConvertito = convOrdine5(n[1:])
    else:
        numeroConvertito = convOrdine3(n[0:3])+'mila'+convOrdine3(n[3:])
    return numeroConvertito
def convOrdine7(n): 
    numeroConvertito = ''
    if n[0]=='0':
        numeroConvertito = convOrdine6(n[1:])
    if n[0]=='1':
        numeroConvertito = 'unmilione'+convOrdine6(n[1:])
    elif n[0]!='1' and n[0]!='0':
        numeroConvertito = convOrdine1(n[0])+'milioni'+convOrdine6(n[1:])
    return numeroConvertito
def convOrdine8(n): 
    numeroConvertito = ''
    if n[0]=='0':
        numeroConvertito = convOrdine7(n[1:]) 
    else:
        numeroConvertito = convOrdine2(n[0:2])+'milioni'+convOrdine6(n[2:])
    return numeroConvertito
def convOrdine9(n): 
    numeroConvertito = '' 
    if n[0]=='0':
        numeroConvertito = convOrdine8(n[1:])
    else:
        numeroConvertito = convOrdine3(n[0:3])+'milioni'+convOrdine6(n[3:])
    return numeroConvertito
def convOrdine10(n): 
    numeroConvertito = '' 
    if n[0]=='0':
        numeroConvertito = convOrdine9(n[1:])
    if n[0]=='1':
        numeroConvertito = 'unmiliardo'+convOrdine9(n[1:])
    elif n[0]!='1' and n[0]!='0':
        numeroConvertito = convOrdine1(n[0])+'miliardi'+convOrdine9(n[1:])
    return numeroConvertito 
def convOrdine11(n):
    if n[0]=='0':
        numeroConvertito = convOrdine10(n[1:])
    else:
        numeroConvertito = convOrdine2(n[0:2])+'miliardi'+convOrdine9(n[2:])
    return numeroConvertito
def convOrdine12(n):
    if n[0]=='0':
        numeroConvertito = convOrdine11(n[1:])
    else:
        numeroConvertito = convOrdine3(n[0:3])+'miliardi'+convOrdine9(n[3:])
    return numeroConvertito
def conv(n):
    if n>1000000000000 or n<0:
        print('Out of range')
    else:
        n = str(n)
        numeroConvertito = ''
        if n=='0':
            numeroConvertito = 'zero'
        if len(n)==1 and n!='0':
            numeroConvertito = convOrdine1(n)
        if len(n)==2: 
            numeroConvertito = convOrdine2(n) 
        if len(n)==3:
            numeroConvertito = convOrdine3(n)
        if len(n)==4:
            numeroConvertito = convOrdine4(n)
        if len(n)==5: 
            numeroConvertito = convOrdine5(n)
        if len(n)==6:
            numeroConvertito = convOrdine6(n)
        if len(n)==7:
            numeroConvertito = convOrdine7(n)
        if len(n)==8:
            numeroConvertito = convOrdine8(n)
        if len(n)==9:
            numeroConvertito = convOrdine9(n)
        if len(n)==10:
            numeroConvertito = convOrdine10(n)
        if len(n)==11: 
            numeroConvertito = convOrdine11(n)
        if len(n)==12:
            numeroConvertito = convOrdine12(n)
        return numeroConvertito









    

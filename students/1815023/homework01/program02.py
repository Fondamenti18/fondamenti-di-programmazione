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
    lettere=''
    c = (str(n))
    zeri = 3 - (len(c) % 3)
    for i in range(0, zeri):
        c = '0' + c  
    triple = len(c) // 3
    suff_p = ['','mila','milioni','miliardi']
    suff_s = ['','mille','milione','miliardo']
    j=0
    if triple == 1:
        return conv100(c)
    for i in range(triple-1,-1,-1):
        if c[j:j+3] != '000':
            if c[j:j+3] == '001' and i>0:
                lettere += suff_s[i]
            else:
                lettere += conv100(c[j:j+3]) + suff_p[i]
        j+=3
        
    return lettere
    
    
def conv100(s):
    lettere = ''
    n = ['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    n10 = ['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    dec = ['','dieci','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    lettere = n[int(s[2])]
    
        
    if s[1] != '0':
        if s[1] == '1':
            lettere = n10[int(s[2])]
        elif s[2] == '1' or s[2] == '8':
            lettere = dec[int(s[1])][:-1] + lettere
        else:
            lettere = dec[int(s[1])] + lettere
        
    
    if s[0] != '0':
        if s[0] == '1':
            lettere = 'cento' + lettere
        elif s[1] == '8': #elisione per ottanta
            lettere = n[int(s[0])] + 'cent' + lettere
        else:
            lettere = n[int(s[0])] + 'cento' + lettere
                
    return lettere

        

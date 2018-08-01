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

unita = {0:"",1:"uno", 2:"due", 3:"tre", 4:"quattro", 5:"cinque", 6:"sei", 7:"sette", 8:"otto", 9:"nove",10:"dieci",11:"undici", 12:"dodici", 13:"tredici", 14:"quattordici", 15:"quindici", 16:"sedici", 17:"diciassette", 18:"diciotto" , 19:"diciannove"}
decine = {0:"",1:"dieci", 2:"venti", 3:"trenta", 4:"quaranta", 5:"cinquanta", 6:"sessanta", 7:"settanta", 8:"ottanta", 9:"novanta"}

def floor_division(n,k):
    return round((n/k)-((n%k)/k))

def elisione(numero):
    new_numero = ""
    for c in range(len(numero)):
        if c != len(numero)-1:            
            if((numero[c]=="a" and numero[c+1] == "u") or (numero[c]=="o" and numero[c+1] == "u") ):
                False
            else:
                new_numero += numero[c]
        else:
            new_numero += numero[c]
            
    return new_numero
        
def conv(n):
    if n < 20:
        return (unita[n])
    if n <100:
        decina = floor_division(n,10)
        unit = n%10
        return elisione(decine[decina]+ unita[unit])
    if n < 1000:
        centinaia = floor_division(n,100)
        unit = unita[centinaia]
        if(n < 200):
            unit = ""
        else:
            if n==100:
                return ("cento")
        return elisione(unit+"cento"+conv(n%100))
    if n < 10000:#10 mila
        migliaia = floor_division(n,1000)
        unit = unita[migliaia]+"mila"
        if(n < 2000):
            unit = "mille"
        return elisione(unit+conv(n%1000))
    if n < 100000:#100 mila
        dec_migliaia = floor_division(n,10000)
        migliaia = n%10000
        migliaia = floor_division(migliaia,1000)
        if (n < 20000):
            unit = unita[(dec_migliaia*10)+(migliaia%10)]+"mila"
        else:    
            unit = decine[dec_migliaia]+unita[migliaia]+"mila"       
        return elisione(unit+conv(n%1000))
    if n < 1000000:#1 milione
        cent_migliaia = floor_division(n,100000)
        dec_migliaia = n%100000
        migliaia = n%10000
        migliaia = floor_division(migliaia,1000)
        unit = unita[cent_migliaia]+"cento"+decine[int(dec_migliaia/10000)]+unita[migliaia]+"mila"
        if (n < 200000):
            unit = "cento"+decine[int(dec_migliaia/10000)]+unita[migliaia]+"mila"
        return elisione(unit+conv(n%1000))
    if n < 10000000:#10 milioni
        milione = floor_division(n,1000000)
        cent_migliaia = n%1000000
        unit = unita[milione]+"milioni"+conv(cent_migliaia)
        if (n < 2000000):
            unit = "unmilione"+conv(cent_migliaia)
        return unit
    if n < 100000000:#100 milioni
        dec_milione = floor_division(n,10000000)
        milione = n%10000000
        cent_migliaia = n%1000000
        unit = decine[dec_milione]+ conv(milione)
        if n < 20000000:
            unit = unita[(dec_milione*10)+(floor_division(milione,1000000))]+"milioni"+conv(cent_migliaia)
        return elisione(unit)
    if n < 1000000000: 
        cent_milioni = floor_division(n,100000000)
        dec_milioni = n%100000000
        milioni = n%10000000
        milioni = floor_division(n,1000000)
        unit = unita[cent_milioni]+"cento"+conv(dec_milioni)
        if cent_milioni==1:
            unit = unita[0]+"cento"+conv(dec_milioni)
        return elisione(unit)
    if n < 10000000000:#10 miliardi
        miliardo = floor_division(n,1000000000)
        cent_milioni = n%1000000000
        dec_milioni = n%100000000
        milioni = n%10000000
        unit = unita[miliardo]+"miliardi"+unita[floor_division(cent_milioni,100000000)]+"cento"+decine[floor_division(dec_milioni,10000000)]+"milioni"+ conv(milioni)
        return elisione(unit)
    if n < 100000000000:#100 miliardi
        dec_miliardo = floor_division(n,10000000000)
        miliardo = n%1000000000
        cent_milioni = n%1000000000
        dec_milioni = n%100000000
        milioni = n%10000000
        cent_migliaia = n%1000000
        unit = decine[dec_miliardo]+unita[floor_division(n,1000000000)%10]+"miliardi"+unita[(floor_division(cent_milioni,100000000))]+"cento"+decine[floor_division(dec_milioni,10000000)]+unita[floor_division(milioni,1000000)]+"milioni"+conv(cent_migliaia)
        if n < 20000000000:
            unit = unita[(dec_miliardo*10)+(floor_division(n,1000000000)%10)]+"miliardi"+unita[floor_division(cent_milioni,100000000)]+"cento"+decine[floor_division(dec_milioni,10000000)]+unita[floor_division(milioni,1000000)]+"milioni"+conv(cent_migliaia)
        return elisione(unit)
    if n < 1000000000000:
        cent_miliardo = floor_division(n,100000000000)
        dec_miliardo = n%10000000000
        miliardo = n%1000000000
        cent_milioni = n%1000000000
        dec_milioni = n%100000000
        milioni = n%10000000
        cent_migliaia = n%1000000
        unit = unita[cent_miliardo]+"cento"+decine[floor_division(dec_miliardo,1000000000)]+unita[floor_division(n,1000000000)%10]+"miliardi"+unita[floor_division(cent_milioni,100000000)]+"cento"+decine[floor_division(dec_milioni,10000000)]+unita[floor_division(milioni,1000000)]+"milioni"+conv(cent_migliaia)
        if n < 200000000000:
            unit = unita[0]+"cento"+decine[floor_division(dec_miliardo,1000000000)]+unita[floor_division(n,1000000000)%10]+"miliardi"+unita[floor_division(cent_milioni,100000000)]+"cento"+decine[floor_division(dec_milioni,10000000)]+unita[floor_division(milioni,1000000)]+"milioni"+conv(cent_migliaia)
            
        return elisione(unit)



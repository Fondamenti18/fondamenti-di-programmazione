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
diz119={1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove',10:'dieci',11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',17:'diciassette',18:'diciotto',19:'diciannove'}
dizDec={2:'venti',3:'trenta',4:'quaranta',5:'cinquanta',6:'sessanta',7:'settanta',8:'ottanta',9:'novanta'}
def convApp(n):
    if n == 0: 
        return ""
         
    elif n <= 19:
        return diz119[n]
                 
    elif n <= 99:
        
        parola = dizDec[n//10]
        unita = n%10
        if unita == 1 or unita == 8:
            parola = parola[:-1]
        return parola + convApp(n%10)
         
         
    elif n <= 999:
        decine = n%100       
        decine = (decine//10)
        parola = "cent"   
        centinaia=''
        if decine != 8:
            parola = parola + "o"
        if n//100!=1:
            centinaia=diz119[n//100]
            
        return centinaia + parola + convApp(n%100)
         
    elif n<= 1999 :
        return "mille" + convApp(n%1000)
     
    elif n<= 999999:
        return convApp(n//1000) +"mila" + convApp(n%1000)
         
    elif n <= 1999999:
        return "unmilione" + convApp(n%1000000)
         
    elif n <= 999999999:
        return convApp(n//1000000)+  "milioni" + convApp(n%1000000)
    elif n <= 1999999999:
        return "unmiliardo" + convApp(n%1000000000)
         
    else:
        return convApp(n//1000000000) + "miliardi" +convApp(n%1000000000)


def conv(n):
    
    
    return convApp(n)

    

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
d= {0:'zero', 1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque', 6:'sei',\
    7:'sette', 8:'otto', 9:'nove', 10:'dieci', 11:'undici', 12:'dodici',13:'tredici',14:'quattordici',\
    15:'quindici', 16:'sedici', 17:'diciassette',18:'diciotto',19:'diciannove',20:'venti',30:'trenta',\
    40:'quaranta',50:'cinquanta',60:'sessanta',70:'settanta',80:'ottanta',90:'novanta',100:'cento'}


    
    
def conv100(n):
    if n<=20:
        return(d[n])
    if n>20 and n<100:
        if n%10==0:
            return d[n]
        decina=d[n//10*10]
        decinat= decina[:-1]#decina tagliata vent trent
        if n%10==1 or n%10==8:
            return decinat + d[n % 10]
     
def conv1000(n):
    if n<100:
        return conv100(n)
    if n==100:
        return d[n]
    if n%100==0:
        return conv100(n//100)+'cento'
    if n>100 and n<200:
        return 'cento'+conv100(n%100)
    if n>200 and n<1000:
        return conv100(n//100)+'cento'+conv100(n%100)
        

def conv(n):
    singolari=['unmiliardo','unmilione','mille']
    plurali=['miliardi','milioni','mila']
    fine=conv1000(n%1000)
    if n<100:
        return conv100(n)
    if n>99 and n<1000:
        return conv1000(n)
    for i in range(0,3):
        n=n//1000
        if n%1000==1:
            fine=singolari[-i-1]+fine
        if n%1000>1:
            fine = plurali[-i-1] + fine
            fine = conv1000(n%1000) + fine
    return fine
    
            
            
        
        
    

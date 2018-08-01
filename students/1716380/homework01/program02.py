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
    dic={0:'',1:'uno',2:'due',3:'tre',4	:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove'
        ,10:'dieci',11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici'
         ,16:'sedici',17:'diciassette',18:'diciotto',19:'diciannove',20:'venti',30:'trenta',
         40:'quaranta',50:'cinquanta',60:'sessanta',70:'settanta',80:'ottanta',90:'novanta',100:'cento'}
    n=int(n)
    st=str(n)
    if n in dic:
        return dic[n]
    if n<100  :
        if int(st[1])==8 or int(st[1])==1:
            return dic[int(st[0]+str(0))].strip('a i')+dic[int(st[1])]
        else :
            return dic[int(st[0]+str(0))]+dic[int(st[1])]
    if n <= 199:
        if n%100 in range(80,90):
            return 'cent'+conv(n%100)
        return dic[100]+conv(n%100)
    if n <= 999:
        if n%100 in range(80,90):
            return dic[int(st[0])]+'cent'+conv(n%100)
        return dic[int(st[0])]+dic[100]+conv(n%100)
    if n <=1999:
        return 'mille' + conv(n%1000)
    if n <= 999999:
        return conv(n//1000)+'mila'+ conv(n%1000)
    if n <= 1999999:
        return 'milione'+conv(n%1000000)
    if n <=999999999:
        return conv(n//1000000)+'milioni'+conv(n%1000000)
    if n <=1999999999:
        return 'miliardo'+conv(n%1000000000)
    if n <=999999999999:
        return conv(n//1000000000)+'miliardi'+conv(n%1000000000)
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
def conv(n):
Scrivete qui il codice della funzione'''
    

   
def conv(n):
    l=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    if n<= 19:
        return l[n]
    
    l15=['vent','trent','quarant','cinquant','sessant','settant','ottant','novant']
    if (n%10==1 or n%10==8) and 1<=n<=99:
        return l15[(n//10)%10-2]+conv(n%10)  
           
    l1=['venti']
    if n<= 29:
        return l1[0]+l[n%10]
    
    l2=['trenta']
    if n<= 39:
        return l2[0]+l[n%10]
    
    l3=['quaranta']
    if n<= 49:
        return l3[0]+l[n%10]
    
    l4=['cinquanta']
    if n<= 59:
        return l4[0]+l[n%10]
    
    l5=['sessanta']
    if n<= 69:
        return l5[0]+l[n%10]
    
    l6=['settanta']
    if n<= 79:
        return l6[0]+l[n%10]
    
    l7=['ottanta']
    if n<= 89:
        return l7[0]+l[n%10]
    
    l8=['novanta']
    if n<=99:
        return l8[0]+l[n%10]
    
    l16=['cent']
    if 180<=n<=189:
        return l16[0]+conv(n%100) 
    
    if 280<=n<=289 or 380<=n<=389 or 480<=n<=489 or 580<=n<=589 or 680<=n<=689 or 780<=n<=789 or 880<=n<=889 or 980<=n<=989:
        return l[n//100]+l16[0]+conv(n%100)
    
    l9=['cento']
    if 100<=n<=179 or 190<=n<=199:
        return l9[0]+conv(n%100)
    
    if n<= 999:
        return l[n//100]+l9[0]+conv(n%100)
    
    l10=['mille']
    if n<= 1999:
        return l10[0]+conv(n%1000)
    
    l11=['mila']
    if n<=999999:
        return conv(n//1000)+l11[0]+conv(n%1000)
    
    l12=['unmilione']
    if n<=1999999:
        return l12[0]+conv(n%1000000)
    
    l17=['milioni']
    if n<=999999999:
        return conv(n//1000000)+l17[0]+conv(n%1000000)
    
    l13=['unmiliardo']
    if n <=1999999999:
        return l13[0]+conv(n%1000000000)
   
    l14=['miliardi']
    if n <=999999999999:
        return conv(n//1000000000)+l14[0]+conv(n%1000000000)
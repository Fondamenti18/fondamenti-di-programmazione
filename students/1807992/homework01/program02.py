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
    risultato=''
    da1a9={0:'',1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove'}
    da10a19={10:'dieci',11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',17:'diciassette',18:'diciotto',19:'diciannove'}
    decine={0:'',2:'venti',3:'trenta',4:'quaranta',5:'cinquanta',6:'sessanta',7:'settanta',8:'ottanta',9:'novanta'}
    decineel={0:'',2:'vent',3:'trent',4:'quarant',5:'cinquant',6:'sessant',7:'settant',8:'ottant',9:'novant'}
    if n==0:
        return 'zero'
    x=[int(i) for i in str(n)]
    if len(x)>=1 and 0<x[-1]<10:
        risultato=da1a9[x[-1]]
    if len(x)>=2:
        if x[-2]==1:
            risultato=da10a19[int(str(x[-2]) + str(x[-1]))]
        elif x[-1]==1 or x[-1]==8:
            risultato=decineel[x[-2]]+risultato
        else:
            risultato=decine[x[-2]]+risultato
    if len(x)>=3 and 0<x[-3]<10:
        if x[-3]==1:
            if x[-2]==8:
                risultato='cent'+risultato
            else:
                risultato='cento'+risultato
        elif x[-2]==8:
            risultato=da1a9[x[-3]]+'cent'+risultato
        else:
            risultato=da1a9[x[-3]]+'cento'+risultato 
    if len(x)==4 or (len(x)>=7 and x[-6]==0 and x[-5]==0 and 0<x[-4]<10):
        if x[-4]==1:
            risultato='mille'+risultato
        else:
            risultato=da1a9[x[-4]]+'mila'+risultato
    if len(x)>=5 and 0<x[-5]<10:
        if x[-5]==1:
            risultato=da10a19[int(str(x[-5]) + str(x[-4]))]+'mila'+risultato
        elif x[-4]==1 or x[-4]==8:
            risultato=decineel[x[-5]]+da1a9[x[-4]]+'mila'+risultato
        else:
            risultato=decine[x[-5]]+da1a9[x[-4]]+'mila'+risultato
    if len(x)>=6 and 0<x[-6]<10:
        if x[-6]==1:
            if x[-5]==8:
                risultato='cent'+risultato
            elif 0<x[-4]<10 and x[-5]==0:
                risultato='cento'+da1a9[x[-4]]+risultato
            else:
                risultato='cento'+risultato
        elif x[-5]==8:
            risultato=da1a9[x[-6]]+'cent'+risultato
        elif 0<x[-4]<10 and x[-5]==0:
            risultato=da1a9[x[-6]]+'cento'+da1a9[x[-4]]+'mila'+risultato
        else:
            risultato=da1a9[x[-6]]+'cento'+risultato 
    if len(x)==7 or (len(x)>=10 and x[-8]==0 and x[-9]==0 and 0<x[-7]<10):
        if x[-7]==1:
            risultato='unmilione'+risultato
        else:
            risultato=da1a9[x[-7]]+'milioni'+risultato
    if len(x)>=8 and 0<x[-8]<10:
        if x[-8]==1:
            risultato=da10a19[int(str(x[-8]) + str(x[-7]))]+'milioni'+risultato
        elif x[-7]==1 or x[-7]==8:
            risultato=decineel[x[-8]]+da1a9[x[-7]]+'milioni'+risultato
        else:
            risultato=decine[x[-8]]+da1a9[x[-7]]+'milioni'+risultato
    if len(x)>=9 and 0<x[-9]<10:
        if x[-9]==1:
            if x[-8]==8:
                risultato='cent'+risultato
            elif 0<x[-7]<10 and x[-8]==0:
                risultato='cento'+da1a9[x[-7]]+risultato
            else:
                risultato='cento'+risultato
        elif x[-8]==8:
            risultato=da1a9[x[-9]]+'cent'+risultato
        elif 0<x[-7]<10 and x[-8]==0:
            risultato=da1a9[x[-9]]+'cento'+da1a9[x[-7]]+'milioni'+risultato
        else:
            risultato=da1a9[x[-9]]+'cento'+risultato
    if len(x)==10:
        if x[-7]==1:
            risultato='unmiliardo'+risultato
        else:
            risultato=da1a9[x[-7]]+'miliardi'+risultato
    if len(x)>=11 and 0<x[-11]<10:
        if x[-11]==1:
            risultato=da10a19[int(str(x[-11]) + str(x[-10]))]+'miliardi'+risultato
        elif x[-10]==1 or x[-10]==8:
            risultato=decineel[x[-11]]+da1a9[x[-10]]+'miliardi'+risultato
        else:
            risultato=decine[x[-11]]+da1a9[x[-10]]+'miliardi'+risultato
    if len(x)==12:
        if x[-12]==1:
            if x[-11]==8:
                risultato='cent'+risultato
            elif 0<x[-10]<10 and x[-11]==0:
                risultato='cento'+da1a9[x[-10]]+risultato
            else:
                risultato='cento'+risultato
        elif x[-11]==8:
            risultato=da1a9[x[-12]]+'cent'+risultato
        elif 0<x[-10]<10 and x[-11]==0:
            risultato=da1a9[x[-12]]+'cento'+da1a9[x[-10]]+'miliardi'+risultato
        else:
            risultato=da1a9[x[-12]]+'cento'+risultato
        
        
            
                     
    return risultato
    
    
            
            
        
        
        
        
        
        

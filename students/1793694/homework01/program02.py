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
def suppm(n,u):
    if 1000 == n:
        return 'mille'
    elif 1000<n<=9000:
        return u[int(n/1000)]+'mila'
def suppud(n,u):
    if 1<=n<=9:
        return u[n]
    elif 10<=n<=19:
        return u[n]
    elif 20<=n<=90 and n%10 != 1 and n%10 !=8:  
        return  u[int(n/10)*10]
    else:
        return u[n]
    
def suppc(n,u):    
    if 100<=n<199:
        return 'cento'
    elif 200<n<=999:
        if 80<=((n)%100)<=89:
        
            return u[int(n/100)]+'cent'
        else:
            
            return u[int(n/100)]+'cento'

            #return u[int(n/100)]+'cento'


def suppfinale(n,u):
    IntToStr2p0=''
    n1=n
    if(9999>=n>=1000):
        n1= (n1//1000)*1000
        IntToStr2p0+=suppm(n1,u)
        n1=n//10
    if(999>=n1>=100):
        #print(n1)
        n1= ((n1%1000))
        
        #print(n1)
        IntToStr2p0+=suppc(n1,u)
        n1=n%100
        #print(n1)
    if n1>20 and (n1%10 == 1 or n1%10 == 8):
        IntToStr2p0+=suppud(n1,u)
        
        print(n1)
    elif (99>=n1>=20 and (n1%10 != 1 or n1%10 !=8)) : 
        n1=(n1//10)*10
       # print(n1)
        IntToStr2p0+=suppud(n1,u)
        n1=n%10
        #print(n1)
    if(19>=n1>=10):
        #print(n1)
        #print(IntToStr2p0)
        IntToStr2p0+=suppud(n1,u)
        
    
        
    if(10>n1>=1):
            #print(n)
        #print(n1)
        IntToStr2p0+=suppud(n1,u)
    return IntToStr2p0
def conv(n):
    IntToStr2p0=''
    n1=0
    u={1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque', 6:'sei', 7:'sette', 8:'otto', 9:'nove', 20:'venti', 21:'ventuno', 28:'ventotto', 30:'trenta', 31:'trentuno', 38:'trentotto', 40:'quaranta', 41:'quarantuno', 48:'quarantotto', 50:'cinquanta', 51:'cinqantuno', 58:'cinquantotto', 60:'sessanta', 61:'sessantuno', 68:'sessantotto', 70:'settanta', 71:'settantuno', 78:'settantotto', 80:'ottanta', 81:'ottantuno', 88:'ottantotto', 90:'novanta', 91:'novantuno', 98:'novantotto', 10:'dieci', 11:'undici', 12:'dodici', 13:'tredici', 14:'quattordici', 15:'quindici', 16:'sedici', 17:'diciassette', 18:'diciotto', 19:'dicianove', 100:'cento', 180:'centottanta', 280:'duecentottanta', 380:'trecentottanta', 480:'quattrocentottanta', 580:'cinquecentottanta', 680:'seicentottanta', 780:'settecentottanta', 880:'ottocentottanta', 980:'novecentottanta', 1000:'mille', 1000000:'un milione', 1000000000:'un miliardo'}
    if(999999999999>=n>=1000000000):
        n1= n//10**9
        #print(n1)
        if(n1 == 1):
            IntToStr2p0+=u[n1*10**9]
        else:
            
            IntToStr2p0+=suppfinale(n1,u)+'miliardi'
        #print(n)
        n=n%((n1*10**9))
        #print(n1)
        #print(n)
    if(999999999>=n>=1000000):
        n1= n//10**6
        #print(n1)
        if(n1 == 1):
            IntToStr2p0+=u[n1*10**6]
        else:    
            IntToStr2p0+=suppfinale(n1,u)+'milioni'
        n=n%(n1*10**6)
    if(999999>=n>=1000):
        n1= n//10**3
        print(n1)
        if(n1 == 1):
            IntToStr2p0+=u[n1*10**3]
        else:
            IntToStr2p0+=suppfinale(n1,u)+'mila'
        n=n%(n1*10**3)
    if(999>=n>=100):
        n1= n//100
        print(n1)
        if(n1 == 1):
            IntToStr2p0+=u[n1*100]
        elif 80<=((n)%100)<=89:
            IntToStr2p0+=suppfinale(n1,u)+'cent'
        else:
            print('cuai')
            IntToStr2p0+=suppfinale(n1,u)+'cento'
        n=n%(n1*10**2)
    if(99>=n>=10):
        n1= n//1
        print(n1)
        if(n1 == 1):
            IntToStr2p0+=u[n1*1]
        else:
            IntToStr2p0+=suppfinale(n1,u)
        n=n%(n1*10**3)
    if(9>=n>=1):
        n1= n//1
        print(n1)
        if(n1 == 1):
            IntToStr2p0+=u[n1*1]
        else:
            IntToStr2p0+=suppfinale(n1,u)
        n=n%(n1*10**3)
    
    
    #elif 1000000<=n<=1999999:
       # print (u[int(n/1000000)*1000000]+u[int(n/100000)%10]+'cento'+u[int(n/10000)%10]+'nta'+u[int(n/1000)%10]+'mila'+u[int(n/100)%10]+'cento'+u[int(n/10)%10]+u[int(n%10)])
    #elif 2000000<=n<=9999999:
        

    return IntToStr2p0
n=17
print(conv(n))
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
 and n != 21 and n != 28):
        return 'venti'
    if(n == 21):
        return 'ventuno'
    if(n == 28):
        return 'ventotto'
'''
def eccezione1(n,nome):
    if( (n%10 == 1 or n%10 == 8) and(n>=20)):
            nome=nome[:-1]
    return nome
def eccezione2(n,nome):
    if(n%100 >= 80 and n%100 <=89):
        nome=nome[:-1]
    return nome
    
def decine(n):
    if(n == 10):
        return 'dieci'
    if(n == 11):
        return 'undici'
    if(n == 12):
        return 'dodici'
    if(n == 13):
        return 'tredici'
    if(n == 14):
        return 'quattordici'
    if(n == 15):
        return 'quindici'
    if(n == 16):
        return 'sedici'
    if(n == 17):
        return 'diciassette'
    if(n == 18):
        return 'diciotto'
    if(n == 19):
        return 'diciannove'
    if(29>=n>=20):
        return 'venti'
    if(39>=n>=30):
        return 'trenta'
    if(49>=n>=40):
        return 'quaranta'
    if(59>=n>=50):
        return 'cinquanta'
    if(69>=n>=60):
        return 'sessanta'
    if(79>=n>=70):
        return 'settanta'
    if(89>=n>=80):
        return 'ottanta'
    if(99>=n>=90):
        return 'novanta'
    
    
def unita(n):
    if(n == 0):
        return ''
    if(n == 1):
        return 'uno'
    if(n == 2):
        return 'due'
    if(n == 3):
        return 'tre'
    if(n == 4):
        return 'quattro'
    if(n == 5):
        return 'cinque'
    if(n == 6):
        return 'sei'
    if(n == 7):
        return 'sette'
    if(n == 8):
        return 'otto'
    if(n == 9):
        return 'nove'
    
def calcolad(n,n2):
    
    nome= decine(n2)
    #if( (n%10 == 1 or n%10 == 8) and(n>=20)):
            #nome=nome[:-1]
    nome=eccezione1(n,nome)
    return nome

def calcolac(n,n2):
    nome=''
    if(n2 == 1):
        nome="cento"
    else:
        nome= unita(n2)+'cento'

    #if(n%100 >= 80 and n%100 <=89):
        #nome=nome[:-1]
    nome=eccezione2(n,nome)
    return nome

def calcolam(n2):
    #print(n2)
    if(n2==1):
        nome='mille'
    elif 9>=n2>1:
        
        nome= unita(n2)+'mila'
    elif 99>=n2>=10:
        nome= decine(n2)+'mila'
    return nome
     
def dcm(n):

    nome=''
    n2=n
    int(n2)
    #print(n)
    if(n >=1000):
        #print('migliaia ok')
        n2=int(n/1000)        
        nome= calcolam(n2)
        
    if(1000> n >= 100):
        #print('centinaia ok')
        n2= int(n/10**2)        
        nome+=calcolac(n,n2)                        
        n2= int(n%(10**2))        
    elif n>=1000:
        #print('centinaia ok 2')
        n2=int(n/100)        
        nome+=calcolac(n,n2)
           
    if(99>= n2 >= 10):
        #print('decine ok')        
        nome+= calcolad(n,n2)     
    elif n2 >=100:
        #print('decine ok 2')
        n2=int(n%1000)
        nome+=calcolad(n,n2)
        
    if(n2>=20 or n2<=9):
        
        n2=int(n%10)
        if(9>= n2 >=1):
            #print ('unita ok')
            nome+=unita(n2)
            
    return nome


                

        
        

def conv(n):
    'Scrivete qui il codice della funzione'
    nome=''
    n2=0
    if 1000000000<= n <1000000000000:
        n2=int(n/10**9)
        
        if(n2 == 1):
            
            nome+='unmiliardo'
        else:
            nome=dcm(n2)+'miliardi'
        n=int(n%((10**9)*n2))
    if 1000000000>n>=1000000:
        n2=int(n/10**6)
        #print(n2)
        if(n2==1):
            nome+='unmilione'
        else:
            nome+=dcm(n2)+'milioni'
        #print(n)
        #print(n%10*)
        n=n%((10**6)*n2)
        #print(n)
    if 1000000>n>=1000:
        
        n2=int(n/1000)
        #print(n2)
        if(9>=n2>=1):
            nome+=calcolam(n2)
        else:
            nome+=dcm(n2)+'mila'
        n=n%(1000*n2)
        #print (n)
    if 1000>n>=100:
        n2=int(n/100)
        #print(n2)
        if(9>=n2>=1):
            nome+=calcolac(n,n2)
        else:
            nome+=dcm(n2)+'cento'
        #nome=eccezione2(n,nome)
        #if(n2 ==1):
            #nome+='cento'
        #else:
            #nome+=dcm(n2)+'cento'
            
            #if(n%100 >= 80 and n%100 <=89):
                #nome=nome[:-1]
            
        n=n%(100*n2)
        
    if 100>n>=10:        
        
        nome+=dcm(n)
    if 10>n>=1:
        nome+=dcm(n)   

        
    
    return nome
#n=1928
#print(n)
#print(conv(n))
        
        
        
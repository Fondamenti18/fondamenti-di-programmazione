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

ATTEnZIOnE: nOn USATE LETTERE ACCEnTATE.
ATTEnZIOnE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def lett(n):
    
    unita=["","uno","due","tre","quattro","cinque","sei","sette","otto","nove"]
    magdieci=["dieci","undici","dodici","tredici","quattordici","quindici","sedici","diciassette","diciotto","diciannove"]
    decine=["","","venti","trenta","quaranta","cinquanta","sessanta","settanta","ottanta","novanta"]
    decineeli=["","","vent","trent","quarant","cinquant","sessant","settant","ottant","novant"]
    centinaia=["","cento","duecento","trecento","quattrocento","cinquecento","seicento","settecento","ottocento","novecento"]
    centinaiaeli=["","cent","duecent","trecent","quattrocent","cinquecent","seicent","settecent","ottocent","novecent"]
    stringa=""
    
    u=n%10
    n=n//10
    d=n%10
    n=n//10
    h=n%10
    
    if h!=0:
        if d == 8:
            stringa=stringa+centinaiaeli[h]
            
        else:
            stringa=stringa+centinaia[h]
        
    if d==1:
        stringa=stringa+magdieci[u]
        
    if d!=0 and d!=1:
        if u==1 or u==8:
            stringa=stringa+decineeli[d]+unita[u]
        else:
            stringa=stringa+decine[d]+unita[u]
            
    if d==0:
        stringa=stringa+unita[u]
        
        
    return stringa
    
    

def conv(n): 
    
    if n == 0:
        stringc = "zero"
        
    else:
        '''controlla u'''
        u=n%1000
        n=n//1000
        txtu=lett(u)
        if n!=0 and u==0:
            stringc=""
        else:
            stringc=txtu
        
        '''controlla k'''
        if n!=0:
            k=n%1000
            n=n//1000
            txtk=lett(k)
            if k == 0:
                stringc = "" + stringc
            else:
                if k == 1:
                    stringc = "mille" + stringc
                else:
                    stringc= txtk + "mila" + stringc
            
            '''controlla M'''
            if n!=0:
                m=n%1000
                n=n//1000
                txtm=lett(m)
                if m == 0:
                    stringc = "" + stringc
                else:
                    if m == 1:
                        stringc = "unmilione" + stringc
                    else:
                        stringc= txtm + "milioni" + stringc
                
                '''controlla G'''
                if n!=0:
                    g=n%1000
                    n=n//1000
                    txtg=lett(g)
                    if g == 0:
                        stringc = "" + stringc
                    else:
                        if g == 1:
                            stringc = "unmiliardo" + stringc
                        else:
                            stringc= txtg + "miliardi" + stringc
                    
                    '''controlla kG'''
                    if n!=0:
                        t=n%1000
                        n=n//1000
                        txtt=lett(t)
                        if t == 0:
                            stringc = "" + stringc
                        else:
                            if t == 1:
                                stringc = "mille" + stringc
                            else:
                                stringc= txtt + "mila" + stringc
         
    return stringc
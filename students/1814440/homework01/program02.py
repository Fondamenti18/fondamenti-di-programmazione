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

def convertiNumero(n):
    ''' QUESTA FUNZIONE CONVERTE LE CENTINAIA O LE DECINE-UNITA '''
    cifre={0:'',1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',
           8:'otto',9:'nove',10:'dieci',11:'undici',12:'dodici',13:'tredici',
           14:'quattordici',15:'quindici',16:'sedici'}
    decine={1:'dici',2:'vent',3:'trent',4:'quarant',6:'sessant'}
    if n in cifre.keys(): return cifre[n]
    decina=int(n/10)
    stringa=''
    if decina in decine.keys(): stringa=decine[decina]
    else: stringa=cifre[decina][0:-1]+'ant' #tolgo l'ultima lettera della parola
    #lo devo fare ora perché la stringa non è mutabile e farlo dopo dà errore
    unita=n%10
    if unita!=1 and unita!=8: stringa+='a' #non posso fare il contrario perché la stringa non è mutabile
    if unita==7: stringa+='s' #diciassette ha doppia s
    stringa=stringa+cifre[unita]
    return stringa

def convertiBlocco(n):
    ''' QUESTA FUNZIONE RICEVE IL NUMERO A TRE CIFRE E LO SPACCHETTA IN CENTINAIA E DECINE-UNITA '''
    stringa=''
    if n==0: return ''
    k=int(n/100)
    if k!=0:
        if k==1: stringa='cento'
        else:
            stringa=convertiNumero(k)+'cent' #centinaia
            if int(n%100/10)!=8: stringa+='o'
    n=n%100
    if n==0: return stringa # blocco concluso
    stringa=stringa+convertiNumero(n) #converto il resto del numero
    return stringa

def conv(n):
    if n==0:
        return 'zero'
    stringa=convertiBlocco(int(n/10**9)) # converto i miliardi
    if(stringa!=''): stringa+='miliardi'
    n=n%10**9 #ottengo il resto
    stringa+=convertiBlocco(int(n/10**6)) # converto i milioni
    if(stringa!=''): stringa+='milioni'
    n=n%10**6 #ottengo il resto
    if int(n/1000)==1: stringa+='mille'
    else:
        stringa+=convertiBlocco(int(n/10**3)) # converto le migliaia
        if(stringa!=''): stringa+='mila'
    n=n%10**3 #ottengo il resto
    stringa+=convertiBlocco(n)
    return stringa

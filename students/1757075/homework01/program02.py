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
    # inizializzo stringhe per risultato
    unita = ''
    migliaia = ''
    milioni = ''
    miliardi = ''
    
    # controllo se n e' un caso particolare
    if n == 0:
        return 'zero'
    
    # calcolo unita'
    unita += conv2(n % 1000)
    
    # preparo per migliaia
    n = n // 1000
    # controllo se sono mille precise
    if n % 1000 == 1:
        migliaia += 'mille'
    # calcolo migliaia
    elif n % 1000 != 0:
        migliaia += conv2(n % 1000)
        migliaia += 'mila'
    
    # preparo per milioni
    n = n // 1000
    # controllo se e' un milione preciso
    if n == 1:
        milioni += 'unmilione'
    # calcolo milioni
    elif n % 1000 != 0:
        milioni += conv2(n % 1000)
        milioni += 'milioni'
    

    # preparo per miliardi
    n = n // 1000
    #controllo se e' un miliardo preciso
    if n == 1:
        miliardi += 'unmilardo'
    # calcolo miliardi
    elif n % 1000 != 0:
        miliardi += conv2(n)
        miliardi += 'miliardi'
        
    return miliardi + milioni + migliaia + unita


def conv2(n):
    # inizializzo
    risultato = ''
    a = 0
    
    # controllo se n e' un caso particolare
    if numeri.get(n) != None:
        return numeri[n]
    
    # controllo se n ha due o tre cifre
    if n > 99:
        # n e' un numero composto tra 100 e 999 (senza contare casi particolari)
        a = n - int(str(n)[1:])      # metto in a le centinaia compongono n
        risultato += numeri[a]       # aggiungo a risultato
    
    n -= a                # metto in n le decine
    
    # controllo se n e' un caso particolare
    if numeri.get(n) != None:
        return risultato + numeri[n]
    
    # n e' un numero compreso tra 21 e 99
    a = n - int(str(n)[1:])
    risultato += numeri[a]
    
    n -= a                                  # metto in n le unita'
    
    # aggiung pure unita' a risultato
    return risultato + numeri[n]
    
    
# casi particolari
numeri = { 0:'',1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque',
    6:'sei', 7:'sette', 8:'otto', 9:'nove', 10:'dieci', 11:'undici', 12:'dodici',
    13:'tredici', 14:'quattordici', 15:'quindici', 16:'sedici', 17:'diciassette',
    18:'diciotto', 19:'diciannove', 20:'venti', 30:'trenta', 40:'quaranta', 
    50:'cinquanta', 60:'sessanta', 70:'settanta',80:'ottanta', 90:'novanta', 
    100:'cento', 200:'duecento', 300:'trecento',400:'quattrocento', 
    500:'cinquecento', 600:'seicento', 700:'settecento',800:'ottocento', 
    900:'novecento', 1000:'mille', 21:'ventuno',  28: 'ventotto', 31:'trentuno',
    38:'trentotto', 41:'quarantuno', 48:'quarantotto', 51:'cinquantuno',
    58:'cinquantotto', 61:'sessantuno', 68:'sessantotto', 71:'settantuno',
    78:'settantotto', 81:'ottantuno', 88:'ottantotto', 91:'novantuno',
    98:'novantotto', 180:'centottanta', 181:'centottantuno', 182:'centottantadue',
    183:'centottantatre', 184:'centottantaquattro', 185:'centottantacinque',
    186:'centottantasei', 187:'centottantasette', 188:'centottantotto',
    189:'centottantanove',280:'duecentottanta',281:'duecentottantuno',282:'duecentottantadue',
    283:'duecentottantatre',284:'duecentottantaquattro',285:'duecentottantacinque',
    286:'duecentottantasei',287:'duecentottantasette',288:'duecentottantotto',
    289:'duecentottantanove',380:'trecentottanta',381:'trecentottantuno',382:'trecentottantadue',
    383:'trecentottantatre',384:'trecentottantaquattro',385:'trecentottantacinque',
    386:'trecentottantasei',387:'trecentottantasette',388:'trecentottantotto',
    389:'trecentottantanove',480:'quattrocentottanta',481:'quattrocentottantuno',482:'quattrocentottantadue',
    483:'quattrocentottantatre',484:'quattrocentottantaquattro',485:'quattrocentottantacinque',
    486:'quattrocentottantasei',487:'quattrocentottantasette',488:'quattrocentottantotto',
    489:'quattrocentottantanove',580:'cinquecentottanta',581:'cinquecentottantuno',582:'cinquecentottantadue',
    583:'cinquecentottantatre',584:'cinquecentottantaquattro',585:'cinquecentottantacinque',
    586:'cinquecentottantasei',587:'cinquecentottantasette',588:'cinquecentottantotto',
    589:'cinquecentottantanove',680:'seicentottanta',681:'seicentottantuno',682:'seicentottantadue',
    683:'seicentottantatre',684:'seicentottantaquattro',685:'seicentottantacinque',
    686:'seicentottantasei',687:'seicentottantasette',688:'seicentottantotto',
    689:'seicentottantanove',880:'ottocentottanta',881:'ottocentottantuno',882:'ottocentottantadue',
    883:'ottocentottantatre',884:'ottocentottantaquattro',885:'ottocentottantacinque',
    886:'ottocentottantasei',887:'ottocentottantasette',888:'ottocentottantotto',
    889:'ottocentottantanove',780:'settecentottanta',781:'settecentottantuno',782:'settecentottantadue',
    783:'settecentottantatre',784:'settecentottantaquattro',785:'settecentottantacinque',
    786:'settecentottantasei',787:'settecentottantasette',788:'settecentottantotto',
    789:'settecentottantanove',980:'novecentottanta',981:'novecentottantuno',982:'novecentottantadue',
    983:'novecentottantatre',984:'novecentottantaquattro',985:'novecentottantacinque',
    986:'novecentottantasei',987:'novecentottantasette',988:'novecentottantotto',
    989:'novecentottantanove'
    }


print(conv(808080808080))

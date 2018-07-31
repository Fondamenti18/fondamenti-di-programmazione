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
    number_names = {
    '0' : '',
    '1' : 'uno',
    '2' : 'due',
    '3' : 'tre',
    '4' : 'quattro',
    '5' : 'cinque',
    '6' : 'sei',
    '7' : 'sette',
    '8' : 'otto',
    '9' : 'nove',
    '10' : 'dieci',
    '11' : 'undici',
    '12' : 'dodici',
    '13' : 'tredici',
    '14' : 'quattordici',
    '15' : 'quindici',
    '16' : 'sedici',
    '17' : 'diciassette',
    '18' : 'diciotto',
    '19' : 'diciannove',
    '20' : 'venti',
    '30' : 'trenta',
    '40' : 'quaranta',
    '50' : 'cinquanta',
    '60' : 'sessanta',
    '70' : 'settanta',
    '80' : 'ottanta',
    '90' : 'novanta'}
    
    if (n == 0):
        return 'zero'  
        

    if (n < 100):
        return conv_decimal(n, number_names)
        
    if (n < 1000):
        return conv_hundreds(n, number_names)
        
    if (n < 1000000):
        return conv_thousands(n)
        
    if (n < 1000000000):
        return conv_millions(n)
    
    return conv_billions(n)
        
        
        
def conv_decimal(n, names):
        if (n <= 20):
            return names[str(n)]
        else:
            r = ''
            r += names[str((n//10)*10)]
                
            if (n % 10) == 1 or (n % 10) == 8:  #Removes the last letter in case the last digit is 1 or 8 (ex: ventotto, trentuno)
                r = r[:-1]
        
            r += names[str(n % 10)]
            return r
        
def conv_hundreds(n, names):
        r = ''
        if (n // 100) != 1:
            r += names[str(n // 100)]
        if ((n % 100) // 10) == 8:
            r += 'cent'
        else:
            r += 'cento'
        r += conv(n % 100)
        return r

def conv_thousands(n):
    r = ''
    if (n // 1000 == 1):
        r = 'mille'
    else:
        r = (conv(n // 1000) + 'mila')
    r +=  conv(n % 1000)
    return r
        
        
def conv_millions(n):
    r = ''
    
    if (n // 1000000 == 1):
        r = 'unmilione'
    else:
        r = (conv(n // 1000000) + 'milioni')
    r +=  conv(n % 1000000)
    
    return r
    
def conv_billions(n):
    r = ''
    
    if (n // 1000000000 == 1):
        r = 'unmiliardo'
    else:
        r = (conv(n // 1000000000) + 'miliardi')
    r +=  conv(n % 1000000000)
    
    return r
        
if __name__ == '__main__':

    print('84002        : ' + conv(84002))
    print('4102         : ' + conv(4102))
    print('1402         : ' + conv(1402))
    print('888888       : ' + conv(888888))
    print('981008818    : ' + conv(981008818))
    print('999999999999 : ' + conv(999999999999))
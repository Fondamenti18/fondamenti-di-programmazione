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

primi10 = ['', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
def decina(n):
     primi19List = ['', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici',
                    'dodici', 'tredici', 'quattordici','quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
     decineList = ['', '', 'venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta','settanta', 'ottanta', 'novanta']
     try:
         
         if int(str(n)[-2:]) < 20:
             return primi19List[int(str(n)[- 2:])]
     
         elif  int(str(n)[-1]) == 1 or int(str(n)[-1]) == 8:
            decine2 = (decineList[int(str(n)[-2])])[:-1]
            return decine2 +  primi19List[int(str(n)[- 1:])]
     
    
         else:  
             decine = (decineList[int(str(n)[-2])])
             
             return decine + primi19List[int(str(n)[- 1:])]
     except IndexError and ValueError:
        return ''
def centinaia(n):
    
    try:
        if int(str(n)[-2]) == 8:
            c = 'cent'
        else:
            c = 'cento'
        if int(str(n)[-3]) > 1:
            return primi10[int(str(n)[-3])] + c + decina(int(str(n)[-2:]))
        elif int(str(n)[-3]) ==1:
            return c + decina(int(str(n)[-2:]))
        else:
            return '' + decina(int(str(n)[-2:]))
    except IndexError or ValueError:
         return '' + decina(int(str(n)[-2:]))

def migliaia(n):
    try:
        if int(str(n)[-6:-3]) == 1:
            return 'mille'
        elif int(str(n)[-6:-3]) > 1:
            return centinaia(int(str(n)[-6:-3])) + 'mila'
        else:
            return '' 
    except IndexError and ValueError:
         return ''
   

def milioni(n):
    try:
        if int(str(n)[-9:-6]) == 1:
            return 'unmilione'
        elif int(str(n)[-9:-6]) > 1:
            return centinaia(int(str(n)[-9:-6])) + 'milioni'
        else:
            return ''
    except IndexError and ValueError:
        return ''
 
def miliardi(n):
    try:
        if int(str(n)[-12:-9]) == 1:
            return 'unmiliardo'
        elif int(str(n)[-12:-9]) > 1:
            return centinaia(int(str(n)[-12:-9])) + 'miliardi'
        else:
            return ''
    except IndexError and ValueError:
            return ''
def conv(n):       
    return (miliardi(n) + milioni(n) + migliaia(n) + centinaia(n))  

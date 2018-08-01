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
    
    
    numeroLettere = ''
    if n == 0: 
        numeroLettere = 'zero'
    elif n <= 19:
        numeroLettere = controllo(n)
        
    elif n <= 99:
        decine = {20:'venti', 30:'trenta',40:'quaranta', 50:'cinquanta', 
                  60:'sessanta', 70:'settanta', 80:'ottanta', 90:'novanta'}
        
        unita = n%10
        lettera = list(decine[n-(unita)])
        if unita == 1 or unita == 8: 
            lettera = lettera[:-1] 
        return ''.join(lettera + controllo(unita))
   
    elif n <= 199:
        return "cento" +''.join(conv(n%100))
    
    elif n <= 999:
        lettera = "cent"
        if int(n%100/10) != 8:
            lettera = lettera + "o"
        return conv(int(n/100)) + lettera + conv(n%100)
    
    elif n<= 1999 :
        return "mille" + conv(n%1000)
     
    elif n<= 999999:
        return conv(int(n/1000)) + "mila" + conv(n%1000)
         
    elif n <= 1999999:
        return "unmilione" +conv(n%1000000)
    
    elif n <= 999999999:
        return conv(int(n/1000000))+ "milioni" + conv(n%1000000)
    
    elif n <= 1999999999:
        return "unmiliardo" + conv(n%1000000000)
         
    else:
        return conv(int(n/1000000000)) + "miliardi" + conv(n%1000000000)
    
    return ''.join(numeroLettere)
    
    
    
 
def controllo(n):
    cifre = {1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque', 6:'sei', 7:'sette', 8:'otto', 9:'nove', 
             10:'dieci', 11:'undici', 12:'dodici', 13:'tredici', 14:'quattordici', 15:'quindici',
             16:'sedici', 17:'diciassette', 18:'diciotto', 19:'dicianove'} 
    
    return [cifre[k] for k in cifre.keys() if n == k]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    print(conv(981008818))
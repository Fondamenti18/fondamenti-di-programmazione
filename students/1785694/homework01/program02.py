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
     unita = {1: 'uno', 2: 'due', 3: 'tre', 4: 'quattro', 5: 'cinque', 6: 'sei', 7: 'sette', 8: 'otto', 9: 'nove', 0: ''}
     decine = {10: 'dieci', 11: 'undici', 12: 'dodici', 13: 'tredici', 14: 'quattordici', 15: 'quindici', 16: 'sedici', 17: 'diciassette', 18: 'diciotto', 19: 'diciannove'}
     decine2 = {0: '', 1: '', 2: 'venti', 3: 'trenta', 4: 'quaranta', 5: 'cinquanta', 6: 'sessanta', 7: 'settanta', 8: 'ottanta', 9: 'novanta'}   
     carattspec= {0: '', 1: '', 2: 'vent', 3: 'trent', 4: 'quarant', 5: 'cinquant', 6: 'sessant', 7: 'settant', 8: 'ottant', 9: 'novant'}
     d1 = n % 100
     m3 = (n // 10000) % 100   
     m4 = (n // 1000) % 100
     mil11 = (n // 1000000) % 100 
     mlrd11 = (n // 10000000000) % 100
     mlrd111 = (n // 1000000000) % 100 
     u = n % 10      
     n = n // 10
     d = n % 10      
     n = n // 10       
     c = n % 10      
     n = n // 10 
     m = n % 10      
     n = n // 10
     m1 = n % 10     
     n = n // 10
     m2 = n % 10     
     n = n // 10
     mil = n % 10   
     n = n // 10
     mil1 = n % 10  
     n = n // 10
     mil2 = n % 10          
     n = n // 10
     mlrd = n % 10                      
     n = n // 10
     mlrd2 = n % 10                     
     n = n // 10
     mlrd3 = n % 10                      
     uni = unita[u]
     dec = decine2[d]
     cent = unita[c]
     mi = unita[m]
     mi1 = decine2[m1]
     mi2 = unita[m2]
     mili = unita[mil]
     mili1 = decine2[mil1]
     mili2 = unita[mil2]
     mlrd1 = unita[mlrd]
     mlrd11 = decine2[mlrd2]
     mlrd21 = unita[mlrd3]
     if d == 1:
         dec = decine[d1]
         uni = ''
     if d != 1 and u == 1:
         dec = carattspec[d]
     if d != 1 and u == 8:
         dec = carattspec[d]
     if c == 1:                      
         cent = 'cento'
     if int(c) and d == 8:
         cent = unita[c] + 'cent' 
     if int(c) and c != 1 and d != 8:
         cent = unita[c] + 'cento'
     if m == 1 and m3 == 00:
         mi = 'mille'
     if int(m) and m3 != 00:
         mi = unita[m] + 'mila'
     if int(m1) and m1 != 1 and m == 1 or m == 8:
         mi1 = carattspec[m1] + unita[m] + 'mila'
         mi = ''
     if int(m1) and m == 0:
         mi1 = decine2[m1] + 'mila'
     if m1 == 1:
         mi1 = decine[m4] + 'mila'
         mi = ''
     if m2 == 1 and m1 != 8:
         mi2 = 'cento'
     if int(m2) and m2 != 1 and m1 == 8:
         mi2 = unita[m2] + 'cent'
     if m2 == 1 and m1 == 8:
         mi2 = 'cent'
     if m2 == 1 and m4 == 00:
         mi2 = 'centomila'
     if int(m2) and m2 != 1 and m4 == 00:
         mi2 = unita[m2] + 'centomila'
     if int(m2) and m2 != 1 and m1 != 8:
         mi2 = unita[m2] + 'cento'
           
     if int(mil) and mil == 1 and mil11 == 00:
         mili = 'unmilione'
     if mil11 is not int and mil == 1:
         mili = 'unmilione'
     if int(mil) and mil != 1:
         mili = unita[mil] + 'milioni'
     if mil1 == 1 and mil11 != 00:
         mili1 = decine[mil11] + 'milioni'
         mili = ''
     if int(mil1) and mil1 != 1 and mil11 != 00:
         mili1 = decine2[mil1]
     if int(mil1) and mil1 != 1 and mil == 1 or mil == 8:
         mili1 = carattspec[mil1] + unita[mil]  + 'milioni'
         mili = ''
     if int(mil1) and mil == 0 and mil1 != 1:
         mili1 = decine2[mil1] + 'milioni'    
     if mil2 == 1 and mil11 == 00:
         mili2 = 'centomilioni'
     if mil2 == 1 and mil1 == 8:
         mili2 = 'cent'
     if int(mil2) and mil2 != 1 and mil1 == 8:
         mili2 = unita[mil2]  + 'cent'
     if mil2 == 1 and mil1 != 8:
         mili2 = 'cento'    
     if int(mil2) and mil2 != 1 and mil11 == 00:
         mili2 = unita[mil2] + 'centomilioni'
     if int(mil2) and mil2 != 1 and mil1 != 8:
         mili2 = unita[mil2] + 'cento'
     if mlrd == 1 and mlrd11 == 00:
         mlrd1 = 'unmiliardo'
     if int(mlrd) and mlrd != 1:
         mlrd1 = unita[mlrd] + 'miliardi'
     if mlrd2 == 1:
         mlrd11 = decine[mlrd111] + 'miliardi'
         mlrd1 = ''
     if int(mlrd2) and mlrd2 != 1:
         mlrd11 = decine2[mlrd2]
     if mlrd2 != 1 and mlrd == 1 or mlrd == 8:
         mlrd11 = carattspec[mlrd2] + unita[mlrd] + 'miliardi'
         mlrd1 = ''
     if mlrd3 == 1 and  mlrd111 == 00:
         mlrd = 'centomiliardi'
     if int(mlrd3) and mlrd3 != 1 and mlrd111 == 00:
         mlrd21 = unita[mlrd3] + 'centomiliardi'
     if int(mlrd3) and mlrd3 != 1 and mlrd11 != 00:
         mlrd21 = unita[mlrd3] + 'cento'
     if mlrd3 == 1 and mlrd11 != 00:
         mlrd21 = 'cento'
     if int(mlrd3) and mlrd2 == 8:
         mlrd21 = unita[mlrd3] + 'cent'
     return str(mlrd21) + str(mlrd11) + str(mlrd1) + str(mili2) + str(mili1) + str(mili) + str(mi2) + str(mi1) + str(mi) + str(cent) + str(dec) + str(uni)
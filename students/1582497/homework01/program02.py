# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:46:40 2017

@author: Pietro
"""

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

    n_list = list(reversed(str(n)))
    billions =[int(x) for x in n_list[9:12]]
    millions = [int(x) for x in n_list[6:9]]
    thousands = [int(x) for x in n_list[3:6]]
    hundreds = [int(x) for x in n_list[0:3]]
    
    zerototen = {0: '',1: 'uno',2: 'due',3: 'tre',4: 'quattro',5: 'cinque',6: 'sei',7: 'sette'
             ,8: 'otto',9: 'nove',10: 'dieci'}
    eleventonineteen = {10: 'dieci',11: 'undici',12: 'dodici',13: 'tredici',14: 'quattordici',15: 'quindici',
                        16: 'sedici',17: 'diciassette',18: 'diciotto',19: 'diciannove'}
    tens = {0:'',1: 'dieci',2: 'venti',3: 'trenta',4: 'quaranta',5: 'cinquanta',
            6: 'sessanta',7: 'settanta',8: 'ottanta',9: 'novanta'}
                
    number1 = ''
    number2 = ''
    number3 = ''
    number4 = ''
    
    for x in range(len(billions)+1):            
        if x == 1:
            if billions[x-1] == 0:
                number4 = ''
            elif len(billions) == 1 and billions[0] == 1:
                number4 = 'unmiliardo'
            elif len(billions) >= 2 and billions[x] == 1:
                number4 = ''
            elif len(billions) == 1 and billions[0] != 1:
                number4 = zerototen[billions[x-1]]+'miliardi'
            else:
                number4 = zerototen[billions[x-1]]
                
        if x == 2:
            if billions[x-1] == 0:
                number4 = '' + number4
            elif billions[x-1] == 1 and len(billions) == 2:
                number4 = eleventonineteen[10+billions[x-2]]+'miliardi'
            elif billions[x-1] == 1 and len(billions) > 2:
                number4 = eleventonineteen[10+billions[x-2]]
            elif len(billions) == 2:
                if billions[x-2] == 1 or billions[x-2] == 8:
                    number4 = tens[billions[1]][:-1]+number4+'miliardi'
                else: 
                    number4 = tens[billions[1]]+number4+'miliardi'  
            else:
                if billions[x-2] == 1 or billions[x-2] == 8:
                    number4 = tens[billions[1]][:-1]+number4
                else:
                    number4 = tens[billions[1]]+number4
        
        if x == 3:
            if billions[x-1] == 1:
                if billions[x-2] == 8:
                    number4 = 'cent'+number4+'miliardi'
                else:
                    number4 = 'cento' + number4+'miliardi'
            else:
                if billions[x-2] == 8:
                    number4 = zerototen[billions[x-1]] + 'cent'+number4+'miliardi'
                else:
                    number4 = zerototen[billions[x-1]] + 'cento'+number4+'miliardi'
    
    for x in range(len(millions)+1):            
        if x == 1:
            if millions[x-1] == 0:
                number3 = ''
            elif len(millions) == 1 and millions[0] == 1:
                number3 = 'unmilione'
            elif len(millions) >= 2 and millions[x] == 1:
                number3 = ''
            elif len(millions) == 1 and millions[0] != 1:
                number3 = zerototen[millions[x-1]]+'milioni'
            else:
                number3 = zerototen[millions[x-1]]+'milioni'
                
        if x == 2:
            if millions[x-1] == 0:
                number3 = '' + number3
            elif millions[x-1] == 1 and len(millions) == 2:
                number3 = eleventonineteen[10+millions[x-2]]+'milioni'
            elif millions[x-1] == 1 and len(millions) > 2:
                number3 = eleventonineteen[10+millions[x-2]]+'milioni'
            elif len(millions) == 2:
                if millions[x-2] == 1 or millions[x-2] == 8:
                    number3 = tens[millions[1]][:-1]+number3+'milioni'
                else: 
                    number3 = tens[millions[1]]+number3+'milioni'  
            else:
                if millions[x-2] == 1 or millions[x-2] == 8:
                    number3 = tens[millions[1]][:-1]+number3
                elif millions[0] == 0:                    
                    number3 = tens[millions[1]]+number3+'milioni'
                else:
                    number3 = tens[millions[1]]+number3
          
        if x == 3:
            if millions[x-1] == 0:
                number3 += ''
            elif millions[x-1] == 1:
                if millions[x-2] == 8:
                    number3 = 'cent'+number3+'milioni'
                elif millions[0] == 0 and millions[1] == 0:
                    number3 = 'cento' + number3+'milioni'
                else:
                    number3 = 'cento' + number3
            else:
                if millions[x-2] == 8:
                    if millions[0] == 0 and millions[1] == 0:
                        number3 = zerototen[millions[x-1]] + 'cent'+number3+'milioni'
                    else:
                        number3 = zerototen[millions[x-1]] + 'cent'+number3
                elif millions[0] == 0 and millions[1] == 0:
                    number3 = zerototen[millions[x-1]] + 'cento'+number3+'milioni' 
                else:
                    number3 = zerototen[millions[x-1]] + 'cento'+number3            
                    
                    
    for x in range(len(thousands)+1):
        if x == 1:
            if thousands[x-1] == 0:
                number2 = ''
            elif len(thousands) == 1 and thousands[0] == 1:
                number2 = 'mille'
            elif len(thousands) >= 2 and thousands[x] == 1:
                number2 = ''
            elif len(thousands) == 1 and thousands[0] != 1:
                number2 = zerototen[thousands[x-1]]+'mila'
            else:
                number2 = zerototen[thousands[x-1]]+'mila'
                
        if x == 2:
            if thousands[x-1] == 0:
                number2 = '' + number2
            elif thousands[x-1] == 1 and len(thousands) == 2:
                number2 = eleventonineteen[10+thousands[x-2]]+'mila'
            elif thousands[x-1] == 1 and len(thousands) > 2:
                number2 = eleventonineteen[10+thousands[x-2]]+'mila'
            elif len(thousands) == 2:
                if thousands[x-2] == 1 or thousands[x-2] == 8:
                    number2 = tens[thousands[1]][:-1]+number2+'mila'
                else: 
                    number2 = tens[thousands[1]]+number2+'mila'  
            else:
                if thousands[x-2] == 1 or thousands[x-2] == 8:
                    number2 = tens[thousands[1]][:-1]+number2
                elif thousands[0] == 0:
                    number2 = tens[thousands[1]]+number2+'mila'
                else:
                    number2 = tens[thousands[1]]+number2
        
        if x == 3:
            if thousands[x-1] == 0:
                number2 += ''
            elif thousands[x-1] == 1:
                if thousands[x-2] == 8:
                    number2 = 'cent'+number2+'mila'
                elif thousands[0] == 0 and thousands[1] == 0:
                    number2 = 'cento' + number2+'mila'
                else:
                    number2 = 'cento' + number2
            else:
                if thousands[x-2] == 8:
                    if thousands[0] == 0 and thousands[1] == 0:
                        number2 = zerototen[thousands[x-1]] + 'cent'+number2+'mila'
                    else:
                        number2 = zerototen[thousands[x-1]] + 'cent'+number2
                elif thousands[0] == 0 and thousands[1] == 0:
                    number2 = zerototen[thousands[x-1]] + 'cento'+number2+'mila' 
                else:
                    number2 = zerototen[thousands[x-1]] + 'cento'+number2
        
        
    for x in range(len(hundreds)+1):            
        if x == 1:
            if hundreds[x-1] == 0:
                number1 = ''
            elif len(hundreds) >= 2 and hundreds[x] == 1:
                number1 = ''
            else:
                number1 = zerototen[hundreds[x-1]]
                
        if x == 2:
            if hundreds[x-1] == 0:
                number1 = '' + number1
            elif hundreds[x-1] == 1:
                number1 += eleventonineteen[10+hundreds[x-2]]
            else:
                if hundreds[x-2] == 1 or hundreds[x-2] == 8:
                    number1 = tens[hundreds[1]][:-1]+number1
                else: 
                    number1 = tens[hundreds[1]]+number1    
        if x == 3:
            if hundreds[x-1] == 0:
                number1 += ''
            elif hundreds[x-1] == 1:
                if hundreds[x-2] == 8:
                    number1 = 'cent'+number1
                else:
                    number1 = 'cento' + number1
            else:
                if hundreds[x-2] == 8:
                    number1 = zerototen[hundreds[x-1]] + 'cent'+number1
                else:
                    number1 = zerototen[hundreds[x-1]] + 'cento'+number1    
    
    return number4+number3+number2+number1

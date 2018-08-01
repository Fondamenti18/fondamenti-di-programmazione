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


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1.000.000.000.000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''
ls = ['','','','','','','','','','','','','']

def unita(n, a = -1):
    n1 = str(n)
    if n1[a] == '0':
        if a == -1:
            ls.append('zero')
    if n1[a] == '1':
        if a == -1:
            ls.append('uno')
        return 'uno'
    if n1[a] == '2':
        if a == -1:
            ls.append('due')
        return 'due'
    if n1[a] == '3':
        if a == -1:
            ls.append('tre') 
        return 'tre'
    if n1[a] == '4':
        if a == -1:
            ls.append('quattro')
        return 'quattro'
    if n1[a] == '5':
        if a == -1:
            ls.append('cinque')
        return 'cinque'
    if n1[a] == '6':
        if a == -1:
            ls.append('sei') 
        return 'sei'
    if n1[a] == '7':
        if a == -1:
            ls.append('sette')     
        return 'sette'
    if n1[a] == '8':
        if a == -1:
            ls.append('otto')
        return 'otto'
    if n1[a] == '9':
        if a == -1:
            ls.append('nove')  
        return 'nove'
    

def decine1(n, a = -1):
    n1 = str(n)
    if n1[a-1] == '1' and n1[a] == '0':
        if a == -1:
            ls.insert(-1,'dieci')
        return 'dieci'
    if n1[a-1] == '1' and n1[a] == '1':
        if a == -1:
            ls.insert(-1,'undici')
        return 'undici'
    if n1[a-1] == '1' and n1[a] == '2':
        if a == -1:
            ls.insert(-1,'dodici')
        return 'dodici'
    if n1[a-1] == '1' and n1[a] == '3':
        if a == -1:
            ls.insert(-1,'tredici')
        return 'tredici'
    if n1[a-1] == '1' and n1[a] == '4':
        if a == -1:
            ls.insert(-1,'quattordici')
        return 'quattordici'
    if n1[a-1] == '1' and n1[a] == '5':
        if a == -1:
            ls.insert(-1,'quindici')
        return 'quindici'
    if n1[a-1] == '1' and n1[a] == '6':
        if a == -1:
            ls.insert(-1,'sedici')
        return 'sedici'
    if n1[a-1] == '1' and n1[a] == '7':
        if a == -1:
            ls.insert(-1,'diciassette')
        return 'diciassette'
    if n1[a-1] == '1' and n1[a] == '8':
        if a == -1:
            ls.insert(-1,'diciotto')
        return 'diciotto'
    if n1[a-1] == '1' and n1[a] == '9':
        if a == -1:
            ls.insert(-1,'diciannove')
        return 'diciannove'

def decine2(n, a = -2):
    n1 = str(n)
    if n1[a] == '2':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            ls.insert(-2,'venti')
            return 'venti'
        else:
            ls.insert(a,'vent')
            return 'vent'
    if n1[a] == '3':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            ls.insert(-2,'trenta')
            return 'trenta'
        else:
            ls.insert(a,'trent')
            return 'trent'
    if n1[a] == '4':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            ls.insert(-2,'quaranta')
            return 'quaranta'
        else:
            ls.insert(a,'quarant')
            return 'quarant'
    if n1[a] == '5':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            ls.insert(-2,'cinquanta')
            return 'cinquanta'
        else:
            ls.insert(a,'cinquant')
            return 'cinquant'
    if n1[a] == '6':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            ls.insert(-2,'sessanta')
            return 'sessanta'
        else:
            ls.insert(a,'sessant')
            return 'sessant'
    if n1[a] == '7':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            ls.insert(-2,'settanta')
            return 'settanta'
        else:
            ls.insert(a,'settant')
            return 'settant'
    if n1[a] == '8':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            ls.insert(-2,'ottanta')
            return 'ottanta'
        else:
            ls.insert(a,'ottant')
            return 'ottant'
    if n1[a] == '9':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            ls.insert(-2,'novanta')
            return 'novanta'
        else:
            ls.insert(a,'novant')
            return 'novant'
        
def decine3(n, a = -2):
    n1 = str(n)
    if n1[a] == '2':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            return 'venti'
        else:
            return 'vent'
    if n1[a] == '3':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            return 'trenta'
        else:
            return 'trent'
    if n1[a] == '4':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            return 'quaranta'
        else:
            return 'quarant'
    if n1[a] == '5':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            return 'cinquanta'
        else:
            return 'cinquant'
    if n1[a] == '6':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            return 'sessanta'
        else:
            return 'sessant'
    if n1[a] == '7':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            return 'settanta'
        else:
            return 'settant'
    if n1[a] == '8':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            return 'ottanta'
        else:
            return 'ottant'
    if n1[a] == '9':
        if a == -2 and n1[-1] != '1' and n1[-1] != '8':
            return 'novanta'
        else:
            return 'novant'

def centinaia(n):
    n1 = str(n)
    stringa = 'cento'
    if n1[-3] == '1':
        if n1[-2] != '8':
            ls.insert(-3, stringa)
        else:
            ls.insert(-3, 'cent')

           
    if n1[-3] == '2' or n1[-3] == '3' or n1[-3] == '4' or n1[-3] == '5' or n1[-3] == '6' or n1[-3] == '7' or n1[-3] == '8' or n1[-3] == '9':
        if n1[-2] != '8':
            v = unita(n,-3)
            ls.insert(-3, v + stringa)
        else:
            v = unita(n,-3)
            ls.insert(-3, v + 'cent')

def migliaia(n):
    n1 = str(n)
    stringa = 'mila'
    if len(n1) >= 5:
        if len(n1) > 5:
            if n1[-6] == '1':
                v = unita(n,-6)
                if n1[-5] == '0' and n1[-4] != '0':
                    v = unita(n,-4)
                    ls.insert(-6, 'cento' + v)
                if n1[-5] == '8':
                    ls.insert(-6, 'cent') 
                if n1[-5] != '0':
                    ls.insert(-6, 'cento') 
                else:
                    ls.insert(-6, 'cento' + stringa)            
            if n1[-6] == '2' or n1[-6] == '3' or n1[-6] == '4' or n1[-6] == '5' or n1[-6] == '6' or n1[-6] == '7' or n1[-6] == '8' or n1[-6] == '9':
                v = unita(n,-6)
                #a = unita(n, -4)
                if n1[-5] == '0':
                    ls.insert(-6, v + 'cento' + stringa) 
                if n1[-5] == '8' and n1[-6] == '8':
                    ls.insert(-6, v + 'cent') 
                else:
                    ls.insert(-6, v + 'cento')
            if n1[-6] == '0':
                v = unita(n, -4)
                ls.insert(-6, v)
        if n1[-5] == '1':
            if n1[-4] == '0' or n1[-4] == '1' or n1[-4] == '2' or n1[-4] == '3' or n1[-4] == '4' or n1[-4] == '5' or n1[-4] == '6' or n1[-4] == '7' or n1[-4] == '8' or n1[-4] == '9':
                v = decine1(n, -4)
                if n1[-4] == '0':
                    ls.insert(-5, v + stringa)
                else:
                    ls.insert(-5, v)        
        if n1[-5] == '2' or n1[-5] == '3' or n1[-5] == '4' or n1[-5] == '5' or n1[-5] == '6' or n1[-5] == '7' or n1[-5] == '8' or n1[-5] == '9':
                v = decine2(n, -5)
                b = unita(n,-4)
                if n1[-4] == '0':
                    ls.insert(-5, v + stringa)
                else:
                    ls.insert(-5, v + b)
        if n1[-4] == '2' or n1[-4] == '3' or n1[-4] == '4' or n1[-4] == '5' or n1[-4] == '6' or n1[-4] == '7' or n1[-4] == '8' or n1[-4] == '9':
            v = unita(n,-4)
            ls.insert(-4, stringa)     
    elif len(n1) < 5 or (n1[-5] == '0' or n1[-5] == '1' or n1[-5] == '2' or n1[-5] == '3' or n1[-5] == '4' or n1[-5] == '5' or n1[-5] == '6' or n1[-5] == '7' or n1[-5] == '8' or n1[-5] == '9'):
        if n1[-4] == '1':
            ls.insert(-4,'mille')
        if n1[-4] == '2' or n1[-4] == '3' or n1[-4] == '4' or n1[-4] == '5' or n1[-4] == '6' or n1[-4] == '7' or n1[-4] == '8' or n1[-4] == '9':
            v = unita(n,-4)
            ls.insert(-4, v + stringa) 
                    
def milioni(n):
    n1 = str(n)
    stringa = 'milione'
    stringa2 = 'milioni'
    if len(n1) > 8:
        if n1[-9] == '1':
            if n1[-8] != '8':
                ls.insert(-9, 'cento' + stringa2)
            else:
                ls.insert(-9, 'cent' + stringa2)
        if n1[-9] == '0' or n1[-9] == '2' or n1[-9] == '3' or n1[-9] == '4' or n1[-9] == '5' or n1[-9] == '6' or n1[-9] == '7' or n1[-9] == '8' or n1[-9] == '9':
            if n1[-8] != '8':
                v = unita(n,-9)
                ls.insert(-9, v + 'cento') 
            else:
                v = unita(n,-9)
                ls.insert(-9, v + 'cent')
    if len(n1) > 7:
        if n1[-8] == '1' and (n1[-7] == '0' or n1[-7] == '1' or n1[-7] == '2' or n1[-7] == '3' or n1[-7] == '4' or n1[-7] == '5' or n1[-7] == '6' or n1[-7] == '7' or n1[-7] == '8' or n1[-7] == '9'):
            v = decine1(n,-7)
            ls.insert(-8, v + stringa2)
        if n1[-8] == '2' or n1[-8] == '3' or n1[-8] == '4' or n1[-8] == '5' or n1[-8] == '6' or n1[-8] == '7' or n1[-8] == '8' or n1[-8] == '9':
            v = decine3(n,-8)
            if n1[-7] == '0':
                ls.insert(-8, stringa2)
            else:
                a = unita(n, -7)
                ls.insert(-8, v + a + stringa2)
    if len(n1) == 6 or len(n1) == 7:
        if n1[-7] == '1':
            v = unita(n,-7)
            ls.insert(-7, v + stringa)
        if n1[-7] == '2' or n1[-7] == '3' or n1[-7] == '4' or n1[-7] == '5' or n1[-7] == '6' or n1[-7] == '7' or n1[-7] == '8' or n1[-7] == '9':
            v = unita(n,-7)
            ls.insert(-7, v + stringa2)

def conv(n):
    a = 0
    n1 = str(n)
    lung = len(n1)
    if lung >= 7:
        milioni(n)
        migliaia(n)
        centinaia(n)
        decine2(n)
        decine1(n)
        if n1[-2] != '1':
            unita(n)        
    if lung == 6 or lung == 5 or lung == 4:
        migliaia(n)
        centinaia(n)
        decine2(n)
        decine1(n)
        if n1[-2] != '1':
            unita(n)
    if lung == 3:
        centinaia(n)
        decine2(n)
        decine1(n)
        if n1[-2] != '1':
            unita(n)
    if lung == 2:
        if n1[-2] == '1':
            decine1(n)
        if (n1[-2] == '2' or n1[-2] == '3' or n1[-2] == '4' or n1[-2] == '5' or n1[-2] == '6' or n1[-2] == '7' or n1[-2] == '8' or n1[-2] == '9'):
            decine2(n)
            unita(n)
    if lung == 1:
        unita(n)
    if len(n1) >= 2 and ls[len(ls)-1] == 'zero':
        del ls[len(ls)-1]
    while a < len(ls):
        if ls[a] == '':
            ls.pop(a)
        else:
            a+=1        
    #print('ls ', ls)
    s = ''.join(ls)
    #print('stringa ', s)
    del ls[0:len(ls)]
    for i in range (13):
        ls.append('')
    return (s)
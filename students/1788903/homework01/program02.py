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
##    numero = str(n)
    base = ['','uno','due','tre','quattro','cinque',
            'sei','sette','otto','nove','dieci',
            'undici','dodici','tredici','quattordici','quindici',
            'sedici','diciassette','diciotto','diciannove']
    decine = ['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    centinaia = 'cento'
    migliaia = ['','mille','mila']
    milioni = ['','unmilione','milioni']
    miliardo = ['','unmiliardo']
    
    unita = int(str(n)[-1])
    if n > 10:
        dec = int(str(n)[1:])
    
    i_dec = n//10
    i_cent = n // 100
    i_migl = n // 1000

    if n <= 19:
        return base[n]

    if n <= 99:
        if n % 10 == 1 or n % 10 == 8:
            return decine[i_dec][:-1] + base[unita]
        else:
            return decine[i_dec] + base[unita]

    if n <= 999:
        if str(n)[0] == '1':
            return centinaia + conv(n%100)
        else:
            return conv(n//100) + centinaia + conv(n%100)
##        if int(str(n)[1:]) % 10 == 1 or int(str(n)[1:]) % 10 == 8 :
##            return base[i_cent] + centinaia + decine[dec//10][:-1] + base[unita]
##        elif str(n)[0] == '1':
##            return centinaia + decine[int(dec/10)][:-1] + base[unita]
##        else:
##            return base[i_cent] + centinaia + decine[dec//10] + base[unita]

    if n <= 1999:
        if int(str(n)[2:]) % 10 == 1 or int(str(n)[2:]) % 10 == 8 :
            if str(n)[1] == '0':
                return migliaia[1] + base[int(str(n)[1:])//100] + decine[int(str(n)[2:])//10][:-1] + base[unita]
            return migliaia[1] + base[int(str(n)[1:])//100] + centinaia + decine[int(str(n)[2:])//10][:-1] + base[unita]
        else:
            return migliaia[1] + base[int(str(n)[1:])//100] + centinaia + decine[int(str(n)[2:])//10] + base[unita]

    if n <= 999999:
        return conv(int(n/1000)) + migliaia[2] + conv(n%1000)
##        if int(numero[1:3]) % 10 == 1 or int(numero[1:3]) % 10 == 8:
##            return base[int(numero[0:1])] + centinaia + decine[int(numero[1:3])//10][:-1] + base[int(numero[2:3])] + migliaia[2] + base[int(numero[3:4])] + centinaia + decine[int(numero[4:])//10] + base[unita]
##        elif int(numero[4:]) % 10 == 1 or int(numero[4:]) % 10 == 8:
##            return base[int(numero[0:1])] + centinaia + decine[int(numero[1:3])//10] + base[int(numero[2:3])] + migliaia[2] + base[int(numero[3:4])] + centinaia + decine[int(numero[4:])//10][:-1] + base[unita]
##        elif int(numero[1:3]) % 10 == 1 and int(numero[4:]) % 10 == 1 or int(numero[1:3]) % 10 == 8 and int(numero[4:]) % 10 == 8:
##            return base[int(numero[0:1])] + centinaia + decine[int(numero[1:3])//10][:-1] + base[int(numero[2:3])] + migliaia[2] + base[int(numero[3:4])] + centinaia + decine[int(numero[4:])//10][:-1] + base[unita]
##        else:
##            return base[int(numero[0:1])] + centinaia + decine[int(numero[1:3])//10] + base[int(numero[2:3])] + migliaia[2] + base[int(numero[3:4])] + centinaia + decine[int(numero[4:])//10] + base[unita]
##
    if n <= 1999999:
        return milioni[1] + conv(n%1000000)
##        if int(numero[2:4]) % 10 == 1 or int(numero[2:4]) % 10 == 8:
##            return milioni[1] + base[int(numero[1:2])] + centinaia + (decine[int(numero[2:4])//10][:len(numero)-1]) + base[int(numero[3:4])] + migliaia[2] + base[int(numero[4:5])] + centinaia + decine[int(numero[5:])//10] + base[unita]
##        elif int(numero[5:]) % 10 == 1 or int(numero[5:]) % 10 == 8:
##            return milioni[1] + base[int(numero[1:2])] + centinaia + decine[int(numero[2:4])//10] + base[int(numero[3:4])] + migliaia[2] + base[int(numero[4:5])] + centinaia + (decine[int(numero[5:])//10][:len(numero)-1]) + base[unita]
##        elif int(numero[2:4]) % 10 == 1 and int(numero[5:]) % 10 == 1 or int(numero[2:4]) % 10 == 8 and int(numero[5:]) % 10 == 8:
##            return milioni[1] + base[int(numero[1:2])] + centinaia + (decine[int(numero[2:4])//10][:len(numero)-1]) + base[int(numero[3:4])] + migliaia[2] + base[int(numero[4:5])] + centinaia + (decine[int(numero[5:])//10][:len(numero)-1]) + base[unita]
##        else:
##            return milioni[1] + base[int(numero[1:2])] + centinaia + decine[int(numero[2:4])//10] + base[int(numero[3:4])] + migliaia[2] + base[int(numero[4:5])] + centinaia + decine[int(numero[5:])//10] + base[unita]
##
    if n <= 999999999:
        return conv(int(n/1000000)) + milioni[2] + conv(int(n%10000))

print(conv(981008818))

    

    

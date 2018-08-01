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


def conv(n):
    'Scrivete qui il codice della funzione'
    n_1a9 = {1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove'}
    n_decine = {10:'diec',20:'vent',30:'trent',40:'quarant',50:'cinquant',60:'sessant',70:'settant',80:'ottant',90:'novant'}
    dieci = {11:'un',12:'do',13:'tre',14:'quattor',15:'quin',16:'se',17:'diciassette',18:'diciotto',19:'diciannove'}
    dici,cento,mille,mila,milione,milioni,miliardo,miliardi = 'dici','cento','mille','mila','un milione','milioni','un miliardo','miliardi'
    numero = len(str(n))
    numeroS = str(n)
    if numero == 1:                                                             #num 1 - 9
        n_f = n_1a9[n]
        return n_f
    elif numero == 2:                                                           #num 10 - 99
        if n in n_decine and n != 20 and n != 10: #cerco corrispondenze, con decine pulite
             n_f = n_decine[n] + 'a'
             return n_f
        for x in n_decine:
            if n == 20 or n == 10: # caso 20 e 10 (decine pulite con i finale < 100)
                return n_decine[n]+'i'
            elif 10 < n < 17: #caso fra 11 e 16
                n_f = dieci[n] + dici
                return n_f
            elif 17 <= n <= 19: #caso fra 17 e 19
                n_f = dieci[n]
                return n_f
            elif '1' in str(n) and n > 20: #caso fuso 1
                n_d = n-1
                n_f = n_decine[n_d] + n_1a9[1]
                return n_f
            elif '8' in str(n) and n > 20: #caso fuso 8
                n_d = n-8
                n_f = n_decine[n_d] + n_1a9[8]
                return n_f
            else: #qualsiasi altro caso esclusi i fusi, da 21 a 99
                if 22 <= n <= 29: #numeri venti prob. i finale
                    n_d = n - int(numeroS[-1])
                    n_f = n_decine[n_d]+'i'+ n_1a9[int(numeroS[-1])]
                    return n_f
                else: #restanti casi
                    n_d = n - int(numeroS[-1])
                    n_f = n_decine[n_d]+'a'+ n_1a9[int(numeroS[-1])]
                    return n_f
    elif numero == 3:                                                           #num 100 - 999
        if (numeroS[1] and numeroS[2]) == '0' and n != 100: #casi centinaia pulite > 100
            n_f = n_1a9[int(numeroS[0])] + cento
            return n_f
        elif numeroS[0] == '1': #casi del cento
            if n == 100:
                n_f = cento
                return n_f
            else: #casi da 101 a 199
                n_f = cento + conv(int(numeroS[1:]))
                return n_f
        for x in n_1a9:
            if numeroS[0] != '1' and int(numeroS[0]) == x: #casi da 201 a 999
                n_f = n_1a9[int(numeroS[0])] + cento #+ conv(int(numeroS[1:]))
                if int(numeroS[1]) == 8:
                    n_f += conv(int(numeroS[1:]))[1:]
                    return n_f
                else:
                    n_f += conv(int(numeroS[1:]))
                    return n_f 
    elif numero == 4:                                                           #num 1k - 9999 
        if numeroS[0] == '1': #casi 1k - 1999
            if numeroS[1:].count('0') == 3: # 1k
                n_f = mille
                return n_f
            else:
                n_f = mille + conv(int(numeroS[1:]))
                return n_f
        elif numeroS[0] != '1': #da 2k a 9k puliti
            if numeroS[1:].count('0') == 3:
                n_f = n_1a9[int(numeroS[0])] + mila
                return n_f
            else:         # da 2k1 a 9999 esclusi 1k
                n_f = n_1a9[int(numeroS[0])] + mila + conv(int(numeroS[1:]))
                return n_f
    elif numero == 5:                                                           #num 10k - 99k
        if numeroS[2:].count('0') == 3: #casi puliti
            n_f = conv(int(numeroS[0:2])) + mila
            return n_f
        else:
            n_f = conv(int(numeroS[0:2]))+ mila + conv(int(numeroS[2:]))
            return n_f
    elif numero == 6:                                                           #num 100k - 999k
        if numeroS[3:].count('0') == 3:
            n_f = conv(int(numeroS[0:3])) + mila
            return n_f
        else:
            n_f = conv(int(numeroS[0:3])) + mila + conv(int(numeroS[3:]))
            return n_f
    elif numero == 7:                                                           #num 1m - 9m
        if numeroS[0] == '1':
            if numeroS[1:].count('0') == 6: #caso un milione
                n_f = milione
                return n_f
            else:   #casi di 1m+1 fino a 2m -1 
                n_f = milione + conv(int(numeroS[1:])) 
                return n_f
        elif numeroS[0] != '1': #da 2m a 9m puliti
            if numeroS[1:].count('0') == 6:
                n_f = n_1a9[int(numeroS[0])] + milioni
                return n_f
            else:         # da 2m1 a 9m esclusi 1m
                n_f = n_1a9[int(numeroS[0])] + milioni + conv(int(numeroS[1:]))
                return n_f 
    elif numero == 8:                                                           #num 10m - 99m
        if numeroS[2:].count('0') == 6: #casi puliti
            n_f = conv(int(numeroS[0:2])) + milioni
            return n_f
        else:
            n_f = conv(int(numeroS[0:2]))+ milioni + conv(int(numeroS[2:]))
            return n_f    
    elif numero == 9:                                                           #num 100m - 999m
        if numeroS[3:].count('0') == 6:
            n_f = conv(int(numeroS[0:3])) + milioni
            return n_f
        else:
            n_f = conv(int(numeroS[0:3])) + milioni + conv(int(numeroS[3:]))
            return n_f
    elif numero == 10:                                                          #num 1M - 9M
        if numeroS[0] == '1': #casi 1M - 1999M
            if numeroS[1:].count('0') == 9: # 1km
                n_f = miliardo
                return n_f
            else:
                n_f = miliardo + conv(int(numeroS[1:]))
                return n_f
        elif numeroS[0] != '1': #da 2M a 9M puliti
            if numeroS[1:].count('0') == 9:
                n_f = n_1a9[int(numeroS[0])] + miliardi 
                return n_f
            else:         # da 2km1 a 9999m esclusi 1km
                n_f = n_1a9[int(numeroS[0])] + miliardi + conv(int(numeroS[1:]))
                return n_f
    elif numero == 11:                                                          #num 10M - 99M
        if numeroS[2:].count('0') == 9: #casi puliti
            n_f = conv(int(numeroS[0:2])) + miliardi
            return n_f
        else:
            n_f = conv(int(numeroS[0:2]))+ miliardi + conv(int(numeroS[2:]))
            return n_f 
    elif numero == 12:                                                          #num 100M - 999M
        if numeroS[3:].count('0') == 9:
            n_f = conv(int(numeroS[0:3])) + miliardi
            return n_f
        else:
            n_f = conv(int(numeroS[0:3])) + miliardi + conv(int(numeroS[3:]))
            return n_f
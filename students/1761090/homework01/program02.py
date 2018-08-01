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
    numeri = ("uno", "due", "tre", "quattro", "cinque", 
                "sei", "sette", "otto", "nove", "dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove", "")
    numeri2 = ["venti","trenta","quaranta","cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
    special = ["vent","trent","quarant", "cinquant", "sessant", "settant", "ottant", "novant"]
    numeri3 = ["cento", "mille", "miloni", "miliardi", "bilione"]
    if n == 19:
        return 'diciannove'
    if n == 0:
        return ""
    if 1 <= n < 19:
        return numeri[n-1]
    elif 20 <= n <= 99:
        n1 = int(n/10)
        n2 = int(n%10)
        if n2 == 8:
            return special[n1-2]+numeri[n2-1]
        elif n2 == 1:
            return special[n1-2]+numeri[n2-1]
        else: 
            return numeri2[n1-2]+numeri[n2-1]
    elif 100 <= n <= 199:
        n2 = int(n%100)
        if n2 == 80:
            return 'cent' + conv(n%100)
        if n2 == 81:
            return 'cent' + conv(n%100)
        if n2 == 82:
            return 'cent' + conv(n%100)
        if n2 == 83:
            return 'cent' + conv(n%100)
        if n2 == 84:
            return 'cent' + conv(n%100)
        if n2 == 85:
            return 'cent' + conv(n%100)
        if n2 == 86:
            return 'cent' + conv(n%100)
        if n2 == 87:
            return 'cent' + conv(n%100)
        if n2 == 88:
            return 'cent' + conv(n%100)
        if n2 == 89:
            return 'cent' + conv(n%100)
        elif n2 == 10:
            return 'cent' + conv(n%100)
        else: 
            return 'cento' + conv(n%100)
    elif 200 <=  n <= 999:
        lst = list(str(n))
        n1 = lst[0]
        pr = int(n1)
        n2 = int(n%100)
        if n2 == 80:
            return conv(pr) +'cent' + conv(n%100)
        if n2 == 81:
            return conv(pr)+'cent' + conv(n%100)
        if n2 == 82:
            return conv(pr)+'cent' + conv(n%100)
        if n2 == 83:
            return conv(pr)+'cent' + conv(n%100)
        if n2 == 84:
            return conv(pr)+'cent' + conv(n%100)
        if n2 == 85:
            return conv(pr)+'cent' + conv(n%100)
        if n2 == 86:
            return conv(pr)+'cent' + conv(n%100)
        if n2 == 87:
            return conv(pr)+'cent' + conv(n%100)
        if n2 == 88:
            return conv(pr)+'cent' + conv(n%100)
        if n2 == 89:
            return conv(pr)+'cent' + conv(n%100)
        elif n2 == 10:
            return conv(pr) +'cent' + conv(n%100)
        else: 
            return conv(pr) + 'cento' + conv(n%100)
    elif 1000 <= n <= 1999:
        return 'mille' + conv(n%1000)
    elif 2000 <= n <= 9999:
        lst = list(str(n))
        n1 = lst[0]
        pr = int(n1)
        return conv(pr) + 'mila' + conv(n%1000)
    elif 10000 <= n <= 99999:
        lst = list(str(n))
        n1 = lst[0]
        n2 = lst[1]
        pr = n1+n2
        pr1 = int(pr)
        return conv(pr1) + 'mila' + conv(n%1000)
    elif 100000 <= n <= 999999:
        lst = list(str(n))
        n1 = lst[0]
        n2 = lst[1]
        n3 = lst[2]
        pr = n1+n2+n3
        pr1 = int(pr)
        return conv(pr1) + 'mila' + conv(n%1000)
    elif n == 1000000:
        return 'unmilione'
    elif 1000001 <= n <= 1999999:
        lst = list(str(n))
        n1 = lst[0]
        pr = n1
        pr1 = int(pr)
        return 'unmilione' + conv(n%1000000)
    elif 2000000 <= n <= 9999999:
        lst = list(str(n))
        n1 = lst[0]
        pr = n1
        pr1 = int(pr)
        return conv(pr1) + 'milioni' + conv(n%1000000)
    elif 10000000 <= n <= 99999999:
        lst = list(str(n))
        n1 = lst[0]
        pr = n1
        n2 = lst[1]
        pr = n1+n2
        pr1 = int(pr)
        return conv(pr1) + 'milioni' + conv(n%1000000)
    elif 100000000 <= n <= 999999999:
        lst = list(str(n))
        n1 = lst[0]
        n2 = lst[1]
        n3 = lst[2]
        pr = n1+n2+n3
        pr1 = int(pr)
        return conv(pr1) + 'milioni' + conv(n%1000000)
    elif n == 1000000000:
        return 'unmiliardo'
    elif 1000000001 <= n <= 1999999999:
        lst = list(str(n))
        n1 = lst[0]
        pr = n1
        pr1 = int(pr)
        return 'unmiliardo' + conv(n%1000000000)
    elif 2000000000 <= n <= 9999999999:
        lst = list(str(n))
        n1 = lst[0]
        pr = n1
        pr1 = int(pr)
        return conv(pr1) + 'miliardi' + conv(n%1000000000)
    elif 10000000000 <= n <= 99999999999:
        lst = list(str(n))
        n1 = lst[0]
        pr = n1
        n2 = lst[1]
        pr = n1+n2
        pr1 = int(pr)
        return conv(pr1) + 'miliardi' + conv(n%1000000000)
    elif 100000000000 <= n <= 999999999999:
        lst = list(str(n))
        n1 = lst[0]
        n2 = lst[1]
        n3 = lst[2]
        pr = n1+n2+n3
        pr1 = int(pr)
        return conv(pr1) + 'miliardi' + conv(n%1000000000)
    elif n == 1000000000000:
        return 'un bilione'

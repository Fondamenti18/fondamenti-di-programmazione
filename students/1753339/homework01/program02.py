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
    decine_a = ['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    # decine_a è una lista che contiene tutte le decine in lettere
    decine_b = ['vent','trent','quarant','cinquant','sessant','settant','ottant','novant']
    # decine_b serve per scrivere le cifre in cui si elimina l'ultima lettera (i per venti, a per gli altri)
    num = ['uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    # num contiene i numeri da uno a nove scritti in lettere | per test di appartenenza in if/elif
    num_2 = [1,2,3,4,5,6,7,8,9]
    # num_2 contine gli interi da 2 a 9 | per test di appartenenza in if/elif
    if n <= 19:
        return('zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove')[n]
        # questo return restituisce la parola corrispondente alla cifra passata (n), se n è compreso (e uguale) tra 0 e 19
    elif 20 <= n <= 99:
        if (n//10) in num_2 and (n%10) == 0:
            return(decine_a[(n//10)-2])
            # ritorna 20 o 30 o 40.... o 90 | l'indice è n-2 perchè la lista nomina le cifre da 20 in poi
        elif (n-1)//10 in num_2 and (n%10) == 1:
            return(decine_b[((n-1)//10)-2] + 'uno')
        elif (n-8)//10 in num_2 and (n%10) == 8:
            return(decine_b[((n-8)//10)-2] + 'otto')
        else:
            #if (n//10) in num_2 and (n%10) != 1 and (n%10) != 8: QUESTA PARTE PUO' ESSERE OMESSA!!
            return(decine_a[(n//10)-2] + num[(n%10)-1])
    elif 100 <= n <= 199:
        if (n//100) == 1 and (n%100) == 0:
            return('cento')
        elif ((n%100)-(n%10)) == 80:
            return('cent' + conv(n%100))
        else:
            return('cento' + conv(n%100))
    elif 200 <= n <= 999:
        if (n//100) in num_2 and (n%100) == 0:
            return(num[(n//100)-1] + 'cento')
        elif ((n%100)-(n%10)) == 80:
            return(num[(n//100)-1] + 'cent' + conv(n%100))
        else:
            return(num[(n//100)-1] + 'cento' + conv(n%100))
    elif 1000 <= n <= 1999:
        return('mille' + conv(n%1000))
    elif 2000 <= n <= 9999:
        return(num[(n//1000)-1] + 'mila' + conv(n%1000))
    elif 10000 <= n <= 19999:
        return(conv(n//1000) + 'mila' + conv(n%1000))
    elif 20000 <= n <= 99999:
        return(conv(n//1000) + 'mila' + conv(n%1000))
    elif 100000 <= n <= 199999:
        return('cento' + conv(n%100000))
    elif 200000 <= n <= 999999:
        return(conv(n//1000) + 'mila' + conv(n%1000))
    elif 1000000 <= n <= 1999999:
        return('unmilione' + conv(n%1000000))
    elif 2000000 <= n <= 999999999:
        return(conv(n//1000000) + 'milioni' + conv(n%1000000))
    elif 1000000000 <= n <= 1999999999:
        return('unmiliardo' + conv(n%1000000000))
    elif 2000000000 <= n <= 999999999999:
        return(conv(n//1000000000) + 'miliardi' + conv(n%1000000000))

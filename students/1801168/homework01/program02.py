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
    numeriu = ['', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    numerid = ['', 'dieci', 'venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta']
    numeric = ['', 'cento', 'duecento', 'trecento', 'quattrocento', 'cinquecento', 'seicento', 'settecento', 'ottocento', 'novecento']
    numerim = ['', 'mille']
    nlst = []

    if n == 0:
        nlst = 'zero'
        
    if n >= 1 and n <= 99:
        if n >= 1 and n <= 19:
            nlst = numeriu[n]
        elif n%10 == 1 or n%10 == 8:
            nlst = numerid[n//10][:-1] + numeriu[n%10]
        else:
            nlst = numerid[n//10] + numeriu[n%10]
        
    if n >= 100 and n <= 999:
        if (n >= 100 and n <= 119 or n >= 200 and n <= 219 or n >= 300 and n <= 319
        or n >= 400 and n <= 419 or n >= 500 and n <= 519 or n >= 600 and n <= 619
        or n >= 700 and n <= 719 or n >= 800 and n <= 819 or n >= 900 and n <= 919):
            nlst = numeric[n//100] + numeriu[n%100]
        elif (n%100 == 80 or n%100 == 81 or n%100 == 82 or n%100 == 83 or n%100 == 84
            or n%100 == 85 or n%100 == 86 or n%100 == 87 or n%100 == 88 or n%100 == 89):
            nlst = numeric[n//100][:-1] + numerid[n//10%10] + numeriu[n%10]
        else:
            nlst = numeric[n//100] + numerid[(n//10%10)] + numeriu[n%10]
    
    if n >= 1000 and n <= 1999:
        if  (n%100 == 1 or n%100 == 2 or n%100 == 3 or n%100 == 4 or n%100 == 5 or n%100 == 6 or n%100 == 7 or
            n%100 == 8 or n%100 == 9 or n%100 == 10 or n%100 == 11 or n%100 == 12 or n%100 == 13 or n%100 == 14 or n%100 == 15 or
            n%100 == 16 or n%100 == 17 or n%100 == 18 or n%100 == 19):
            nlst = numerim[n//1000] + numeric[n//100%10] + numeriu[n%100]
        elif (n%100 == 80 or n%100 == 81 or n%100 == 82 or n%100 == 83 or n%100 == 84
            or n%100 == 85 or n%100 == 86 or n%100 == 87 or n%100 == 88 or n%100 == 89):
            nlst = numerim[n//1000] + numeric[n//100%10][:-1] + numerid[n//10%10] + numeriu[n%10]
        else:
            nlst = numerim[n//1000] + numeric[n//100%10] + numerid[n//10%10] + numeriu[n%10]
    
    if n >= 2000 and n <= 19999:
        if (n%100 == 1 or n%100 == 2 or n%100 == 3 or n%100 == 4 or n%100 == 5 or n%100 == 6 or n%100 == 7 or
            n%100 == 8 or n%100 == 9 or n%100 == 10 or n%100 == 11 or n%100 == 12 or n%100 == 13 or n%100 == 14 or n%100 == 15 or
            n%100 == 16 or n%100 == 17 or n%100 == 18 or n%100 == 19):
                nlst = numeriu[n//1000] + 'mila' + numeric[n//100%10] + numeriu[n%100]
        elif (n%100 == 80 or n%100 == 81 or n%100 == 82 or n%100 == 83 or n%100 == 84
            or n%100 == 85 or n%100 == 86 or n%100 == 87 or n%100 == 88 or n%100 == 89):
            nlst = numeriu[n//1000] + 'mila' + numeric[n//100%10][:-1] + numerid[n//10%10] + numeriu[n%10]
        else:
            nlst = numeriu[n//1000] + 'mila' + numeric[n//100%10] + numerid[n//10%10] + numeriu[n%10]
    
    if n >= 20000 and n <= 99999:
        if (n%100 == 1 or n%100 == 2 or n%100 == 3 or n%100 == 4 or n%100 == 5 or n%100 == 6 or n%100 == 7 or
            n%100 == 8 or n%100 == 9 or n%100 == 10 or n%100 == 11 or n%100 == 12 or n%100 == 13 or n%100 == 14 or n%100 == 15 or
            n%100 == 16 or n%100 == 17 or n%100 == 18 or n%100 == 19):
            nlst = numerid[n//10000] + numeriu[n//1000%10] + 'mila' + numeric[n//100%10] + numeriu[n%100]
        elif (n%100 == 80 or n%100 == 81 or n%100 == 82 or n%100 == 83 or n%100 == 84
            or n%100 == 85 or n%100 == 86 or n%100 == 87 or n%100 == 88 or n%100 == 89):
            nlst = numerid[n//10000] + numeriu[n//1000%10] + 'mila' + numeric[n//100%10][:-1] + numerid[n//10%10] + numeriu[n%10]
        else:
            nlst = numerid[n//10000] + numeriu[n//1000%10] + 'mila' + numeric[n//100%10] + numerid[n//10%10] + numeriu[n%10]
    
    if n >= 100000 and n <= 999999:
        if (n%100 == 1 or n%100 == 2 or n%100 == 3 or n%100 == 4 or n%100 == 5 or n%100 == 6 or n%100 == 7 or
            n%100 == 8 or n%100 == 9 or n%100 == 10 or n%100 == 11 or n%100 == 12 or n%100 == 13 or n%100 == 14 or n%100 == 15 or
            n%100 == 16 or n%100 == 17 or n%100 == 18 or n%100 == 19
            or n//1000%100 == 1 or n//1000%100 == 2 or n//1000%100 == 3 or n//1000%100 == 4 or n//1000%100 == 5 or n//1000%100 == 6
            or n//1000%100 == 7 or n//1000%100 == 8 or n//1000%100 == 9 or n//1000%100 == 10 or n//1000%100 == 11 or n//1000%100 == 12 
            or n//1000%100 == 13 or n//1000%100 == 14 or n//1000%100 == 15 or n//1000%100 == 16 or n//1000%100 == 17 or n//1000%100 == 18 
            or n//1000%100 == 19):
            nlst = numeric[n//100000] + numerid[n//10000%10] + numeriu[n//1000%100] + 'mila' + numeric[n//100%10] + numerid[n//10%10] + numeriu[n%100]
        elif (n%100 == 80 or n%100 == 81 or n%100 == 82 or n%100 == 83 or n%100 == 84
            or n%100 == 85 or n%100 == 86 or n%100 == 87 or n%100 == 88 or n%100 == 89
            or n//1000%100 == 80 or n//1000%100 == 81 or n//1000%100 == 82 or n//1000%100 == 83 or n//1000%100 == 84 or n//1000%100 == 85 or n//1000%100 == 86
            or n//1000%100 == 87 or n//1000%100 == 88 or n//1000%100 == 89):
            nlst = numeric[n//100000][:-1] + numerid[n//10000%10] + numeriu[n//1000%10] + 'mila' + numeric[n//100%10][:-1] + numerid[n//10%10] + numeriu[n%10]
        else:
            nlst = numeric[n//100000] + numerid[n//10000%10] + numeriu[n//1000%10] + 'mila' + numeric[n//100%10] + numerid[n//10%10] + numeriu[n%10]        
        
    if n >= 1000000 and n <= 1999999:
        if (n%100 == 1 or n%100 == 2 or n%100 == 3 or n%100 == 4 or n%100 == 5 or n%100 == 6 or n%100 == 7 or
            n%100 == 8 or n%100 == 9 or n%100 == 10 or n%100 == 11 or n%100 == 12 or n%100 == 13 or n%100 == 14 or n%100 == 15 or
            n%100 == 16 or n%100 == 17 or n%100 == 18 or n%100 == 19
            or n//1000%100 == 1 or n//1000%100 == 2 or n//1000%100 == 3 or n//1000%100 == 4 or n//1000%100 == 5 or n//1000%100 == 6
            or n//1000%100 == 7 or n//1000%100 == 8 or n//1000%100 == 9 or n//1000%100 == 10 or n//1000%100 == 11 or n//1000%100 == 12 
            or n//1000%100 == 13 or n//1000%100 == 14 or n//1000%100 == 15 or n//1000%100 == 16 or n//1000%100 == 17 or n//1000%100 == 18 
            or n//1000%100 == 19):
            nlst = 'unmilione' + numeric[n//100000%10]  + numerid[n//10000%10] + numeriu[n//1000%10] + 'mila' + numeric[n//100%10] +  numeriu[n%100]
        else:
            nlst = 'unmilione' + numeric[n//100000%10] + numerid[n//10000%10] + numeriu[n//1000%10] + 'mila' + numeric[n//100%10] + numerid[n//10%10] + numeriu[n%10]
            
    if n >= 2000000 or n <= 999999999:
        if (n%100 == 1 or n%100 == 2 or n%100 == 3 or n%100 == 4 or n%100 == 5 or n%100 == 6 or n%100 == 7 or
            n%100 == 8 or n%100 == 9 or n%100 == 10 or n%100 == 11 or n%100 == 12 or n%100 == 13 or n%100 == 14 or n%100 == 15 or
            n%100 == 16 or n%100 == 17 or n%100 == 18 or n%100 == 19
            or n//1000%100 == 1 or n//1000%100 == 2 or n//1000%100 == 3 or n//1000%100 == 4 or n//1000%100 == 5 or n//1000%100 == 6
            or n//1000%100 == 7 or n//1000%100 == 8 or n//1000%100 == 9 or n//1000%100 == 10 or n//1000%100 == 11 or n//1000%100 == 12 
            or n//1000%100 == 13 or n//1000%100 == 14 or n//1000%100 == 15 or n//1000%100 == 16 or n//1000%100 == 17 or n//1000%100 == 18 
            or n//1000%100 == 19
            or n//1000000%100 == 1 or n//1000000%100 == 2 or n//1000000%100 == 3 or n//1000000%100 == 4 or n//1000000%100 == 5 or n//1000000%100 == 6
            or n//1000000%100 == 7 or n//1000000%100 == 8 or n//1000000%100 == 9 or n//1000000%100 == 10 or n//1000000%100 == 11 or n//1000000%100 == 12
            or n//1000000%100 == 13 or n//1000000%100 == 14 or n//1000000%100 == 15 or n//1000000%100 == 16 or n//1000000%100 == 17 or n//1000000%100 == 18
            or n//1000000%100 == 19):
            3+1
            
        
    return nlst

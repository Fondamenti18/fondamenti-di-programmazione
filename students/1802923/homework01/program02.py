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

def cifra(n):
    out = []
    num = n

    prima_decina = [ 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove' ]
    seconda_decina = [ 'dieci', 'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove' ]
    decine = [ 'venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta' ]

    cento = 'cento'
    centinaia = [cento]

    for x in prima_decina[1:]:
        temp = x + cento
        centinaia.append(temp)

    i = int(num[-1])
    # print('La prima cifra è ' + str(i))
    seconda_cifra = None

    if len(num) == 1:
        out.append(prima_decina[i - 1])

    if len(num) > 1:
        seconda_cifra = int(num[-2])
        # print('La seconda cifra è ' + str(seconda_cifra))

        if seconda_cifra == 1:
            # print('Appendo: ' + seconda_decina[i])
            out.append(seconda_decina[i])

        elif seconda_cifra == 0:
            # print('Appendo: ' + prima_decina[i - 1])
            out.append(prima_decina[i - 1])

        else:
            x = decine[seconda_cifra - 2]

            if i == 1 or i == 8:
                x = x[:-1]
            
            if i != 0:
                out.append(prima_decina[i - 1])

            out.append(x)

    if len(num) > 2:
        # print('Numero con più di due cifre')
        i = int(num[-3])
        x = centinaia[i - 1]

        if seconda_cifra == 8:
            x = x[:-1]
        
        if num[0] != '0':
            out.append(x)

    # print(out)
    out_f = ''.join(reversed(out))
    return out_f

def conv(n):

    out = []
    num = str(n)

    if len(num) < 4:
        out = cifra(num)
        # print(out)
    else:
        out.append(cifra(num[-3:]))

        if len(num) == 4:
            if num[-4] == '1':
                out.append('mille')
            else:
                out.append('mila')
                out.append(cifra(num[-4]))

        if len(num) == 5:
            out.append('mila')
            out.append(cifra(num[:-3]))
        elif len(num) > 5:
            out.append('mila')
            out.append(cifra(num[-6:-3]))

        if len(num) == 7:
            if num[-7] == '1':
                out.append('unmilione')
            else:
                out.append('milioni')
                out.append(cifra(num[-7]))

        if len(num) == 8:
            out.append('milioni')
            out.append(cifra(num[:-5]))
        elif len(num) > 8:
            out.append('milioni')
            out.append(cifra(num[-9:-6]))

    if len(num) < 4:
        out_f = ''.join(out)
    else:
        out_f = ''.join(reversed(out))
    return out_f
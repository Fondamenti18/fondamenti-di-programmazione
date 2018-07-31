''' In determinate occasioni ci capita di dover scrivere i numeri in lettere,
ad esempio quando dobbiamo compilare un assegno.
Puo' capitare che alcuni numeri facciano sorgere in noi qualche dubbio.

Le perplessita' nascono soprattutto nella scrittura dei numeri composti con 1 e 8.
Tutti i numeri come venti, trenta, quaranta, cinquanta, ecc... elidono la vocale
finale (la 'i' per 20, la 'a' per tutti gli altri) fondendola con la vocale iniziale
del numero successivo; scriveremo quindi ventuno, ventotto, trentotto,
cinquantuno ecc...

Il numero cento, nella formazione dei numeri composti con uno e otto, non si comporta
cosi'; il numero 'cento' e tutte le centinaia (duecento, trecento, ecc...),
infatti, non elidono la vocale finale. Dunque non scriveremo centuno,  trecentotto ma centouno,
trecentootto, ecc...

I numeri composti dalle centinaia e dalla decina 'ottanta' invece tornano ad elidere
la vocale finale; scriveremo quindi centottanta, duecentottanta,  ecc...,
non centoottanta, duecentoottanta, ...

Il numero 'mille' non elide in nessun numero composto la vocale finale; scriveremo
quindi milleuno,  milleotto, milleottanta, ecc...

Altri esempi sono elencati nel file grade02.txt


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000000000000,
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def exception(m, n):
    vocal = ('a', 'e', 'i', 'o', 'u')
    if n[:1] in vocal:
        m = m[:len(m) - 1]
    return m + n


def fixed(n):
    One2Twen = {'1': 'uno', '2': 'due', '3': 'tre',
                '4': 'quattro', '5': 'cinque', '6': 'sei',
                '7': 'sette', '8': 'otto', '9': 'nove', '10': 'dieci',
                '11': 'undici', '12': 'dodici', '13': 'tredici',
                '14': 'quattordici', '15': 'quindici',
                '16': 'sedici', '17': 'diciassette',
                '18': 'diciotto', '19': 'diciannove', '0': ''
                }
    return (One2Twen[n])


def Decimi(leng, value):
    Prefix = {'2': 'venti', '3': "trenta", '4': "quaranta",
              '5': "cinquanta", '6': "sessanta",
              '7': "settanta", '8': "ottanta", '9': "novanta", '0': ''}

    if int(value) <= 9:  # if values goes from 0 to 9
        return fixed(value[leng - 1:])

    elif 10 <= int(value) <= 19:  # values 10 to 19
        return fixed(value)

    else:
        last = fixed(value[1:])
        med = Prefix[value[:1]]
        return exception(med, last)  # call exception functions


def CentosUp(leng, value):
    Prefix = {3: 'cento', 0: ''}
    Suff = Decimi(len(value[1:]), value[1:])

    if value[:1] is '0':
        return Prefix[0] + Suff
    elif value[:1] is '1':
        if Suff[:1] is 'o' and len(Suff) > 4:
            return Prefix[leng] + Suff[1:]
        else:
            return Prefix[leng] + Suff
    else:
        pre = fixed(value[:1])
        if Suff[:1] is 'o' and len(Suff) > 4:
            return pre + Prefix[leng] + Suff[1:]
        else:
            return pre + Prefix[leng] + Suff



def chkExtermis(leng,value):
    if value[:1] is '0':
        leng -=1
        value = value[1:]
    return leng, value


#def rightChoice():


def Mila(leng, value):
    prefix = {0: '', 1: 'mille', 4: 'mila'}

    leng, value = chkExtermis(leng,value)

    if leng == 5:
        pre = Decimi(len(value[:2]), value[:2])
        suffix = CentosUp(len(value[2:]), value[2:])
        return pre + prefix[leng - 1] + suffix

    elif leng == 6:  # if length is 6
        pre = CentosUp(len(value[:3]), value[:3])
        suffix = CentosUp(len(value[3:]), value[3:])
        return pre + prefix[leng - 2] + suffix


    else:
        suffix = CentosUp(len(value[1:]), value[1:])
        if value[:1] is '0':
            return prefix[0] + suffix
        elif value[:1] is '1':
            return prefix[1] + suffix

        else:
            pre = fixed(value[:1])
            return pre + prefix[leng] + suffix


def Milion(leng, value):
    prefix = {0: '', 7: 'unomilione', 8: 'milioni'}

    leng, value=chkExtermis(leng, value)

    if leng == 9:
        pre = CentosUp(len(value[:3]), value[:3])
        suffix = Mila(len(value[3:]), value[3:])
        return pre + prefix[leng - 1] + suffix

    elif leng == 8:
        pre = Decimi(len(value[:2]), value[:2])
        suffix = Mila(len(value[2:]), value[2:])
        return pre + prefix[leng] + suffix

    else:
        suffix = Mila(len(value[1:]), value[1:])
        if value[:1] is '0':
            return prefix[0] + suffix
        elif value[:1] is '1':
            return prefix[leng] + suffix
        else:
            pre = fixed(value[:1])
            return pre + prefix[leng + 1] + suffix


def Miliardi(leng, value):
    prefix = {0: '', 10: 'unmiliardo', 11: 'miliardi'}

    leng, value = chkExtermis(leng, value)

    if leng == 12:
        pre = CentosUp(len(value[:3]), value[:3])
        suffix = Milion(len(value[3:]), value[3:])

        return pre + prefix[leng - 1] + suffix

    elif leng == 11:
        pre = Decimi(len(value[:2]), value[:2])
        suffix = Milion(len(value[2:]), value[2:])

        return pre + prefix[leng] + suffix

    else:
        suffix = Milion(len(value[1:]), value[1:])
        if value[:1] is '0':
            return prefix[0] + suffix
        elif value[:1] is '1':
            return prefix[leng] + suffix
        else:
            pre = fixed(value[:1])
            return pre + prefix[leng + 1] + suffix



def checkLen(leng, n):
    '''Check the length and call the proper function to convert number in letter'''
    if leng == 1:
        return fixed(n)
    elif leng == 2:
        return Decimi(leng, n)
    elif leng == 3:
        return CentosUp(leng, n)
    elif 4 <= leng <= 6:
        return Mila(leng, n)
    elif 7 <= leng <= 9:
        return Milion(leng, n)
    elif 10 <=leng <= 12:
        return Miliardi(leng,n)


def conv(n):
    '''Scrivete qui il codice della funzione'''
    num = str(n)
    chklen = len(num)
    return checkLen(chklen, num)

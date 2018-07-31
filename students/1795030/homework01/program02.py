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
    ls = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici',
          'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    dic_1 = {'venti' : 20, 'trenta': 30, 'quaranta' : 40, 'cinquanta': 50, 'sessanta': 60, 'settanta':70,
	          'ottanta' : 80, 'novanta':90, 'cento':100}
    ls_2 = ['mille', 'mila']
    ls_3 = ['milioni', 'milione']
    ls_4 = ['miliardo', 'miliardi']
    s = str(n)
    if n < 20:
        return funzione_19_(n)
    if 20<=n<100:
        return funzione_99_(n)
    if 100<=n<1000:
        return funzione_999_(n)
    if 1000<=n<10000:
        return funzione_9999_(n)
    if 10000<=n<100000:
        return funzione_99999_(n)
    if 100000<=n<1000000:
        return funzione_999999_(n)
    if 1000000<=n<1000000000:
        return funzione_999999999_(n)
    if 1000000000<=n<1000000000000:
        return funzione_999999999999_(n)
                
                            
            
def funzione_19_(n):
    ls = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici',
          'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    for i in range(0, 20):
        if i == n:
            return ls[i]


def funzione_99_(n):
    s = str(n)
    ls = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici',
          'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    dic_1 = {'venti' : 20, 'trenta': 30, 'quaranta' : 40, 'cinquanta': 50, 'sessanta': 60, 'settanta':70,
	          'ottanta' : 80, 'novanta':90, 'cento':100}
    l = list(range(1, 20))
    if n in l:
        return ls[n]
    else:
        n1 = n - int(s[1]); lst=[]
        lst.append(n1); lst.append(int(s[1]))
        for i in lst:
            for j in dic_1:
                if i == dic_1[j]:
                    m = j
                    break
        if ls[i] == 'zero':
            return m
        else:
            lst1 = []; a = ''
            if ls[i].startswith('u') or ls[i].startswith('o'):
                for f in range(len(m)-1):
                    lst1.append(m[f])
                for el in range(len(lst1)):
                    a += lst1[el]
                return a + ls[i]
            else:
                return m + ls[i]


def funzione_999_(n):
    ls = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici',
          'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    i = 'cento'
    e = 'cent'
    s = str(n)
    if n == 100:
        return i
    l = list(range(200, 1000, 100))
    if n in l:
        for y in range(2, 10):
            if int(s[0]) == y:
                return ls[y] + i
                break
    else:
        n2 = int(s[1:])
        if int(s[0]) == 1:
            if n2 in list(range(80, 90)):
                return e + funzione_99_(n2)
            else:
                d = i + funzione_99_(n2)
                return d
        else:
            if n2 in list(range(80, 90)):
                return  ls[int(s[0])] + e + funzione_99_(n2)
            elif not n2 in list(range(80, 90)):
                d = ls[int(s[0])] + i + funzione_99_(n2)
                return d


def funzione_9999_(n):
    ls = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci', 'undici', 'dodici',
          'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto', 'diciannove']
    ls_2 = ['mille', 'mila']
    s = str(n)
    if s == '1000':
        return ls_2[0]
    elif s != '1000':
        l = list(range(1, 10))
        t = list(range(1, 11))
        if int(s[0]) in l:
            if int(s[0]) == 1 and int(s[1]) == 0 and int(s[2:]) in t:
                return ls_2[0] + funzione_19_(int(s[2:]))
            elif int(s[0]) == 1 and int(s[1]) == 0 and not int(s[2:]) in l:
                return ls_2[0] + funzione_99_(int(s[2:]))
            elif int(s[0]) == 1 and int(s[1]) !=0:
                return ls_2[0] + funzione_999_(int(s[1:]))
            elif int(s[0]) != 1 and s[1:] == '000':
                return ls[int(s[0])] + ls_2[1]
            elif int(s[0])!=1 and int(s[1])==0 and int(s[2:]) in t:
                return ls[int(s[0])] + ls_2[1] + funzione_19_(int(s[2:]))
            elif int(s[0])!=1 and int(s[1])==0 and not int(s[2:]) in t:
                return ls[int(s [0])] + ls_2[1] + funzione_99_(int(s[2:]))
            elif int(s[0])!=1 and int(s[1])!=0:
                return ls[int(s[0])] + ls_2[1] + funzione_999_(int(s[1:]))

def funzione_99999_(n):
    ls_2 = ['mille', 'mila']
    s = str(n)
    if len(s) == 5:
        l = list(range(10, 20))
        if s[2:] == '000':
            if int(s[:2]) in l:
                return funzione_19_(int(s[:2])) + ls_2[1]
            elif int(s[:2]) in list(range(20, 100)):
                return funzione_99_(int(s[:2])) + ls_2[1]
        elif s[2:]!='000':
            if int(s[:2]) in l and int(s[2:]) in list(range(100, 1000)):
                return funzione_19_(int(s[:2])) + ls_2[1] + funzione_999_(int(s[2:]))
            elif int(s[:2]) in l and int(s[2]) == 0 and int(s[3:]) in list(range(1, 20)):
                return funzione_19_(int(s[:2])) + ls_2[1] + funzione_19_(int(s[3:]))
            elif int(s[:2]) in l and int(s[2]) == 0 and int(s[3:]) in list(range(20, 100)):
                return funzione_19_(int(s[:2])) + ls_2[1] + funzione_99_(int(s[3:]))
            elif int(s[:2]) in list(range(20, 100)) and int(s[2:]) in list(range(100, 1000)):
                return funzione_99_(int(s[:2])) + ls_2[1] + funzione_999_(int(s[2:]))
            elif int(s[:2]) in list(range(20, 100)) and int(s[2]) == 0 and int(s[3:]) in list(range(1, 20)):
                return funzione_99_(int(s[:2])) + ls_2[1] + funzione_19_(int(s[3:]))
            elif int(s[:2]) in list(range(20, 100)) and int(s[2]) == 0 and int(s[3:]) in list(range(20, 100)):
                return funzione_99_(int(s[:2])) + ls_2[1] + funzione_99_(int(s[3:]))

    
def funzione_999999_(n):
    ls_2 = ['mille', 'mila']
    s = str(n)
    if s[3:] == '000':
        return funzione_999_(int(s[:3])) + ls_2[1]
    else:
        l = list(range(100, 1000))
        if int(s[3:]) in l:
            return funzione_999_(int(s[:3])) + ls_2[1] + funzione_999_(int(s[3:]))
        elif int(s[3]) == 0:
            if int(s[4:]) in list(range(1, 20)):
                return funzione_999_(int(s[:3])) + ls_2[1] + funzione_19_(int(s[4:]))
            elif int(s[4:]) in list(range(20, 100)):
                return funzione_999_(int(s[:3])) + ls_2[1] + funzione_99_(int(s[4:]))
                                     

def funzione_999999999_(n):
    ls_3 = ['milioni', 'milione']
    s = str(n)
    if len(s) == 7:
        if int(s[0]) in list(range(1, 10)):
            if s[1:]=='000000':
                if s[0] == '1':
                    return 'un' + ls_3[1]
                else:
                    return funzione_19_(int(s[0])) + ls_3[0]
            elif s[1:]!='000000':
                if s[1] == '0' and s[2] != '0':
                    if s[0] == '1':
                        return 'un' + ls_3[1] + funzione_99999_(int(s[2:]))
                    else:
                        return funzione_19_(int(s[0])) + ls_3[0] + funzione_99999_(int(s[2:]))
                elif s[1:3] == '00' and s[3] != '0':
                    if s[0] == '1':
                        return 'un' + ls_3[1] + funzione_9999_(int(s[3:]))
                    else:
                        return funzione_19_(int(s[0])) + ls_3[0] + funzione_9999_(int(s[3:]))
                elif s[1:4] == '000' and s[4] != '0':
                    if s[0] == '1':
                        return 'un' + ls_3[1] + funzione_999_(int(s[4:]))
                    else:
                        return funzione_19_(int(s[0])) + ls_3[0] + funzione_999_(int(s[4:]))
                elif s[1:5] == '0000' and s[5]!='0':
                    if s[0] == '1':
                        return 'un' + ls_3[1] + funzione_99_(int(s[5:]))
                    else:
                        return funzione_19_(int(s[0])) + ls_3[0] + funzione_99_(int(s[5:]))
                elif s[1:6]=='00000' and s[6] != '0':
                    if s[0] == '1':
                        return 'un' + ls_3[1] + funzione_19_(int(s[6:]))
                    else:
                        return funzione_19_(int(s[0])) + ls_3[0] + funzione_19_(int(s[6:]))
                else:
                    return funzione_19_(int(s[0])) + ls_3[0] + funzione_999999(int(s[1:]))
    elif len(s) == 8:
        if int(s[:2]) in list(range(10, 20)):
            if s[2:]=='000000':
                return funzione_19_(int(s[:2])) + ls_3[0]
            elif s[2:]!='000000':
                if s[2]=='0' and s[3] != '0':
                    return funzione_19_(int(s[:2])) + ls_3[0] + funzione_99999_(int(s[3:]))
                elif s[2:4]=='00' and s[4] !='0':
                    return funzione_19_(int(s[:2])) + ls_3[0] + funzione_9999_(int(s[4:]))
                elif s[2:5] == '000' and s[5] != '0':
                    return funzione_19_(int(s[:2])) + ls_3[0] + funzione_999_(int(s[5:]))
                elif s[2:6]=='0000' and s[6] != '0':
                    return funzione_19_(int(s[:2])) + ls_3[0] + funzione_99_(int(s[6:]))
                elif s[2:7]=='00000' and s[7] != '0':
                    return funzione_19_(int(s[:2])) + ls_3[0] + funzione_19_(int(len(s)-1))
                else:
                    return funzione_19_(int(s[:2])) + ls_3[0] + funzione_999999_(int(s[2:]))
        if int(s[:2]) in list(range(20, 100)):
            if s[2:]=='000000':
                return funzione_99_(int(s[:2])) + ls_3[0]
            elif s[2:]!='000000':
                if s[2]=='0' and s[3] != '0':
                    return funzione_99_(int(s[:2])) + ls_3[0] + funzione_99999_(int(s[3:]))
                elif s[2:4]=='00' and s[4] != '0':
                    return funzione_99_(int(s[:2])) + ls_3[0] + funzione_9999_(int(s[4:]))
                elif s[2:5] == '000' and s[5] != '0':
                    return funzione_99_(int(s[:2])) + ls_3[0] + funzione_999_(int(s[5:]))
                elif s[2:6]=='0000' and s[6] != '0':
                    if int(s[6:]) in list(range(10, 20)):
                        return funzione_99_(int(s[:2])) + ls_3[0] + funzione_19_(int(s[6:]))
                    else:
                        return funzione_99_(int(s[:2])) + ls_3[0] + funzione_99_(int(s[6:]))
                elif s[2:7]=='00000' and s[7] != '0':
                       return funzione_99_(int(s[:2])) + ls_3[0] + funzione_19_(len(s)-1)
                else:
                    return funzione_99_(int(s[:2])) + ls_3[0] + funzione_999999_(int(s[2:]))
    elif len(s) == 9:
        if s[3:] == '000000':
            return funzione_999_(int(s[:3])) + ls_3[0]
        elif s[3:] != '000000':
            if s[3] == '0' and s[4] != '0':
                return funzione_999_(int(s[:3])) + ls_3[0] + funzione_99999_(int(s[4:]))
            elif s[3:5] == '00' and s[5]!='0':
                return funzione_999_(int(s[:3])) + ls_3[0] + funzione_9999_(int(s[5:]))
            elif s[3:6] == '000' and s[6] != '0':
                return funzione_999_(int(s[:3])) + ls_3[0] + funzione_999_(int(s[6:]))
            elif s[3:7] == '0000' and s[7] != '0':
                if int(s[7:]) in list(range(10, 20)):
                    return funzione_999_(int(s[:3])) + ls_3[0] + funzione_19_(int(s[7:]))
                else:
                    return funzione_999_(int(s[:3])) + ls_3[0] + funzione_99_(int(s[7:]))
            elif s[3:8] == '00000' and s[8] != '0':
                return funzione_999_(int(s[:3])) + ls_3[0] + funzione_9_(len(s)-1)
            else:
                return funzione_999_(int(s[:3])) + ls_3[0] + funzione_999999_(int(s[3:]))
            
                
def funzione_999999999999_(n):
    s = str(n)
    ls_4 = ['miliardo', 'miliardi']
    l = list(range(10, 20))
    q = list(range(20, 100))
    if len(s) == 10:
        if s[0] == '1':
            if s[1:] == '000000000':
                return 'un' + ls_4[0]
            elif s[1:] != '000000000':
                if s[1] == '0' and s[2:] != '00000000':
                    return 'un' + ls_4[0] + funzione_999999999_(int(s[2:]))
                elif s[1:3] == '00' and s[3:] != '0000000':
                    return 'un' + ls_4[0] + funzione_999999999_(int(s[3:]))
                else:
                    return 'un' + ls_4[0] + funzione_999999999_(int(s[1:]))
        else:
            if s[1:] == '000000000':
                return funzione_19_(int(s[0])) + ls_4[1]
            elif s[1:] != '000000000':
                if s[1] == '0' and ls[2:] == '00000000':
                    return funzione_19_(int(s[0])) + ls_4[1] + funzione_999999999_(int(s[2:]))
                elif s[1:3] == '00' and s[3:] != '0000000':
                    return funzione_19_(int(s[0])) + ls_4[1] + funzione_999999999_(int(s[3:]))
                else:
                    return funzione_19_(int(s[0])) + ls_4[1] + funzione_999999999_(int(s[1:]))
    elif len(s) == 11:
        if int(s[:2]) in l:
            if s[2:] == '000000000':
                return funzione_19_(int(s[:2])) + ls_4[1] 
            elif s[2:] != '000000000':
                if s[2] == '0' and s[3:] == '00000000':
                    return funzione_19_(int(s[:2])) + ls_4[1] + funzione_999999999_(int(s[3:]))
                elif s[2:4] == '00' and s[4:]== '0000000':
                    return funzione_19_(int(s[:2])) + ls_4[1] + funzione_999999999_(int(s[4:]))
                else:
                    return funzione_19_(int(s[:2])) + ls_4[1] + funzione_999999999_(int(s[2:]))
        if int(s[:2]) in q:
            if s[2:] == '000000000':
                return funzione_99_(int(s[:2])) + ls_4[1] 
            elif s[2:] != '000000000':
                if s[2] == '0' and s[3:] == '00000000':
                    return funzione_99_(int(s[:2])) + ls_4[1] + funzione_999999999_(int(s[3:]))
                elif s[2:4] == '00' and s[4:]== '0000000':
                    return funzione_99_(int(s[:2])) + ls_4[1] + funzione_999999999_(int(s[4:]))
                else:
                    return funzione_99_(int(s[:2])) + ls_4[1] + funzione_999999999_(int(s[2:]))
    elif len(s) == 12:
        if s[3:] == '000000000':
            return funzione_999_(int(s[:3])) + ls_4[1]
        elif s[3:]!='000000000':
            if s[3] == '0' and s[4] != '0':
                return funzione_999_(int(s[:3])) + ls_4[1] + funzione_999999999_(int(s[4:]))
            elif s[3:5] == '00' and s[5] != '0':
                return funzione_999_(int(s[:3])) + ls_4[1] + funzione_999999999_(int(s[5:]))
            else:
                return funzione_999_(int(s[:3])) + ls_4[1] + funzione_999999999_(int(s[3:]))
            
                
                    
                            
                                                              
                                                              

            
            
            

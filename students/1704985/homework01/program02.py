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



dict_unita={'0':'',
            '1':'uno',
            '2':'due',
            '3':'tre',
            '4':'quattro',
            '5':'cinque',
            '6':'sei',
            '7':'sette',
            '8':'otto',
            '9':'nove',
            '10':'dieci',
            '11':'undici',
            '12':'dodici',
            '13':'tredici',
            '14':'quattordici',
            '15':'quindici',
            '16':'sedici',
            '17':'diciassette',
            '18':'diciotto',
            '19':'dicianove'}
dict_decine={'2':'venti',
             '3':'trenta',
             '4':'quaranta',
             '5':'cinquanta',
             '6':'sessanta',
             '7':'settanta',
             '8':'ottanta',
             '9':'novanta'}

def decine(stringa):
    return dict_decine[stringa]

def unita(stringa):
    return dict_unita[stringa]

def tripla(string_in):
    if (len(string_in)==1):
        string_out = unita(string_in[0])
    if (len(string_in)==2):
        if (string_in[0]=='1'):
            string_out = unita(string_in[0]+string_in[1])
        else:
            if (string_in[0]!='0'):
                string_out= decine(string_in[0])    
                if (string_in[1] == '1' or string_in[1] == '8'):
                    string_out = string_out[:len(string_out)-1]
                string_out = string_out + unita(string_in[1])
            else:
                string_out = unita(string_in[1])
            
    if (len(string_in)==3):
        if (string_in[0]=='1'):
            string_out = 'cento' + tripla(string_in[1]+string_in[2]) 
        else:
            if (string_in[0]=='0'):
                string_out = unita(string_in[0]) + tripla(string_in[1]+string_in[2])
            else:
                if (string_in[1]=='8'):
                    string_out = unita(string_in[0]) + 'cent' + tripla(string_in[1]+string_in[2])
                else:
                    string_out = unita(string_in[0]) + 'cento' + tripla(string_in[1]+string_in[2])

    return string_out

def sestupla(string_in):
    if (len(string_in)==4):
        if (string_in[0]=='1'):
            return 'mille'+tripla(string_in[1:])
        return tripla(string_in[0])+'mila'+tripla(string_in[1:])
    if (len(string_in)==5):
        return tripla(string_in[0]+string_in[1])+'mila'+tripla(string_in[2:])
    if (len(string_in)==6):
        if (string_in[0]=='0' and string_in[1]=='0' and string_in[2]=='0'):
            return tripla(string_in[3:])
        return tripla(string_in[:3])+'mila'+tripla(string_in[3:])



def milioni(string_in):
    if (len(string_in)==7):
        if (string_in[0]=='1'):
            return 'unmilione'+sestupla(string_in[1:])
        return tripla(string_in[0])+'milioni'+sestupla(string_in[1:])
    if (len(string_in)==8):
        if ((string_in[0])=='0' and (string_in[1])=='0'):
            return tripla(string_in[:1])+'milioni'+sestupla(string_in[1:])
    if (len(string_in)==9):
        if (string_in[0]=='0' and string_in[1]=='0' and string_in[2]=='0'):
           return sestupla(string_in[3:])
        return tripla(string_in[:3])+'milioni'+sestupla(string_in[3:])

def miliardi(string_in):
    if (len(string_in)==10):
        if (string_in[0]=='1'):
            return 'unmiliardo'+milioni(string_in[1:])
    if (len(string_in)==11):
        return tripla(string_in[:2])+'miliardi'+milioni(string_in[2:])
    if (len(string_in)==12):
        return tripla(string_in[:3])+'miliardi'+milioni(string_in[3:])
       
def conv(n):
    string_in=str (n)
    if (len(string_in)<=3):
        return tripla(string_in)
    if (len(string_in)>3 and len(string_in)<=6):
        return sestupla(string_in)
    if (len(string_in)>6 and len(string_in)<=9):
        return milioni(string_in)
    if (len(string_in)>9 and len(string_in)<=12):
        return miliardi(string_in)
    

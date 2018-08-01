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
    stringa=''
    s=str(n)
    lista1=list(s)
    lista1.reverse()
    lista=['','','','','','','','','','','','']
    lista1+=lista
    unit={'0':'','1':'uno','2':'due','3':'tre','4':'quattro','5':'cinque','6':'sei','7':'sette','8':'otto','9':'nove','10':'dieci','11':'undici','12':'dodici','13':'tredici','14':'quattordici','15':'quindici','16':'sedici','17':'diciassette','18':'diciotto','19':'diciannove','':''}
    dec={'0':'','1':'','2':'venti','3':'trenta','4':'quaranta','5':'cinquanta','6':'sessanta','7':'settanta','8':'ottanta','9':'novanta','':''}
    cento={'0':'','1':'cento','2':'duecento','3':'trecento','4':'quattrocento','5':'cinquecento','6':'seicento','7':'settecento','8':'ottocento','9':'novecento','':''}
    vent={'':'','2':'vent','3':'trent','4':'quarant','5':'cinquant','6':'sessant','7':'settant','8':'ottant','9':'novant'}
    cent={'0':'','1':'cent','2':'duecent','3':'trecent','4':'quattrocent','5':'cinquecent','6':'seicent','7':'settecent','8':'ottocent','9':'novecent','':''}
    '''@@@@@@@@@@@@@@@@@@@@@@@@@@MILIARDI@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
    if(n>999999999):
        string3=lista1[10]+lista1[9]
        try:
            if(lista1[9]=='1' and(lista1[10]=='' or(lista1[10]=='0' and lista1[11]=='0'))):
                stringa+=(cento[lista1[11]]+dec[lista1[10]]+'unmiliardo')
            else:
                stringa+=(cento[lista1[11]]+dec[lista1[10]]+unit[string3]+'miliardi')
        except KeyError:
            if(lista1[10]=='8' and (lista1[11]=='1' or lista1[11]=='2' or lista1[11]=='3'or lista1[11]=='4'or lista1[11]=='5'or lista1[11]=='6'or lista1[11]=='7'or lista1[11]=='8'or lista1[11]=='9')) and ((lista1[9]=='8' or lista1[9]=='1') and (lista1[10]=='2' or lista1[10]=='3' or lista1[10]=='4' or lista1[10]=='5' or lista1[10]=='6' or lista1[10]=='7' or lista1[10]=='8' or lista1[10]=='9')):
                stringa+=cent[lista1[11]]+vent[lista1[10]]+unit[lista1[9]]+'miliardi'
            elif((lista1[9]=='8' or lista1[9]=='1') and (lista1[10]=='2' or lista1[10]=='3' or lista1[10]=='4' or lista1[10]=='5' or lista1[10]=='6' or lista1[10]=='7' or lista1[10]=='8' or lista1[10]=='9')):
                stringa+=(cento[lista1[11]]+vent[lista1[10]]+unit[lista1[9]]+'miliardi')
            elif(lista1[10]=='8' and (lista1[11]=='1' or lista1[11]=='2' or lista1[11]=='3'or lista1[11]=='4'or lista1[11]=='5'or lista1[11]=='6'or lista1[11]=='7'or lista1[11]=='8'or lista1[11]=='9')):
                stringa+=cent[lista1[11]]+dec[lista1[10]]+unit[lista1[9]]+'miliardi'
            else:
                stringa+=(cento[lista1[11]]+dec[lista1[10]]+unit[lista1[9]]+'miliardi')
    '''@@@@@@@@@@@@@@@@@@@@@@@@@@MILIONI@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
    if(n>999999):
        string2=lista1[7]+lista1[6]
        try:
            if(lista1[6]=='1' and (lista1[7]=='' or (lista1[7]=='0' and lista1[8]=='0'))):
                stringa+=(cento[lista1[8]]+dec[lista1[7]]+'unmilione')
            else:
                stringa+=(cento[lista1[8]]+dec[lista1[7]]+unit[string2]+'milioni')
        except KeyError:
            if(lista1[7]=='8' and (lista1[8]=='1' or lista1[8]=='2' or lista1[8]=='3'or lista1[8]=='4'or lista1[8]=='5'or lista1[8]=='6'or lista1[8]=='7'or lista1[8]=='8'or lista1[8]=='9')) and ((lista1[6]=='8' or lista1[6]=='1') and (lista1[7]=='2' or lista1[7]=='3' or lista1[7]=='4' or lista1[7]=='5' or lista1[7]=='6' or lista1[7]=='7' or lista1[7]=='8' or lista1[7]=='9')):
                stringa+=cent[lista1[8]]+vent[lista1[7]]+unit[lista1[6]]+'milioni'
            elif((lista1[6]=='8' or lista1[6]=='1') and (lista1[7]=='2' or lista1[7]=='3' or lista1[7]=='4' or lista1[7]=='5' or lista1[7]=='6' or lista1[7]=='7' or lista1[7]=='8' or lista1[7]=='9')):
                stringa+=(cento[lista1[8]]+vent[lista1[7]]+unit[lista1[6]]+'milioni')
            elif(lista1[7]=='8' and (lista1[8]=='1' or lista1[8]=='2' or lista1[8]=='3'or lista1[8]=='4'or lista1[8]=='5'or lista1[8]=='6'or lista1[8]=='7'or lista1[8]=='8'or lista1[8]=='9')):
                stringa+=cent[lista1[8]]+dec[lista1[7]]+unit[lista1[6]]+'milioni'
            else:
                stringa+=(cento[lista1[8]]+dec[lista1[7]]+unit[lista1[6]]+'milioni')
    '''@@@@@@@@@@@@@@@@@@@@@@@@@MIGLIAIA@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
    if(n>999):
        string1=lista1[4]+lista1[3]
        try:
            if(lista1[3]=='1' and (lista1[4]=='' or (lista1[4]=='0' and lista1[5]=='0'))):
                stringa+=(cento[lista1[5]]+dec[lista1[4]]+'mille')
            else:
                stringa+=(cento[lista1[5]]+dec[lista1[4]]+unit[string1]+'mila')
        except KeyError:
            if(lista1[4]=='8' and (lista1[5]=='1' or lista1[5]=='2' or lista1[5]=='3'or lista1[5]=='4'or lista1[5]=='5'or lista1[5]=='6'or lista1[5]=='7'or lista1[5]=='8'or lista1[5]=='9')) and ((lista1[3]=='8' or lista1[3]=='1') and (lista1[4]=='2' or lista1[4]=='3' or lista1[4]=='4' or lista1[4]=='5' or lista1[4]=='6' or lista1[4]=='7' or lista1[4]=='8' or lista1[4]=='9')):
                stringa+=cent[lista1[5]]+vent[lista1[4]]+unit[lista1[3]]+'mila'
            elif((lista1[3]=='8' or lista1[3]=='1') and (lista1[4]=='2' or lista1[4]=='3' or lista1[4]=='4' or lista1[4]=='5' or lista1[4]=='6' or lista1[4]=='7' or lista1[4]=='8' or lista1[4]=='9')):
                stringa+=(cento[lista1[5]]+vent[lista1[4]]+unit[lista1[3]]+'mila')
            elif(lista1[4]=='8' and (lista1[5]=='1' or lista1[5]=='2' or lista1[5]=='3'or lista1[5]=='4'or lista1[5]=='5'or lista1[5]=='6'or lista1[5]=='7'or lista1[5]=='8'or lista1[5]=='9')):
                stringa+=cent[lista1[5]]+dec[lista1[4]]+unit[lista1[3]]+'mila'
            else:
                stringa+=(cento[lista1[5]]+dec[lista1[4]]+unit[lista1[3]]+'mila')
    '''@@@@@@@@@@@@@@@@@@@@@@@@@CENTINAIA@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
    if(n>0):
        string=lista1[1]+lista1[0]
        try:
            stringa+=cento[lista1[2]]+dec[lista1[1]]+unit[string]
        except KeyError:
            if(lista1[1]=='8' and (lista1[2]=='1' or lista1[2]=='2' or lista1[2]=='3'or lista1[2]=='4'or lista1[2]=='5'or lista1[2]=='6'or lista1[2]=='7'or lista1[2]=='8'or lista1[2]=='9')) and ((lista1[0]=='8' or lista1[0]=='1') and (lista1[1]=='2' or lista1[1]=='3' or lista1[1]=='4' or lista1[1]=='5' or lista1[1]=='6' or lista1[1]=='7' or lista1[1]=='8' or lista1[1]=='9')):
                stringa+=cent[lista1[2]]+vent[lista1[1]]+unit[lista1[0]]
            elif((lista1[0]=='8' or lista1[0]=='1') and (lista1[1]=='2' or lista1[1]=='3' or lista1[1]=='4' or lista1[1]=='5' or lista1[1]=='6' or lista1[1]=='7' or lista1[1]=='8' or lista1[1]=='9')):
                stringa+=cento[lista1[2]]+vent[lista1[1]]+unit[lista1[0]]
            elif(lista1[1]=='8' and (lista1[2]=='1' or lista1[2]=='2' or lista1[2]=='3'or lista1[2]=='4'or lista1[2]=='5'or lista1[2]=='6'or lista1[2]=='7'or lista1[2]=='8'or lista1[2]=='9')):
                stringa+=cent[lista1[2]]+dec[lista1[1]]+unit[lista1[0]]
            else:
                stringa+=cento[lista1[2]]+dec[lista1[1]]+unit[lista1[0]]
    return(stringa)
print(conv(981008818))
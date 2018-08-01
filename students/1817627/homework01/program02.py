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
unoanove=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
diecia19=['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
ventia99=['','dieci','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
ventanovant=['','','vent','trent','quarant','cinquant','sessant','settant','ottant','novant']
def finoacento(n):
    x=str(n)
    if n>0 and n<=9:
        return(unoanove[n])
    if n>9 and n<=19:
        return(diecia19[n-10])
    if n>19 and n<=99:
        if x[-1]=='1' or x[-1]=='8':
            return ventanovant[int(x[-2])]+unoanove[int(x[-1])]
        elif x[-1]=='0':
            return ventia99[int(x[-2])]
        else:
            return ventia99[int(x[-2])]+unoanove[int(x[-1])]

def finoamille(n):
    x=str(n)
    if n>=0 and n<=99:
        return finoacento(n)
    if n>99 and n<=199:
        if x[-1]=='0' and x[-2]=='0':
            return 'cento'
        elif x[-2]=='8':
            return('cent'+finoacento(int(x[1:])))
        else:
            return('cento'+finoacento(int(x[1:])))
    if n>199 and n<=999:
        if x[-2]=='8':
            return(unoanove[int(x[-3])]+'cent'+finoacento(int(x[1:])))
        elif x[-1]=='0' and x[-2]=='0':
            return (unoanove[int(x[-3])]+'cento')
        elif x[-1]=='0':
            return unoanove[int(x[-3])]+'cento'+finoacento(int(x[1:]))
        else:
            return unoanove[int(x[-3])]+'cento'+finoacento(int(x[1:]))
            
def seicifre(n):
    x=str(n)
    if n>=0 and n<=999:
        return finoamille(n)
    if n>999 and n<=9999:
        if n==1000:
            return 'mille'
        elif x[-4]=='1':
            return 'mille'+finoamille(int(x[1:]))
        elif x[-3]=='0' and x[-2]=='0' and x[-1]=='0':
            return unoanove[int(x[-4])]+'mila'
        else:
            return unoanove[int(x[-4])]+'mila'+finoamille(int(x[1:]))
    if n>9999 and n<=99999:
        if x[-3]=='0' and x[-2]=='0' and x[-1]=='0':
            return finoamille(int(x[:2]))+'mila'
        else:
            return finoamille(int(x[:2]))+'mila'+finoamille(int(x[2:]))
    if n>99999 and n<=999999:
        if x[-3]=='0' and x[-2]=='0' and x[-1]=='0':
            return finoamille(int(x[:3]))+'mila'
        else:
            return finoamille(int(x[:3]))+'mila'+finoamille(int(x[3:]))
    
def milioni(n):
    x=str(n)
    if n>=0 and n<=999999:
        return seicifre(n)
    if n==1000000:
        return 'unmilione'
    if n>999999 and n<=9999999:
        if x[-7]=='1':
            return 'unmilione'+seicifre(int(x[1:]))
        elif x[-1]=='0' and x[-2]=='0' and x[-3]=='0' and x[-4]=='0' and x[-5]=='0'and x[-6]=='0':
            return unoanove[int(x[-7])]+'milioni'
        else:
            return unoanove[int(x[-7])]+'milioni'+seicifre(int(x[1:]))
    if n>9999999 and n<=99999999:
        if x[-1]=='0' and x[-2]=='0' and x[-3]=='0' and x[-4]=='0' and x[-5]=='0'and x[-6]=='0':
            return seicifre(int(x[:2]))+'milioni'
        else:
            return seicifre(int(x[:2]))+'milioni'+seicifre(int(x[2:]))
    if n>99999999 and n<=999999999:
        if x[-1]=='0' and x[-2]=='0' and x[-3]=='0' and x[-4]=='0' and x[-5]=='0' and x[-6]=='0':
            return seicifre(int(x[:3]))+'milioni'
        else:
            return seicifre(int(x[:3]))+'milioni'+seicifre(int(x[3:]))
        
def miliardi(n):
    x=str(n)
    if n>=0 and n<=999999999:
        return milioni(n)
    if n==1000000000:
        return 'unmiliardo'
    if n>999999999 and n<=9999999999:
        if x[-10]=='1':
            return 'unmiliardo'+milioni(int(x[1:]))
        elif x[3:]=='000000000':
            return unoanove[int(x[-10])]+'miliardi'
        else:
            return unoanove[int(x[-10])]+'miliardi'+milioni(int(x[1:]))
    if n>9999999999 and n<=99999999999:
        if x[3:]=='000000000':
            return milioni(int(x[:2]))+'miliardi'
        else:
            return milioni(int(x[:2]))+'miliardi'+milioni(int(x[2:]))
    if n>99999999999 and n<=999999999999:
        if x[3:]=='000000000':
            return milioni(int(x[:3]))+'miliardi'
        else:
            return milioni(int(x[:3]))+'miliardi'+milioni(int(x[3:]))
        
def conv(n):
    '''converte un numero compreso tra 0 e mille miliardi in lettere'''
    if n>0 and n<1000000000000:
        return miliardi(n)

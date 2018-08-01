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
    eccezioni = {0: '',1: 'uno',2: 'due',3: 'tre',4: 'quattro',5: 'cinque',6: 'sei',7: 'sette'
                  ,8: 'otto',9: 'nove',10: 'dieci',11: 'undici',12: 'dodici',13: 'tredici',
                  14: 'quattordici',15: 'quindici',16: 'sedici',17: 'diciassette',
                  18: 'diciotto',19: 'diciannove',100: 'cento',1000: 'mille'}
    tens = {20: 'venti',30: 'trenta',40: 'quaranta',50: 'cinquanta',
            60: 'sessanta',70: 'settanta',80: 'ottanta',90: 'novanta'}
    lista = [int(i) for i in str(n)]
    s = ''
    lista.reverse()
    x = len(lista)-1
    while x>=0:
        lista[x] = lista[x]*10**(x)
        x = x-1
    lista.reverse()
    i=0
    while i<len(lista):
        
        if lista[i] in range(1,20):
            if lista[i] == 10:
                lista[i] += lista[i+1]
                del lista[i+1]
            elif len(lista)>=2 and (lista[i]==1 or lista[i]==8):
                if lista[i-1]!=0:
                    s = s[:-1]
            s += eccezioni[lista[i]]
            
        if lista[i] in range(20,100):
            if len(lista)>=3 and lista[i]==80:
                if lista[i-1]!=0:
                    s = s[:-1]
            s += tens[lista[i]]
            
        if lista[i] in range(100,1000):
            if lista[i] == 100:
                s += eccezioni[lista[i]]
            else:
                b = lista[i]/100
                s += eccezioni[b]+'cento'
                
        if lista[i] in range(1000,10000):
            if lista[i] == 1000 and len(lista)==4:
                s += eccezioni[lista[i]]
            else:
                b = lista[i]/1000
                if (b == 1 or b == 8) and lista[i-1]!=0:
                    s = s[:-1]
                s += eccezioni[b]+'mila'
                
        if lista[i] in range(10000,100000):
            if lista[i] == 10000:
                lista[i] += lista[i+1]
                del lista[i+1]
                b = lista[i]/1000
                s += eccezioni[b]+'mila'
            else:
                b = lista[i]/1000
                if len(lista)>=6 and b==80:
                    if lista[i-1]!=0:
                        s = s[:-1]
                s += tens[b]
                if lista[i+1]==0:
                    s +='mila'
                
        if lista[i] in range(100000,1000000):
            if lista[i] == 100000:
                b = lista[i]/1000
                s += eccezioni[b]
                if lista[i+1]==0 and lista[i+2]==0:
                    s +='mila'
            else:
                b = lista[i]/100000
                s += eccezioni[b]+'cento'
                if lista[i+1]==0 and lista[i+2]==0:
                    s +='mila'
                
        if lista[i] in range(1000000,20000000):
            if lista[i] == 1000000 and len(lista)==7:
                b = lista[i]/1000000
                s += eccezioni[b][:-1]+'milione'
            else:
                if lista[i] == 10000000:
                    lista[i] += lista[i+1]
                    del lista[i+1]
                b = lista[i]/1000000
                if (b == 1 or b == 8) and lista[i-1]!=0:
                    s = s[:-1]
                s += eccezioni[b]+'milioni'
                
        if lista[i] in range(20000000,100000000):
            b = lista[i]/1000000
            if len(lista)>=9 and b==80:
                    if lista[i-1]!=0:
                        s = s[:-1]
            s += tens[b]
            if lista[i+1]==0:
                    s +='milioni'
            
        if lista[i] in range(100000000,1000000000):
            if lista[i] == 100000000:
                b = lista[i]/1000000
                s += eccezioni[b]
                if lista[i+1]==0 and lista[i+2]==0:
                    s +='milioni'
            else:
                b = lista[i]/100000000
                s += eccezioni[b]+'cento'
                if lista[i+1]==0 and lista[i+2]==0:
                    s +='milioni'
                
        if lista[i] in range(1000000000,20000000000):
            if lista[i] == 1000000000 and len(lista)==10:
                b = lista[i]/1000000000
                s += eccezioni[b][:-1]+'miliardo'
                
            else:
                if lista[i] == 10000000000:
                    lista[i] += lista[i+1]
                    del lista[i+1]
                b = lista[i]/1000000000
                if (b == 1 or b == 8) and lista[i-1]!=0:
                    s =s[:-1]
                s += eccezioni[b]+'miliardi'
                
        if lista[i] in range(20000000000,100000000000):
            b = lista[i]/1000000000
            if len(lista)>=12 and b==80:
                    if lista[i-1]!=0:
                        s = s[:-1]
            s += tens[b]
            if lista[i+1]==0:
                    s +='miliardi'
            
        if lista[i] in range(100000000000,1000000000000):
            if lista[i] == 100000000000:
                b = lista[i]/1000000000
                s += eccezioni[b]
                if lista[i+1]==0 and lista[i+2]==0:
                    s +='miliardi'
            else:
                b = lista[i]/100000000000
                s += eccezioni[b]+'cento'
                if lista[i+1]==0 and lista[i+2]==0:
                    s +='miliardi'
        
        i +=1
    return s

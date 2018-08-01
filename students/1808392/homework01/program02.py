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


def conv(n):
    cifra = str(n) # converto in stringa 
    if len(cifra) <= 3:
        Ris = leggiNum(Valid(n),'1')
    elif len(cifra) <= 6:
        Ris = leggiNum(Valid(int(cifra[:-3])),'2')
        Ris += leggiNum(Valid(int(cifra[len(cifra)-3:])),'1')
    elif len(cifra) <= 9:
        Ris = leggiNum(Valid(int(cifra[:-6])),'3')
        Ris += leggiNum(Valid(int(cifra[len(cifra)-6:-3])),'2')
        Ris += leggiNum(Valid(int(cifra[len(cifra)-3:])),'1')
    elif len(cifra) <= 12:
        Ris = leggiNum(Valid(int(cifra[:-9])),'4')
        Ris += leggiNum(Valid(int(cifra[len(cifra)-9:-6])),'3')
        Ris += leggiNum(Valid(int(cifra[len(cifra)-6:-3])),'2')
        Ris += leggiNum(Valid(int(cifra[len(cifra)-3:])),'1')
   
    return Ris
    
def leggiNum(n,tipo):
    # questa funzione mi serve a trasformare il numero considerando 3 cifre
    
    # fino 19 li salvo, perchè non seguono alcuna regola
 
    tras= {}
    suffisso = {}
    tras[0] = ''
    tras[1] = 'uno'
    tras[2] = 'due'
    tras[3] = 'tre'
    tras[4] = 'quattro'
    tras[5] = 'cinque'
    tras[6] = 'sei'
    tras[7] = 'sette'
    tras[8] = 'otto'
    tras[9] = 'nove'
    tras[10] = 'dieci'
    tras[11] = 'undici'
    tras[12] = 'dodici'
    tras[13] = 'tredici'
    tras[14] = 'quattordici'
    tras[15] = 'quindici'
    tras[16] = 'sedici'
    tras[17] = 'diciassette'
    tras[18] = 'diciotto'
    tras[19] = 'diciannove'
    
    # salvo le decine
    tras[20] = 'venti'
    tras[30] = 'trenta'
    tras[40] = 'quaranta'
    tras[50] = 'cinquanta'
    tras[60] = 'sessanta'
    tras[70] = 'settanta'
    tras[80] = 'ottanta'
    tras[90] = 'novanta'
    
    # salvo centinaia e migliaia
    tras[100] = 'cento'
    tras[1000] = 'mille'
    
    #aggiungo suffisso
    suffisso[1] = ''
    suffisso[2] = 'mila'
    suffisso[3]= 'milioni'
    suffisso[4]= 'miliardi'
    
    #compongo il numero 
    cifra = n
    n = int(n)
    res = ''
    
    countx = 0
    if tipo == '2' and n == 1:
        return tras[1000]
    
    if (n <= 20 or n==100) or (cifra[-1] == "0" and len(cifra) == 2):
        res = tras[n]
    else:
        for l in cifra: 
            countx +=1
            if len(cifra) == 3 and  countx == 1:  
                if l != '1':
                    res = res + tras[int(l)] + tras[100]
                else:
                        res = res + tras[100]
         
            elif (countx == 1 and len(cifra)==2) or (countx==2 and len(cifra)==3):
                if (len(cifra) == 3 and int(cifra[1:3]) <= 20):
                    res += tras[int(cifra[1:3])]
                    return res + suffisso[int(tipo)]
                elif l in ('1','8'):
                    res = res[:-1] +  tras[int(l + '0')]
                else:
                    res += tras[int(l + '0')]
            elif (len(cifra)==3 and countx >2) or (countx > 1 and len(cifra) == 2):
                    if l in ('1','8') :
                        res = res[:-1] + tras[int(l)] 
                    else:
                        res = res + tras[int(l)] 
      
    res += suffisso[int(tipo)]
        
    return res

def Valid(n):
    # elimino 0 non significativi
    cifra=str(n)
    num=n
    countx = 0
    for l in cifra:
        countx += 1
        if l == '0':
            num = cifra[countx:]
        else:
            return str(num)
        
    if num == '':
        return '0'
    else:
        return str(num)

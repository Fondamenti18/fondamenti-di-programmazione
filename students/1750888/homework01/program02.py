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
    diz1_9={'0':"",'1':'uno','2':'due','3':'tre','4':'quattro','5':'cinque','6':'sei','7':'sette','8':'otto','9':'nove'}            
    diz10_19={'00':"",'10':'dieci','11':'undici','12':'dodici','13':'tredici','14':'quattordici','15':'quindici','16':'sedici','17':'diciassette','18':'diciotto','19':'diciannove'}
    diz20_90={'00':"",'20':'venti','30':'trenta','40':'quaranta','50':'cinquanta','60':'sessanta','70':'settanta','80':'ottanta','90':'novanta'}
    diz100_900={'000':'','100':'cento','200':'duecento','300':'trecento','400':'quattrocento','500':'cinquecento','600':'seicento','700':'settecento','800':'ottocento','900':'novecento'}
    
        
            
        
    numero = str(n)
    lista = []
    while len(numero) >= 3:
        s = numero[-3:]
        lista.append(s)
        numero = numero[:-3]
    if len(numero)!=0:
        lista.append(numero)
            
    lista_lettere = []
    for el in lista:
        temporaneo1 = ""
        temporaneo2 = ""
        temporaneo3 = ""
        if len(el) == 3:
            centinaia3=el[0]+"00"
            temporaneo1= diz100_900.get(centinaia3)
            if el[1] != "1":
                decina3=el[1]+"0"
                temporaneo2=diz20_90.get(decina3)
                unita3=el[2]
                temporaneo3=diz1_9.get(unita3)
                if el[2]=="1" or el[2]=="8":
                    temporaneo2=temporaneo2[:-1]
            else:
                decina3= el[1]+el[2]
                temporaneo2 = diz10_19.get(decina3)
            if el[1]=="8":
                temporaneo1=temporaneo1[:-1]
        elif len(el) == 2:
            if el[0] != "1":
                decina2 = el[0]+"0"
                temporaneo2 = diz20_90.get(decina2)
                unita2 = el[1]
                temporaneo3=diz1_9.get(unita2)
                if el[1]=="1" or el[1]=="8":
                    temporaneo2=temporaneo2[:-1]
            else:
                decina2 = el[0]+el[1]
                temporaneo2 = diz10_19.get(decina2)
        else:
            temporaneo3 = diz1_9.get(el[0])
        
        numero = temporaneo1+temporaneo2+temporaneo3
        lista_lettere.append(numero)
    
    lista_definitiva = []
    index = len(lista_lettere)-1
    for i in range(len(lista_lettere)):
        lista_definitiva.append(lista_lettere[index])
        index -= 1
    
    numero_finale = ''
    
    if len(lista_definitiva) == 1:
        numero_finale = lista_definitiva[0]
    else:
        if len(lista_definitiva) == 2:
            numero_finale = mille(lista_definitiva[0]) + lista_definitiva[1]
        elif len(lista_definitiva) == 3:
            numero_finale = milioni(lista_definitiva[0])+mille(lista_definitiva[1])+lista_definitiva[2]
        else:
            numero_finale = miliardi(lista_definitiva[0])+milioni(lista_definitiva[1])+mille(lista_definitiva[2])+lista_definitiva[3]
            
    return numero_finale        
    
                    
                    
def mille(s):
    if s == "uno":
        return "mille"
    else:
        return s+"mila"

def milioni(s):
    if s == "uno":
        return "unmilione"
    else:
        return s+"milioni"
        
def miliardi(s):
    if s == "uno":
        return "unmiliardo"
    else:
        return s+"miliardi"


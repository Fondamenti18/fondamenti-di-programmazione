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
    risultato = ''
    indice = 1
    peso = ['','mila','milioni','miliardi','milamiliardi'] #ricordarsi i casi del singolare
    m = n
    
    if m == 0:
        risultato = 'zero'    
    else:
        while (m > 0):
            tripletta = m % 1000
            terzina=traduci(tripletta,m,indice)
            if terzina in ['','uno','mille','unmilione','unmiliardo','unmilamiliardo']:
            
                    risultato=terzina+risultato
            else:
                 risultato=terzina  + peso[indice-1 ] + risultato
            indice = indice + 1         
            m = m // 1000
    return risultato
            
def traduci(t,m,indice):
    risultato = cento(t) # centinaia
   
    if (t==0): return ''
    elif (t==1)  and (indice==1) and (risultato==''):  #  PROVA
        return 'uno'
    elif (t==1)  and (indice==2) and (risultato==''):
        return 'mille'
    elif (t==1)  and(indice==2)and (risultato==''):
        return 'unmilione'
    elif (t==1)  and(indice==4)and(risultato==''):
        return'unmiliardo'
    elif (t==1)  and(indice==5)and (risultato==''):
        return 'unmilamiliardo'
    else:
         t = t % 100
         risultato = troncadecine(risultato, t) + decine(t) # decine con eccezioni 
         if (t < 10) or (t > 19):
             if (t // 10) > 0: # ci sono decine
                 t = t % 10
                 risultato = troncaunita(risultato, t) + unita(t) # unita   
        
             else:  #niente decine
                  risultato = risultato + unita(t) # unita
    return risultato    
            
def cento(t):
    centinaiaList = ['', 'due', 'tre','quattro','cinque','sei','sette','otto','nove']
    risultato = ''
    if t >= 100: # centinaia
        centinaia = t // 100
        risultato = centinaiaList[centinaia - 1] + 'cento'
    return risultato
    
def decine(t):
    risultato = ''
    decinaList = ['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    secondistrani = ['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    if (t > 9) and (t < 20): # eccezioni da 10 a 19   
        risultato = secondistrani[t-10]  
    elif t >= 20: #decine da 20 in poi
        decina = t // 10
        risultato = decinaList[decina - 2]
    return risultato

def unita(t): #prova   
    unitaList = ['','uno','due','tre','quattro','cinque','sei','sette','otto','nove']
    
    return unitaList[t]
    
def troncadecine(s, t):  #risolve problema dei numeri tra centoottanta e centoottantanove
    if ((t >= 80) and (t < 90)) and (s != ''):
        s = s[:len(s) - 1]
    return s
            
def troncaunita(s, t):
    if ((t == 1) or (t == 8)) and (s != ''):
        s = s[:len(s) - 1]
    return s







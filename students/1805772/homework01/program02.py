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


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000000000000 (999 miliardi), 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def conv(n):
    
    copia = n   #modificando uno non modifico l'altro
    parola = ''
        
    ventina = ('uno' , 'due' , 'tre' , 'quattro' , 'cinque' , 'sei' , 'sette' , 'otto' , 'nove' , 'dieci' , 'undici' , 'dodici' , 'tredici' , 'quattordici' , 'quindici' , 'sedici' , 'diciassette' , 'diciotto' , 'diciannove' )
    decine = ('vent' , 'trent' , 'quarant' , 'cinquant' , 'sessant' , 'settant' , 'ottant' , 'novant')
    centinaia = ('cento' , 'duecento' , 'trecento' , 'quattorcento' , 'cinquecento' , 'seicento' , 'settecento' , 'ottocento' , 'novecento')
    bandieraVenti = False
    bandieraDecine = False
    bandieraMigliaia = False

    if copia >= 1000 and copia <= 1999:
        parola = parola + 'mille'
        copia = copia - 1000
        bandieraMigliaia == True
    elif copia >= 2000 and copia <= 19999:
        bandieraMigliaia == True
        for x in range(2 , 19):
            if copia >= (x * 1000) and copia <= ((x * 1000) + 999):
                parola = parola + ventina[x-1] + 'mila'
                break
        copia = copia - (x * 1000)    
        
    if copia >= 100 and copia <= 999:
        i = 0
        while i <  9:
            if copia >= ((i+1) * 100) and copia <= ((i+1) * 100 + 99):
                parola = parola + centinaia[i]
                break
            i = i + 1
        copia = copia - ((i+1) * 100)    #l'incremento alla riga precedente fallisce con break
    
        
    if copia >= 80 and copia < 90 and (parola == '' or bandieraMigliaia == True):
        parola = parola + 'ottant'
        copia = copia - 80
        bandieraDecine = True
    elif copia >= 80 and copia < 90 and parola != '':
        parola = parola + 'ttant'
        copia = copia - 80
        bandieraDecine = True
    elif copia >= 20 and copia <= 99:
        bandieraDecine == True
        i = 0
        while i <=  8:
            if copia >= ((i+2) * 10) and copia <= ((i+2) * 10 + 9):
                parola = parola + decine[i]
                break
            i = i + 1
        copia = copia - ((i+2) * 10)
        if i == 0:
            bandieraVenti = True

        
    if copia != 0:
        if (copia == 8 or copia == 1) or (copia == 8 or copia == 1 and bandieraDecine == True):
            parola = parola + ventina[copia-1]
        elif bandieraVenti == True:
            parola = parola + 'i' + ventina[copia-1]
        elif bandieraDecine == True:
            parola = parola + 'a' + ventina[copia-1]
        else:
            parola = parola + ventina[copia-1]      
    elif copia == 0:
        if bandieraVenti == True:
            parola = parola + 'i'
        elif bandieraDecine == True:
            parola = parola + 'a'
            
    return(parola)


if __name__ == '__main__':
    conv(12358)

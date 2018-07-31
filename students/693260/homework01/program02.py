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
    NumeroInStringa = str(n)

    ValoreConvertito = ""
    
    if n in StringheNumeriche:
        return StringheNumeriche[n]
    
    StringaInBlocchiDaTre = []
    
    indice1 = len(NumeroInStringa)
    
    indice2 = indice1 - 3
    
    if indice2 < 0:
            
        indice2 = 0
    
    Risultato = NumeroInStringa[indice2:indice1+1]
    
    while Risultato != "":
        
        Risultato = "0" * (3 - len(Risultato)) + Risultato
        
        StringaInBlocchiDaTre.append(Risultato)
        
        indice1 = indice2
        
        indice2 = indice1 - 3
        
        if indice2 < 0:
            
            indice2 = 0
    
        Risultato = NumeroInStringa[indice2:indice1]
        
# Inversione dell'ordine dei Blocchi
        
    StringaInBlocchiDaTreNonInvertiti = StringaInBlocchiDaTre[:]
        
    StringaInBlocchiDaTre = []
        
    IndiceBlocchi = len(StringaInBlocchiDaTreNonInvertiti)
        
    while IndiceBlocchi > 0:
            
        StringaInBlocchiDaTre.append(StringaInBlocchiDaTreNonInvertiti[IndiceBlocchi - 1])
            
        IndiceBlocchi -= 1
            
# Analisi dei blocchi
    
    NumeroBlocchi = len(StringaInBlocchiDaTre)
    
    IndiceNumeroBlocco = -1
    
    ValoreConvertito = ""
 
    for StringaSottoBloccoDaTre in StringaInBlocchiDaTre:
        
        IndiceNumeroBlocco += 1

        ValoreConvertito = ValoreConvertito + str(CalcolaCentinaia(int(StringaSottoBloccoDaTre)))
        
        if StringaSottoBloccoDaTre != "000":
            
            CodiceSuffisso = int(str(IndiceNumeroBlocco) + str(NumeroBlocchi)) 
        
            if CodiceSuffisso in SuffissiNumerici:
            
                ValoreConvertito = ValoreConvertito + SuffissiNumerici[CodiceSuffisso]
                
                # Rettifica 'veloce' dei casi 1000, 100000, 1000000, 1000000000
                
                if n < 10000:
                    
                    ValoreConvertito = ValoreConvertito.replace( "unomila", "mille")
                
                if n < 1000000:
                    
                    ValoreConvertito = ValoreConvertito.replace( "unomilioni", "unmilione")
                  
                if n < 1000000000:
                    
                    ValoreConvertito = ValoreConvertito.replace( "unomiliardi", "unmiliardo")
                
    return ValoreConvertito

def CalcolaDecine(n):
    
    ValoreRestituito = ""
    
    if n == 0:
        
        return ValoreRestituito
    
    if n in StringheNumeriche:
    
        return StringheNumeriche[n]
      
    Unita = int(n - ((n // 10) * 10))
    
    Decine = int(n - Unita)
    
    ValoreRestituito = StringheNumeriche[Decine]
    
    if Unita == 1 or Unita == 8:
        
        ValoreRestituito = ValoreRestituito[:-1]
        
    ValoreRestituito = ValoreRestituito + StringheNumeriche[Unita]
    
    return ValoreRestituito

def CalcolaCentinaia(n):
    
    ValoreRestituito = ""
    
    if n == 0:
        
        return ValoreRestituito
 
    if n in StringheNumeriche:
    
        ValoreRestituito = StringheNumeriche[n]   
        
    else:

        Decine = n - ((n // 100) * 100)
    
        Centinaia = int(n - Decine)
        
        if Centinaia != 0:
        
            if Centinaia in StringheNumeriche:
        
                ValoreRestituito = StringheNumeriche[Centinaia] 
        
            else:    
        
                Centinaia = int(Centinaia / 100)
            
                ValoreRestituito = ValoreRestituito + StringheNumeriche[Centinaia] + "cento"



    
        if Decine != 0:
        
            if Decine > 79 and Decine < 90:
            
                ValoreRestituito = ValoreRestituito[:-1] + CalcolaDecine(Decine)
        
            else:
            
                ValoreRestituito = ValoreRestituito + CalcolaDecine(Decine)

    return ValoreRestituito

StringheNumeriche = {0 : "zero", 
         1 : "uno", 
         2 : "due", 
         3 : "tre", 
         4 : "quattro", 
         5 : "cinque", 
         6 : "sei", 
         7 : "sette", 
         8 : "otto", 
         9 : "nove", 
         10 : "dieci", 
         11 : "undici", 
         12 : "dodici", 
         13 : "tredici", 
         14 : "quattordici", 
         15 : "quindici", 
         16 : "sedici", 
         17 : "diciassette", 
         18 : "diciotto", 
         19 : "diciannove",
         20 : "venti",
         30 : "trenta",
         40 : "quaranta",
         50 : "cinquanta",
         60 : "sessanta",
         70 : "settanta",
         80 : "ottanta",
         90 : "novanta",
         100 : "cento",
         1000 : "mille",
         1000000 : "unmilione",
         1000000000 : "ummiliardo"
         }    
    
SuffissiNumerici = {2 : "mila", 
         3 : "milioni", 
         13 : "mila",
         4 : "miliardi", 
         14 : "milioni", 
         24 : "mila", 
         5 : "mila", 
         15 : "miliardi", 
         25 : "milioni", 
         35 : "mila"
         }



#print("--------")
#print(conv(123))

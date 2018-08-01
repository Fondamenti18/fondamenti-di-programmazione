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


# Funzione citerativa che scrive in lettere in mio numero
def conv(n):
    
    # mi assicuro che non ci siano zeri iniziali!
    numero=int(n)
    
    # caso semplice: verifico se numero a una cifre da [0-19]
    if numero <= 19:
        return dict_base[numero]

    # verifico se numero a due cifre e inferiore a 99
    elif numero >= 20 and numero <= 99:
        lettera = dict_base[(numero // 10) * 10]
        # ricavo il resto
        resto = numero % 10
        
        #gestisco l'elusione per 1 o 8
        if resto == 1 or resto == 8:
            lettera = lettera[:-1]
        return lettera + dict_base[resto]
         
    # verifico se numero a tre cifre e inferiore/uguale a 999
    elif numero >= 100 and numero <= 999:
        return calcola_lettere(numero, 100)  
    
    # verifico se numero inferiore/uguale a 999999
    elif numero >= 1000 and numero <= 999999:
        return calcola_lettere(numero, 1000)    

    # Tratto i milioni
    # verifico se numero inferiore/uguale a 999999999
    elif numero >= 1000000 and numero <= 999999999: 
        return calcola_lettere(numero, 1000000)    

    # Tratto i miliardi
    # verifico se numero inferiore/uguale a 999999999999
    elif numero >= 1000000000 and numero <= 999999999999: 
        return calcola_lettere(numero, 1000000000)    

# funziione che genera le lettere per i numeri > 99
def calcola_lettere(numero, divisore):
        lettere = conv(numero // divisore)
        
        if lettere == "uno":
            lettere = dict_base[divisore]
        else:
            lettere += dict_ext[divisore]
        # calcolo il resto     
        resto = numero % divisore
        #gestisco le elusioni
        if divisore == 100: #gestisco elusione per le centinaia
            if (resto // 10) == 8:
                lettere = lettere[:-1]
        return lettere + conv(resto)
   

"""
Definisco il mio dizionario di supporto
"""
dict_base={0:"", 1:"uno", 2:"due", 3:"tre", 4:"quattro", 5:"cinque",
           6:"sei", 7:"sette", 8:"otto", 9:"nove", 10:"dieci", 
           11:"undici", 12:"dodici", 13:"tredici", 14:"quattordici", 
           15:"quindici", 16:"sedici", 17:"diciassette", 18:"diciotto", 
           19:"diciannove", 20:"venti", 30:"trenta", 40:"quaranta",
           50:"cinquanta", 60:"sessanta", 70:"settanta", 80:"ottanta", 
           90:"novanta", 100:"cento", 1000: "mille", 1000000:"unmilione", 1000000000:"unmiliardo"}

dict_ext = {100:"cento", 1000:"mila", 1000000:"milioni", 1000000000:"miliardi"}

if __name__ == '__main__':
    print(conv(9981001818))
    print(conv(128))
 

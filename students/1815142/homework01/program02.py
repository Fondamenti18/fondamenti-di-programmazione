


'''
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
    primi_numeri=("", "due", "tre", "quattro", "cinque", 
                "sei", "sette", "otto", "nove")
    primi_9_numeri=("","uno", "due", "tre", "quattro", "cinque","sei", "sette", "otto", "nove")
    prima_decina=("dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove")
    decine=("venti", "trenta", "quaranta",
                  "cinquanta", "sessanta", 
                  "settanta", "ottanta", "novanta")
    nil=""
    nil1=""
    nil2=""
    nil3=""
    if n <= 19:
        return ("uno", "due", "tre", "quattro", "cinque", 
                "sei", "sette", "otto", "nove", "dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove")[n-1]
    if n>999999999:
        testo=""
        a=n//1000000000
        b=str(a)
        if len(b)<3:
            l=3-len(b)
            b='0'*l+b
        if b[0]!='0':
            if b[1]=='8':
                nil3=primi_numeri[int(b[0])-1]+"cent"
            else:
                nil3=primi_numeri[int(b[0])-1]+"cento"
        if b[1]!='0':
            if b[1]=='1':
                nil3+=prima_decina[int(b[2])]
            else:
                testo=decine[int(b[1])-2]
                if b[2]=='1' or b[2]=='8':
                    testo=testo[:-1]
            nil3=nil3+testo
        if b[1]=='1':
            nil3=nil3+"miliardi"
        else:
            nil3=nil3+primi_9_numeri[int(b[2])]+"miliardi"
        if b[0]=='0' and b[1]=='0' and b[2]=='1':
            nil3="unmiliardo"
        n=n-(a*1000000000)

    if n>999999:
        testo=""
        a=n//1000000
        b=str(a)
        if len(b)<3:
            l=3-len(b)
            b='0'*l+b
        if b[0]!='0':
            if b[1]=='8':
                nil=primi_numeri[int(b[0])-1]+"cent"
            else:
                nil=primi_numeri[int(b[0])-1]+"cento"
        if b[1]!='0':
            if b[1]=='1':
                testo=prima_decina[int(b[2])]
            else:
                testo=decine[int(b[1])-2]
                if b[2]=='1' or b[2]=='8':
                    testo=testo[:-1]
            nil=nil+testo
        if b[1]=='1':
            nil=nil+"milioni"
        else:
            nil=nil+primi_9_numeri[int(b[2])]+"milioni"
        if b[0]=='0' and b[1]=='0' and b[2]=='1':
            nil="unmilione"
        n=n-(a*1000000)

    if n>999:
        testo=""
        a=n//1000
        b=str(a)
        if len(b)<3:
            l=3-len(b)
            b='0'*l+b
        if b[0]!='0':
            if b[1]=='8':
                nil1=primi_numeri[int(b[0])-1]+"cent"
            else:
                nil1=primi_numeri[int(b[0])-1]+"cento"
        if b[1]!='0':
            if b[1]=='1':
                testo=prima_decina[int(b[2])]
            else:
                testo=decine[int(b[1])-2]
                if b[2]=='1' or b[2]=='8':
                    testo=testo[:-1]
            nil1=nil1+testo
        if b[1]=='1':
            nil1=nil1+"mila"
        else:
            nil1=nil1+primi_9_numeri[int(b[2])]+"mila"
        if b[0]=='0' and b[1]=='0' and b[2]=='1':
            nil1="mille"
        n=n-(a*1000)

    if n>19:
        testo=""
        a=n
        b=str(a)
        if len(b)<3:
            l=3-len(b)
            b='0'*l+b
        if b[0]!='0':
            if b[1]=='8':
                nil2=primi_numeri[int(b[0])-1]+"cent"
            else:
                nil2=primi_numeri[int(b[0])-1]+"cento"
        if b[1]!='0':
            if b[1]=='1':
                testo=prima_decina[int(b[2])]
            else:
                testo=decine[int(b[1])-2]
                if b[2]=='1' or b[2]=='8':
                    testo=testo[:-1]
        if b[1]!='1':
            nil2=nil2+testo+primi_9_numeri[int(b[2])]
        else:
            nil2=nil2+testo

    numero=nil3+nil+nil1+nil2

    if  10 <= n <= 19:
        numero+=("uno", "due", "tre", "quattro", "cinque", 
                "sei", "sette", "otto", "nove", "dieci", 
                "undici", "dodici", "tredici", 
                "quattordici", "quindici", "sedici", 
                "diciassette", "diciotto", "diciannove")[n-1]

    

    return(numero)            
            
            
        

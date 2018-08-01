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
    numeriunita={"0":"", "1":"uno", "2":"due", "3":"tre", "4":"quattro", "5":"cinque", "6":"sei", "7":"sette", "8":"otto", "9":"nove"}
    numeridecine={"10":"dieci", "11":"undici", "12":"dodici", "13":"tredici","14":"quattordici", "15":"quindici", "16":"sedici", 
                  "17":"diciassette", "18":"diciotto", "19":"diciannove", "2":"venti", "3":"trenta", "4":"quaranta", 
                  "5":"cinquanta", "6":"sessanta", "7":"settanta", "8":"ottanta", "9":"novanta"}
    numericongiunzioni={0:"", 3:"mila", 6:"milioni", 9:"miliardi", "mila":"mille", "milioni": "unmilione", "miliardi":"unmiliardo"}
    numero=str(n)
    numero=numero.zfill(12)
    lunghezza=len(numero)
    stringanum=""
    pinizio=0
    pfine=3
    for a in range(0,4):
        substringa=numero[pinizio:pfine]
        if substringa=="000":
            pinizio=pinizio+3
            pfine=pfine+3
            lunghezza=lunghezza-3
            continue
        for b in range(0,3):
            lettera=substringa[b]
            if b==0:  
                if lettera!="0" and lettera!="1":
                    stringanum=stringanum+numeriunita.get(lettera)+ "cento"
                elif lettera=="1":
                    stringanum=stringanum+"cento"
                else:
                    continue
            if b==1 and lettera=="1": 
                lettera=substringa[b:]
                stringanum=stringanum+numeridecine.get(lettera)
                break
            if b==1 and lettera !="1" and lettera!="0": 
                if substringa[2]=="1" or substringa[2]=="8":
                    appoggio=numeridecine.get(lettera)
                    stringanum=stringanum+appoggio[:-1]
                elif lettera=="8" :
                    stringanum=stringanum+"ttanta"
                elif substringa[2]=="1" or substringa[2]=="8" and lettera=="8":
                    stringanum=stringanum+"ttant"
                elif lettera=="0":
                    continue
                else:
                    stringanum=stringanum+ numeridecine.get(lettera)
            if b==2:
                stringanum=stringanum+numeriunita.get(lettera)
        lunghezza=lunghezza-3
        pinizio=pinizio+3
        pfine=pfine+3
        if stringanum=="uno":
            poggino=numericongiunzioni.get(lunghezza)
            stringanum=numericongiunzioni.get(poggino)
        else:
            stringanum=stringanum+numericongiunzioni.get(lunghezza)
        a=a+1
    return(stringanum)
                
            
        
        


    
    
    
    
    
    

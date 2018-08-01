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
        num={"0":"","1":"uno","2":"due","3":"tre","4":"quattro","5":"cinque","6":"sei","7":"sette","8":"otto","9":"nove","10":"dieci","11":"undici","12":"dodici","13":"tredici","14":"quattordici","15":"quindici","16":"sedici","17":"diciassette","18":"diciotto","19":"dicianove"}
        decine=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
        ordini=['cento','mila','milioni','miliardi']
        nString=str(n)

        if n<20:
                return num[nString]


        if len(nString)==2:
                index=n//10-2
                if nString[1]=='1' or nString[1]=='8':
                    return decine[index][0:-1]+num[nString[1]]
                    
                else:
                    return decine[index]+num[nString[1]]

        if len(nString)==3:
                ordine=ordini[0]
                restoNum=conv(int(nString[1:]))
                if nString[0]=='1':
                    if restoNum!='' and restoNum[0:4]=='otta':
                        return ordine[:-1]+restoNum
                    else:
                        return ordine+restoNum
                else:
                    if restoNum!='' and restoNum[0:4]=='otta':
                        return num[nString[0]]+ordine[:-1]+restoNum
                    else:
                        return num[nString[0]]+ordine+restoNum


        if 3<len(nString)<=6:
                numMila=conv(int(nString[:len(nString)-3]))
                restoNum=conv(int(nString[len(nString)-3:]))
                if nString[0]=='1' and len(nString)==4:
                    return 'mille'+restoNum
                else:
                    return numMila+ordini[1]+restoNum


        if 6<len(nString)<=9:
                numMilioni=conv(int(nString[:len(nString)-6]))
                restoNum=conv(int(nString[len(nString)-6:]))
                if nString[0]=='1' and len(nString)==7:
                    return 'unmilione'+restoNum
                else:
                    return numMilioni+ordini[2]+restoNum

        if 9<len(nString)<=12:
                numMiliardi=conv(int(nString[:len(nString)-9]))
                restoNum=conv(int(nString[len(nString)-9:]))
                if nString[0]=='1' and len(nString)==10:
                    return 'unmiliardo'+restoNum
                else:
                    return numMiliardi+ordini[3]+restoNum
                
                                    
                        
                

                        
                                
                



































































































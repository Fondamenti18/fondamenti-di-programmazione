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
    numero=str(n)
    stringa=""
    unitaDecine=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    decine=['venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    centinaia=['cento','duecento','trecento','quatrocento','cinquecento','seicento','ottocento','novecento',]
    migliaia=['mille','duemila','tremila','quattromila','cinquemila','seimila','ottomila','novemila']
    
    i=0
    f=len(numero)
    
    if(numero[i:f]=='0'):
        stringa=stringa+'zero'
        i+=1
        
    
    while(i<f):

        if(int(numero[i:f])<20):
            if(numero[i:f]=='1'):
                stringa+=unitaDecine[1]
            elif(numero[i:f]=='2'):
                stringa+=unitaDecine[2]
            elif(numero[i:f]=='3'):
                stringa+=unitaDecine[3]
            elif(numero[i:f]=='4'):
                stringa+=unitaDecine[4]
            elif(numero[i:f]=='5'):
                stringa+=unitaDecine[5]
            elif(numero[i:f]=='6'):
                stringa+=unitaDecine[6]
            elif(numero[i:f]=='7'):
                stringa+=unitaDecine[7]
            elif(numero[i:f]=='8'):
                stringa+=unitaDecine[8]
            elif(numero[i:f]=='9'):
                stringa+=unitaDecine[9]
            elif(numero[i:f]=='10'):
                stringa+=unitaDecine[10]
                i+=1
            elif(numero[i:f]=='11'):
                stringa+=unitaDecine[11]
                i+=1
            elif(numero[i:f]=='12'):
                stringa+=unitaDecine[12]
                i+=1
            elif(numero[i:f]=='13'):
                stringa+=unitaDecine[13]
                i+=1
            elif(numero[i:f]=='14'):
                stringa+=unitaDecine[14]
                i+=1
            elif(numero[i:f]=='15'):
                stringa+=unitaDecine[15]
                i+=1
            elif(numero[i:f]=='16'):
                stringa+=unitaDecine[16]
                i+=1
            elif(numero[i:f]=='17'):
                stringa+=unitaDecine[17]
                i+=1
            elif(numero[i:f]=='18'):
                stringa+=unitaDecine[18]
                i+=1
            elif(numero[i:f]=='19'):
                stringa+=unitaDecine[19]
                i+=1
            
            i += 1
        
        elif(int(numero[i:f])<100):
            if(numero[i+1:f]=='1'):
                if(numero[i:f]=='21'):
                    stringa+='vent'
                elif(numero[i:f]=='31'):
                    stringa+='trent'
                elif(numero[i:f]=='41'):
                    stringa+='quarant'
                elif(numero[i:f]=='51'):
                    stringa+='cinquant'
                elif(numero[i:f]=='61'):
                    stringa+='sessant'
                elif(numero[i:f]=='71'):
                    stringa+='settant'
                elif(numero[i:f]=='81'):
                    if(numero[i-1:f-1]=='28'):
                        stringa+='ttant'
                    elif(numero[i-1:f-1]=='38'):
                        stringa+='ttant'
                    elif(numero[i-1:f-1]=='48'):
                        stringa+='ttant'
                    elif(numero[i-1:f-1]=='58'):
                        stringa+='ttant'
                    elif(numero[i-1:f-1]=='68'):
                        stringa+='ttant'
                    elif(numero[i-1:f-1]=='78'):
                        stringa+='ttant'
                    elif(numero[i-1:f-1]=='88'):
                        stringa+='ttant'
                    elif(numero[i-1:f-1]=='98'):
                        stringa+='ttant'
                elif(numero[i:f]=='91'):
                    stringa+='novant'
            else:
                if(numero[i:f-1]=='2'):
                    if(numero[i:f]=='28'):
                        stringa+='vent'
                    else:
                        stringa+=decine[0]
                elif(numero[i:f-1]=='3'):
                    if(numero[i:f]=='38'):
                        stringa+='trent'
                    else:
                        stringa+=decine[1]
                elif(numero[i:f-1]=='4'):
                    if(numero[i:f]=='48'):
                        stringa+='quarant'
                    else:
                        stringa+=decine[2]
                elif(numero[i:f-1]=='5'):
                    if(numero[i:f]=='58'):
                        stringa+='cinquant'
                    else:
                        stringa+=decine[3]
                elif(numero[i:f-1]=='6'):
                    if(numero[i:f]=='68'):
                        stringa+='sessant'
                    else:
                        stringa+=decine[4]
                elif(numero[i:f-1]=='7'):
                    if(numero[i:f]=='78'):
                        stringa+='settant'
                    else:
                        stringa+=decine[5]
                elif(numero[i:f-1]=='8'):
                    if(numero[i:f]=='88'):
                        stringa+='ottant'
                    elif(numero[i-1:f-1]=='18'):
                        stringa+='ttanta'
                    elif(numero[i-1:f-1]=='28'):
                        stringa+='ttanta'
                    elif(numero[i-1:f-1]=='38'):
                        stringa+='ttanta'
                    elif(numero[i-1:f-1]=='48'):
                        stringa+='ttanta'
                    elif(numero[i-1:f-1]=='58'):
                        stringa+='ttanta'
                    elif(numero[i-1:f-1]=='68'):
                        stringa+='ttanta'
                    elif(numero[i-1:f-1]=='78'):
                        stringa+='ttanta'
                    elif(numero[i-1:f-1]=='88'):
                        stringa+='ttant'
                    elif(numero[i-1:f-1]=='98'):
                        stringa+='ttanta'
                    else:
                        stringa+=decine[6]
                elif(numero[i:f-1]=='9'):
                    if(numero[i:f]=='98'):
                        stringa+='novant'
                    else:
                        stringa+=decine[7]
            
            i += 1
            
        elif(int(numero[i:f])<1000):
            if(numero[i:f-2]=='1'):
                stringa+=centinaia[0]
            elif(numero[i:f-2]=='2'):
                stringa+=centinaia[1]
            elif(numero[i:f-2]=='3'):
                stringa+=centinaia[1]
            elif(numero[i:f-2]=='4'):
                stringa+=centinaia[2]
            elif(numero[i:f-2]=='5'):
                stringa+=centinaia[3]
            elif(numero[i:f-2]=='6'):
                stringa+=centinaia[4]
            elif(numero[i:f-2]=='7'):
                stringa+=centinaia[5]
            elif(numero[i:f-2]=='8'):
                stringa+=centinaia[6]
            elif(numero[i:f-2]=='9'):
                stringa+=centinaia[7]
            
    
            i += 1
        while(f-i>3):
            #centomila
            if(int(numero[i:f-3])>=100):
                if(numero[i:f-5]=='1'):
                    stringa+=centinaia[0]+'mila'
                elif(numero[i:f-5]=='2'):
                    stringa+=centinaia[1]+'mila'
                elif(numero[i:f-5]=='3'):
                    stringa+=centinaia[1]+'mila'
                elif(numero[i:f-5]=='4'):
                    stringa+=centinaia[2]+'mila'
                elif(numero[i:f-5]=='5'):
                    stringa+=centinaia[3]+'mila'
                elif(numero[i:f-5]=='6'):
                    stringa+=centinaia[4]+'mila'
                elif(numero[i:f-5]=='7'):
                    stringa+=centinaia[5]+'mila'
                elif(numero[i:f-5]=='8'):
                    stringa+=centinaia[6]+'mila'
                elif(numero[i:f-5]=='9'):
                    stringa+=centinaia[7]+'mila'
        
            #diecimila
            if((int(numero[i:f-3])>=10)):
                if(numero[i:f-3]=='1'):
                    stringa+=unitaDecine[1]+'mila'
                elif(numero[i:f-3]=='2'):
                    stringa+=unitaDecine[2]+'mila'
                elif(numero[i:f-3]=='3'):
                    stringa+=unitaDecine[3]+'mila'
                elif(numero[i:f-3]=='4'):
                    stringa+=unitaDecine[4]+'mila'
                elif(numero[i:f-3]=='5'):
                    stringa+=unitaDecine[5]+'mila'
                elif(numero[i:f-3]=='6'):
                    stringa+=unitaDecine[6]+'mila'
                elif(numero[i:f-3]=='7'):
                    stringa+=unitaDecine[7]+'mila'
                elif(numero[i:f-3]=='8'):
                    stringa+=unitaDecine[8]+'mila'
                elif(numero[i:f-3]=='9'):
                    stringa+=unitaDecine[9]+'mila'
                elif(numero[i:f-3]=='10'):
                    stringa+=unitaDecine[10]+'mila'
                elif(numero[i:f-3]=='11'):
                    stringa+=unitaDecine[11]+'mila'
                elif(numero[i:f-3]=='12'):
                    stringa+=unitaDecine[12]+'mila'
                elif(numero[i:f-3]=='13'):
                    stringa+=unitaDecine[13]+'mila'
                elif(numero[i:f-3]=='14'):
                    stringa+=unitaDecine[14]+'mila'
                elif(numero[i:f-3]=='15'):
                    stringa+=unitaDecine[15]+'mila'
                elif(numero[i:f-3]=='16'):
                    stringa+=unitaDecine[16]+'mila'
                elif(numero[i:f-3]=='17'):
                    stringa+=unitaDecine[17]+'mila'
                elif(numero[i:f-3]=='18'):
                    stringa+=unitaDecine[18]+'mila'
                elif(numero[i:f-3]=='19'):
                        stringa+=unitaDecine[19]+'mila'
        
            #mille
            else:
                if(numero[i:f-3]=='1'):
                    stringa+=migliaia[0]
                elif(numero[i:f-3]=='2'):
                    stringa+=migliaia[1]
                elif(numero[i:f-3]=='3'):
                    stringa+=migliaia[1]
                elif(numero[i:f-3]=='4'):
                    stringa+=migliaia[2]
                elif(numero[i:f-3]=='5'):
                    stringa+=migliaia[3]
                elif(numero[i:f-3]=='6'):
                    stringa+=migliaia[4]
                elif(numero[i:f-3]=='7'):
                    stringa+=migliaia[5]
                elif(numero[i:f-3]=='8'):
                    stringa+=migliaia[6]
                elif(numero[i:f-3]=='9'):
                    stringa+=migliaia[7]
            i += 1
        
    return stringa

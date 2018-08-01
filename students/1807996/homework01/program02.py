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
    #creo una lista NUMERO vuota a cui concateno tutti i numeri trasformati in lettere
    numero=[]
    """creo una stringa vuota NNN che riempio con 12 cifre, 
    in modo tale da poter valorizzare attraverso il comando int(nnn[cent:uni+1]) un determinato intervallo
    e poterlo studiare"""
    nnn=''
    #stringa di output
    fin=''
    centinaia=['','cento','duecento','trecento','quattrocento','cinquecento','seicento','settecento','ottocento','novecento']
    unita=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    decine=['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
    cent=0
    dec=1
    uni=2
    #riempimento stringa NNN
    for x in range (12):
        if x < (12-(len(str(n)))):
            nnn+='0'
        if x== (12-(len(str(n)))):
            nnn+=str(n)
            break
    #studio, conversione numero
    for x in range (4):
        #studio cent
        if int(nnn[cent])>0 or int(nnn[dec])>0 or int(nnn[uni])>0:
            numero+=[centinaia[int(nnn[cent])]]
            #studio dec
            if (int(nnn[dec])>1 or int(nnn[dec])==0) and int(nnn[dec])!=8:
                numero+=[decine[int(nnn[dec])]]
                #studio uni
                if int(nnn[uni])>=0 and int(nnn[uni])!=1 and int(nnn[uni])!=8:
                    numero+=[unita[int(nnn[uni])]]
                    if int(nnn[cent:uni+1])>0 and cent==0:
                        numero+=['miliardi']
                    if int(nnn[cent:uni+1])>0 and cent==3:
                        numero+=['milioni']
                    if int(nnn[cent:uni+1])>0 and cent==6:
                        numero+=['mila']
                if int(nnn[uni])==8:
                    if len(numero)==dec+1:
                        numero[dec]=numero[dec][:-1]
                        numero+=['otto']
                    else:
                        numero[dec+(len(numero)-(dec+1))]=numero[dec+(len(numero)-(dec+1))][:-1]
                        numero+=['otto']
                    if int(nnn[cent:uni+1])>0 and cent==0:
                        numero+=['miliardi']
                    if int(nnn[cent:uni+1])>0 and cent==3:
                        numero+=['milioni']
                    if int(nnn[cent:uni+1])>0 and cent==6:
                        numero+=['mila']

                if int(nnn[uni])==1:
                    if len(numero)==dec+1:
                        numero[dec]=numero[dec][:-1]
                        numero+=['uno']
                    else:
                        numero[dec+(len(numero)-(dec+1))]=numero[dec+(len(numero)-(dec+1))][:-1]
                        numero+=['uno']
                        
                    if int(nnn[cent:uni+1])>0 and cent==0:
                        numero+=['miliardi']
                        if int(nnn[uni])!=1:
                            numero+=['miliardi']
                        else:
                            numero[uni+(len(numero)-(uni+1))]=''
                            numero+=['unmiliardo']
                    if int(nnn[cent:uni+1])>0 and cent==3:
                        if int(nnn[uni])!=1:
                            numero+=['milioni']
                        else:
                            numero[uni+(len(numero)-(uni+1))]=''
                            numero+=['unmilione']
                        
                    if int(nnn[cent:uni+1])>0 and cent==6:
                        if int(nnn[uni])!=1:
                            numero+=['mila']
                        else:
                            numero[uni+(len(numero)-(uni+1))]=''
                            numero+=['mille']
                            
            if int(nnn[dec])==8 and int(nnn[uni])!=8 and int(nnn[uni])!=1:
                if int(nnn[cent])==0:
                    numero+=['ottanta']
                else:
                    numero+=['ttanta']
                    if int(nnn[uni])>=0 and int(nnn[uni])!=1 and int(nnn[uni])!=8:
                        numero+=[unita[int(nnn[uni])]]
                        if int(nnn[cent:uni+1])>0 and cent==0:
                            numero+=['miliardi']
                            if int(nnn[cent:uni+1])>0 and cent==3:
                                numero+=['milioni']
                            if int(nnn[cent:uni+1])>0 and cent==6:
                                numero+=['mila'] 
                    
            if int(nnn[dec])==8 and (int(nnn[uni])==8 or int(nnn[uni])==1):
                if int(nnn[cent])!=0:
                    numero+='ttant',unita[int(nnn[uni])]
                    if int(nnn[cent:uni+1])>0 and cent==0:
                        numero+=['miliardi']
                    if int(nnn[cent:uni+1])>0 and cent==3:
                        numero+=['milioni']
                    if int(nnn[cent:uni+1])>0 and cent==6:
                        numero+=['mila']
                if int(nnn[cent])==0:
                    numero+='ottant',unita[int(nnn[uni])]
                    if int(nnn[cent:uni+1])>0 and cent==0:
                        numero+=['miliardi']
                    if int(nnn[cent:uni+1])>0 and cent==3:
                        numero+=['milioni']
                    if int(nnn[cent:uni+1])>0 and cent==6:
                        numero+=['mila']

            if int(nnn[dec])==1:
                numero+=[unita[int(nnn[dec:cent+3])]]
                if int(nnn[cent:uni+1])>0 and cent==0:
                    numero+=['miliardi']
                if int(nnn[cent:uni+1])>0 and cent==3:
                    numero+=['milioni']
                if int(nnn[cent:uni+1])>0 and cent==6:
                    numero+=['mila']
                    
        cent+=3
        dec+=3
        uni+=3
    for x in range (len(numero)):
        fin+=str(numero[x])
    return fin


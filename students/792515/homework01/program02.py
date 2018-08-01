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
    nStringa=str(n)
    StrMax=str(1000000000000)
    lsStrDefUnita=[]
    lsStrDefCentinaia=[]
    lsStrDefMigliaia=[]
    lsStrDefCMigliaia=[]
    lsStrDefMilioni=[]
    lsStrDefCMilioni=[]
    lsStrDefMiliardi=[]
    lsStrDefCMiliardi=[]
    lsStrDefBilioni=[]
    lsStrDef=[]
    StrDef=''
#Formatto la stringa che contiene il numero n aggiungendo zeri non significativi fino alla lunghezza di StrMax
    nStringa=(len(StrMax)-len(nStringa))*'0'+nStringa
    #Bilione=''
    #Miliardi=''
    #Milioni=''
    #Migliaia=''
    #Centinaia=''
    #Decine=''
    #Unita=''
    #print(nStringa[0])
    #print(nStringa[1]+nStringa[2]+nStringa[3])
    #print(nStringa[4]+nStringa[5]+nStringa[6])
    #print(nStringa[7]+nStringa[8]+nStringa[9])
    #print(nStringa[10])
    #print(nStringa[11])
    #print(nStringa[12])
    Posizione=-1
    #creo una lista che contiene i simboli dei primi 19 numeri
    lsNum1=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19']
    #creo una lista che contiene la scrittura in lettere dei primi 19 numeri
    lsStr1=['uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
    #creo una lista che contiene i simboli dei numeri da 2 a 9 intesi come decine (2 decine etc.)
    lsNum2=['2','3','4','5','6','7','8','9']
    #creo una lista che contiene la scrittura in lettere delle decine da 2 a 9
    lsStr2=['vent','trent','quarant','cinquant','sessant','settant','ottant','novant']

#prime due posizioni (tra1 e 99)
    #per prima cosa cerco il numero uno:
    if nStringa[10]+nStringa[11]+nStringa[12]=='001':
        lsStrDefUnita=['uno']
    #per seconda cosa cerco i numeri da 2 a 19:
    elif nStringa[11]+nStringa[12] in lsNum1:
        Posizione=lsNum1.index(nStringa[11]+nStringa[12])
        lsStrDefUnita=[lsStr1[Posizione]]
    # se il numero è maggiore di diciannove e non ha unità, sarà una decina intera (venti,trenta...)
    #..scrivo il numero senza applicare l'elisione
    elif nStringa[11]!='0' and nStringa[12]=='0':
        Posizione=lsNum2.index(nStringa[11])
        lsStrDefUnita=[lsStr2[Posizione]]
        if nStringa[11]=='2':
            lsStrDefUnita=[lsStr2[Posizione]]+['i']
        else:
            lsStrDefUnita=[lsStr2[Posizione]]+['a']        
    # ...se il numero è maggiore di diciannove ed ha unità, sarà un numero compreso tra venti e novantanove...
    #..scrivo il numero applicando l'elisione
    elif nStringa[11]!='0' and nStringa[12]!='0':
        Posizione=lsNum2.index(nStringa[11])
    #...applico l'elisione...
        if nStringa[12]=='1' or nStringa[12]=='8':
            lsStrDefUnita=[lsStr2[Posizione]]
            Posizione=lsNum1.index('0'+nStringa[12])
            lsStrDefUnita=lsStrDefUnita+[lsStr1[Posizione]]
        elif nStringa[11]=='2':
            lsStrDefUnita=[lsStr2[Posizione]]+['i']
            Posizione=lsNum1.index('0'+nStringa[12])
            lsStrDefUnita=lsStrDefUnita+[lsStr1[Posizione]]            
        else:
            lsStrDefUnita=[lsStr2[Posizione]]+['a']
            Posizione=lsNum1.index('0'+nStringa[12])
            lsStrDefUnita=lsStrDefUnita+[lsStr1[Posizione]]
            
#centinaia (tra 100 e 999)
    if nStringa[10]!='0':
        if nStringa[10]=='1':
            lsStrDefCentinaia=['cent']
        else:
            Posizione=lsNum1.index('0'+nStringa[10])
            lsStrDefCentinaia=[lsStr1[Posizione]]+['cent']            
#applico l'elisione
        if nStringa[11]!='8':
            lsStrDefCentinaia=lsStrDefCentinaia+['o']            

#migliaia (da 1000 a 99.999)
    #per prima cosa cerco il numero mille:
    if nStringa[7]+nStringa[8]+nStringa[9]=='001':
        lsStrDefMigliaia=['mille']
    #per seconda cosa cerco i numeri da 2000 a 19000:
    elif nStringa[8]+nStringa[9] in lsNum1:
        Posizione=lsNum1.index(nStringa[8]+nStringa[9])
        lsStrDefMigliaia=[lsStr1[Posizione]]+['mila']
    # se il numero è maggiore di diciannovemila e non ha unità, sarà una decina intera (ventimila,trentamila...)
    #..scrivo il numero senza applicare l'elisione
    elif nStringa[8]!='0' and nStringa[9]=='0':
        Posizione=lsNum2.index(nStringa[8])
        lsStrDefMigliaia=[lsStr2[Posizione]]+['mila']
        if nStringa[8]=='2':
            lsStrDefMigliaia=[lsStr2[Posizione]]+['i']+['mila']
        else:
            lsStrDefMigliaia=[lsStr2[Posizione]]+['a']+['mila']
    # ...se il numero è maggiore di diciannovemila ed ha unità, sarà un numero compreso tra ventimila e novantanovemila...
    #..scrivo il numero applicando l'elisione
    elif nStringa[8]!='0' and nStringa[9]!='0':
        Posizione=lsNum2.index(nStringa[8])
    #...applico l'elisione...
        if nStringa[9]=='1' or nStringa[9]=='8':
            lsStrDefMigliaia=[lsStr2[Posizione]]
            Posizione=lsNum1.index('0'+nStringa[9])
            lsStrDefMigliaia=lsStrDefMigliaia+[lsStr1[Posizione]]+['mila']
        elif nStringa[8]=='2':
            lsStrDefMigliaia=[lsStr2[Posizione]]+['i']+['mila']
            Posizione=lsNum1.index('0'+nStringa[9])
            lsStrDefMigliaia=lsStrDefMigliaia+[lsStr1[Posizione]]+['mila']            
        else:
            lsStrDefMigliaia=[lsStr2[Posizione]]+['a']
            Posizione=lsNum1.index('0'+nStringa[9])
            lsStrDefMigliaia=lsStrDefMigliaia+[lsStr1[Posizione]]+['mila']


#centinaia di migliaia
    if nStringa[7]!='0':
        if nStringa[7]=='1':
            lsStrDefCMigliaia=['cent']
        else:
            Posizione=lsNum1.index('0'+nStringa[7])
            lsStrDefCMigliaia=[lsStr1[Posizione]]+['cent']
        #applico l'elisione
        if nStringa[8]!='8':
            lsStrDefCMigliaia=lsStrDefCMigliaia+['o']            

    #alla fine mi assicuro che se il numero è nelle migliaia ci sia scritto "mila"
    if len(lsStrDefCMigliaia)>0 and len(lsStrDefMigliaia)==0:
        lsStrDefCMigliaia=lsStrDefCMigliaia+['mila']

#milioni
#(tra 1 e 99 milioni)
    #per prima cosa cerco il numero un milione:
    if nStringa[4]+nStringa[5]+nStringa[6]=='001':
        lsStrDefMilioni=['unmilione']
    #per seconda cosa cerco i numeri da 2.000.000 a 19.000.000:
    elif nStringa[5]+nStringa[6] in lsNum1:
        Posizione=lsNum1.index(nStringa[5]+nStringa[6])
        lsStrDefMilioni=[lsStr1[Posizione]]+['milioni']
    # se il numero è maggiore di diciannove milioni e non ha unità, sarà una milionata intera (ventimilioni,trentamilioni...)
    #..scrivo il numero senza applicare l'elisione
    elif nStringa[5]!='0' and nStringa[6]=='0':
        Posizione=lsNum2.index(nStringa[5])
        lsStrDefMilioni=[lsStr2[Posizione]]+['milioni']
        if nStringa[5]=='2':
            lsStrDefMilioni=[lsStr2[Posizione]]+['i']+['milioni']
        else:
            lsStrDefMilioni=[lsStr2[Posizione]]+['a']+['milioni']
    # ...se il numero è maggiore di diciannovemilioni ed ha unità, sarà un numero compreso tra ventimilioni e novantanovemilioni...
    #..scrivo il numero applicando l'elisione
    elif nStringa[5]!='0' and nStringa[6]!='0':
        Posizione=lsNum2.index(nStringa[5])
    #...applico l'elisione...
        if nStringa[6]=='1' or nStringa[6]=='8':
            lsStrDefMilioni=[lsStr2[Posizione]]
            Posizione=lsNum1.index('0'+nStringa[6])
            lsStrDefMilioni=lsStrDefMilioni+[lsStr1[Posizione]]+['milioni']
        elif nStringa[5]=='2':
            lsStrDefMilioni=[lsStr2[Posizione]]+['i']+['milioni']
            Posizione=lsNum1.index('0'+nStringa[6])
            lsStrDefMilioni=lsStrDefMilioni+[lsStr1[Posizione]]+['milioni']            
        else:
            lsStrDefMilioni=[lsStr2[Posizione]]+['a']
            Posizione=lsNum1.index('0'+nStringa[6])
            lsStrDefMilioni=lsStrDefMilioni+[lsStr1[Posizione]]+['milioni']

#centinaia di milioni (tra 100 e 999 milioni)
    if nStringa[4]!='0':
        if nStringa[4]=='1':
            lsStrDefCMilioni=['cent']
        else:
            Posizione=lsNum1.index('0'+nStringa[4])
            lsStrDefCMilioni=[lsStr1[Posizione]]+['cent']
#applico l'elisione
        if nStringa[5]!='8':
            lsStrDefCMilioni=lsStrDefCMilioni+['o']

    #alla fine mi assicuro che se il numero è nei milioni ci sia scritto "milione" se è 1, "milioni" se >1
    if len(lsStrDefCMilioni)>0 and len(lsStrDefMilioni)==0:
        lsStrDefCMilioni=lsStrDefCMilioni+['milioni']

#miliardi
#(tra1 e 99) miliardi
    #per prima cosa cerco il numero un miliardo:
    if nStringa[1]+nStringa[2]+nStringa[3]=='001':
        lsStrDefMiliardi=['unmiliardo']
    #per seconda cosa cerco i numeri da 2.000.000.000 a 19.000.000.000:
    elif nStringa[2]+nStringa[3] in lsNum1:
        Posizione=lsNum1.index(nStringa[2]+nStringa[3])
        lsStrDefMiliardi=[lsStr1[Posizione]]+['miliardi']
    # se il numero è maggiore di diciannove miliardi e non ha unità, sarà una miliardata intera (ventimiliardi,trentamiliardi...)
    #..scrivo il numero senza applicare l'elisione
    elif nStringa[2]!='0' and nStringa[3]=='0':
        Posizione=lsNum2.index(nStringa[2])
        lsStrDefMiliardi=[lsStr2[Posizione]]+['miliardi']
        if nStringa[2]=='2':
            lsStrDefMiliardi=[lsStr2[Posizione]]+['i']+['miliardi']
        else:
            lsStrDefMiliardi=[lsStr2[Posizione]]+['a']+['miliardi']
    # ...se il numero è maggiore di diciannovemiliardi ed ha unità, sarà un numero compreso tra ventimiliardi e novantanovemiliardi...
    #..scrivo il numero applicando l'elisione
    elif nStringa[2]!='0' and nStringa[3]!='0':
        Posizione=lsNum2.index(nStringa[2])
    #...applico l'elisione...
        if nStringa[3]=='1' or nStringa[3]=='8':
            lsStrDefMiliardi=[lsStr2[Posizione]]
            Posizione=lsNum1.index('0'+nStringa[3])
            lsStrDefMiliardi=lsStrDefMiliardi+[lsStr1[Posizione]]+['miliardi']
        elif nStringa[2]=='2':
            lsStrDefMiliardi=[lsStr2[Posizione]]+['i']+['miliardi']
            Posizione=lsNum1.index('0'+nStringa[3])
            lsStrDefMiliardi=lsStrDefMiliardi+[lsStr1[Posizione]]+['miliardi']            
        else:
            lsStrDefMiliardi=[lsStr2[Posizione]]+['a']
            Posizione=lsNum1.index('0'+nStringa[3])
            lsStrDefMiliardi=lsStrDefMiliardi+[lsStr1[Posizione]]+['miliardi']

#centinaia di miilardi (tra 100 e 999 miliardi)
    if nStringa[1]!='0':
        if nStringa[1]=='1':
            lsStrDefCMiliardi=['cent']
        else:
            Posizione=lsNum1.index('0'+nStringa[1])
            lsStrDefCMiliardi=[lsStr1[Posizione]]+['cent']
        #applico l'elisione
        if nStringa[2]!='8':
            lsStrDefCMiliardi=lsStrDefCMiliardi+['o']

    #alla fine mi assicuro che se il numero è nei miliardi ci sia scritto "miliardo" se è 1, "miliardi" se >1
    if len(lsStrDefCMiliardi)>0 and len(lsStrDefMiliardi)==0:
        lsStrDefCMiliardi=lsStrDefCMiliardi+['miliardi']

#il bilione...
    if nStringa[0]=='1':
        lsStrDefBilioni=['unbilione']
        
    lsStrDef=lsStrDefBilioni+lsStrDefCMiliardi+lsStrDefMiliardi+lsStrDefCMilioni+lsStrDefMilioni+lsStrDefCMigliaia+lsStrDefMigliaia+lsStrDefCentinaia+lsStrDefUnita
    
    for i in range(len(lsStrDef)):
        StrDef=StrDef+lsStrDef[i]
    return StrDef

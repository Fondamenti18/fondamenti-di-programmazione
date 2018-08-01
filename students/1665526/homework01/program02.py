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



'Scrivete qui il codice della funzione'
def decine(n):
   
    diz={0:"",1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove',10:'dieci',
                11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',17:'diciassette',18:'diciotto',
                19:'dicianove',20:'venti',30:'trenta',40:'quaranta',50:'cinquanta',60:'sessanta',70:'settanta',80:'ottanta',
                90:'novanta',100:'cento',1000:'mille',10000000:'milione',1000000000:'miliardo'}
    if n in diz==0:
       return diz[0]
    if n in diz:
       return diz[n]
    sn=str(n)
    a=diz[int(sn[-2]+str(0))].strip('a i')+diz[int(sn[-1])]#corregge xxxuno e xxxotto
    b=diz[int(sn[-2]+'0')]+diz[int(sn[-1])]#decodifica gli ultimi due numeri
    if len(sn)==2:
       if len (sn)==2 and (sn[-1]==str(1) or sn[-1]==str(8)):
           return a
       return b
def centinaia(n):
    diz={0:"",1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove',10:'dieci',
                11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',17:'diciassette',18:'diciotto',
                19:'dicianove',20:'venti',30:'trenta',40:'quaranta',50:'cinquanta',60:'sessanta',70:'settanta',80:'ottanta',
                90:'novanta',100:'cento',1000:'mille',10000000:'milione',1000000000:'miliardo'}
    if n in diz==0:
       return diz[0]
    if n in diz:
       return diz[n]
    sn=str(n)
    if len(sn)==3:
        if sn[-3]==str(1) and sn[-2]==str(8):#caso specifico 180
            return 'cent'+str(decine(int(sn[-2:])))
        if sn[-3]==str(1):
            return 'cento'+str(decine(int(sn[-2:])))
        if sn[-2]==str(8):#caso cento/ottanta
            if sn[-1]==str(1) and sn[-1]==str(8):
                return diz[int(sn[-3])]+str(decine(int(sn[-2:])))
            return diz[int(sn[-3])]+'cent'+str(decine(int(sn[-2:])))
        if len(sn)==3:#caso generico
            return diz[int(sn[-3])]+'cento'+str(decine(int(sn[-2:])))
def migliaia(n):
    diz={0:"",1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove',10:'dieci',
                11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',17:'diciassette',18:'diciotto',
                19:'dicianove',20:'venti',30:'trenta',40:'quaranta',50:'cinquanta',60:'sessanta',70:'settanta',80:'ottanta',
                90:'novanta',100:'cento',1000:'mille',10000000:'milione',1000000000:'miliardo'}
    if n in diz==0:
       return diz[0]
    if n in diz:
       return diz[n]
    sn=str(n)
    if len(sn)==4:#caso generico per xxxx
        if sn[-3]==str(0) and sn[0]==str(1):
            return 'mille'+str(decine(int(sn[-3:])))
        if sn[-3]==str(0) and sn[-2]==str(0):#caso 2001
            return diz[int(sn[-4])]+'mila'+str(decine(int(sn[-1])))
        if sn[-3]==str(0):#caso in cui c'è uno zero nelle centinaia
            return diz[int(sn[-4])]+'mila'+str(decine(int(sn[-3:])))
        if sn[0]==str(1):#caso per mille
            return 'mille'+str(centinaia(int(sn[-3:])))
        return diz[int(sn[-4])]+'mila'+str(centinaia(int(sn[-3:])))
    if len(sn)==5:
        if sn[2]==str(0):#caso in cui c'è uno zero nelle centinaia
            return str(decine(int(sn[-5]+sn[-4])))+'mila'+str(decine(int(sn[-3:])))
        if sn[-3]==str(0) and sn[0]==str(1):
            return 'mille'+str(decine(int(sn[-3:])))
        if sn[-3]==str(0) and sn[-2]==str(0):#caso 2001
            return diz[int(sn[-5]+sn[-4])]+'mila'+str(decine(int(sn[-1])))
        
        return str(decine(int(sn[-5]+sn[-4])))+'mila'+str(centinaia(int(sn[-3:])))
    if len(sn)==6:
        if sn[-3]==str(0):
            return str(centinaia(int(sn[-6]+sn[-5]+sn[-4])))+'mila'+str(decine(int(sn[-2:])))
        return str(centinaia(int(sn[-6]+sn[-5]+sn[-4])))+'mila'+str(centinaia(int(sn[-3:])))
    
def milioni(n):
     diz={0:"",1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove',10:'dieci',
                11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',17:'diciassette',18:'diciotto',
                19:'dicianove',20:'venti',30:'trenta',40:'quaranta',50:'cinquanta',60:'sessanta',70:'settanta',80:'ottanta',
                90:'novanta',100:'cento',1000:'mille',10000000:'milione',1000000000:'miliardo'}
     if n in diz==0:
       return diz[0]
     if n in diz:
       return diz[n]
     sn=str(n)
     if len(sn)==7:
         if sn[0]==str(1):
             if sn[-6]==str(0) and sn[-5]==str(0) and sn[-4]==str(0):
                 return 'unmilione'+ str(centinaia(int(sn[-3:])))
             return 'unmilione'+str(migliaia(int(sn[-6:])))
         if sn[-6]==str(0) and sn[-5]==str(0) and sn[-4]==str(0):
             return diz[int(sn[-7])]+'milioni'+ str(centinaia(int(sn[-3:])))
         return diz[int(sn[-7])]+'milioni'+str(migliaia(int(sn[-6:])))
     if len(sn)==8:
         if sn[-6]==str(0) and sn[-5]==str(0) and sn[-4]==str(0):
             return str(decine(int(sn[-8]+sn[-7])))+'milioni'+ str(centinaia(int(sn[-3:])))
         return str(decine(int(sn[-8]+sn[-7])))+'milioni'+str(migliaia(int(sn[-6:])))
     if len(sn)==9:
         if sn[-6]==str(0) and sn[-5]==str(0) and sn[-4]==str(0):
             return str(centinaia(int(sn[-9]+sn[-8]+sn[-7])))+'milioni'+ str(centinaia(int(sn[-3:])))
         return str(centinaia(int(sn[-9]+sn[-8]+sn[-7])))+'milioni'+str(migliaia(int(sn[-6:])))
def miliardi(n):
     diz={0:"",1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove',10:'dieci',
                11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',17:'diciassette',18:'diciotto',
                19:'dicianove',20:'venti',30:'trenta',40:'quaranta',50:'cinquanta',60:'sessanta',70:'settanta',80:'ottanta',
                90:'novanta',100:'cento',1000:'mille',10000000:'milione',1000000000:'miliardo'}
     if n in diz==0:
       return diz[0]
     if n in diz:
       return diz[n]
     sn=str(n)
     if len(sn)==10:
         if sn[0]==str(1):
             if sn[-9]==str(0) and sn[-8]==str(0) and sn[-7]==str(0):
                 return 'unmiliardo'+ str(migliaia(int(sn[4:])))
             return 'unmiliardo'+str(milioni(int(sn[1:])))
         if sn[-9]==str(0) and sn[-8]==str(0) and sn[-7]==str(0):
             return diz[int(sn[-7])]+'milioni'+ str(migliaia(int(sn[4:])))
         return diz[int(sn[-10])]+'miliardi'+str(milioni(int(sn[1:])))
     if len(sn)==11:
         if sn[-9]==str(0) and sn[-8]==str(0) and sn[-7]==str(0):
             return 'unmiliardo'+ str(migliaia(int(sn[4:])))
         if sn[-9]==str(0) and sn[-8]==str(0) and sn[-7]==str(0):
             return diz[int(sn[-7])]+'milioni'+ str(migliaia(int(sn[4:])))
         return str(decine(int(sn[-11]+sn[-10])))+'miliardi'+str(milioni(int(sn[2:])))
     if len(sn)==12:
         if sn[-9]==str(0) and sn[-8]==str(0) and sn[-7]==str(0):
             return 'unmiliardo'+ str(migliaia(int(sn[4:])))
         if sn[-9]==str(0) and sn[-8]==str(0) and sn[-7]==str(0):
             return diz[int(sn[-7])]+'milioni'+ str(migliaia(int(sn[4:])))
         return str(centinaia(int(sn[-12]+sn[-11]+sn[-10])))+'miliardi'+str(milioni(int(sn[3:])))
def conv(n):
   'Scrivete qui il codice della funzione'
   diz={0:"zero",1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove',10:'dieci',
                11:'undici',12:'dodici',13:'tredici',14:'quattordici',15:'quindici',16:'sedici',17:'diciassette',18:'diciotto',
                19:'dicianove',20:'venti',30:'trenta',40:'quaranta',50:'cinquanta',60:'sessanta',70:'settanta',80:'ottanta',
                90:'novanta',100:'cento',1000:'mille',10000000:'milione',1000000000:'miliardo'}
   if n in diz==0:
       return diz[0]
   if n in diz:
       return diz[n]
   sn=str(n)
   if len(sn)==2:
       return decine(n)
   if len(sn)==3:
       return centinaia(n)
   if len(sn)==4 or len(sn)==5 or len(sn)==6:
       return migliaia(n)
   if len(sn)==7 or len(sn)==8 or len(sn)==9:
       return milioni(n)
   if len(sn)==10 or len(sn)==11 or len(sn)==12:
       return miliardi(n)
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

u= ['','uno','due','tre','quattro','cinque','sei','sette','otto','nove', 'dieci', 'undici','dodici','tredici',
    'quattordici','quindici','sedici','diciassette','diciotto','diciannove','venti']
d=['','','','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta'] 

def conv(n):
    numero=''
    n=str(n)
    uni= unita(n)
    dec=decine(n)
    
    
    if int(n)< 10:
        
        numero+= uni
    if 10<=int(n) <100:
        numero+= dec
        
    if  100<int(n)<1000:
       cen=centinaia(n)
       numero=cen+dec
    
    if 1000<=int(n)<1000000:
       mig=migliaia(n)
       numero+= mig
    
    if 1000000<=int(n)<1000000000:
       numero+= milioni(n) 
    
    if 1000000000<=int(n)<1000000000000:
       mil= miliardi(n)
       numero+= mil

               
        
    return numero

def miliardi(n):
    
    if 1000000000<=int(n[-12:])<=1999999999:
        mln=milioni(n)
        return 'unmiliardo'+mln
    if 1999999999<int(n[-12:])<10000000000:
        uu=unita(n[-10])
        mln=milioni(n)
        return uu+'miliardi'+ mln
        
    if 10000000000<=int(n[-12:])<100000000000:
        mln=milioni(n)
        
        dd= decine(n[-11:-9])        
        return dd+'miliardi'+ mln
      
    if 100000000000<=int(n[-12:])<1000000000000:
        mln=milioni(n)
        
        cc= centinaia(n[-12:-9])
        dd= decine(n[-11:-9])
        return cc+dd+'miliardi'+mln




def milioni(n):
    if int(n[-9:-6])==0:
       mig=migliaia(n)
       return mig
    
    if 1000000<=int(n[-9:])<=1999999:
        mig=migliaia(n)
        return 'unmilione'+mig
    if 1999999<int(n[-9:])<10000000:
        uu=unita(n[-4])
        mig=migliaia(n)
        return uu+'milioni'+ mig
        
    if 10000000<=int(n[-9:])<100000000:
        mig=migliaia(n)
        
        dd= decine(n[-8:-6])        
        return dd+'milioni'+ mig
      
    if 100000000<=int(n[-9:])<1000000000:
        mig=migliaia(n)
        
        cc= centinaia(n[-9:-6])
        dd= decine(n[-8:-6])
        return cc+dd+'milioni'+ mig

def migliaia(n):
    dec=decine(n)
    if int(n[-6:-3])==0:
       cen=centinaia(n)
       return cen+dec
    
    if 1000<=int(n[-6:])<1999:
        cen=centinaia(n)
        return 'mille'+cen+dec
    if 1999<int(n[-6:])<10000:
        cen=centinaia(n)
        uu=unita(n[-4])
        return uu+'mila'+cen+dec
        
    if 10000<=int(n[-6:])<100000:
        cen=centinaia(n)
        
        dd= decine(n[-5:-3])        
        return dd+'mila'+cen+dec
      
    if 100000<=int(n[-6:])<1000000:
        cen=centinaia(n)
        
        cc= centinaia(n[-6:-3])
        dd= decine(n[-5:-3])
        return cc+dd+'mila'+cen+dec
    

def unita(n):
       n=str(n)
       i=0
       while i<10:
            if int(n[-1]) == i:
                return u[i]
                break
            i+=1 
  
def decine(n):
    uni=unita(n)
    lun= len(n)
    if int(n[lun-2]) == 0:
        return ''+uni
     
    if int(n[lun-2]) == 1:
       return u[int(n[lun-2: lun])]
    if int(n[lun-2]) == 2:
        if int(n[lun-1])== 1 or int(n[lun-1])== 8:
           return u[20][:-1]+uni
        else:
           return u[20]+uni
    j=3
    ld= len(d)
    while j<ld:
        if int(n[lun-2]) ==  j:
            if int(n[lun-1])== 1 or int(n[lun-1])== 8:
                return d[j][:-1]+uni
            else:
                return d[j]+uni
           
        j+=1
     
def centinaia(n):
            n=str(n)
            cento='cento'
            c=1
            if int(n[-3])==0:
                return ''
            while c<10:
                if int(n[-2]) == 8:
                    if int(n[-3]) == 1:
                        return cento[:-1]
                    elif int(n[-3]) == c:
                        return u[c]+cento[:-1] 
                else:    
                    if int(n[-3]) == 1:
                       return cento
                    elif int(n[-3]) == c:
                        return u[c]+cento
                
                c+=1 
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
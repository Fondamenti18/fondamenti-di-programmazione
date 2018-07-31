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
n=981001818
secondo=['zero','dieci','vent','trent','quarant','cinquant','sessant','settant','ottant','novant']
primo=['zero','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
ultimo=['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove']


def conv(n):
    listaN=[int(x) for x in str(n)]
    puntalun=len(str(n))
    return(''.join(pre(puntalun, listaN)))

def pre(puntalun, listaN):
    
    bol='false'
    primavolt='true'
    finale=[]
    numero=0
    while puntalun>0:
        zero='true'
        mil='false'
        print(puntalun)
        
        
        
        if (puntalun%3==0):   #----------primo numero
            if ultimo[listaN[numero]]!='uno'and ultimo[listaN[numero]]!='zero':    
                finale.append(ultimo[listaN[numero]])
                zero='false'
            if ultimo[listaN[numero]]!='zero':
                finale+=['cent']
                if secondo[listaN[numero+1]]!='ottant':
                    finale+=['o']
                
                zero='false'
            numero+=1
            puntalun-=1
        
        
        
        
        if puntalun==11 or puntalun==8 or puntalun==5 or puntalun==2:
            if secondo[listaN[numero]]!='zero'and secondo[listaN[numero]]!='dieci':     #secondo e terzo numero
                finale.append(secondo[listaN[numero]])
                voca =secondo[listaN[numero]]
                nex= ultimo[listaN[numero+1]]
                ellisse(voca,finale,nex)
                zero='false'
                
            if secondo[listaN[numero]]=='dieci':
                 finale.append(primo[listaN[numero+1]+1])
                 bol='true' 
                 zero='false'
            numero+=1
            puntalun-=1
        
        
        if puntalun==10 or puntalun==7 or puntalun==4 or puntalun==1:                               #terzo numero e zeri
            if bol=='false' and ultimo[listaN[numero]]!='zero':
                if primavolt=='true' and ultimo[listaN[numero]]=='uno' and puntalun==4:
                    zero='false'
                    mil='true'
                else:
                    finale.append(ultimo[listaN[numero]])
                    zero='false'
                    
            if (puntalun==10 and zero!='true' and primavolt=='false') or primavolt=='true' and puntalun==10 :
                finale+=['miliardi']               
                primavolt='false'
            if  (puntalun==7 and zero!='true' and primavolt=='false') or primavolt=='true'and puntalun==7:
                finale+=['milioni']
                primavolt='false'
            if  (puntalun==4 and zero!='true' and primavolt=='false') or primavolt=='true'and puntalun==4:
                if mil=='true':
                    finale+=['mille']
                else:
                    finale+=['mila']
                primavolt='false'
            numero+=1
            puntalun-=1
        bol='false'
        
    
    return finale


def ellisse(voca,finale,nex):                                                    #ellisse
    if voca[-1]=='t' and (nex[0] not in 'aeiou'):
        if voca=='vent':
            finale+=['i']
        else:
            finale+=['a']
        
        
    
    
    






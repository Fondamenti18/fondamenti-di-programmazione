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
    num=str(n)
    lunghezza=len(num)
    nome=""
    
    if n<0 or n>1000000000000:
        nome="Numero inserito non valido" 
    elif lunghezza==1:
        nome=unita(num)
    elif lunghezza==2:
        nome=decine(num[0]+num[1])
    elif lunghezza==3:
        if n==100:
            nome="cento"
        else:
            nome=centinaia(num[0],num[1])+decine(num[1]+num[2])
    elif lunghezza==4:
        if n==1000:
            nome="mille"
        elif n>1000 and n<2000:
            nome="mille"+centinaia(num[1],num[2])+decine(num[2]+num[3])
        elif n>=2000 and n<=9999:
            nome=prefisso(num[0])+"mila"+centinaia(num[1],num[2])+decine(num[2]+num[3])
    elif lunghezza==5:
        if n==10000:
            nome="diecimila"
        else:
            nome=decine(num[0]+num[1])+"mila"+centinaia(num[2],num[3])+decine(num[3]+num[4])
    elif lunghezza==6:
        if n==100000:
            nome="centomila"
        else:
            nome=centinaia(num[0],num[1])+decine(num[1]+num[2])+"mila"+centinaia(num[3],num[4])+decine(num[4]+num[5])      
    elif lunghezza==7:
        if n==1000000:
            nome="un milione"
        elif n>1000000 and n<=1999999:
            nome="un milione "+centinaia(num[1],num[2])+decine(num[2]+num[3])+"mila"+centinaia(num[4],num[5])+decine(num[5]+num[6])
        else:
            nome=prefisso(num[0])+" milioni "+centinaia(num[1],num[2])+decine(num[2]+num[3])+"mila"+centinaia(num[4],num[5])+decine(num[5]+num[6])
    elif lunghezza==8:
        if n==10000000:
            nome="dieci milioni"
        else:
            nome=decine(num[0]+num[1])+"milioni"+centinaia(num[2],num[3])+decine(num[3]+num[4])+"mila"+centinaia(num[5],num[6])+decine(num[6]+num[7])
    elif lunghezza==9:
        if n==100000000:
            nome="cento milioni"
        else:
            nome=centinaia(num[0],num[1])+decine(num[1]+num[2])+"milioni"+centinaia(num[3],num[4])+decine(num[4]+num[5])+"mila"+centinaia(num[6],num[7])+decine(num[7]+num[8])
    elif lunghezza==10:
        if n==1000000000:
            nome="un miliardo"
        elif n>1000000000 and n<=1999999999:
            nome="un miliardo"+centinaia(num[1],num[2])+decine(num[2]+num[3])+"milioni"+centinaia(num[4],num[5])+decine(num[5]+num[6])+"mila"+centinaia(num[7],num[8])+decine(num[8]+num[9])
        else:
            nome=prefisso(num[0])+"miliardi"+centinaia(num[1],num[2])+decine(num[2]+num[3])+"milioni"+centinaia(num[4],num[5])+decine(num[5]+num[6])+"mila"+centinaia(num[7],num[8])+decine(num[8]+num[9])
    elif lunghezza==11:
        if n==10000000000:
            nome="dieci miliardi"
        else:
            nome=decine(num[0]+num[1])+"miliardi"+centinaia(num[2],num[3])+decine(num[3]+num[4])+"milioni"+centinaia(num[5],num[6])+decine(num[6]+num[7])+"mila"+centinaia(num[8],num[9])+decine(num[9]+num[10])
    elif lunghezza==12:
        if n==100000000000:
            nome="cento miliardi"
        else:
            nome=centinaia(num[0],num[1])+decine(num[1]+num[2])+"miliardi"+centinaia(num[3],num[4])+decine(num[4]+num[5])+"milioni"+centinaia(num[6],num[7])+decine(num[7]+num[8])+"mila"+centinaia(num[9],num[10])+decine(num[10]+num[11])
    elif n==1000000000000:
        nome="un biliardo" 
    
    return nome
        

def prefisso(num):
    n=int(num)
    nome=""
    
    if n==2:
        nome="due"
    elif n==3:
        nome="tre"
    elif n==4:
        nome="quattro"
    elif n==5:
        nome="cinque"
    elif n==6:
        nome="sei"
    elif n==7:
        nome="sette"
    elif n==8:
        nome="otto"
    elif n==9:
        nome="nove"
    
    return nome
       

def converti_1(num):
    nome=""
    n=int(num)
    
    if n==10:
        nome="dieci"
    elif n==11:
        nome="undici"
    elif n==12:
        nome="dodici"
    elif n==13:
        nome="tredici"
    elif n==14:
        nome="quattordici"
    elif n==15:
        nome="quindici"
    elif n==16:
        nome="sedici"
    elif n==17:
        nome="diciassette"
    elif n==18:
        nome="diciotto"
    elif n==19:
        nome="diciannove"
    
    return nome
    

def unita(num):
    n=int(num)
    nome=""
    
    if n==0:
        nome="zero"
    elif n==1:
        nome="uno"
    elif n==2:
        nome="due"
    elif n==3:
        nome="tre"
    elif n==4:
        nome="quattro"
    elif n==5:
        nome="cinque"
    elif n==6:
        nome="sei"
    elif n==7:
        nome="sette"
    elif n==8:
        nome="otto"
    elif n==9:
        nome="nove"
    
    return nome
           
def decine(num):
    n=int(num)
    nome=""
    
    if n>=10 and n<=19:
        nome=converti_1(num)
    else:
        if n>=20 and n<=29:
            nome="venti"
        elif n>=30 and n<=39:
            nome="trenta"
        elif n>=40 and n<=49:
            nome="quaranta"
        elif n>=50 and n<=59:
            nome="cinquanta"
        elif n>=60 and n<=69:
            nome="sessanta"
        elif n>=70 and n<=79:
            nome="settanta"
        elif n>=80 and n<=89:
            nome="ottanta"
        elif n>=90 and n<=99:
            nome="novanta"
    
    if (num[-1]=="1" or num[-1]=="8") and (n>=20 and n<=29):
        nome=nome.replace("i","")
    if (num[-1]=="1" or num[-1]=="8") and (n in [31,38,41,48,51,58,61,68,71,78,81,88,91,98]):
        nome=nome[0:len(nome)-1]
    if num[-1]!="0" and not(n>=10 and n<=19):
        nome=nome+unita(num[-1])   
        
    
    return nome

def centinaia(num,succ):
    n=int(num)
    nome=""
    
    if n==1:
        nome="cento"
    elif n==2:
        nome="duecento"
    elif n==3:
        nome="trecento"
    elif n==4:
        nome="quattrocento"
    elif n==5:
        nome="cinquecento"
    elif n==6:
        nome="seicento"
    elif n==7:
        nome="settecento"
    elif n==8:
        nome="ottocento"
    elif n==9:
        nome="novecento"
    
    if succ=="8":
        nome=nome[0:len(nome)-1]
    
    return nome
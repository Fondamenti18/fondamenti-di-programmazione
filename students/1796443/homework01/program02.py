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
def decine (x,c,ls,ls1):
    if x=='0':
        ls1+=['']
    if x=='1':
        if ls[c-1]=='0':
            ls1+=['dieci']
        if ls[c-1]=='1':
            ls1+=['undici']
        if ls[c-1]=='2':
            ls1+=['dodici']
        if ls[c-1]=='3':
            ls1+=['tredici']
        if ls[c-1]=='4':
            ls1+=['quattordici']
        if ls[c-1]=='5':
            ls1+=['quindici']
        if ls[c-1]=='6':
            ls1+=['sedici']
        if ls[c-1]=='7':
            ls1+=['diciassette']
        if ls[c-1]=='8':
            ls1+=['diciotto']
        if ls[c-1]=='9':
            ls1+=['diciannove']
    if x=='2':
        if ls[c-1]=='1' or ls[c-1]=='8':
            ls1+=['vent']
        else:
            ls1+=['venti']
    if x=='3':
        if ls[c-1]=='1' or ls[c-1]=='8':
            ls1+=['trent']
        else:
            ls1+=['trenta']
    if x=='4':
        if ls[c-1]=='1' or ls[c-1]=='8':
            ls1+=['quarant']
        else:
            ls1+=['quaranta']
    if x=='5':
        if ls[c-1]=='1' or ls[c-1]=='8':
            ls1+=['cinquant']
        else:
            ls1+=['cinquanta']
    if x=='6':
        if ls[c-1]=='1' or ls[c-1]=='8':
            ls1+=['sessant']
        else:
            ls1+=['sessanta']
    if x=='7':
        if ls[c-1]=='1' or ls[c-1]=='8':
            ls1+=['settant']
        else:
            ls1+=['settanta']
    if x=='8':
        if ls[c-1]=='1' or ls[c-1]=='8':
            ls1+=['ottant']
        else:
            ls1+=['ottanta']
    if x=='9':
        if ls[c-1]=='1' or ls[c-1]=='8':
            ls1+=['novant']
        else:
            ls1+=['novanta']

def centinaia (x,c,ls,ls1):
    if x=='0':
        ls1+=['']
    if x=='1':
        if ls[c-1]=='8':
            ls1+=['cent']
        else:
            ls1+=['cento']
    if x=='2':
        if ls[c-1]=='8':
            ls1+=['duecent']
        else:
            ls1+=['duecento']
    if x=='3':
        if ls[c-1]=='8':
            ls1+=['trecent']
        else:
            ls1+=['trecento']
    if x=='4':
        if ls[c-1]=='8':
            ls1+=['quattrocent']
        else:
            ls1+=['quattrocento']
    if x=='5':
        if ls[c-1]=='8':
            ls1+=['cinquecent']
        else:
            ls1+=['cinquecento']
    if x=='6':
        if ls[c-1]=='8':
            ls1+=['seicent']
        else:
            ls1+=['seicento']
    if x=='7':
        if ls[c-1]=='8':
            ls1+=['settecent']
        else:
            ls1+=['settecento']
    if x=='8':
        if ls[c-1]=='8':
            ls1+=['ottocent']
        else:
            ls1+=['ottocento']
    if x=='9':
        if ls[c-1]=='8':
            ls1+=['novecent']
        else:
            ls1+=['novecento']
                    
def unitelse (x,c,ls,ls1):
    if x=='1' and (ls[c+1]!='0' or ls[c+2]!='0'):
        ls1+=['uno']
    if x=='2':
        ls1+=['due']
    if x=='3':
        ls1+=['tre']
    if x=='4':
        ls1+=['quattro']
    if x=='5':
        ls1+=['cinque']
    if x=='6':
        ls1+=['sei']
    if x=='7':
        ls1+=['sette']
    if x=='8':
        ls1+=['otto']
    if x=='9':
        ls1+=['nove']
                    
def unit (x,c,ls,ls1):
    if x=='0' or ls[c+1]=='1':
        ls1+=['']
    else:
        if x=='1':
            ls1+=['uno']
        if x=='2':
            ls1+=['due']
        if x=='3':
            ls1+=['tre']
        if x=='4':
            ls1+=['quattro']
        if x=='5':
            ls1+=['cinque']
        if x=='6':
            ls1+=['sei']
        if x=='7':
            ls1+=['sette']
        if x=='8':
            ls1+=['otto']
        if x=='9':
            ls1+=['nove']
                    
def conv(n):
    'Scrivete qui il codice della funzione'
    s=str(n)
    i=len(s)
    lsa=list(s)
    while i<12:
        lsa[0:0]='0'
        s=''.join(lsa)
        i=len(s)
    c=0
    ls=[]
    ls1=[]
    for x in s:
        ls+=[s[i-1-c]]
        c+=1
    c=0
    for x in ls:
        if c==0:
            unit(x,c,ls,ls1)
        if c==1:
            decine(x,c,ls,ls1)
        if c==2:
            centinaia (x,c,ls,ls1)
        if c==3:
            if x=='1' and ls[c+1]=='0' and ls[c+2]=='0':
                ls1+=['mille']
            else:
                if x!='0' or ls[c+1]!='0' or ls[c+2]!='0':
                    ls1+=['mila']
            if x=='0' or ls[c+1]=='1':
                ls1+=['']
            else:
                unitelse (x,c,ls,ls1)
        if c==4:
            decine(x,c,ls,ls1)
        if c==5:
            centinaia (x,c,ls,ls1)
        if c==6:
            if x=='0' and ls[c+1]=='0' and ls[c+1]=='0':
                ls1+=['']
            else:
                if x=='1' and ls[c+1]=='0' and ls[c+2]=='0':
                    ls1+=['unmilione']
                else:
                    ls1+=['milioni']
            if x=='0' or ls[c+1]=='1':
                ls1+=['']
            else:
                unitelse (x,c,ls,ls1)
        if c==7:
            decine(x,c,ls,ls1)
        if c==8:
            centinaia (x,c,ls,ls1)
        if c==9:
            if x=='0' and ls[c+1]=='0' and ls[c+1]=='0':
                ls1+=['']
            else:
                if x=='1' and ls[c+1]=='0' and ls[c+2]=='0':
                    ls1+=['unmiliardo']
                else:
                    ls1+=['miliardi']
            if x=='0' or ls[c+1]=='1':
                ls1+=['']
            else:
                unitelse (x,c,ls,ls1)
        if c==10:
            decine(x,c,ls,ls1)
        if c==11:
            centinaia (x,c,ls,ls1)
        c+=1
    ls1.reverse()
    return ''.join(ls1)
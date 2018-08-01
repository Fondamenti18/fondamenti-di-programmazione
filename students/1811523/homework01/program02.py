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
    if n>=1000000000000:
        return "numero troppo grande!"
    elif n<=0:
        return "numero troppo piccolo!"
    n=str(n)
    m=len(n)
    l=len(n)
    c=0
    d=False
    k=''
    while c<=m:
        if l==12 or l==9 or l==6 or l==3:
            if n[c+1]=='8':
                if(n[c])=='9':
                    k=k+'novecent'
                if(n[c])=='8':
                    k=k+'ottocent'
                if(n[c])=='7':
                    k=k+'settecent'
                if(n[c])=='6':
                    k=k+'seicent' 
                if(n[c])=='5':
                    k=k+'cinquecent'
                if(n[c])=='4':
                    k=k+'quattrocent'
                if(n[c])=='3':
                    k=k+'trecent' 
                if(n[c])=='2':
                    k=k+'duecent'
                if(n[c])=='1':
                    k=k+'cent'
                if(n[c]=='0'):
                    k=k+''
            else:
                if(n[c])=='9':
                    k=k+'novecento'
                if(n[c])=='8':
                    k=k+'ottocento'
                if(n[c])=='7':
                    k=k+'settecento'
                if(n[c])=='6':
                    k=k+'seicento'  
                if(n[c])=='5':
                    k=k+'cinquecento'
                if(n[c])=='4':
                    k=k+'quattrocento'
                if(n[c])=='3':
                    k=k+'trecento' 
                if(n[c])=='2':
                    k=k+'duecento'
                if(n[c])=='1':
                    k=k+'cento'
        if l==11 or l==8 or l==5 or l==2:
            if (n[c+1]=='0') or (n[c+1]=='9'):
                if(n[c])=='9':
                    k=k+'novanta'
                if(n[c])=='8':
                    k=k+'ottanta'
                if(n[c])=='7':
                    k=k+'settanta'
                if(n[c])=='6':
                    k=k+'sessanta' 
                if(n[c])=='5':
                    k=k+'cinquanta'
                if(n[c])=='4':
                    k=k+'quaranta'
                if(n[c])=='3':
                    k=k+'trenta'
                if(n[c])=='2':
                    k=k+'venti'
                if(n[c])=='1':
                    d=True
                if(n[c]=='0'):
                    k=k+''
            else:
                if(n[c])=='9':
                    k=k+'novant'
                if(n[c])=='8':
                    k=k+'ottant'
                if(n[c])=='7':
                    k=k+'settant'
                if(n[c])=='6':
                    k=k+'sessant'   
                if(n[c])=='5':
                    k=k+'cinquant'
                if(n[c])=='4':
                    k=k+'quarant'
                if(n[c])=='3':
                    k=k+'trent'   
                if(n[c])=='2':
                    k=k+'vent'
                if(n[c])=='1':
                    d=True
                if(n[c]=='0'):
                    k=k+''
        if l==10 or l==7 or l==4 or l==1:
            if d==True:
                if(n[c])=='0':
                    k=k+'dieci'
                if(n[c])=='1':
                    k=k+'undici'
                if(n[c])=='2':
                    k=k+'dodici'
                if(n[c])=='3':
                    k=k+'tredici'
                if(n[c])=='4':
                    k=k+'quattordici'
                if(n[c])=='5':
                    k=k+'quindici'
                if(n[c])=='6':
                    k=k+'sedici'
                if(n[c])=='7':
                    k=k+'diciassette'
                if(n[c])=='8':
                    k=k+'diciotto'
                if(n[c])=='9':
                    k=k+'diciannove'
                if l==4:
                    k=k+'mila'
                elif l==7:
                    k=k+'milioni'
                elif l==10:
                    k=k+'miliardi'
            else:
                if(n[c])=='9':
                    if l==10:
                        k=k+'novemiliardi'
                    elif l==7:
                        k=k+'novemilioni'
                    elif l==4:
                        k=k+'novemila'
                    elif l==1:
                        k=k+'nove'
                if(n[c])=='8':
                    if l==10:
                        k=k+'ottomiliardi'
                    elif l==7:
                        k=k+'ottomilioni'
                    elif l==4:
                        k=k+'ottomila'
                    elif l==1:
                        k=k+'otto'
                if(n[c])=='7':
                    if l==10:
                        k=k+'settemiliardi'
                    elif l==7:
                        k=k+'settemilioni'
                    elif l==4:
                        k=k+'settemila'
                    elif l==1:
                        k=k+'sette'
                if(n[c])=='6':
                    if l==10:
                        k=k+'seimiliardi'
                    elif l==7:
                        k=k+'seimilioni'
                    elif l==4:
                        k=k+'seimila'   
                    elif l==1:
                        k=k+'sei'
                if(n[c])=='5':
                    if l==10:
                        k=k+'cinquemiliardi'
                    elif l==7:
                        k=k+'cinquemilioni'
                    elif l==4:
                        k=k+'cinquemila'
                    elif l==1:
                        k=k+'cinque'
                if(n[c])=='4':
                    if l==10:
                        k=k+'quattromiliardi'
                    elif l==7:
                        k=k+'quattromilioni'
                    elif l==4:
                        k=k+'quattromila'
                    elif l==1:
                        k=k+'quattro'
                if(n[c])=='3':
                    if l==10:
                        k=k+'tremiliardi'
                    elif l==7:
                        k=k+'tremilioni'
                    elif l==4:
                        k=k+'tremila'
                    elif l==1:
                        k=k+'tre'
                if(n[c])=='2':
                    if l==10:
                        k=k+'duemiliardi'
                    elif l==7:
                        k=k+'duemilioni'
                    elif l==4:
                        k=k+'duemila'
                    elif l==1:
                        k=k+'due'
                if(n[c]=='0'):
                    if l==4:
                        k=k+'mila'
                    elif l==7:
                        k=k+'milioni'
                    elif l==10:
                        k=k+'miliardi'
            if(n[c])=='1'and d==False:
                if l==10:
                    if c>1:
                        if(n[c-1]=='0'and n[c-2]=='0'):
                            k=k+'unmiliardo'
                        else:
                            k=k+'unomiliardi'
                    elif c==1:
                        if n[c-1]=='0':
                            k=k+'unmiliardo'
                        else:
                            k=k+'unomiliardi'
                    elif c==0:
                        k=k+'unmiliardo'
                elif l==7:
                    if c>1:
                        if(n[c-1]=='0'and n[c-2]=='0'):
                            k=k+'unmilione'
                        else:
                            k=k+'unomilioni'
                    elif c==1:
                        if n[c-1]=='0':
                            k=k+'unmilione'
                        else:
                            k=k+'unomilioni'
                    elif c==0:
                        k=k+'unmilione'
                elif l==4:
                    if c>1:
                        if(n[c-1]=='0'and n[c-2]=='0'):
                            k=k+'mille'
                        else:
                            k=k+'unomila'
                    elif c==1:
                        if n[c-1]=='0':
                            k=k+'mille'
                        else:
                            k=k+'unomila'
                    elif c==0:
                        k=k+'mille'
                elif l==1:
                    k=k+'uno'
            
            d=False
        l-=1
        c+=1
    return k
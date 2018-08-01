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


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1 000 000 000 000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def conv(n):
    s = str(n)
       
    
    conv_U ={
         '0':"",
         '1':"uno",
         '2':"due",
         '3':"tre",
         '4':"quattro",
         '5':"cinque",
         '6':"sei",
         '7':"sette",
         '8':"otto",
         '9':"nove",
         }
    
    conv_D ={
            '0':"",
            '1':"dieci",
            '2':"venti",
            '3':"trenta",
            '4':"quaranta",
            '5':"cinquanta",
            '6':"sessanta",
            '7':"settanta",
            '8':"ottanta",
            '9':"novanta",
            }
       
    conv_DU ={
             '0':"dieci",
             '1':"undici",
             '2':"dodici",
             '3':"tredici",
             '4':"quattordici",
             '5':"quindici",
             '6':"sedici",
             '7':"diciassette",
             '8':"diciotto",
             '9':"diciannove",
            }
    

    def miliardi(G):
         if G[-12:-9]=='000' or len(G)<10:
            return milioni(G[-9:])
         elif G[-12:-9]=='001' or len(G)==10 and G[0]=='1': 
             return "unmiliardo" + milioni(G[-9:])
         else:
             return centinaia(G[-12:-9]) + "miliardi" + milioni(G[-9:])
       
    
    def milioni(M):
         if M[-9:-6]=='000' or len(M)<7:
            return migliaia(M[-6:])
         elif M[-9:-6]=='001' or len(M)==7 and M[0]=='1': 
             return "unmilione" + migliaia(M[-6:])
         else:
             return centinaia(M[-9:-6]) + "milioni" + migliaia(M[-6:])

    
    def migliaia(m):
        if len(m)<4 or m[-6:-3]=='000':
            return centinaia(m[-3:]) 
        elif len(m)==4 and m[0]=='1' or m[-6:-3]=='001':
            return "mille" + centinaia(m[-3:]) 
        else:
            return centinaia(m[:-3]) + "mila" + centinaia(m[-3:]) 
      
    def centinaia(c): 
        if len(c)!=3 or c[0]=='0':
           return decine(c[-2:])
        elif c[0]=="1":
            if c[-2]!='8':
                return "cento" + decine(c[-2:])
            else: 
                return "cent"+ decine(c[-2:])
        elif c[-2]=='8':
            return conv_U[c[-3]] + "cent" + decine(c[-2:])
        else:
            return conv_U[c[-3]] + "cento" + decine(c[-2:])
        
    def decine(d):
        if len(d)!=2 or d[-2]=='0':
            return unita(d[-1])
        if d[-2]=='1':
            return conv_DU[d[-1]]
        elif d[-1]=='1' or d[-1]=='8':
            temp = list(conv_D[d[-2]])
            temp.pop()
            return  "".join(temp) + unita(d[-1])
        else:
            return conv_D[d[-2]] + unita(d[-1])
        
    def unita(u): 
            return conv_U[u]
    
    
    #converts numbers based on the number of digits
    def switch_digits(l):
        if l==12: return miliardi(s)
        elif l==11: return miliardi(s)
        elif l==10: return miliardi(s)
        elif l==9: return milioni(s)
        elif l==8: return milioni(s)
        elif l==7: return milioni(s)
        elif l==6: return migliaia(s)
        elif l==5: return migliaia(s)
        elif l==4: return migliaia(s)
        elif l==3: return centinaia(s)
        elif l==2: return decine(s)
        elif l==1: return unita(s)
            
    
 
    return switch_digits(len(s))



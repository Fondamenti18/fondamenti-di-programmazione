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


def convert(n):
        n=str(n)
        non_eli={'0':'','2':'venti','3':'trenta','4':'quaranta','5':'cinquanta','6':'sessanta','7':'settanta','8':'ottanta','9':'novanta'}
        lett_num={'0':'','1':'uno', '2':'due', '3':'tre', '4':'quattro','5':'cinque','6':'sei','7':'sette','8':'otto','9':'nove','10':'dieci','11':'undici','12':'dodici','13':'tredici','14':'quattordici','15':'quindici','16':'sedici','17':'diciassette','18':'diciotto','19':'dicianove'}
        if n in lett_num:
                return lett_num[n]
        if len(n)==2:
                if n[1]!='1' and n[1]!='8':
                        return non_eli[n[0]]+lett_num[n[1]]
                else:
                        return non_eli[n[0]][:-1]+lett_num[n[1]]

        if len(n)==3:
                if n[0]=='1':
                        if n[1]=='8':
                                if n[2]!='1' and n[2]!='8':
                                        return 'cent'+non_eli[n[1]]+lett_num[n[2]]
                                else:
                                        return 'cent'+non_eli[n[1]][:-1]+lett_num[n[2]]
                        if n[1:] in lett_num:
                                return 'cento'+lett_num[n[1:]]
                        else:
                                if n[2]!='1' and n[2]!='8':
                                        return 'cento'+non_eli[n[1]]+lett_num[n[2]]
                                else:
                                        return 'cento'+non_eli[n[1]][:-1]+lett_num[n[2]]
                else:
                        if n[1]=='8':
                                if n[2]!='1' and n[2]!='8':
                                        return lett_num[n[0]]+'cent'+non_eli[n[1]]+lett_num[n[2]]
                                else:
                                        return lett_num[n[0]]+'cent'+non_eli[n[1]][:-1]+lett_num[n[2]]

                        if n[1:] in lett_num:
                                return lett_num[n[0]]+'cento'+lett_num[n[1:]]
                            
                        else:
                                if n[2]!='1' and n[2]!='8':
                                        return lett_num[n[0]]+'cento'+non_eli[n[1]]+lett_num[n[2]]
                                else:
                                        return lett_num[n[0]]+'cento'+non_eli[n[1]][:-1]+lett_num[n[2]]

def conv(n):
        n=str(n)

#CENTO       
        if len(n)<=3:
                return convert(int(n))


#MILLE       
        if 4<=len(n)<=6:
                if len(n)==4:
                    if n[0]=='1':
                        return 'mille'+convert(int(n[len(n)-3:]))
                    else:
                        return convert(int(n[:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))
                else:
                    return convert(int(n[:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))




#MILIONE
                
        if 7<=len(n)<=9:
                if len(n)==7:
                        if n[0]=='1':
                                if n[1]=='0' and n[2]=='0':
                                        if n[3]=='0':
                                                return 'un'+'milione'+convert(int(n[len(n)-3:]))
                                        if n[3]=='1':
                                                return 'un'+'milione'+'mille'+convert(int(n[len(n)-3:]))
                                        else:
                                                return 'un'+'milione'+convert(int(n[len(n)-4:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))
                                else:
                                        return 'un'+'milione'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))
                                 
        
                        else:
                                if n[1]=='0' and n[2]=='0':
                                        if n[3]=='0':
                                                return convert(int(n[:len(n)-6]))+'milioni'+convert(int(n[len(n)-3:]))
                                        if n[3]=='1':
                                                return convert(int(n[:len(n)-6]))+'milioni'+'mille'+convert(int(n[len(n)-3:]))
                                        else:
                                                return convert(int(n[:len(n)-6]))+'milioni'+convert(int(n[len(n)-4:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))
                                else:
                                        return convert(int(n[:len(n)-6]))+'milioni'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))

                if len(n)==8:
                        if n[2]=='0' and n[3]=='0':
                                if n[4]=='0':
                                        return convert(int(n[:len(n)-6]))+'milioni'+convert(int(n[len(n)-3:]))
                                if n[4]=='1':
                                        return convert(int(n[:len(n)-6]))+'milioni'+'mille'+convert(int(n[len(n)-3:]))
                                else:
                                        return convert(int(n[:len(n)-6]))+'milioni'+convert(int(n[len(n)-4:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))                         
                        else:
                                return convert(int(n[:len(n)-6]))+'milioni'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))


                if len(n)==9:
                        if n[3]=='0' and n[4]=='0':
                                if n[5]=='0':
                                        return convert(int(n[:len(n)-6]))+'milioni'+convert(int(n[len(n)-3:]))
                                if n[5]=='1':
                                        return convert(int(n[:len(n)-6]))+'milioni'+'mille'+convert(int(n[len(n)-3:]))
                                else:
                                        return convert(int(n[:len(n)-6]))+'milioni'+convert(int(n[len(n)-4:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))
                        else:
                                return convert(int(n[:len(n)-6]))+'milioni'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))



                        

#MILIARDO                                 

        
        if 10<=len(n)<=12:


                
                    if len(n)==10:
                        if n[0]=='1': 
                            if n[3]=='1':
                                if n[4]=='0' and n[5]=='0':
                                    if n[6]=='0':
                                            return 'un'+'miliardo'+'e'+'un'+'milione'+convert(int(n[len(n)-3:]))
                                    if n[6]=='1':
                                            return 'un'+'miliardo'+'e'+'un'+'milione'+'mille'+convert(int(n[len(n)-3:]))
                                    else:
                                            return 'un'+'miliardo'+'e'+'un'+'milione'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))


                            if n[1]=='0' and n[2]=='0' and n[3]=='0':
                                if n[4]=='0' and n[5]=='0':
                                    if n[6]=='0':
                                        return 'un'+'miliardo'+convert(int(n[len(n)-3:]))
                                    if n[6]=='1':
                                        return 'un'+'miliardo'+'mille'+convert(int(n[len(n)-3:]))
                                    else:
                                        return 'un'+'miliardo'+convert(int(n[len(n)-4:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))
                                else:
                                    return 'un'+'miliardo'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))   
                                        
                                
                            else:
                                    if n[4]=='0' and n[5]=='0':
                                            if n[6]=='0':
                                                    return 'un'+'miliardo'+convert(int(n[len(n)-9:len(n)-6]))+'milioni'+convert(int(n[len(n)-3:]))
                                            if n[6]=='1':
                                                    return 'un'+'miliardo'+convert(int(n[len(n)-9:len(n)-6]))+'milioni'+'mille'+convert(int(n[len(n)-3:]))
                                            else:
                                                    return 'un'+'miliardo'+convert(int(n[len(n)-9:len(n)-6]))+'milioni'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))
                                    else:
                                        return 'un'+'miliardo'+convert(int(n[len(n)-9:len(n)-6]))+'milioni'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))


                                                
                        else:
                            if n[3]=='1':
                                if n[1]=='0' and n[2]=='0':
                                    if n[4]=='0' and n[5]=='0':
                                        if n[6]=='0':
                                                return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+convert(int(n[len(n)-3:]))
                                        if n[6]=='1':
                                                return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+'mille'+convert(int(n[len(n)-3:]))
                                        else:
                                                return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))

                                    else:
                                        return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))


                                else:
                                    return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-9:len(n)-6]))+'milioni'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))
                            


                            if n[3]=='0':
                                if n[1]=='0' and n[2]=='0':
                                    if n[4]=='0' and n[5]=='0':
                                        if n[6]=='0':
                                            return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-3:]))
                                        if n[6]=='1':
                                            return convert(int(n[:len(n)-9]))+'miliardi'+'mille'+convert(int(n[len(n)-3:]))
                                        else:
                                            return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))

                            else:
                                return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-9:len(n)-6]))+'milioni'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))









                    if len(n)==11:
                        if n[2]=='0' and n[3]=='0' and n[4]=='0':
                                if n[5]=='0' and n[6]=='0':
                                        if n[7]=='0':
                                                return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-3:]))
                                        if n[7]=='1':
                                                return convert(int(n[:len(n)-9]))+'miliardi'+'mille'+convert(int(n[len(n)-3:]))
                                        else:
                                                return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-4:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))
                                else:
                                        return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))

                        if n[2]=='0' and n[3]=='0' and n[4]=='1':
                                if n[5]=='0' and n[6]=='0':
                                        if n[7]=='1':
                                                return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+'mille'+convert(int(n[len(n)-3:]))
                                        if n[7]=='0':
                                                return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+convert(int(n[len(n)-3:]))
                                        else:
                                                return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))        
                                else:
                                        return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))

                        else:
                                return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-9:len(n)-6]))+'milioni'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))





                    if len(n)==12:
                            if n[3]=='0' and n[4]=='0' and n[5]=='0':
                                if n[6]=='0' and n[7]=='0':
                                        if n[8]=='0':
                                                return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-3:]))
                                        if n[8]=='1':
                                                return convert(int(n[:len(n)-9]))+'miliardi'+'mille'+convert(int(n[len(n)-3:]))
                                        else:
                                                return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-4:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))
                                else:
                                        return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))

                            if n[3]=='0' and n[4]=='0' and n[5]=='1':
                                if n[6]=='0' and n[7]=='0':
                                        if n[8]=='1':
                                                return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+'mille'+convert(int(n[len(n)-3:]))
                                        if n[8]=='0':
                                                return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+convert(int(n[len(n)-3:]))
                                        else:
                                                return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))        
                                else:
                                        return convert(int(n[:len(n)-9]))+'miliardi'+'e'+'un'+'milione'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:]))

                            else:
                                return convert(int(n[:len(n)-9]))+'miliardi'+convert(int(n[len(n)-9:len(n)-6]))+'milioni'+convert(int(n[len(n)-6:len(n)-3]))+'mila'+convert(int(n[len(n)-3:])) 














d={'0':'', '2':'due', '3':'tre', '4':'quattro', '5':'cinque', '6':'sei', '7':'sette', '8':'otto', '9':'nove'}    
    
def fino_a_99(n):    
    numero=''
    n='   '+str(n)
    pos=len(n)-1
    d1={'0':'', '1':'uno', '2':'due', '3':'tre', '4':'quattro', '5':'cinque', '6':'sei', '7':'sette', '8':'otto', '9':'nove', '10':'dieci', '11':'undici', '12':'dodici', '13':'tredici', '14':'quattordici', '15':'quindici', '16':'sedici', '17':'diciassette', '18':'diciotto', '19':'dicannove'}
    d2={'0':'', '1':'dieci', '2':'venti', '3':'trenta', '4':'quaranta', '5':'cinquanta', '6':'sessanta', '7':'settanta', '8':'ottanta', '9':'novanta'}
    
    while pos>=3:
        if pos==len(n)-1 and n[len(n)-2]!='1':
            numero=numero+d1[n[pos]]
            pos=pos-1
        elif pos==len(n)-2 and n[pos]=='1':
            numero=d1[n[pos]+n[pos+1]]
            pos=pos-1
        elif pos==len(n)-2 and n[pos]!='1':
            if n[len(n)-1]!='1' and n[len(n)-1]!='8':
                numero=d2[n[pos]]+numero
                pos=pos-1
            else:
                if n[len(n)-1]=='1':
                    numero=d2[n[pos]][:len(d2[n[pos]])-1]+'uno'
                    pos=pos-1
                elif n[len(n)-1]=='8':
                    numero=d2[n[pos]][:len(d2[n[pos]])-1]+'otto'
                    pos=pos-1
        else:
            pos=pos-1
    return(numero)
                    
def fino_a_999(n2,numero):
    
    if numero[0:6]!='ottant':
        if n2=='1':
            numero='cento'+numero
        elif n2=='0':
            numero=''+numero
        else:
            numero=d[n2]+'cento'+numero
        
    else:
        if n2=='1':
            numero='cent'+numero
        elif n2=='0':
            numero=''+numero
        else:
            numero=d[n2]+'cent'+numero
        
    return numero    

def fino_a_999999(n3,numero):
    
    if len(n3)==3:
        if n3=='000':
            numero=''+numero
        else:
            n4=n3[1:3]
            numero1=fino_a_99(n4)
            n5=n3[0]
            numero1=fino_a_999(n5,numero1)
            numero=numero1+'mila'+numero
    elif len(n3)==2:
        numero1=fino_a_99(n3)
        numero=numero1+'mila'+numero
    elif len(n3)==1:
        if n3=='1':
            numero='mille'+numero
        else:
            numero=d[n3]+'mila'+numero
    return numero

def fino_a_999999999(n6,numero):
    
    if len(n6)==3:
        if n6=='000':
            numero=''+numero
        else:
            n7=n6[1:3]
            numero1=fino_a_99(n7)
            n8=n6[0]
            numero1=fino_a_999(n8,numero1)
            numero=numero1+'milioni'+numero
    elif len(n6)==2:
        numero1=fino_a_99(n6)
        numero=numero1+'milioni'+numero
    elif len(n6)==1:
        if n6=='1':
            numero='unmilione'+numero
        else:
            numero=d[n6]+'milioni'+numero
    return numero
    
def fino_a_999999999999(n9,numero):
    
    if len(n9)==3:
        if n9=='000':
            numero=''+numero
        else:
            n10=n9[1:3]
            numero1=fino_a_99(n10)
            n11=n9[0]
            numero1=fino_a_999(n11,numero1)
            numero=numero1+'miliardi'+numero
    elif len(n9)==2:
        numero1=fino_a_99(n9)
        numero=numero1+'miliardi'+numero
    elif len(n9)==1:
        if n9=='1':
            numero='unmiliardo'+numero
        else:
            numero=d[n9]+'miliardi'+numero
    return numero        
    
def conv(n):
    n=str(n)
    n1=n[len(n)-2:len(n)]
    numero=fino_a_99(n1)
    if len(n)<=2:
        return numero
    
    n2=n[-3]
    
    numero=fino_a_999(n2,numero)
    if len(n)==3:
        return numero
    if len(n)>=6:
        n3=n[-6:-3]
    elif len(n)==5:
        n3=n[-5:-3]
    elif len(n)==4:
        n3=n[-4]
    numero=fino_a_999999(n3,numero)
    if 4<=len(n)<=6:
        return numero
    if len(n)>=9:
        n6=n[-9:-6]
    elif len(n)==8:
        n6=n[-8:-6]
    elif len(n)==7:
        n6=n[-7]
    numero=fino_a_999999999(n6,numero)
    if 7<=len(n)<=9:
        return numero
    if len(n)==12:
        n9=n[-12:-9]
    elif len(n)==11:
        n9=n[-11:-9]
    elif len(n)==10:
        n9=n[-10]
    numero=fino_a_999999999999(n9,numero)
    if 10<=len(n)<=12:
        return numero

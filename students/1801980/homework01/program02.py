def unita(n):
    pre='dici'
    if n==0: return('')
    if n==1: return('uno')
    if n==2: return('due')
    if n==3: return('tre')
    if n==4: return('quattro')
    if n==5: return('cinque')
    if n==6: return('sei')
    if n==7: return('sette')
    if n==8: return('otto')
    if n==9: return('nove')
    if n==10: return('dieci')
    if n==11: return('un'+pre)
    if n==12: return('do'+pre)
    if n==13: return('tre'+pre)
    if n==14: return('quattor'+pre)
    if n==15: return('quin'+pre)
    if n==16: return('se'+pre)
    if n==17: return(pre+'assette')
    if n==18: return(pre+'otto')
    if n==19: return(pre+'nove')

def decine(n):
    num_str=str(n)
    if n<20: return (unita(n))
    if num_str[0]=='2':
        if n==21: return('ventuno')
        elif n==28: return('ventotto')
        elif n==20: return('venti')
        else: return ('venti'+ unita(n-20))
    if num_str[0]=='3':
        if n==31: return('trentuno')
        elif n==38: return('trentotto')
        else: return ('trenta' + unita(n-30))
    if num_str[0]=='4':
        if n==41: return('quarantuno')
        elif n==48: return('quarantotto')
        else: return ('quaranta' + unita(n-40))
    if num_str[0]=='5':
        if n==51: return('cinquantuno')
        elif n==58: return('cinquantotto')
        else: return('cinquanta'+ unita(n-50))
    if num_str[0]=='6':
        if n==61: return('sessantuno')
        elif n==68: return('sessantotto')
        else: return ('sessanta'+ unita(n-60))
    if num_str[0]=='7':
        if n==71: return('settantuno')
        elif n==78: return('settantotto')
        else: return (str('settanta' + unita(n-70)))
    if num_str[0]=='8':
        if n==81: return('ottantuno')
        elif n==88: return('ottantotto')
        else: return ('ottanta' + unita(n-80))
    if num_str[0]=='9':
        if n==91: return('novantuno')
        elif n==98: return('novantotto')
        else: return ('novanta'+ unita(n-90))

def centinaia(n):
    num_str=str(n)
    x=''
    if n<100: return (decine(n))
    if num_str[1]!='8':
        x ='o'
    if num_str[0]=='1': return('cent'+ x + decine(n-100))
    if num_str[0]=='2': return('duecent'+ x + decine(n-200))
    if num_str[0]=='3': return('trecent'+ x + decine(n-300))
    if num_str[0]=='4': return('quattrocent'+ x + decine(n-400))
    if num_str[0]=='5': return('cinquecent'+ x + decine(n-500))
    if num_str[0]=='6': return('seicent'+ x + decine(n-600))
    if num_str[0]=='7': return('settecent'+ x + decine(n-700))
    if num_str[0]=='8': return('ottocent'+ x + decine(n-800))
    if num_str[0]=='9': return('novecent'+ x + decine(n-900))

def migliaia(n):
    num_str=str(n)
    if n<1000: return(centinaia(n))
    if num_str[0]=='1': return('mille' + centinaia(n-1000))
    if num_str[0]=='2': return('duemila' + centinaia(n-2000))
    if num_str[0]=='3': return('tremila' + centinaia(n-3000))
    if num_str[0]=='4': return('quattromila'+ centinaia(n-4000))
    if num_str[0]=='5': return('cinquemila'+ centinaia(n-5000))
    if num_str[0]=='6': return('seimila'+ centinaia(n-6000))
    if num_str[0]=='7': return('settemila'+ centinaia(n-7000))
    if num_str[0]=='8': return('ottomila'+ centinaia(n-8000))
    if num_str[0]=='9': return('novemila'+ centinaia(n-9000))
    

def decine_migliaia(n):
    num_str=str(n)
    if n<10000: return(migliaia(n))
    if num_str[0]=='1': return(unita(int(num_str[0]+num_str[1]))+'mila'+ migliaia(n-(int(num_str[0]+num_str[1]))*1000))
    if num_str[0]=='2': return(decine(int(num_str[0]+num_str[1]))+'mila'+ migliaia(n-(int(num_str[0]+num_str[1]))*1000))
    if num_str[0]=='3': return(decine(int(num_str[0]+num_str[1]))+'mila'+ migliaia(n-(int(num_str[0]+num_str[1]))*1000))
    if num_str[0]=='4': return(decine(int(num_str[0]+num_str[1]))+'mila'+ migliaia(n-(int(num_str[0]+num_str[1]))*1000))
    if num_str[0]=='5': return(decine(int(num_str[0]+num_str[1]))+'mila'+ migliaia(n-(int(num_str[0]+num_str[1]))*1000))
    if num_str[0]=='6': return(decine(int(num_str[0]+num_str[1]))+'mila'+ migliaia(n-(int(num_str[0]+num_str[1]))*1000))
    if num_str[0]=='7': return(decine(int(num_str[0]+num_str[1]))+'mila'+ migliaia(n-(int(num_str[0]+num_str[1]))*1000))
    if num_str[0]=='8': return(decine(int(num_str[0]+num_str[1]))+'mila'+ migliaia(n-(int(num_str[0]+num_str[1]))*1000))
    if num_str[0]=='9': return(decine(int(num_str[0]+num_str[1]))+'mila' + migliaia(n-(int(num_str[0]+num_str[1]))*1000))

def centinaia_migliaia(n):
    num_str=str(n)
    if n<100000: return(decine_migliaia(n))
    if num_str[0]=='1': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'mila'+decine_migliaia(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000))
    if num_str[0]=='2': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'mila'+decine_migliaia(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000))
    if num_str[0]=='3': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'mila'+decine_migliaia(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000))
    if num_str[0]=='4': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'mila'+decine_migliaia(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000))
    if num_str[0]=='5': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'mila'+decine_migliaia(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000))
    if num_str[0]=='6': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'mila'+decine_migliaia(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000))
    if num_str[0]=='7': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'mila'+decine_migliaia(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000))
    if num_str[0]=='8': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'mila'+decine_migliaia(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000))
    if num_str[0]=='9': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'mila'+decine_migliaia(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000))

def milione(n):
    num_str=str(n)
    if n<1000000: return (centinaia_migliaia(n))
    if num_str[0]=='1': return('unmilione'+ centinaia_migliaia(n-1000000))
    if num_str[0]=='2': return('duemilioni'+ centinaia_migliaia(n-2000000))
    if num_str[0]=='3': return('tremilioni'+ centinaia_migliaia(n-3000000))
    if num_str[0]=='4': return('quattromilioni'+ centinaia_migliaia(n-4000000))
    if num_str[0]=='5': return('cinquemilioni'+ centinaia_migliaia(n-5000000))
    if num_str[0]=='6': return('seimilioni'+ centinaia_migliaia(n-6000000))
    if num_str[0]=='7': return('settemilioni'+ centinaia_migliaia(n-7000000))
    if num_str[0]=='8': return('ottomilioni'+ centinaia_migliaia(n-8000000))
    if num_str[0]=='9': return('novemilioni'+ centinaia_migliaia(n-9000000))

def decine_milioni(n):
    num_str=str(n)
    if n<10000000: return (milione(n))
    if num_str[0]=='1': return(unita(int(num_str[0]+num_str[1]))+'milioni'+ milione(n-(int(num_str[0]+num_str[1]))*1000000))
    if num_str[0]=='2': return(decine(int(num_str[0]+num_str[1]))+'milioni'+ milione(n-(int(num_str[0]+num_str[1]))*1000000))
    if num_str[0]=='3': return(decine(int(num_str[0]+num_str[1]))+'milioni'+ milione(n-(int(num_str[0]+num_str[1]))*1000000))
    if num_str[0]=='4': return(decine(int(num_str[0]+num_str[1]))+'milioni'+ milione(n-(int(num_str[0]+num_str[1]))*1000000))
    if num_str[0]=='5': return(decine(int(num_str[0]+num_str[1]))+'milioni'+ milione(n-(int(num_str[0]+num_str[1]))*1000000))
    if num_str[0]=='6': return(decine(int(num_str[0]+num_str[1]))+'milioni'+ milione(n-(int(num_str[0]+num_str[1]))*1000000))
    if num_str[0]=='7': return(decine(int(num_str[0]+num_str[1]))+'milioni'+ milione(n-(int(num_str[0]+num_str[1]))*1000000))
    if num_str[0]=='8': return(decine(int(num_str[0]+num_str[1]))+'milioni'+ milione(n-(int(num_str[0]+num_str[1]))*1000000))
    if num_str[0]=='9': return(decine(int(num_str[0]+num_str[1]))+'milioni'+ milione(n-(int(num_str[0]+num_str[1]))*1000000))

def centinaia_milioni(n):
    num_str= str(n)
    if n<100000000: return (decine_milioni(n))
    if num_str[0]=='1': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'milioni'+decine_milioni(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000))
    if num_str[0]=='2': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'milioni'+decine_milioni(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000))
    if num_str[0]=='3': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'milioni'+decine_milioni(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000))
    if num_str[0]=='4': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'milioni'+decine_milioni(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000))
    if num_str[0]=='5': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'milioni'+decine_milioni(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000))
    if num_str[0]=='6': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'milioni'+decine_milioni(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000))
    if num_str[0]=='7': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'milioni'+decine_milioni(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000))
    if num_str[0]=='8': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'milioni'+decine_milioni(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000))
    if num_str[0]=='9': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'milioni'+decine_milioni(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000))

def miliardi(n):
    pre='miliardi'
    num_str=str(n)
    if n<1000000000: return (centinaia_milioni(n))
    if num_str[0]=='1': return('unmiliardo'+centinaia_milioni(n-1000000000))
    if num_str[0]=='2': return('due'+pre+ centinaia_milioni(n-2000000000))
    if num_str[0]=='3': return('tre'+pre+ centinaia_milioni(n-3000000000))
    if num_str[0]=='4': return('quattro'+pre+ centinaia_milioni(n-4000000000))
    if num_str[0]=='5': return('cinque'+pre+ centinaia_milioni(n-5000000000))
    if num_str[0]=='6': return('sei'+pre+centinaia_milioni(n-6000000000))
    if num_str[0]=='7': return('sette'+pre+centinaia_milioni(n-7000000000))
    if num_str[0]=='8': return('otto'+pre+centinaia_milioni(n-8000000000))
    if num_str[0]=='9': return('nove'+pre+centinaia_milioni(n-9000000000))

def decine_miliardi(n):
    num_str=str(n)
    if n<10000000000: return (miliardi(n))
    if num_str[0]=='1': return(unita(int(num_str[0]+num_str[1]))+'miliardi'+ miliardi(n-(int(num_str[0]+num_str[1]))*1000000000))
    if num_str[0]=='2': return(decine(int(num_str[0]+num_str[1]))+'miliardi'+ miliardi(n-(int(num_str[0]+num_str[1]))*1000000000))
    if num_str[0]=='3': return(decine(int(num_str[0]+num_str[1]))+'miliardi'+ miliardi(n-(int(num_str[0]+num_str[1]))*1000000000))
    if num_str[0]=='4': return(decine(int(num_str[0]+num_str[1]))+'miliardi'+ miliardi(n-(int(num_str[0]+num_str[1]))*1000000000))
    if num_str[0]=='5': return(decine(int(num_str[0]+num_str[1]))+'miliardi'+ miliardi(n-(int(num_str[0]+num_str[1]))*1000000000))
    if num_str[0]=='6': return(decine(int(num_str[0]+num_str[1]))+'miliardi'+ miliardi(n-(int(num_str[0]+num_str[1]))*1000000000))
    if num_str[0]=='7': return(decine(int(num_str[0]+num_str[1]))+'miliardi'+ miliardi(n-(int(num_str[0]+num_str[1]))*1000000000))
    if num_str[0]=='8': return(decine(int(num_str[0]+num_str[1]))+'miliardi'+ miliardi(n-(int(num_str[0]+num_str[1]))*1000000000))
    if num_str[0]=='9': return(decine(int(num_str[0]+num_str[1]))+'miliardi'+ miliardi(n-(int(num_str[0]+num_str[1]))*1000000000))

def centinaia_miliardi(n):
    num_str=str(n)
    if n<100000000000: return(decine_miliardi(n))
    if num_str[0]=='1': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'miliardi'+decine_miliardi(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000000))
    if num_str[0]=='2': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'miliardi'+decine_miliardi(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000000))
    if num_str[0]=='3': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'miliardi'+decine_miliardi(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000000))
    if num_str[0]=='4': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'miliardi'+decine_miliardi(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000000))
    if num_str[0]=='5': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'miliardi'+decine_miliardi(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000000))
    if num_str[0]=='6': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'miliardi'+decine_miliardi(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000000))
    if num_str[0]=='7': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'miliardi'+decine_miliardi(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000000))
    if num_str[0]=='8': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'miliardi'+decine_miliardi(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000000))
    if num_str[0]=='9': return(centinaia(int(num_str[0]+num_str[1]+num_str[2]))+'miliardi'+decine_miliardi(n-(int(num_str[0]+num_str[1]+num_str[2]))*1000000000))
    
def conv (n):
    num_str= str(n)
    l=len(num_str)
    if l==1:return unita(n)
    elif l==2:return decine(n)
    elif l==3:return centinaia(n)
    elif l==4:return migliaia(n)
    elif l==5:return decine_migliaia(n)
    elif l==6:return centinaia_migliaia(n)
    elif l==7:return milioni(n)
    elif l==8:return decine_milioni(n)
    elif l==9:return centinaia_milioni(n)
    elif l==10:return miliardi(n)
    elif l==11:return decine_miliardi(n)
    elif l==12:return centinaia_miliardi(n)

    
    

    
    






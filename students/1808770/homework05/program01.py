def decodificatore(configurazione):
    global numbers,switch_me,copy,lista,stepAside
    if len(configurazione)==1:
        numbers,switch_me,copy,lista,stepAside=[0,1,2,3,4,5,6,7,8,9],0,0,[],[]
    l,c,n,risposta=configurazione[0],configurazione,numbers,[]
    if len(c)>1:
        a,b=c[-1][1]
        if switch_me==1:
            switch_me=0
            return lebasiproprio(l,c,n)
        if a+b==0:
            del n[-2],n[-1]
            numberOne=int(str(n[-1])+str(n[-2]))
            risposta=[int(x) if int(x)!=0 else x for x in str(numberOne*10**(l-2))]
        elif a+b==2 and len(stepAside)==0:
            lista.append(c[-1][1])
            risposta=trovanedue(c,n,lista)
        elif len(stepAside)>0:
            if 1 in c[-1][1] and 0 in c[-2][1]:
                copy=c[0]-1
            return finisci(c[-1][1],c)
        else:
            switch_me=1
            risposta=[int(x) if int(x)!=0 else x for x in str(n[-1]*10**(l-1))]
    else:
        copy=l-1
        numberOne=int(str(n[-1])+str(n[-2]))
        risposta=[int(x) if int(x)!=0 else x for x in str(numberOne*10**(l-2))]
    return risposta

def lebasiproprio(l,c,n):
    global numbers
    if c[-1][1]==(0,0):
        del n[-1]
        numberOne=int(str(n[-1])+str(n[-2]))
        risposta=[int(x) if int(x)!=0 else x for x in str(numberOne*10**(l-2))]
    elif c[-1][1] in [(1,0),(0,1)]:
        del n[-2]
        numberOne=int(str(n[-1])+str(n[-2]))
        risposta=[int(x) if int(x)!=0 else x for x in str(numberOne*10**(l-2))]
    return risposta

def trovanedue(c,n,lista):
    global copy
    if 2 in lista[0] or len(lista)==1:
        if len(lista)==1 or 2 in lista[1]:
            if len(lista)==1 or 2 in lista[-1] and 1 not in lista[-2]:
                risposta=[x if x!=n[-1] else "0" for x in c[-1][0]]
                if type(risposta[copy])==str:
                    risposta[copy]=n[-1]
                    copy-=1
                else:
                    if c[-1][0][:2].count("0")==0:
                        return finisci(c[-1][0],c)
                    risposta=[x if x!=n[-1] and x!=n[-2] else "0" for x in c[-1][0]]
                    risposta[0]=n[-2]
                    risposta[1]=n[-1]
            elif 1 in lista[-1]:
                if 2 in lista[-2]:
                    copy=c[0]-1
                risposta=[x if x!=n[-2] else "0" for x in c[-1][0]]
                if type(risposta[copy])==int:
                    copy-=1
                risposta[copy]=n[-2]
                copy-=1
            elif 2 in lista[-1] and 1 in lista[-2]:
                return finisci(c[-1][0],c)
        elif 1 in lista[1]:
            if len(lista)==2:
                copy=c[0]-1
                risposta=[x if x!=n[-1] else "0" for x in c[-1][0]]
                risposta[copy-1]=n[-1]
            elif 1 in lista[2]:
                return finisci(c[-3][0],c)
            elif 2 in lista[2]:
                if 2 in lista[-1] and len(lista)>3:
                    return finisci(c[-1][0],c)
                if len(lista)==3:
                    copy=c[0]-2
                risposta=["0" for x in c[-1][0]]
                risposta[-1]=n[-1]
                risposta[copy]=n[-2]
                copy-=1
    elif 1 in lista[0]:
        risposta=trovanedue_2(c,n,lista)
    return risposta

def trovanedue_2(c,n,lista):
    global copy
    if len(lista)==2:
        copy=c[0]-1
        if 1 in lista[1]:
            risposta=[x if x!=n[-1] else "0" for x in c[-1][0]]
            risposta[copy-1]=n[-1]
            copy-=2
        elif 2 in lista[1]:
            risposta=[x if x!=n[-1] else "0" for x in c[-2][0]]
            risposta[-2]=n[-1]
    else:
        if 1 in lista[1] and 1 in lista[2] and not (2 in lista[-1]):
            risposta=[x if x!=n[-1] else "0" for x in c[-1][0]]
            risposta[copy]=n[-1]
            copy-=1
        elif 2 in lista[1] and 2 in lista[2]:
            if len(lista)>3 and 2 in lista[-1]:
                return finisci(c[-1][0],c)
            risposta=["0" for x in c[-1][0]]
            risposta[0]=n[-1]
            risposta[copy]=n[-2]
            copy-=1
        elif 2 in lista[1] and 1 in lista[2]:
            return finisci(c[-2][0],c)
        else:
            return finisci(c[-1][0],c)
    return risposta

def finisci(base,c):
    global numbers,copy,stepAside
    n,sA=numbers,stepAside
    if len(sA)==0:
        del n[-2],n[-1]
        sA.append(base)
        risposta=sA[0]
        risposta[risposta.index("0")]=n[-1]
    elif 0 in base and base[0]+base[1]==len(c[-1][0])-c[-1][0].count("0"):
        del n[-1]
        sA=[sA[-1]]
        risposta=sA[0]
        risposta[risposta.index("0")]=n[-1]
    elif 0 in base:
        risposta=[x if x not in n else "0" for x in sA[-1]]
        del n[-1]
        risposta[risposta.index("0")]=n[-1]
    elif 1 in base:
        sA[-1][sA[-1].index(n[-1])]="0"
        risposta=sA[-1]
        for x in range(copy,-1,-1):
            if type(risposta[x])==str:
                risposta[x]=n[-1]
                copy-=1
                break
            copy-=1
    sA.append(risposta)
    return risposta





numbers,switch_me,copy,lista,stepAside=[0,1,2,3,4,5,6,7,8,9],0,0,[],[]
def div(ls):
    for i in range(len(ls)-1,-1,-1):
        if ls[i].islower()==False:    
            del(ls[i])
    return ls
def cancel(ls):
    for i in ls:
       if ls.count(i)>1:
            ls.remove(i)
    for i in ls:
       if ls.count(i)>1:
            ls.remove(i)
    return (ls)
def codifica(ls,txt):
    parola=''
    ls=list(ls)
    ls=div(ls)
    ls=cancel(ls)   
    ls1=sorted(ls)      
    ls1.append(' ')
    ls.append(' ')
    txt=list(txt) 
    for i in range(0,len(txt)):
        for x in range(0,len(ls1)):
            if txt[i]==ls1[x]:
              parola=ls[x]
            if not txt[i] in ls1:               
              parola=txt[i]  
        txt[i] = parola
    txt=''.join(txt)
    return(txt)
def decodifica(ls,txt):
    parola=''
    ls=list(ls)
    ls=div(ls)
    ls=cancel(ls)   
    ls1=sorted(ls)      
    ls1.append(' ')
    ls.append(' ')
    txt=list(txt) 
    for i in range(0,len(txt)):
        for x in range(0,len(ls1)):
            if txt[i]==ls[x]:
              parola=ls1[x]
            if not txt[i] in ls:               
              parola=txt[i]  
        txt[i] = parola
    txt=''.join(txt)
    return(txt)

def elimina(s):
    c=''
    for x in range(len(s)):
        if s[x].isalpha()==True and s[x].islower()==True:
            c+=s[x]
    return c





def ordina(st):
    ls = []
    nw_ls = []
    s=''
    for j in st:
        ls.append(j)
    ls.reverse()
    for z in ls[0:len(ls)-1]:
        if z not in nw_ls:
            nw_ls.append(z)
    nw_ls.reverse()
    return nw_ls       



def codifica(chiave,testo):
    chiave1=chiave
    t=testo
    ordina(elimina(chiave1))
    s=''
    s1=sorted(ordina(elimina(chiave1))) #lista ordinata
    s2=ordina(elimina(chiave1)) #lista disordinata
   
    lista=[]
    x=0
    y=0
   
    ls=list(t) #lista del testo
    while x<len(ls):
        y=0
        while y<len(s1):
            if ls[x]==s1[y]:
               lista.append(s2[y])
               y=len(s2)
            elif y==len(s2)-1:
                lista.append(ls[x])
                y+=1
            else:
                y+=1
        x+=1
    for z in lista:
        s+=str(z)
    return s

def decodifica(chiave,testo):
    chiave1=chiave
    t=testo
    ordina(elimina(chiave1))
    s=''
    s1=sorted(ordina(elimina(chiave1))) #lista ordinata
    s2=ordina(elimina(chiave1)) #lista disordinata
   
    lista=[]
    x=0
    y=0
   
    ls=list(t) #lista del testo
    while x<len(ls):
        y=0
        while y<len(s2):
            if ls[x]==s2[y]:
               lista.append(s1[y])
               y=len(s1)
            elif y==len(s1)-1:
                lista.append(ls[x])
                y+=1
            else:
                y+=1
        x+=1
    for z in lista:
        s+=str(z)
    return s


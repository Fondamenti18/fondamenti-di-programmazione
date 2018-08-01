def key(k,l,c,o):
    for i in range(len(k)):
        if(k[i]>='a' and k[i]<='z'):
            l+=[k[i]]
            
    l2=l[:]
    
    for i in l:     #lettere da trasformare (var in dizionario)
        a=l2.pop()
        if a not in c:
            c+=a
    
    o=c[:]      #lettere dell'alfabeto (keys in dizionario)
    o.sort()
    c.reverse()
    
    return c,o
    
def codifica(chiave, testo):
    l=[]
    c=[]
    o=[]
    d={}   #dizionario
    
    c,o=key(chiave,l,c,o)
    i=0
    for c in c:
        d[o[i]]=c
        i+=1
    txt=''
            
    for i in testo:
        if i in o:
            txt+=d[i]
        else:
            txt+=i
    
    return txt

def decodifica(chiave, testo):
    l=[]
    c=[]
    o=[]
    d={}
    
    c,o=key(chiave,l,c,o)
    
    i=0
    for o in o:
        d[c[i]]=o
        i+=1
    
    txt=''
    
    for i in testo:
        if i in c:
            txt+=d[i]
        else:
            txt+=i
    
    return txt
def post(fposts,insieme):
    f=open(fposts, encoding='utf-8')
    testo=f.read()
    f.close()
    testo=testo.replace(">"," ")    
    lparole=testo.split() 
    normalizza(lparole)
    testox=' '.join(lparole)
    lparole=testox.split()
    risultato=creains(lparole, insieme)
    return risultato

def normalizza(lparole):
    i=0
    while i<len(lparole):
        if lparole[i]!='<POST':
            parola=creap(lparole[i])
            lparole[i]=parola.lower()
        i+=1
def creains(lparole, insieme):
    risultato=set()
    i=0
    while i<len(lparole):
        if lparole[i]=='<POST':
            numpost=lparole[i+1]
            i+=2
        else:
            for x in insieme:
                if x.lower()==lparole[i]:
                    risultato.add(numpost)
            i+=1
    return risultato

def creap(iparole):
    parola=''
    for x in iparole:
        if x.isalpha() or x.isdigit():
            parola+=x
        else:
            parola+=' ' 
    return parola
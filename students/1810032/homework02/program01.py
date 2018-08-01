def post(fposts,insieme):
    ls = list(insieme)
    ls2 = []
    ls3 = []
    ls4 = []
    a=set()
    for x in ls:
        x1 = x.lower()
        ls2.append(x1)
    f = open(fposts) 
    text = f.read()
    id_post = ''
    flag = 0    
    ls3 = list(text)
    for x in range(len(ls3)):
        if ls3[x] == '.' or ls3[x] == '?':
            ls4.append(' ')
        if ls3[x] == '>':
            ls4.append(ls3[x])
            ls4.append(' ')
        else:
            ls4.append(ls3[x])
    text2 = ''.join(ls4)
    f1 = open('fposts2.txt', 'w') 
    f1.write(text2)
    f1.close()
    f1 = open('fposts2.txt') 
    for riga in f1:
        for parola in riga.split():
            if flag == 1:
                id_post = parola
                flag = 0 
            if parola == '<POST>':
                flag=1
            for c in range(len(ls2)):
                if parola.lower() == ls2[c]:
                    a.add(id_post)                    
    f.close()
    f1.close()
    return a
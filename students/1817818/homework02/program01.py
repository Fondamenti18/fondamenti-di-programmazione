def identificatore(s):
    s = s[0:].strip()
    s = s[0:s.find('\n')]
    return s.strip()
def isParola(post,parola):
    verificato = False
    for s in post:      
        contatoreSpeciali = 0
        for char in s:
            caratteriSpeciali = False
            if  not char.isalpha():
                contatoreSpeciali +=1
            if contatoreSpeciali+len(parola) == len(s):
                caratteriSpeciali = True
        if (parola.lower() == s) or (s.find(parola.lower())!=-1 and caratteriSpeciali): 
            verificato = True
    return verificato
def post(fposts,insieme):
    listaID = set({})
    insieme = insieme
    tempFin = open(fposts,'r',encoding='utf-8')
    fin = tempFin.read()
    tempFin.close()
    fin = fin.split('<POST>')
    id = ''
    for post in fin:
        post = post.lower()
        id = identificatore(post)
        post = post.split()
        for parola in insieme:
            verificato = isParola(post,parola)       
            if verificato and (id not in listaID):
                listaID.add(id)
    return listaID 































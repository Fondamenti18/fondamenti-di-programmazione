import re

def post(fposts,insieme):
    ''' implementare qui la funzione'''
    f=open(fposts)
    risultato=set()
    righe=[x for x in f.readlines()]
    
    ID=funcID(righe)
    testi_post=funcTesto(righe)

    c=0
    for testo in testi_post:
        for parola in insieme:
            if re.search(r'\b' + parola.lower() + r'\b',testo):
                risultato.add(ID[c])
                break
        c+=1
    return risultato

def funcID(righe):
    strID=''
    
    lista_id=[]
    for i in righe:
        if "<POST>" in i:
            for x in i:
                if x.isdigit()==1:
                    strID+=x
            lista_id+=[strID]
            strID=''
    return lista_id

def funcTesto(righe):
    stringa=''
    lista_testo=[]
    stringa=''.join(righe)
    for testo_post in stringa.split("<POST>"):
        lista_testo.append(testo_post.lower())
    del lista_testo[0]
    return lista_testo

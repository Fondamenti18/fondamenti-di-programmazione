def gen_chiave(stringa):
    stringa2=""
    for x,y in enumerate(stringa):
        if 'a'<=y<='z' and stringa.count(y,x)==1:
            stringa2+=y
    stringa="".join(sorted(stringa2))
    return stringa2,stringa
def codifica(chiave, testo):
    x,y=gen_chiave(chiave)
    c=str.maketrans(y,x)
    return testo.translate(c)
def decodifica(chiave, testo):
    x,y=gen_chiave(chiave)
    c=str.maketrans(x,y)
    return testo.translate(c)

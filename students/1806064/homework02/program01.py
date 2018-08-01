def stringapulita(frase):
    frase_nuova=""
    for i in frase:
        if i.isalnum():
            frase_nuova+=i
        else:
            frase_nuova+=" "
    return frase_nuova

def cercapost(f,insieme):
    insieme_output=set()
    for i in f:
        i=stringapulita(i)
        i=i.split()
        if i==[]:
            continue
        identita=i.pop(0)
        if set(i) & insieme:
            insieme_output.add(identita)
    return insieme_output

def post(fposts,insieme):
    insieme_lower=set()
    with open(fposts,"r") as f:
        f=f.read()
        f=f.lower()
        f=f.split("<post>")
    for i in insieme:
        insieme_lower.add(i.lower())
    return cercapost(f,insieme_lower)

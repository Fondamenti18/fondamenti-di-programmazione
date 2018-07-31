import re
def controllo(stringa,insieme):
    for j in insieme:
        j = j.lower()
        if (" "+j+" ") in stringa:
            return True
        if stringa[-len(j)-1:]== (" "+j):
            return True
    return False

def post(fposts,insieme):
    with open(fposts,"r", encoding="utf-8") as f:
        risultato= set()
        totale=f.read()
        totale=re.sub("\W+"," ",totale)
        lista=totale.split("POST")
        for i in range(len(lista)):
            temp = lista[i]
            if controllo(temp.lower(),insieme):
                risultato.add(temp.split()[0])
    f.close()
    return risultato


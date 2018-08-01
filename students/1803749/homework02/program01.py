
def post(fposts, insieme):
    # Legge un file.
    listaIndici = set()
    insieme2 = []
    for parola in insieme:
        p2 = parola.lower()
        insieme2.append(p2)
    print (insieme2)
    in_file = open(fposts, "r")
    text = in_file.read()
    in_file.close()
    text = text.lower()
    
    
    text = " ".join(text.split("\n"))
    listaPost = text.split("<post>")
    for post in listaPost:
        
        for parolaChiave in insieme2:
            ind1 = post.find(parolaChiave)
            if ind1 != -1:
                if not post[ind1-1].isalpha() and not post[ind1+len(parolaChiave)].isalpha():
                        iden = searchID(post)
                        listaIndici.add(iden)
                        break
      
                    
                    
    return listaIndici

def searchID(stringa):
    listaParole = stringa.split(" ")
    for parola in listaParole:
        if  parola.isdigit():
            return parola
            break
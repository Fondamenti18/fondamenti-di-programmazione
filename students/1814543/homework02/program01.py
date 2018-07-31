def notAlpha2Alphanumeric(lista):
    ris = []
    for stringa in lista:
        new_s = str()
        for c in stringa:
            if c.isalpha():
                new_s = new_s + c
            else:
                break
        ris.append(new_s)
    return ris        
def post(fposts,insieme):
    risultato = set()
    currentPostID = ""
    myfile=open(fposts, "r",encoding = 'utf-8')  
    my_linee =  myfile.readlines()
    for linea in my_linee:
        if "<POST>" in linea:
            new_s = linea.replace("<POST>", "")
            new_s = new_s.strip()
            currentPostID = new_s
        else:
            new_linea = linea.upper()
            splitlinea=new_linea.split()
            splitlinea_new = notAlpha2Alphanumeric(splitlinea)
            for parolaDaCercare in insieme:
                new_parola = parolaDaCercare.upper()
                if new_parola in splitlinea_new:
                    risultato.add(currentPostID)
                    break
    return risultato
    
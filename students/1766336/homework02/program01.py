def post(fposts,insieme):
        import string
        import re
        in_file = open(fposts,"r")
        testo = in_file.read()
        in_file.close()
        insiemeRisultato=[]
        testo=testo.split()
        ID = ""
        tag =False

        for word in testo:
                if "<POST>" in word:
                        if word == "<POST>":
                            tag =True
                            ID = ""
                        else:
                            ID=word.replace("<POST>","")
                else:
                        if isNumber(word) and tag == True:
                                tag = False
                                ID = word
                        else:
                                for parola in insieme:
                                        if ID == "4":
                                            ris = True
                                        risultato = controllaParola(word, parola)
                                        if risultato == True and ID not in insiemeRisultato:
                                                insiemeRisultato.append(ID)
                                                break
        set1=set(insiemeRisultato)
        return set1
				


def controllaParola(parolaFile, parolaInput):
    import re
    import string
    if parolaFile.isalpha():
        if parolaInput.lower() == parolaFile.lower():
            return True
        else:
            return False
    else:
        regex=re.compile('[^a-zA-Z]')
        stringa=regex.sub(' ',parolaFile)
        lista=stringa.split()
        presente=False
        for parola in lista:
            if parola.lower()==parolaInput.lower():
                presente=True
        if presente == True:
            return True
        else:
            return False
	



def isNumber(stringa):
    try:
        int(stringa)
        return True
    except ValueError:
        return False



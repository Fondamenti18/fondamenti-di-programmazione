#retstituisce un insieme tutto lowercase
def ins_low(insieme):
    x=set()
    for el in insieme:
        x.add(el.lower())
    return x

#restituisce le righe del file grezze
def leggi_file(fposts):
    file = open(fposts, "r")
    righe=file.readlines()
    file.close()
    return righe

#ricava l ID dal titolo
def elabora_titolo(riga):
    lista=riga[:-1].split("<POST>")
    for elemento in lista:
        stringa=elemento.strip()
        if stringa.isnumeric():
            return stringa

#controlla la presenza di parole desiderate nel paragrafo del post
def elabora_par(riga,insieme_ret,insieme_low,ultimo_id):
    riga=riga.lower()
    parole=riga.split(' ')
    for parola in parole:
        if prepara_parola(parola) in insieme_low:
            insieme_ret.add(ultimo_id)
            break
    return insieme_ret

#pulisce la parola da eventuale punteggiatura e altro
def prepara_parola(parola):
    parola=parola.strip()
    if parola.isdigit() == False:
        if parola[-1:].isalpha() is False:
            return parola[:-1]
    return parola

#funzione principale
def post(fposts,insieme):

    insieme_low=ins_low(insieme)
    righe=leggi_file(fposts)
    
    insieme_ret=set()
    ultimo_id=0
    
    for riga in righe:
        if '<POST>' in riga:
            ultimo_id=elabora_titolo(riga)
        else:
            insieme_ret=elabora_par(riga,insieme_ret,insieme_low,ultimo_id)

    return insieme_ret


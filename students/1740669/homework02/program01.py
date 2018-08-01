import string
def trans_low_up(string):
    stringa =''
    if str.islower(string):
        stringa = str.capitalize(string)
    else:
        stringa = str.lower(string)
    return stringa
        
def clean_string(stringa):
    new_stringa = ''
    for char in stringa:
        if (char == '[' or char == ']') or (('a' <= char <= 'z') or('A' <= char <= 'Z')):
            new_stringa = new_stringa + char
    return new_stringa

    
def post(pfile,insieme):
    id_post = {}
    list_post = []
    parola_pulita = ''
    #new_id = ''
    new_idpost = ''
    Input_file = open (pfile,'r')       #apertura file
    testo = Input_file.read()       #legge il contenuto del file
    post = 'False'
    ID = 'False'
    lista_parole = testo.rsplit()
    #print(lista_parole)
    for parola in lista_parole:
        #print(parola)
        if '<POST>' in parola:
            post = 'true'
            for char in parola:
                if ('0' <= char <= '9'):
                    ID = 'true'
                    new_idpost = new_idpost + char
                    id_post = new_idpost
                    post = 'false'
        elif post == 'true':
            id_post = parola    #salvataggio ID
            ID = 'true'
            post = 'false'
        elif ID == 'true':
            parola_pulita = clean_string(parola)
            new_parola = trans_low_up(parola_pulita)
            for c in insieme:
                if (parola_pulita == c) or (new_parola == c):
                    #print(parola_pulita)
                    list_post.append(id_post)
                    ID = 'False'
    elenco_post = set(list_post)
    return elenco_post

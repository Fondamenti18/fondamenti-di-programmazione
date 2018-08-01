#OTTIMIZZA E RENDI PIU' COMPATTO
import re

def parole(fposts): #Prende un file e crea una lista delle righe non vuote minuscole
    with open(fposts, 'r') as f: return list(filter(None, (map(lambda x:x.lower()[:-1],f))))
    
def normale(fposts): #Elimina spazi dal titolo dei post
    text = parole(fposts)
    for p in range(len(text)): 
        if '<post>' in text[p]: text[p] = text[p].replace(' ','')
    return text

def diz(fposts):
    #Crea un dizionario avente come chiave il POST e come valore una stringa che è il testo associatovi
    text = normale(fposts)
    diz = {}
    ls = []
    for p in range(len(text)-1,-1,-1):
        if '<post>' not in text[p]: ls.append(text[p])
        else:
            diz[text[p]] = ' '.join(ls)
            ls = []
    return diz

def trova(fposts, s):
    #Restituisce una lista con chiavi corrispondenti
    dic = diz(fposts)
    ldic = list(dic.items())
    return list(map(lambda p: p[0], filter(lambda p: re.search(r"\b"+re.escape(s)+r"\b", p[1]), ldic)))

def ID(s):
    #Restituisce il numero ID
    ls = []
    for i in list(s):
        try:
          ls.append(int(i))
        except ValueError: pass
    return ''.join([str(n) for n in ls])

def temp(fposts, insieme):
    ls = []
    for i in insieme:
        ls += trova(fposts, i.lower())
    return ls

def post(fposts,insieme):
    return {ID(j) for j in temp(fposts,insieme)}

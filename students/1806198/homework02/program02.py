import json
#prepara la riga
def elabora_riga(riga,limite):
    ls=riga[:-1].split(limite)
    return ls[1].strip()

#crea una struttura per un controllo facilitato
def crea_strutt(righe):
    lssub={}
    lscomp=set()
    for indice in range(0,len(righe)-1):
        riga=righe[indice]
        if 'comp' in riga:
            stringa=elabora_riga(riga,'comp')
            riga_succ=righe[indice+1]
            if 'sub' in riga_succ:
                lssub[stringa]=elabora_riga(riga_succ,'sub')
            else:
                lscomp.add(stringa)
    return lscomp,lssub

def cerca_percorso(k,lssub):
    chiavi=lssub.keys()
    lista=[]
    while True:
        if k in chiavi:
            y=lssub.get(k)
            lista+=[y]
            k=y
        else:
            break
    lista.reverse()
    return lista

#ritorna le righe del file
def leggi_file(fcompiti):
    file = open(fcompiti, "r")
    righe=file.readlines()
    file.close()
    return righe

#funzione principale
def pianifica(fcompiti,insi,fout):
    
    dizionario={}
    lscomp,lssub=crea_strutt(leggi_file(fcompiti))
    
    for x in insi:
        if x in lscomp:
            dizionario[x]=[]
        elif x in lssub.keys():
            dizionario[x]=cerca_percorso(x,lssub)
                   
    with open(fout,'w') as file:
        json.dump(dizionario,file)


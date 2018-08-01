def rimuovicarattere(parola):
    for i in parola:                   #eliminazione caratteri
        if((i<'a')or(i>'z')):
            parola=parola.replace(i,"")

    return parola

def rimuoviocc(parola):                 #elimina tutte le occorenze tranne l'ultima
    conta=0
    for i in parola:
        for h in parola:
            if(h==i):
                conta=conta+1
            if(conta>1):
                parola=parola.replace(i,"",1)
                conta=0
        conta=0
    return parola


def ordina(parola):
    s=""
    for i in sorted(parola):           #ordina la chiave
        s+=i
    return s

    
def crea_dizionario(a, b):             #serve a creare il dizionario 
    d={}
    i=0
    for i in range(0,len(a)):
        d[b[i]]=a[i]
    return d


def codifica(chiave, testo):           
    chiave=rimuovicarattere(chiave)
    chiave=rimuoviocc(chiave)
    d=crea_dizionario(chiave,ordina(chiave))
    cod=""
    h=0
    for i in testo:
        if(i in d):
            cod+=d[i]
        else:
            cod+=testo[h]
        h=h+1
    return cod


def decodifica(chiave,testo):
    chiave=rimuovicarattere(chiave)
    chiave=rimuoviocc(chiave)
    d=crea_dizionario(ordina(chiave),chiave)
    cod=""
    h=0
    for i in testo:
        if(i in d):
            cod+=d[i]
        else:
            cod+=testo[h]
        h=h+1
    return cod



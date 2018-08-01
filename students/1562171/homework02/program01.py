"""
Created on Thu Nov  2 02:52:59 2017

@author: NICO
"""

def eliminaCar(stringa):
    for i in stringa:
        if((i<'0')or(i>'9')):
            if ((i<'A')or(i>'z')):
                if(i!=' '):
                    stringa=stringa.replace(i,"")
    return stringa

def post(fposts,insieme):
    f=open(fposts,"r")
    posts=[]
    riga=0
    t=""
    p=[]
    n=0
    prova=[]
    for linea in f:
        #print(linea)
        for i in linea:                         
            if i=="<":                              #estraggo il numero del post
                linea=linea.replace(" ","")         #
                linea=linea.replace("<POST>","")    #
                n=linea.replace("\n","")            #fine estrazione
                riga=1                              #pongo a 1 il controllo     
                prova+=[n]                          
        if(riga!=1) and (linea!="\n"):
            t=linea.replace("\n","")                #creo linea senza "a capo"
            t=t.lower()                             #elimino maiuscole
            t=eliminaCar(t)                         #elimino caratteri speciali
            p+=t.split(" ")                         #faccio una lista delle parole senza spazi
        for el in insieme:                          #per ogni elemento dell'insieme
            if el.lower() in p:                     #se insieme è contenuto in p
                posts+=[n]                          #aggiungo alla lista dei numeri post
        #print(p)
        p=[]                                        #svuoto p
        riga=0                                      #azzero il controllo
    var = set(posts)  
    return var
                
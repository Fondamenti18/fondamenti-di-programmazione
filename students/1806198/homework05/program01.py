#librerie
import random 
import itertools

#set globale di tutte le possibili combinazioni
ins=set()

#funzione che ritorna la valutazione del tentativo
#presa dal simulatore,per evitare problemi di import
def valutazione(cod1, cod2):
    x=0; ins=set(cod1)
    for i in range(len(cod1)):
        if cod1[i]==cod2[i]: x+=1
    y=len(ins & set(cod2))-x  
    return x,y

#specifica se ancora non è stata trovata una cifra da scartare sicuramente
#(solo per il codice di 8 cifre, per diminuire il tempo di calcolo)
def semplificabile(configurazione):
    if len(configurazione)==1: return True
    if configurazione[0]!=8: return False
    for i in range(1,len(configurazione)):
        if configurazione[i][0][0]!=configurazione[i][0][1]: return False
        if configurazione[i][1]==(0,0):return False
    return True

#genera la lista delle possibili cifre presenti, tranne quella scartata
#(solo per il codice di 8 cifre, per diminuire il tempo di calcolo)
def gen_cifre(configurazione):
    ls=[a for a in range(0,10)]
    for i in range(1,len(configurazione)):
        if configurazione[i][1]==(0,0):
            ls.remove(configurazione[i][0][0])
            return ls
    return ls

#genera l insieme di tutte le possibili soluzioni
def gen_set(x,ls=[0,1,2,3,4,5,6,7,8,9]):
    global ins
    for el in itertools.permutations(ls, x): ins.add(el)
    return list(ins.pop())

#ritorna l insieme dei tentativi non compatibili con l ultimo tentativo
def non_compatibili(ris,ultima):
    ins2=set()
    for el in ins:
        tupla=valutazione(ultima,el)
        if tupla[0] not in ris or tupla[1] not in ris: ins2.add(el)
    return ins2

#funzione principale
def decodificatore(configurazione):

    global ins

    #iniziallizazione di tutte le poss. combinazioni
    if semplificabile(configurazione):
        ins.clear()
        if configurazione[0]!=8: return gen_set(configurazione[0])
        risposta=[len(configurazione)-1 for i in range(configurazione[0])]   
            
    elif len(ins)==0:
        risposta=gen_set(configurazione[0],gen_cifre(configurazione))

    #inoltro tentativi
    else:
        
        #ripesco l ultimo tentativo effettuato
        ultima=list(configurazione[-1][0])
        ins4=(configurazione[-1][1][0],configurazione[-1][1][1])

        #creo l insieme degli elementi da scartare rispetto all'ultimo tentativo
        ins2=non_compatibili(ins4,ultima)

        #li scarto e scelgo una risposta a caso tra le rimanenti
        ins=ins.difference(ins2)
        risposta=ins.pop()

    return list(risposta)

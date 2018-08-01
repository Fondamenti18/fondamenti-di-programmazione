'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco per il gioco del Mastermind. 

Nel gioco del Mastermind un  giocatore (il "decodificatore"), deve indovinare un  codice segreto.
Il codice segreto e' di N cifre decimali distinte (NO RIPETIZIONI, solo 10 possibili simboli per ciascuna posizione).
Il decodificatore cerca di indovinare il codice per tentativi. Strategicamente  nel tentativo 
possono essere presenti anche cifre ripetute pur  sapendo che nel codice non sono presenti ripetizioni. 
In risposta ad  ogni tentativo viene fornito un aiuto producendo una coppia di interi (a,b) dove:

- a e' il numero di cifre giuste al posto giusto,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo al posto giusto.
- b e' il numero di cifre  giuste ma al posto sbagliato,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo solo al posto sbagliato.

Ad esempio per il codice
    34670915 e il tentativo
    93375948
la risposta deve essere la coppia (2,3).
Il 2 viene fuori dal contributo delle cifre 7 e 9 del codice da indovinare in quarta e sesta posizione,
il numero 2 e' dovuto alle cifre 3,4,5 che compaiono tra le cifre del tentativo ma mai al posto giusto.

Nella nostra versione di Mastermind il valore di N (lunghezza del codice) puo' essere 6, 7 o 8 e nella coppia data
in  risposta ai tentativi non si vuole rivelare quale delle due due cifre rappresenta il numero di  cifre giuste al posto giusto 
di conseguenza nella coppia di risposta  i valori di a e b possono risultare invertiti.
Ad esempio per il codice 34670915 e il tentativo 93375948 le risposte (2,3) e (3,2) sono entrambe possibili.


Una configurazione del  gioco viene rappresentata come lista di liste (L). 
Il primo elemento di L e' un intero N rappresentante la lunghezza del codice.
Ciascuno degli eventuali altri elementi di L rappresenta un tentativo fin qui
effettuato dal decodificatore e la relativa risposta.
Piu' precisamente  L[i] con i>0, se presente, conterra' una tupla composta da due elementi:
- la lista di N cifre  con il tentativo effettuato dal decodificatore in un qualche passo precedente
- la tupla di interi (a,b) ricevuta in risposta.


Il programma che dovete realizzare contiene la seguente funzione:
 
    decodificatore(configurazione)

che e' l'AI che guida il gioco. La funzione  riceve come input la configurazione attuale del gioco e produce un tentativo (lista di caratteri in '0-9').

Per questo esercizio la valutazione avverra' nel seguente modo: 
avete 150 tentativi e 30 secondi di tempo per indovinare quanti piu' codici possibile.
Il punteggio ottenuto e' dato dal numero di codici che riuscite ad indovinare.

Tutti i vostri elaborati al termine verranno valutati su di uno stesso set di codici,
questa operazione  determinera' una classifica dei vostri elaborati.
Per entrare in classifica bisogna indovinare almeno cinque codici.
La classifica viene suddivisa in 14 fasce che corrispondono ai voti da 18 a 31 ed a 
ciascun programma viene assegnato il voto corrispondente.
Se il numero di valori diversi e' minore di 14 il voto sara' proporzionale alla posizione
nella graduatoria (con il primo che prende 31 e l'ultimo 18)

In allegato vi viene fornito un  simulatore di gioco (simulatore1.py) che vi permettera' di 
autovalutare la vostra strategia. Il simulatore genera  codici casuali e invoca il vostro 
programma per ottenere i vari tentativi. Appena un codice  viene indovinato ne viene 
proposto uno nuovo. Il processo termina quando avete esaurito i vostri 150 tentativi
o sono passati  i 30 secondi.

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti
'''

import random 
# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti
cifre=[0,0,0,0,0,0,0,0,0,0]
nt=0
rispostaf=[]
lista=[]
tupla=()
pos=0
prec1=(0,0)
prec2=(0,0)
c1=-1
c2=-1
c3=-1
g=0
e=2
testa=0
coda=0
inizio=0
i=0
k=0
k1=0
def trovac3(cifre):
    for i in range(0,10):
            if cifre[i]==0:
                c3=i
                break
    return c3
def cambiac1(cifre):
     for i in range(0,10):
            if cifre[i]!=0:
                c1=i
                cifre[i]=0
                break
     return c1
def cambiac2(cifre):
     for i in range(0,10):
            if cifre[i]!=0:
                c2=i
                cifre[i]=0
                break
     return c2
def avantic1(c1,c2,c3,risposta,testa,k):
    for i in range(testa,k):
        if risposta[i]!=c2 and risposta[i]!=c3:
            continue
        else:
            temp=risposta[i]
            risposta[i]=c1
            risposta[testa]=temp
            break
    return risposta,i
def cercatesta(risposta,c3,k):
    for i in range(0,k):
        if(risposta[i]!=c3):
          continue
        else:
          return i
def cercatestac1(risposta,c1,k):
    for i in range(0,k):
        if(risposta[i]!=c1):
          continue
        else:
          return i      
def cercacoda(risposta,c2,k):
    for i in range(k-1,-1,-1):
        if(risposta[i]!=c2):
          continue
        else:
          return i      
def c1avanti(c1,c3,risposta,testa,k):
    for i in range(testa,k):
        if risposta[i]!=c3:
            continue
        else:
            temp=risposta[testa]
            risposta[testa]=c3
            risposta[i]=temp
            break
    return risposta,i
def c2avanti(c2,c3,risposta,coda,k):
    for i in range(coda,-1,-1):
        if risposta[i]!=c3:
            continue
        else:
            risposta[coda]=c3
            risposta[i]=c2
            break
    return risposta,i
def posizionec1(c1,k,rispostaf):
    for i in range(0,k):
        if rispostaf[i]==c1:
            return i
            
# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti

def decodificatore(configurazione):
    ''' inserire qui la vostra soluzione'''
    global cifre
    global nt
    global rispostaf
    global lista
    global tupla
    global pos
    global prec1
    global prec2
    global c1
    global c2
    global c3
    global g
    global e
    global testa
    global coda
    global inizio
    global i
    global k
    global k1
    
        
    k=configurazione[0]
    print(k)
    if(g+1==k1):
        nt=0
        k=configurazione[0]
        g=0
        e=2
        pos=0
        prec1=(0,0)
        prec2=(0,0)
        testa=0
        coda=0
        inizio=0
        c1=-1
        c2=-1
        c3=-1
    coda=k-1     
    print(g)
    k1=k
    print (k1)
    if(nt==0):
        nt+=1
        return [0]*k
    print(nt)
    lista,tupla=configurazione[nt]
    
    print(lista,tupla)
    
    if(nt>0 and nt<=9):
        if(tupla!=(0,0)):
            cifre[nt-1]=1
        else: 
            cifre[nt-1]=0
        nt+=1
        return [nt-1]*k
    elif (nt==10):
        if tupla!=(0,0):
            cifre[nt-1]=1
        else:
            cifre[nt-1]=0
        nt+=1
    print(cifre)
    
    if(pos==0 ):
        c3=trovac3(cifre)
        c1=cambiac1(cifre)
        c2=cambiac2(cifre)
        rispostaf=[c1]
        for i in range(1,k-1):
            rispostaf+=[c3]
        rispostaf+=[c2]
        pos=1
        return rispostaf 
    if (pos==1):
        if(prec1==(0,0) or prec2==(0,0) and g==0):
            nt+=1
            prec1=prec2
            prec2=tupla
            inizio=0
            rispostaf,testa=avantic1(c1,c2,c3,rispostaf,testa,k)
            print(testa)
            return rispostaf 
        elif((g==0 and prec1==(2,0) or prec1==(0,2)) and prec2==(1,1) and tupla==(1,1)):
            nt+=1
            rispostaf[0]=c1
            rispostaf[testa]=c3
            g=2
            e=1
            c1=cambiac1(cifre)
            testa=cercatesta(rispostaf,c3,k)
            rispostaf[testa]=c1
            return rispostaf 
        elif(g>1 and (tupla==(g,e) or tupla==(e,g)) ):
            nt+=1
            if testa==k-2:
               rispostaf,testa=avantic1(c1,c2,c3,rispostaf,testa,k)
               g+=1
               e=1
               c1=cambiac1(cifre)
               testa=cercatesta(rispostaf,c3,k)
               rispostaf[testa]=c1
               return rispostaf 
            else:
               testa=cercatestac1(rispostaf,c1,k)
               rispostaf,testa=c1avanti(c1,c3,rispostaf,testa,k)
               return rispostaf
        elif(g>1 and (tupla==(g+e,0) or tupla==(0,g+e)) ):
            nt+=1
            g+=1
            e=1
            c1=cambiac1(cifre)
            testa=cercatesta(rispostaf,c3,k)
            print(testa)
            rispostaf[testa]=c1
            return rispostaf
        elif(g==0 and (prec1==(2,0) or prec1==(0,2)) and prec2==(1,1) and (tupla==(2,0) or tupla==(0,2))):
            
            rispostaf[testa-1]=c1
            rispostaf[testa]=c3
            nt+=1
            g=1
            e=1
            coda=cercacoda(rispostaf,c2,k)
            rispostaf,coda=c2avanti(c2,c3,rispostaf,coda,k)
            return rispostaf
        elif(g==0 and (prec1==(2,0) or prec1==(0,2)) and (prec2==(2,0) or prec2==(0,2)) and tupla==(1,1)):
            nt+=1
            g=1
            e=1
            coda=cercacoda(rispostaf,c2,k)
            rispostaf,coda=c2avanti(c2,c3,rispostaf,coda,k)
            return rispostaf
        elif(g==1 and tupla==(1,1)):
            nt+=1
            print(coda)
            coda=cercacoda(rispostaf,c2,k)
            rispostaf,coda=c2avanti(c2,c3,rispostaf,coda,k)
            print(coda)
            return rispostaf
        elif(g==1 and (tupla==(2,0) or tupla==(0,2))):
            nt+=1
            g=2
            e=1
            c1=cambiac1(cifre)
            testa=cercatesta(rispostaf,c3,k)
            rispostaf[testa]=c1
            return rispostaf 
        elif(g==0 and (prec1==(2,0) or prec1==(0,2)) and (prec2==(2,0) or prec2==(0,2)) and (tupla==(2,0) or tupla==(0,2))):
            nt+=1
            prec1=prec2
            prec2=tupla
            if testa==k-2:
               rispostaf,testa=avantic1(c1,c2,c3,rispostaf,testa,k)
               g=-1
               e=1
               
               return rispostaf 
            else:
                rispostaf,testa=avantic1(c1,c2,c3,rispostaf,testa,k)
                return rispostaf
        
        elif(g==-1 and (prec1==(2,0) or prec1==(0,2)) and (prec2==(2,0) or prec2==(0,2)) and (tupla==(2,0) or tupla==(0,2))):
            nt+=1
            prec1=prec2
            prec2=tupla
            g=2
            e=1
            c1=cambiac1(cifre)
            testa=cercatesta(rispostaf,c3,k)
            rispostaf[testa]=c1
            return rispostaf 
        elif(g==-1 and (prec1==(2,0) or prec1==(0,2)) and (prec2==(2,0) or prec2==(0,2)) and tupla==(1,1)):  
            nt+=1
            prec1=prec2
            prec2=tupla
            g=1
            e=1
            coda=cercacoda(rispostaf,c2,k)
            rispostaf,coda=c2avanti(c2,c3,rispostaf,coda,k)
            return rispostaf
        
        
        
        
        
        elif(g==0 and prec1==(1,1) and (prec2==(2,0) or prec2==(0,2)) and(tupla==(2,0) or tupla==(0,2))):
            nt+=1
            rispostaf[inizio]=c1
            rispostaf[testa]=c3
            g=1
            e=1
            coda=cercacoda(rispostaf,c2,k)
            rispostaf,coda=c2avanti(c2,c3,rispostaf,coda,k)
            return rispostaf
        elif(g==0 and prec1==(1,1) and (prec2==(2,0) or prec2==(0,2)) and tupla==(1,1)):
            nt+=1
            rispostaf[testa-1]=c1
            rispostaf[testa]=c3
            g=2
            e=1
            c1=cambiac1(cifre)
            testa=cercatesta(rispostaf,c3,k)
            rispostaf[testa]=c1
            return rispostaf 
        elif(g==0 and prec1==(1,1) and prec2==(1,1) and (tupla==(2,0) or tupla==(0,2))):
            nt+=1
            g=2
            e=1
            c1=cambiac1(cifre)
            testa=cercatesta(rispostaf,c3,k)
            rispostaf[testa]=c1
            return rispostaf 
        elif(g==0 and prec1==(1,1) and prec2==(1,1) and tupla==(1,1)):
            nt+=1
            prec1=prec2
            prec2=tupla
            rispostaf,testa=c1avanti(c1,c3,rispostaf,testa,k)
            return rispostaf
    
    n=configurazione[0]
    x='0123456789'
    risposta=[]
    for _ in range(n):
        y=random.choice(x)
        risposta+=[int(y)]
        x=x.replace(y,'')
    return risposta


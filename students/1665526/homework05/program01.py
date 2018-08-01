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
import itertools

# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti
z=0
a=[]
zorro=0
lol=[]
g=[]
count=0
x=[0,1,2,3,4,5,6,7,8,9]
l=[]
nn=[]
asd=0
yy=[]
j=[]
nice=0
jk=[]
dic=[]
def decodificatore(configurazione):
    ''' inserire qui la vostra soluzione'''
    global x,yy,l,count,nn,j,z,a,g,dic,lol,nice,jk,asd,zorro
    if len(configurazione)==1:
        count=0
        zorro=0
        x=[0,1,2,3,4,5,6,7,8,9]
        l.clear()
        nn.clear()
        nice=0
        asd=0
        a.clear()
        yy.clear()
        j.clear()
        dic.clear()
        jk.clear()
        z=0
        
    l=[]
    n=configurazione[0]
    risposta=[]
    roundd=round(n/2)
    if len(yy)==n:
            x=[]
    if len(yy)==n:
            x=[]
    if len(yy)==n:
            x=[]
    if x!=[] and  len(configurazione)>1 and configurazione[-1][-1][0]+configurazione[-1][-1][1]==0:
        if configurazione[-1][0].count(configurazione[-1][0][0])>5:
            j.append(x[0])
            x=x[1:]
            yy.append(x[0])
            x=x[1:]
        if configurazione[-1][0].count(configurazione[-1][0][0])<5:
            j.append(x[0])
            j.append(x[1])
            x=x[2:]
    if x!=[] and len(configurazione)>1 and configurazione[-1][-1][0]+configurazione[-1][-1][1]==1:
        if configurazione[-1][0].count(configurazione[-1][0][0])<5:
            for i in range(n):
                l.append(configurazione[-1][0][0])
            #count+=1
            return l
        if configurazione[-1][0].count(configurazione[-1][0][0])>5:
            #x.remove(configurazione[-1][0][-1])
            yy.append(x[0])
            x=x[2:]
    if x!=[] and len(configurazione)>1 and configurazione[-1][-1][0]+configurazione[-1][-1][1]==2:
        yy.append(x[0])
        yy.append(x[1])
        x=x[2:]
    if len(x)>=1:
        for i in range(roundd):
            risposta.append(x[0])
            #count+=1
    if len(x)>1:
        for i in range(n-roundd):
            risposta.append(x[1])
            #count+=1
    if len(x)==1:
        for i in range(n):
            risposta.append(x[0])
            x=[]
    if j==[] and x==[] and yy!=[]:
        if 1 not in yy: j.append(1)
        if 0 not in yy: j.append(0)
        if 2 not in yy: j.append(2)
        if 3 not in yy: j.append(3)
        if 4 not in yy: j.append(4)
        if 5 not in yy: j.append(5)
        if 6 not in yy: j.append(6)
        if 7 not in yy: j.append(7)
        if 8 not in yy: j.append(8)
        if 9 not in yy: j.append(9)
    
    if x==[] and yy!=[]:
        nn=itert(yy)
        lol=yy.copy()
        for i in range(len(lol)):
            jk.append(j[0])
        yy.clear()
    if x==[] and yy==[]:
        
        if configurazione[-1][-1]==(0,n) or configurazione[-1][-1]==(n,0):
            dex(n,nn,configurazione[-1][0])
            print(len(nn))
        if (configurazione[-1][-1]==(1,n-1) or configurazione[-1][-1]==(n-1,1)) and asd==0:
            a.clear()
            a=configurazione[-1][0].copy()
            g=configurazione[-1][0].copy()
            a[z]=jk[0]
            print(len(nn))
            return a
        if (configurazione[-1][-1]==(1,n-2) or configurazione[-1][-1]==(n-2,1)) and asd==0 and zorro==0:
            a=g.copy()
            for i in nn[:]:
                if i[z]==g[z]:nn.remove(i)
            z+=1
            a[z]=jk[0]
            print(len(nn))
            return a
        if (configurazione[-1][-1]==(0,n-1) or configurazione[-1][-1]==(n-1,0) )and asd==0 and zorro==0:
            for i in nn[:]:
                if i[z]!=g[z]:nn.remove(i)
            asd+=1
            dex(n,nn,configurazione[-1][0])
        if (configurazione[-1][-1]==(1,n-1) or configurazione[-1][-1]==(n-1,1)) and asd!=0:
            dic=configurazione[-1][0]
            dic[z]=jk[0]
            dex(n,nn,dic)
            print(len(nn))
        '''if (configurazione[-1][-1]==(2,n-2) or configurazione[-1][-1]==(n-2,2)) and asd!=0:
            a=configurazione[-1][0].copy()
            g=configurazione[-1][0].copy()
            a[z]=jk[0]
            zorro+=1
            return a
        if (configurazione[-1][-1]==(1,n-2) or configurazione[-1][-1]==(n-2,1) or configurazione[-1][-1]==(1,n-3) or configurazione[-1][-1]==(n-3,1)) and asd!=0:
            a=g.copy()
            a[z]=jk[0]
            a[nice]=jk[0]
            for i in nn[:]:
                if i[nice]==a[nice]:nn.remove(i)'''
           
        dot=random.choice(nn)
        for i in nn[:]:
            if i==dot:nn.remove(i)
        return dot
    return risposta
def itert(lista):
    cc=[]
    a=itertools.permutations(lista)
    for i in a:
        cc.append(list(i))
    return cc
def dex(n,nn,qls):
    if n==6:
        a,b,c,d,e,f=qls
        for i in nn[:]:
            if i[0]==a or i[1]==b or i[2]==c or i[3]==d or i[4]==e or i[5]==f: nn.remove(i)
    if n==7:
        a,b,c,d,e,f,g=qls
        for i in nn[:]:
            if i[0]==a or i[1]==b or i[2]==c or i[3]==d or i[4]==e or i[5]==f or i[6]==g: nn.remove(i)
    if n==8:
        a,b,c,d,e,f,g,h=qls
        for i in nn[:]:
            if i[0]==a or i[1]==b or i[2]==c or i[3]==d or i[4]==e or i[5]==f or i[6]==g or i[7]==h: nn.remove(i)

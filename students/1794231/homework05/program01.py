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

def decodificatore(configurazione):
    if len (configurazione)==1:
        global dati
        dati=[[], [], [], [], [], [], [], []]
    n=configurazione[0]
    x='0123456789'
    f=0
    if dati[4]!=[]:
        if configurazione[-1][1]==(1,1):
            dati[0].append(str(dati[4][1]))
        elif configurazione[-1][1]==(2,0) or configurazione[-1][1]==(0,2):
            dati[0].append(str(dati[4][1]))
            dati[7].append(dati[4][0])
            dati[7].append(dati[5][0])
        else:
            dati[0].append(str(dati[4][0]))
        del dati[4][0]
        del dati[4][0]
    risposta=[]
    non=dati[0][:]
    base=dati[1][:]
    cifra=dati[2][:]
    scop=dati[3][:]
    if len(dati[0])!=(10-n):
        risposta=trovanulli(configurazione)
        if risposta!=[]:
            return risposta
    if dati[1]==[]:
        for indice in range(1, len(configurazione)):
            if configurazione[indice][1]==(n, 0) or configurazione[indice][1]==(0, n):
                if base==[]:
                    base=configurazione[indice][0]
                    dati[1]=base[:]
    if base==[]:
        for e in non:
            x=x.replace(e, '')
        for _ in range(n):
            y=random.choice(x)
            risposta+=[int(y)]
            x=x.replace(y,'')
        return risposta
    if type(dati[0][0]) == str:
        dati[0]=[]
        for nx in range(len(non)):
            dati[0].append(int(non[nx]))
        non=dati[0][:]
    if dati[6]!=[]:
        if dati[6][-1]!='a':
            risposta=base[:]
            risposta[-1]=dati[6][0]
            dati[6].append('a')
            return risposta
        else:
            if scop==[]:
                for _ in range(n):
                    scop.append(None)
            if configurazione[-1][1][0]==1 or configurazione[-1][1][1]==1:
                scop[-1]=dati[6][0]
            else:
                scop[-1]=dati[6][1]
            dati[6]=[]
            dati[3]=scop[:]
            f=1
    if dati[7]!=[]:
        if dati[7][-1]!='a':
            risposta=base[:]
            risposta[0]=dati[7][0]
            dati[7].append('a')
            return risposta
        else:
            if scop==[]:
                for _ in range(n):
                    scop.append(None)
            if configurazione[-1][1][0]==1 or configurazione[-1][1][1]==1:
                scop[0]=dati[7][0]
            else:
                scop[0]=dati[7][1]
            dati[7]=[]
            dati[3]=scop[:]
            f=1
    if dati[3]==[]:
        for _ in range(n):
                dati[3].append(None)
        scop=dati[3][:]
    risposta=base[:]
    if configurazione[-1][1][0]==1 or configurazione[-1][1][1]==1:
        if f==0:
            scop[cifra[1]]=cifra[0]
            cifra=[]
    elif cifra!=[]:
        risposta[cifra[1]]=non[0]
    if not None in scop:
        return scop
    if cifra == []:
        for num in base:
            if not num in scop:
                cifra=[num, 0]
                break
    for x in range(len(risposta)):
        if risposta[x]==cifra[0]:
            risposta[x]=non[0]
            break
    for giusto in range(len(scop)):
        if scop[giusto]!=None:
            risposta[giusto]=non[0]
    f=0
    while f==0:
        if risposta[cifra[1]] == non[0]: cifra[1]+=1
        else: f=1
    risposta[cifra[1]]=cifra[0]
    dati[2]=cifra[:]
    dati[3]=scop[:]
    return risposta
def trovanulli(configurazione):
    r=[]
    if len(configurazione)==1:
        for _ in range(configurazione[0]-1):
            r.append(0)
        r.append(1)
    elif len(configurazione)==2:
        for _ in range(configurazione[0]-1):
            r.append(2)
        r.append(3)
    elif len(configurazione)==3:
        for _ in range(configurazione[0]-1):
            r.append(4)
        r.append(5)
    elif len(configurazione)==4:
        for _ in range(configurazione[0]-1):
            r.append(6)
        r.append(7)
    elif len(configurazione)==5:
        for _ in range(configurazione[0]-1):
            r.append(8)
        r.append(9)
    else:
        if dati[4]==[]:
            for indice in range(1, 6):
                if configurazione[indice][1]==(0,0):
                    dati[0].append(str(configurazione[indice][0][0]))
                    dati[0].append(str(configurazione[indice][0][-1]))
                elif configurazione[indice][1]==(1,0) or configurazione[indice][1]==(0,1):
                    dati[4].append(configurazione[indice][0][0])
                    dati[4].append(configurazione[indice][0][-1])
                elif configurazione[indice][1]==(1,1):
                    dati[5].append(configurazione[indice][0][0])
                    dati[5].append(configurazione[indice][0][-1])
                elif configurazione[indice][1]==(2,0) or configurazione[indice][1]==(0,2):
                    dati[5].append(configurazione[indice][0][0])
                    dati[5].append(configurazione[indice][0][-1])
                    dati[6].append(configurazione[indice][0][0])
                    dati[6].append(configurazione[indice][0][-1])
        if dati[4]!=[]:
            r.append(dati[4][0])
            for _ in range(configurazione[0]-1):
                r.append(dati[5][0])
    return(r)




'''
[2, 1, 6, 0, 5, 4]
[0, 1, 3, 8, 6, 7, 4]
'''










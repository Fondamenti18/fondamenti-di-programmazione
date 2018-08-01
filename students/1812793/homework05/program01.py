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
def decodificatore(configurazione):
    ''' inserire qui la vostra soluzione'''
    n=configurazione[0]
    risposta=[]
    if len(configurazione)<11:
        if len(configurazione)==1:
            for i in range(n):
                risposta+=[0]
        elif configurazione[-1][1]==(0,0):
            for i in range(n):
                risposta+=[configurazione[-1][0][0]+1]
        else:
            for i in range(int(n/2)):
                risposta+=[configurazione[-1][0][0]]
            for i in range(n-int(n/2)):
                risposta+=[configurazione[-1][0][-1]+1]
    elif len(configurazione)==11:
        quart=()
        quart=trova_quartine(configurazione)
        print(quart)
        configurazione+=[quart]
        risposta=list(quart[0])+list(quart[1])
    elif n==7 and (len(set(configurazione[-1][0]))==n and (configurazione[-1][1][0]==0 or configurazione[-1][1][1]==0)):
        if configurazione[-1][0][2]==configurazione[11][0][0] and (configurazione[-1][1][0]==0 or configurazione[-1][1][1]==0):
            risposta=configurazione[11][1]+configurazione[11][0]
        else:
            risposta=shift(configurazione[11][0])+shift(configurazione[11][1])
        
    elif (len(set(configurazione[-1][0]))==n and (configurazione[-1][1][0]==0 or configurazione[-1][1][1]==0)):
        if len(configurazione)==13:
            risposta=list(configurazione[11][1])+list(configurazione[11][0])
        else:
            if configurazione[-1][0][int(n/2)-1]==configurazione[11][1][0]:
                risposta=shift(configurazione[11][0])+shift(configurazione[11][1])
            else:
                risposta=shift(configurazione[-1][0][0:int(n/2)])+shift(configurazione[-1][0][int(n/2):])
    else:
        if configurazione[-1][1][0]+configurazione[-1][1][1]==n and len(configurazione)<21:
            while len(configurazione)<22:
                configurazione+=[configurazione[-1]]
            risposta=[configurazione[20][0][0]]+[configurazione[20][0][-1] for x in range(n-1)]
        elif configurazione[-1][1][0]==0 or configurazione[-1][1][1]==0:
            if len(set(configurazione[-1][0][int(n/2):]))==1 and (configurazione[-1][1][0]+configurazione[-1][1][1])<int(n/2)+1:
                risposta=configurazione[-1][0]
                s=trova_prox(configurazione[20][0][0:int(n/2)],configurazione[-1])
                for i in range(n):
                    if risposta[i]==configurazione[20][0][-1]:
                        risposta[i]=s
                        break
            elif len(set(configurazione[-1][0][int(n/2):]))==1 and (configurazione[-1][1][0]+configurazione[-1][1][1])==int(n/2)+1:
                risposta=[configurazione[20][0][0]]*n
                risposta[int(n/2)]=configurazione[20][0][int(n/2)]
            elif len(set(configurazione[-1][0][:int(n/2)]))==1 and (len(set(configurazione[-1][0][int(n/2):]))==int(n/2) or (n==7 and len(set(configurazione[-1][0][int(n/2):]))==int(n/2)+1)) and configurazione[20][0][0] not in configurazione[-1][0][int(n/2):]:
                '''condizione che porta a creare il tentativo finale'''
                risposta=[]
                t=False
                for i in configurazione[21:]:
                    if i[1][0]+i[1][1]==int(n/2)+1:
                        if t==False:
                            risposta+=i[0][:int(n/2)]
                            t=True
                        else:
                            risposta+=i[0][int(n/2):]
                            break
                #print(risposta)
                            
            else:
                risposta=configurazione[-1][0]
                s=trova_prox(configurazione[20][0][int(n/2):n],configurazione[-1])
                '''if len(configurazione)<45:
                    print(s)'''
                for i in range(int(n/2),n):
                    if risposta[i]==configurazione[20][0][0]:
                        risposta[i]=s
                        break
        else:
            if len(set(configurazione[-1][0][int(n/2):n]))==1 and (configurazione[-1][1][0]+configurazione[-1][1][1])<int(n/2)+1:
                risposta=configurazione[-1][0]
                a=trova_ultimo(configurazione[20][0][0:int(n/2)],configurazione[-1],"p")
                '''if len(configurazione)<33:
                    print(a)'''
                t=False
                for i in range(n):
                    if risposta[i]==a:
                        risposta[i]=configurazione[20][0][-1]
                        t=True
                    elif risposta[i]==configurazione[20][0][-1] and t==True:
                        risposta[i]=a
                        break
            else:
                risposta=configurazione[-1][0]
                a=trova_ultimo(configurazione[20][0][int(n/2):],configurazione[-1],"s")
                '''if len(configurazione)<50:
                    print(a)'''
                t=False
                for i in range(n):
                    if risposta[i]==a:
                        risposta[i]=configurazione[20][0][0]
                        t=True
                    elif risposta[i]==configurazione[20][0][0] and t==True:
                        risposta[i]=a
                        break

    return risposta

'''FUNZIONI'''

def trova_quartine(c):
    a=[]
    b=[]
    first=True
    for i in range(1,len(c)):
        if first==True and (c[i][1]==(1,0) or c[i][1]==(0,1)):
            first=False
            a+=[c[i][0][-1]]
        elif c[i][1]==(1,1):
            a+=[c[i][0][-1]]
        elif c[i][1]==(0,2) or c[i][1]==(2,0):
            b+=[c[i][0][-1]]
    if len(a)<=len(b):
        return (a,b)
    else:
        return (b,a)

def shift(tent):
    newtent=[]
    for i in range(len(tent)-1):
        newtent+=[tent[i]]
    newtent=[tent[-1]]+newtent
    return newtent

def trova_prox(c20,c):
    #n=len(c)
    a=False
    for i in c20:
        f=False
        #for j in range(22,n):
        if i in c[0]:
            f=True
            #break
        if a==True and f==False:
            return i
        a=f

def trova_ultimo(c20,c,carattere):
    n=len(c[0])
    a=False
    for i in c20:
        f=False
        #for j in range(22,n):
        if carattere=="p":
            if i in c[0][:int(n/2)]:
                ult=i
                f=True
                #break
                #print(ult)
        else:
            if i in c[0][int(n/2):]:
                ult=i
                f=True
        if a==True and f==False:
            return ult
        a=f
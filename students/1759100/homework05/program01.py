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


# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti

a=0 #elemento tupla
b=0 #elemento tupla
s=[] #numeri presenti nella combinazione
lista=[0,1,2,3,4,5,6,7,8,9] #possibili numeri
index=0
controllo=1 #bit di controllo
num1=0 
num2=0 #numero di cui bisogna ricercare la posizione
combinazione=[]
ten=[] #tentativo
h=0 #indice
i=1 #indice
def decodificatore(configurazione):
    global a,b,index,controllo,lista,combinazione,s,num2,num1,i,ten,h,inversi
    if len(configurazione)==1:#resetta le variabili globali
        controllo,i=1,1
        h=0
    lunghezza=configurazione[0]
    if controllo==1:
        lista=[0,1,2,3,4,5,6,7,8,9]
        combinazione,s,ten=[],[],[]
        for _ in range(lunghezza):
            index=lunghezza-1
            combinazione.append('')
            ten.append('')
            controllo-=1
    risposta=[]
    try:
        if len(configurazione)==1:#cerca  gli elementi corretti
            risposta=found(risposta,lista,lunghezza)            
        elif len(s)<lunghezza:
            tentativo,tupla=configurazione[-1]
            a,b=tupla
            if len(s)!=lunghezza:
                if len(lista)==1:
                    s.append(lista[0])
                else:risposta=rintraccia(risposta,lunghezza)
        if len(s)==lunghezza:#cerca tutte le possibili combinazioni
            tentativo,tupla=configurazione[-1]
            c,d=tupla
            if c>=1 or d>=1:
                if (c==1 or d==1):# è appena uscito dal passo precedente oppure il numero non è in posiszione corretta
                    num1=s[0]
                    num2=s[i]
                    a,b=c,d
                    risposta=change(num1,num2)
                elif ((c==2 and d==0) or (c==0 and d==2) ) and i<=lunghezza-2: # il numero scelto è in posiszione corretta
                    i+=1
                    indice_vuoto=combinazione.index(num2)
                    ten[indice_vuoto]=num2
                    a,b=c,d
                    index=lunghezza-1
                    try:
                        num2=s[i]
                        risposta=change(num1,num2,indice_vuoto)
                    except IndexError:
                        pass
                elif ((c==2 and d==0) or (c==0 or d==2)) and ten.count('')==2: #gli ultimi due numeri sono in posiszione corretta
                    indice_vuoto=combinazione.index(num2)
                    ten[indice_vuoto]=num2
                    indice_vuoto1=ten.index('')
                    ten[indice_vuoto1]=num1
                    risposta=ten
                elif (c>=2 and d>=2) or (c>=2 and d>=2): # num2 potrebbe dover essere scambiato con num1
                    t=ten[:]
                    indice_num1=t.index(num1)
                    if h==indice_num1 :
                        h+=1
                    if h<len(combinazione):
                        t[h],t[indice_num1]=t[indice_num1],t[h]
                        risposta=t[:]
                        h+=1                        
    except IndexError:
        pass
    return risposta

def change(num1,num2,ind=0):#tenta le varie posizioni di num2
    global combinazione,index,ten
    a=combinazione[:]
    while ten[index]!='':
        index-=1
    if index>-1:
        for x in range(len(combinazione)):
           a[x]=num1
        combinazione=a[:]
        combinazione[index]=num2
        index-=1
    return combinazione


def rintraccia(risposta,lunghezza):#cerca i possibili elementi della combinazione
    global s,lista
    if a==b and b==0 : 
        if len(lista)==1: #gli elementi sono terminati
            pass 
        else: #riduco la lista
            lista=lista[1:]
            risposta=found(risposta,lista,lunghezza)
    elif a==1 or b==1: # nuovo elemento trovato
        if len(lista)==1:
            s.append(lista[0])
        else:
            s.append(lista[0])
            lista=lista[1:]
            risposta=found(risposta,lista,lunghezza)
    return risposta

def found(risposta,lista,lunghezza): #crea una combinazione di 'f' e un elemento
    for _ in range(lunghezza):
        risposta+=['f']
    risposta[index]=lista[0]
    return risposta
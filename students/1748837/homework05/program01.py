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
coding={}
numbers=[]

def decodificatore(configurazione):
    lConfig=len(configurazione)
    if lConfig==1:
            print('boh')
            coding.clear()
            numbers.clear()
    if lConfig<11 and len(numbers)!=configurazione[0]:
        risposta=[lConfig-1]*configurazione[0]
        return risposta
    else:
        lastTry=configurazione[lConfig-1]
        if lConfig==11:
            setNumbers(getNumbers(configurazione))
            return first2Numbers(lastTry[0],numbers[0],numbers[1])
        if lConfig<(configurazione[0]+11):                              #cerco su tutte le  cifre n 
            if detect(lastTry[1]):
                coding[lConfig-12]=[lastTry[0][lConfig-12]]
                if len(coding.keys())==2:
                    lista=list(coding.keys())
                    coding[lConfig-12]+=[lastTry[0][lista[0]]]
                    coding[lista[0]]+=[coding[lConfig-12][1]]
                    coding[lConfig-12]=coding[lConfig-12][::-1]
            return first2Numbers(lastTry[0],numbers[0],numbers[1])
        if lConfig==(configurazione[0]+11) :                           #faccio un tentativo con una delle mie 2 ipotesi 
            if  detect(lastTry[1]):                                    #controllo se al tentativo precedente o avuto un possibile match sulle 2 cifre
                coding[lConfig-12]=[lastTry[0][lConfig-12]]
                lista=list(coding.keys())
                coding[lConfig-12]+=[lastTry[0][lista[0]]]
                coding[lista[0]]+=[coding[lConfig-12][1]]
                coding[lConfig-12]=coding[lConfig-12][::-1]
            begin=[numbers[2]]*configurazione[0]
            for i in coding.keys():
                begin[i]=coding[i][0]
            return begin
        if lConfig==(configurazione[0]+12):                            #controllo il tentativo precedentemente fatto e seleziono l'ipotesi corretta 
            print(coding)
            if detect(lastTry[1]):
                for i in coding.keys():
                    coding[i]=coding[i][0]
            else:
                for i in coding.keys():
                    coding[i]=coding[i][1]
            print(coding)
            return trying(lastTry[0],numbers[2],numbers[3])
        if lConfig<=(configurazione[0]*2+9):                         #cerco la posizione di un altro numero, conoscendo ormai quella dei primi due trovati
            print(lConfig)
            if detect(lastTry[1]):
                coding[lastTry[0].index(numbers[3])]=numbers[3]
                print(coding)
            return trying(lastTry[0],numbers[2],numbers[3])
        if lConfig<=(configurazione[0]*3+6)and numbers[4] not in coding.values():                           #cerco la posizione di un altro numero, conoscendo ormai quella dei  tre trovati
            print(lConfig)
            if  detect(lastTry[1]) and lConfig==(configurazione[0]*2+10):
                coding[lastTry[0].index(numbers[3])]=numbers[3]
                print(coding)
            if  detect(lastTry[1])and numbers[4] in lastTry[0]:
                coding[lastTry[0].index(numbers[4])]=numbers[4]
                print(coding)
            return trying(lastTry[0],numbers[2],numbers[4])
        if lConfig<=(configurazione[0]*4+2) and numbers[5] not in coding.values():
            print(lConfig,numbers[5] not in coding.values())
            if  detect(lastTry[1]) and lConfig==(configurazione[0]*3+7):
                coding[lastTry[0].index(numbers[4])]=numbers[4]
                print(coding)
            if  detect(lastTry[1])and numbers[5] in lastTry[0]:
                coding[lastTry[0].index(numbers[5])]=numbers[5]
                print(coding)
            return trying(lastTry[0],numbers[2],numbers[5])
        if lConfig<=(configurazione[0]*5-2)and numbers[6] not in coding.values():
            print(lConfig)
            if  detect(lastTry[1]) and lConfig==(configurazione[0]*4+3) and numbers[5] not in coding.values():
                coding[lastTry[0].index(numbers[5])]=numbers[5]
                print(coding)
            if  detect(lastTry[1])and numbers[6] in lastTry[0] :
                coding[lastTry[0].index(numbers[6])]=numbers[6]
                print(coding)
            return trying(lastTry[0],numbers[2],numbers[6])
        if lConfig:
            print(lConfig)
            if  detect(lastTry[1]) and lConfig==(configurazione[0]*5-2)and numbers[6] not in coding.values():
                coding[lastTry[0].index(numbers[6])]=numbers[6]
                print(coding)
            if  detect(lastTry[1])and numbers[7] in lastTry[0] :
                coding[lastTry[0].index(numbers[7])]=numbers[7]
                print(coding)
            return trying(lastTry[0],numbers[2],numbers[7])
            
        
        
        

#funzione di comodo che da i miei tentativi desume quali numeri ci siano nel codice            
def getNumbers(configurazione):
    numbers=[]
    for i in configurazione[1:11]:
        if i[1].count(1)!=0:
            numbers+=[i[0][0]]
    return numbers

#setter per il codice 
def setCoding(index,number):
    coding[index]=number

#setter per i numeri del codice
def setNumbers(num):
    numbers.extend(num)
    

def detect(lastTryR):  
    return lastTryR.__contains__(0)

def first2Numbers(lastTry,numberFixed,number):
    result=[numberFixed]*len(lastTry)
    if lastTry.__contains__(number):
        result[lastTry.index(number)+1]=number
    else:
        result[0]=number
    return result
 
def trying(lastTry,numberFixed,number):
    result=[numberFixed]*len(lastTry)
    for i in coding.keys():
        result[i]=coding[i]
    if lastTry.__contains__(number)and numberFixed in lastTry[lastTry.index(number):] :
        result[lastTry.index(numberFixed,lastTry.index(number))]=number
    else:
        result[result.index(numberFixed)]=number
    return result      
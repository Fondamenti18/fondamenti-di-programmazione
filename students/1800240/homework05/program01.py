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

cifrePresenti = []
cifreAssenti = []
trovate = []
faseProgramma = 0
faseTrovaVerso = True
scorrimentoCifra = 0
testPosizione = 0
sottoFasePrimaCoppia = 0
casoInteressante1 = 0 
casoInteressante2 = 0

def decodificatore(configurazione):

#Dichiaro le variabili globali    
    global faseProgramma
    global cifrePresenti 
    global cifreAssenti
    global trovate
    global casoInteressante1 
    global casoInteressante2
    global sottoFasePrimaCoppia
    global faseTrovaVerso   
    global scorrimentoCifra
    global testPosizione
    
    lunconf = len(configurazione)
    n = configurazione[0]
    ris = []
    
    if lunconf == 1:
        
#Primo turno, qui inizializzo un nuovo gioco
        faseProgramma = 0
        sottoFasePrimaCoppia = -1
        cifrePresenti = []
        cifreAssenti  = []
        ris = []
        
        trovate = []
        for i in range(n):
            trovate.append(-1)
            
        casoInteressante1 = -1
        casoInteressante2 = -1
        faseTrovaVerso = False
        
        for i in range(n):
            ris.append(0)
        scorrimentoCifra = 0
        testPosizione = 0
    
    else:
        
# Non e' il primo turno, quindi comincio ad analizzare la configurazione di gioco
        ld  = lunconf-1
        a = configurazione[ld][1][0]
        b = configurazione[ld][1][1]
        ab = a+b
        maxab = max(a,b)
        
# Con i primi 10 tentativi trovo le cifre che sono presenti nel codice
# e quelle che non lo sono        
        if lunconf <= 11:
            if ab > 0:
                cifrePresenti.append(ld-1)
            else:
                cifreAssenti.append(ld-1)
        if lunconf <= 10:
            ris = []
            for i in range(n):
                ris.append(ld)
            return ris
        
        else:
#            if lunconf == 11:
#                print('Cifre presenti', cifrePresenti)
#                print('Cifre assenti', cifreAssenti)
            
# Completata la ricerca delle cifre presenti e assenti
            
# Entro nella Fase 0, devo tovare la posizione delle prime due cifre
            
#                        if sottoFasePrimaCoppia == 0 : ris = [c2,c1,c1,c1,c1,c1,c1]
#                        if sottoFasePrimaCoppia == 1 : ris = [c1,c2,c1,c1,c1,c1,c1]
#                        if sottoFasePrimaCoppia == 2 : ris = [c1,c1,c2,c1,c1,c1,c1]
#                        if sottoFasePrimaCoppia == 3 : ris = [c1,c1,c1,c2,c1,c1,c1]
#                        if sottoFasePrimaCoppia == 4 : ris = [c1,c1,c1,c1,c2,c1,c1]
#                        if sottoFasePrimaCoppia == 5 : ris = [c1,c1,c1,c1,c1,c2,c1]
#                        if sottoFasePrimaCoppia == 6 : ris = [c1,c1,c1,c1,c1,c1,c2]
            
# Due di queste configurazioni danno come risultato (2,0)/(0,2), le indiviudo e salvo le posizioni
# Una coppia giusta, l'altra invertita            
            
            if faseProgramma == 0:
#                print('Fase 0')
                sottoFasePrimaCoppia += 1
                
                if sottoFasePrimaCoppia > n:
                    faseProgramma = 1
                else:
                    c1 = cifrePresenti[0]
                    c2 = cifrePresenti[1]
                    
                    if sottoFasePrimaCoppia > 0 and sottoFasePrimaCoppia <= n:
                        if maxab == 2:  
                            if casoInteressante1 < 0 :
                                casoInteressante1 = sottoFasePrimaCoppia-1
#                                print('Caso 1:', casoInteressante1)
                            else:
                                casoInteressante2 = sottoFasePrimaCoppia-1    
#                                print('Caso 2:', casoInteressante2)
                    if sottoFasePrimaCoppia <= n:
                        
                        ris = []
                        for i in range(n) :
                            if i == sottoFasePrimaCoppia:
                                ris.append(c2)
                            else:
                                ris.append(c1)
                        
                        if sottoFasePrimaCoppia < n :
                            return ris
                        else :
                            faseProgramma = 1
                            
# Aggiungo una terza cifra conosciuta in tutte le posizioni tranne quelle che ho salvato
# Se ritorna (3,0)/(0,3) le posizioni sono giuste altrimenti vanno invertite
# Salvo le posizoni individuate nella lista 'trovate'                   
            if faseProgramma == 1:
#                print('Fase 1')
                c1 = cifrePresenti[0]
                c2 = cifrePresenti[1]
                c3 = cifrePresenti[2]
                
                if faseTrovaVerso:
                    if maxab == 3:
                        trovate[casoInteressante1] = c1
                        trovate[casoInteressante2] = c2
                    else :
#                        print('/n Inverso')
                        trovate[casoInteressante1] = c2
                        trovate[casoInteressante2] = c1
                   
                    faseProgramma = 2    
                    scorrimentoCifra = 0
                else:
                    ris = []
                    for i in range(n):
                        if i == casoInteressante1:
                            ris.append(c1)
                        else:
                            if i == casoInteressante2:
                                ris.append(c2)
                            else:
                                ris.append(c3)
                   
                    faseTrovaVerso = True
                    return ris
                
# Per determinare la posizione della terza cifra la sostituisco in tutta la sequenza 
# con una cifra NON presente nel codice
# Poi provo la cifra in tutte le posizoni fino ad ottenere (3,0)/(0,3)            
            if faseProgramma == 2:
#                print('Fase 2')
                c3 = cifrePresenti[2]
                cf = cifreAssenti[0]
                
                if scorrimentoCifra > 0:
                   if maxab == 3:
                       trovate[testPosizione] = c3   
                       faseProgramma = 3
                       scorrimentoCifra = 0
                       
                if faseProgramma == 2:
                    
                    ris = []
                    falseAggiunte = 0
                    for i in range(n):
                        if trovate[i] != -1:
                            ris.append(trovate[i])
                        else:
                            if scorrimentoCifra == falseAggiunte:
                                ris.append(c3)
                                testPosizione = i
                            else :   
                                ris.append(cf)
                            falseAggiunte += 1
                            
                    scorrimentoCifra += 1
                    return ris

# Ripeto lo stesso procedimento fino a trovare tutte le cifre del codice          
            if faseProgramma == 3:
#                print('Fase 3')                 
                c3 = cifrePresenti[3]
                cf = cifreAssenti[0]
                
                if scorrimentoCifra > 0:
                   if maxab == 4:
                       trovate[testPosizione] = c3   
                       faseProgramma = 4
                       scorrimentoCifra = 0
                       
                if faseProgramma == 3:
                    
                    ris = []
                    falseAggiunte = 0
                    for i in range(n):
                        if trovate[i] != -1:
                            ris.append(trovate[i])
                        else:
                            if scorrimentoCifra == falseAggiunte:
                                ris.append(c3)
                                testPosizione = i
                            else :   
                                ris.append(cf)
                            falseAggiunte += 1

                    scorrimentoCifra += 1
                    return ris
                
            if faseProgramma == 4:
#                print('Fase 4')
                c3 = cifrePresenti[4]
                cf = cifreAssenti[0]
                
                if scorrimentoCifra > 0:
                   if maxab == 5:
                       trovate[testPosizione] = c3   
                       faseProgramma = 5
                       scorrimentoCifra = 0
                       
                if faseProgramma == 4:
                    
                    ris = []
                    falseAggiunte = 0
                    for i in range(n):
                        if trovate[i] != -1:
                            ris.append(trovate[i])
                        else:
                            if scorrimentoCifra == falseAggiunte:
                                ris.append(c3)
                                testPosizione = i
                            else :   
                                ris.append(cf)
                            falseAggiunte += 1

                    scorrimentoCifra += 1
                    return ris
                
            if faseProgramma == 5:
#                print('Fase 5')
                c3 = cifrePresenti[5]
                cf = cifreAssenti[0]
                
                if scorrimentoCifra > 0:
                   if maxab == 6:
                       trovate[testPosizione] = c3   
                       faseProgramma = 6
                       scorrimentoCifra = 0
                       
                if faseProgramma == 5:
                    
                    ris = []
                    falseAggiunte = 0
                    for i in range(n):
                        if trovate[i] != -1:
                            ris.append(trovate[i])
                        else:
                            if scorrimentoCifra == falseAggiunte:
                                ris.append(c3)
                                testPosizione = i
                            else :   
                                ris.append(cf)
                            falseAggiunte += 1
                       
                    scorrimentoCifra += 1
                    return ris
                
            if faseProgramma == 6:
#                print('Fase 6')
                c3 = cifrePresenti[6]
                cf = cifreAssenti[0]
                
                if scorrimentoCifra > 0:
                   if maxab == 7:
                       trovate[testPosizione] = c3   
                       faseProgramma = 7
                       scorrimentoCifra = 0
                       
                if faseProgramma == 6:
                    
                    ris = []
                    falseAggiunte = 0
                    for i in range(n):
                        if trovate[i] != -1:
                            ris.append(trovate[i])
                        else:
                            if scorrimentoCifra == falseAggiunte:
                                ris.append(c3)
                                testPosizione = i
                            else :   
                                ris.append(cf)
                            falseAggiunte += 1
                       
                    scorrimentoCifra += 1
                    return ris
                
            if faseProgramma == 7:
#                print('Fase 7')
                c3 = cifrePresenti[7]
                cf = cifreAssenti[0]
                
                if scorrimentoCifra > 0:
                   if maxab == 8:
                       trovate[testPosizione] = c3   
                       faseProgramma = 8
                       scorrimentoCifra = 0
                       
                if faseProgramma == 7:
                    
                    ris = []
                    falseAggiunte = 0
                    for i in range(n):
                        if trovate[i] != -1:
                            ris.append(trovate[i])
                        else:
                            if scorrimentoCifra == falseAggiunte:
                                ris.append(c3)
                                testPosizione = i
                            else :   
                                ris.append(cf)
                            falseAggiunte += 1
                       
                    scorrimentoCifra += 1
                    return ris
                
    return ris
    
            
        
            
    

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

cifreOK = []

cifreKO = []

combinazioni = []

''' 
La variabile contiene, ad ogni tentativo, la seguenza di cifreOK e -1
date dal posizionamento degli strike e delle celle ancora incognite del codice:
Esempio l'inizializzazione di un codice a 5 cifre
[-1, -1, -1, -1, -1]
significa che non è stato ancora individuato uno strike
Esempio l'inizializzazione con 2 cifreOK (0, 1)significa
che sono stati trovati 2 strike nelle posizioni indicate dalle cifreOK
[-1, 0, -1, -1, 1]
'''
codicepotenziale = []

'''
La variabile, inzializzata con tanti -1 quante sono le cifre del codice da trovare,
contiene gli strike trovati rappresentati dal numero di cifreOK nelle giuste posizioni
della lista
'''
codicetrovato = []

# Contien il numero di tentativi fatti finora
numerotentativo = 0

# Contiene il numero dei primi 10 tentativi: serve per generare i codici di ricerca delle cifreOK e cifreKO
primi10tentativi = 0

'''
Variabile che contiene le possibili scelte per trovare una combinazione accettabile di risultati.
'''
listatarget = []

target = {}

'''
La variabile 'posizionidisponibili contiente le posizioni ancora disponibili dove
poter tentare di posizionare una cifra.
IL calcolo avviene inizializzando la variabile al numero di cifreKO ancora presenti nella
variabile codicepotenziale (rappresentate dal valore -1) e sottraendo il numero di cifreOK
prensenti nella variabile codicetrovato (rappresentano gli strike certi)
'''
posizionidisponibili = 0

'''
Variabile che contiene la lista delle posizioni assunte dalla cifra cercata.
'''
posizionecorrente = []

# Contatore delle cifre trovate in qualita di strike
numerocifretrovate = 0 

contatoretentativi = 0

def inizializzavariabiliglobali(lunghezzacodicedatrovare):
 
    global combinazioni
    
    global cifreOK
    
    cifreOK = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    global cifreKO
    
    cifreKO = [] 
    
    global codicepotenziale
    
    codicepotenziale = []
    
    for _ in range(0, lunghezzacodicedatrovare):
        
        codicepotenziale.append(-1)
    
    global numerotentativo
    
    numerotentativo = 0
    
    global primi10tentativi 
    
    primi10tentativi = 0
    
    global codicetrovato
    
    codicetrovato = []
    
    for _ in range(0, lunghezzacodicedatrovare):
        
        codicetrovato.append(-1)    

    global target
    
    target = {}
    
    target["A"] = ["A", ((0,0)), ["B", "C"], ()]
    
    target["B"] = ["B", ((1,1), (1,1)), ["D", "E"], ()]

    target["C"] = ["C", ((2,0), (0,2)), ["F", "GH"], ()]

    target["D"] = ["D", ((1,1), (1,1)), [], ()]
    
    target["E"] = ["E", ((2,0), (0,2)), ["L", "M"], ()]
    
    target["F"] = ["F", ((1,1), (1,1)), ["F1", "F2"], ()]
    
    target["F1"] = ["F1", ((1,1), (1,1)), [], ()]
    
    target["F2"] = ["F2", ((2,0), (0,2)), [], ()]
    
    target["GH"] = ["GH", ((2,0), (0,2)), ["N", "GH"], ("CHECKGH")]

    #target["I"] = ["I", ((2,0), (0,2)), [], ()]
    
    target["L"] = ["L", ((1,1), (1,1)), [], ()]
    
    target["M"] = ["M", ((2,0), (0,2)), [], ()]
    
    target["N"] = ["N", ((1,1), (1,1)), [], ()]
    
    target["O"] = ["O", ((1,1), (1,1)), [], ()]

    #target["P"] = ["P", ((1,1), (1,1)), [], ()]
    
    target["X"] = ["X", ((-1,0), (0,-1)), [], ()]
    
    global listatarget
    
    listatarget = []
    
    global cifradatrovare
    
    cifradatrovare = -1
        
    global posizionecorrenteCDT
    
    posizionecorrenteCDT = []    
    
    global numerocifretrovate

    numerocifretrovate = 0
    
    global contatoretentativi
    
    contatoretentativi = 0
        
def decodificatore(configurazione):
    
    global cifreOK
    
    global cifreKO

    global combinazioni
    
    global numerotentativo
    
    global primi10tentativi
    
    global codicetrovato
    
    global cifretrovate
    
    global listatarget
    
    global numerocifretrovate
    
    global codicepotenziale
    
    global cifradatrovare
    
    global posizionecorrenteCDT
    
    global contatoretentativi
    
    # In caso di nuovo codice, la lungheza della variabile configurazione è uguale ad 1
    if len(configurazione) == 1:
        
        inizializzavariabiliglobali(configurazione[0])
    
    else:
        
        # Visualizzo l'ultimo tentaativo ed il risultato ottenuto
        
        print("")
    
    # Se la variabile primi10tentativi e minore di 10
    # allora ancora non ho provato nessuna cifre
    if primi10tentativi < 10:
        
        codicepotenziale = generaprimi10codici(configurazione[0])
        
    else:
            
        # Se la lunghezza del set di cifre ammesse e maggiore della lunghezza del codice
        # allora elimino le cifre inutili dal set di cifre ammesse
        
        if configurazione[0] < len(cifreOK):
            
            if len(configurazione) > 1:
                
                eliminacifreinutili(configurazione, configurazione[0])
        
        if len(cifreOK) == configurazione[0]:
            
            print("----------------------------------------------------------------------------")
            
            if codicetrovato != [-1, -1, -1, -1,-1]:
                
                print("CODICE TROVATO:", codicetrovato)
            #print("Ultimo tentativo", configurazione[len(configurazione) - 1])
            #print("------------")
            
            # Se sono qui, ho trovato le cfreOK e sono pronto a cercare le possibili combinazioni
            
            '''
            Dalla seconda cifra in avanti, vale sempre la ricerca del singolo strike
            '''
            if numerocifretrovate > 0: 
            
                esitocontrollorisultato = checkrisultato(configurazione[len(configurazione) - 1][1])
                
                if esitocontrollorisultato == "X":
                    
                    print("CONFIGURAZIONE:", configurazione[len(configurazione) - 1][0])
                    
                    print("CASO X")
                    
                    # La n cifra e in strike
                    
                    numerocifretrovate += 1
                        
                    codicetrovato[posizionecorrenteCDT[len(posizionecorrenteCDT) - 1]] = cifradatrovare   
                    
                    codicepotenziale = codicetrovato[:]
                        
                    listatarget = ["X"]
                    
                    for _ in cifreOK:
                        
                        if _ not in codicetrovato:
                            
                            cifradatrovare = _
                            
                            break

                    codicepotenziale = posizionacifra(codicepotenziale, cifradatrovare, cifreOK)
                    
                    posizionecorrenteCDT = []
                    
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare))
                
                else:
                
                    codicepotenziale = muovicifra(codicepotenziale, cifradatrovare, cifreOK)
                
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare))
                
            '''
            Primo caso che si verifica temporalmente: numerocifretrovate 0 (ancora non ho fatto nessun tentativo)
            lunghezza dei risultati dei tentativi 0 (non avendo fatto nessun tentativo non ho neanche i risultati)
            '''
            if numerocifretrovate == 0 and contatoretentativi < 12:
                                                
                listatarget = ["B", "C"]
                
                codicepotenziale = primotentativo(configurazione[0])
                
                cifradatrovare = cifreOK[1]
                
                posizionecorrenteCDT.append(1)
                
                contatoretentativi = 11
                
                print("CASO A")
                
            '''
            Secondo caso che si verifica temporalmente: non ho ancora trovate nessuna cifra, ma ho a disposizione
            un risultato di un tentativo (l'undicesimo). L'unica operazione necessaria e verificare
            i risultati traget ("B" e "C")
            '''
            if numerocifretrovate == 0 and contatoretentativi == 12:
                                
                esitocontrollorisultato = checkrisultato(configurazione[len(configurazione) - 1][1])
                
                if esitocontrollorisultato == "B":
                    
                    print("CASO B")
                    
                    listatarget = ["D", "E"]
                
                elif esitocontrollorisultato == "C":
                    
                    print("CASO C")
                    
                    listatarget = ["F", "GH"]
                
                codicepotenziale = muovicifra(codicepotenziale, cifradatrovare, cifreOK)
                
                posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare)) 
                               
                 
            '''
            Terzo caso che si verifica temporalmente: non ho ancora trovato nessuna cifra ma ho a disposizione gia due risultati
            Analizzo il secondo risultato (ultimo in fatto temporale) per capire se posso gia considerare strike qualche cifra
            '''            
            if numerocifretrovate == 0 and contatoretentativi == 13:
            
                esitocontrollorisultato = checkrisultato(configurazione[len(configurazione) - 1][1])
                
                if esitocontrollorisultato == "D":
                    
                    print("CASO D")
                    # I cifra in strike gia dall'inizio
                    
                    codicetrovato[0] = codicepotenziale[0]
                    
                    numerocifretrovate = 1
                    
                    listatarget = ["X"]
                    
                    codicepotenziale = muovicifra(codicepotenziale, cifradatrovare, cifreOK)
                
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare))   
                 
                elif esitocontrollorisultato == "E":
                    
                    print("CASO E")
                    
                    listatarget = ["L", "M"]
                    
                    codicepotenziale = muovicifra(codicepotenziale, cifradatrovare, cifreOK)
                
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare))   
               
                elif esitocontrollorisultato == "F":
                    
                    print("CASO F")
                    
                    listatarget = ["F1", "F2"]
                    
                    codicepotenziale = muovicifra(codicepotenziale, cifradatrovare, cifreOK)
                
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare))   
                                    
                elif esitocontrollorisultato == "GH":
                
                    print("CASO GH")
                    
                    # Se la I e II cifre sono in posizioni note, sono entrambe in strike
                    
                    if codicepotenziale[0] == cifreOK[1] and codicepotenziale[1] == cifreOK[0]:
                        
                        numerocifretrovate = 2
                        
                        codicetrovato[0] = codicepotenziale[0]
                        
                        codicetrovato[1] = codicepotenziale[1]
                        
                        codicepotenziale = codicetrovato[:]
                        
                        cifradatrovare = cifreOK[2]
                        
                        codicepotenziale = posizionacifra(codicepotenziale, cifradatrovare, cifreOK)
                    
                        posizionecorrenteCDT = []
                    
                        posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare))
                        
                        listatarget = ["X"]
                
                    else:
                        
                        listatarget = ["O", "GH"]
                        
                        codicepotenziale = muovicifra(codicepotenziale, cifradatrovare, cifreOK)
                
                        posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare)) 
                    
            '''
            Altro caso che si puo verificare temporalmente: se non ho ancora trovato nessuna cifra ma ho a disposizione gia tre risultati
            Analizzo il terzo risultato (ultimo in fatto temporale) per capire se posso gia considerare strike qualche cifra
            '''            
            if numerocifretrovate == 0 and contatoretentativi == 14:
                
                esitocontrollorisultato = checkrisultato(configurazione[len(configurazione) - 1][1])
                
                if esitocontrollorisultato == "F1":
                    
                    print("CASO F1")
                
                    # II cifra strike 2 posizioni precedenti
                
                    numerocifretrovate = 1
                    
                    codicetrovato[posizionecorrenteCDT[len(posizionecorrenteCDT) - 3]] = cifradatrovare
                    
                    codicepotenziale[posizionecorrenteCDT[len(posizionecorrenteCDT) - 1]] = -1
                    
                    cifradatrovare = cifreOK[0]
                    
                    posizionecorrenteCDT = []
                    
                    codicepotenziale = posizionacifra(codicepotenziale, cifradatrovare, cifreOK)
                    
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare)) 

                    listatarget = ["X"]
                    
                elif esitocontrollorisultato == "F2":
                    
                    print("CASO F2")
                
                    # II cifra strike posizione precedente
                
                    numerocifretrovate = 1
                    
                    codicetrovato[posizionecorrenteCDT[len(posizionecorrenteCDT) - 2]] = cifradatrovare
                    
                    codicepotenziale[posizionecorrenteCDT[len(posizionecorrenteCDT) - 2]] = cifradatrovare
                    
                    codicepotenziale[posizionecorrenteCDT[len(posizionecorrenteCDT) - 1]] = -1
                    
                    cifradatrovare = cifreOK[0]
                    
                    posizionecorrenteCDT = []
                    
                    #codicepotenziale = posizionacifra(codicepotenziale, cifradatrovare, cifreOK)
                    
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare)) 

                    listatarget = ["X"]
                                    
                elif esitocontrollorisultato == "L":
                    
                    print("CASO L")
                    
                    # I cifra strike, II cifra in strike posizione precedente
                    
                    numerocifretrovate = 2
                    
                    codicetrovato[0] = codicepotenziale[0]
                    
                    codicetrovato[posizionecorrenteCDT[len(posizionecorrenteCDT) - 2]] = cifradatrovare                    
                    
                    codicepotenziale = codicetrovato[:]
                    
                    cifradatrovare = cifreOK[2]
                    
                    posizionecorrenteCDT = []
                    
                    codicepotenziale = posizionacifra(codicepotenziale, cifradatrovare, cifreOK)
                    
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare)) 

                    listatarget = ["X"]
                
                elif esitocontrollorisultato == "M":
                    
                    print("CASO M")
                    
                    # II cifra in strike all'inizio
                    
                    numerocifretrovate = 1
                    
                    codicetrovato[1] = cifradatrovare
                    
                    codicepotenziale[1] = cifradatrovare
                                        
                    codicepotenziale[posizionecorrenteCDT[len(posizionecorrenteCDT) - 1]] = -1 
                    
                    cifradatrovare = cifreOK[0]
                    
                    posizionecorrenteCDT = []
                    
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare)) 
                    
                    listatarget = ["X"]
                
                elif esitocontrollorisultato == "N":
                    
                    print("CASO N")
                    
                    # II cifra in strike 
                    
                    numerocifretrovate = 1
                        
                    codicetrovato[posizionecorrenteCDT[len(posizionecorrenteCDT) - 1]] = cifradatrovare                    
                    
                    cifradatrovare = cifreOK[0]
                    
                    posizionecorrenteCDT = []
                    
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare)) 
                    
                    listatarget = ["X"]
                
                elif esitocontrollorisultato == "O":
                
                    print("CASO O")
                    
                    # II cifra in strike 
                    
                    numerocifretrovate = 1
                    
                    codicetrovato[posizionecorrenteCDT[len(posizionecorrenteCDT) - 1]] = cifradatrovare                    
                    
                    cifradatrovare = cifreOK[0]
                    
                    posizionecorrenteCDT = []
                    
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare)) 
                    
                    listatarget = ["X"]
                    
                elif esitocontrollorisultato == "GH":
                
                    print("CASO GH")
                    
                    # Se la I e II cifre sono in posizioni note, sono entrambe in strike
                    
                    if codicepotenziale[0] == cifreOK[1] and codicepotenziale[1] == cifreOK[0]:
                        
                        numerocifretrovate = 2
                        
                        codicetrovato[0] = codicepotenziale[0]
                        
                        codicetrovato[1] = codicepotenziale[1]
                        
                        codicepotenziale = codicetrovato[:]
                        
                        cifradatrovare = cifreOK[2]
                        
                        codicepotenziale = posizionacifra(codicepotenziale, cifradatrovare, cifreOK)
                    
                        posizionecorrenteCDT = []
                    
                        posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare))
                        
                        listatarget = ["X"]
                
                    else:
                        
                        listatarget = ["O", "GH"]
                        
                        codicepotenziale = muovicifra(codicepotenziale, cifradatrovare, cifreOK)
                
                        posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare)) 

            '''
            Ultimo caso possibile, con vari tentativi di spostamento
            '''           
            if numerocifretrovate == 0 and contatoretentativi > 14:
                
                esitocontrollorisultato = checkrisultato(configurazione[len(configurazione) - 1][1])
                
                if esitocontrollorisultato == "O":
                    
                    print("CASO O")
                    
                    # II cifra in strike 
                    
                    numerocifretrovate += 1
                        
                    codicetrovato[posizionecorrenteCDT[len(posizionecorrenteCDT) - 1]] = cifradatrovare

                    cifradatrovare = cifreOK[0]
                    
                    posizionecorrenteCDT = []
                    
                    posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare))
                        
                    listatarget = ["X"]
                    
                elif esitocontrollorisultato == "GH":   
                
                    print("CASO GH")
                    
                    # Se la I e II cifre sono in posizioni note, sono entrambe in strike
                    
                    if codicepotenziale[0] == cifreOK[1] and codicepotenziale[1] == cifreOK[0]:
                        
                        numerocifretrovate = 2
                        
                        codicetrovato[0] = codicepotenziale[0]
                        
                        codicetrovato[1] = codicepotenziale[1]
                        
                        codicepotenziale = codicetrovato[:]
                        
                        cifradatrovare = cifreOK[2]
                        
                        codicepotenziale = posizionacifra(codicepotenziale, cifradatrovare, cifreOK)
                    
                        posizionecorrenteCDT = []
                    
                        posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare))
                    
                        listatarget = ["X"]
                
                    else:
                        
                        listatarget = ["O", "GH"]
                        
                        codicepotenziale = muovicifra(codicepotenziale, cifradatrovare, cifreOK)
                
                        posizionecorrenteCDT.append(trovaposizionecifra(codicepotenziale, cifradatrovare)) 
             
                
    contatoretentativi += 1
    
    print("CODICE PROVA:", codicepotenziale)
    return codicepotenziale    






        
def generacombinazione(ncifre):
    
    combinazione=[]
    
    global cifreOK  
    
    x=cifreOK
    
    for _ in range(ncifre):
    
        y=random.choice(x)
        
        while y in combinazione:
            
            y=random.choice(x)    
        
        combinazione+=[int(y)]
        
    return combinazione
    




def eliminacifreinutili(configurazione, numeromassimocifre):
    
    global cifreKO
    
    global cifreOK
    
    for _ in range(1, len(configurazione)):
        
        tentativo, risultato = configurazione[_]
        
        if risultato == (0, 0):
            
            for _ in tentativo:
                
                if _ in cifreOK:
               
                    cifreOK.remove(_) 
                    
                    cifreKO.append(_)
                        
        elif risultato[0] + risultato[1] == numeromassimocifre:
            
            cifreOK.append(list(tentativo))





            
def primotentativo(lunghezzacodice):
    
    global cifreOK
    
    global cifreKO
    
    tempcodice = [cifreOK[0], cifreOK[1]]
    
    for _ in range(2, lunghezzacodice):
        
        tempcodice.append(-1)
        
    return tempcodice






def generaprimi10codici(lunghezzacodice):
    
    global primi10tentativi
    
    tmpcodice = []
    
    for _ in range(0, lunghezzacodice):
        
        tmpcodice.append(primi10tentativi)
        
    primi10tentativi += 1
    
    return tmpcodice






'''
Funzione che restiusce la posizione di una cifra all'interno di una lista.
Se la cifra non esiste, restitusce -1
'''
def trovaposizionecifra(codice, cifra):
    
    for _ in range(0, len(codice)):
        
        if codice[_] == cifra:
            
            return _
        
    return -1

'''
Funzione che posiziona una cifra nella prima posizione disponibile (rappresentata da una cifra -1)
'''
def posizionacifra(codice, cifradaposizionare, cifreOK):
    
    ppd = trovaposizionecifra(codice, -1)
    
    if ppd != -1:
        
        codice[ppd] = cifradaposizionare
        
    return codice
    
def muovicifra(codice, cifra, cifreOK):
    
    posizionecorrente = trovaposizionecifra(codice, cifra)
    
    if posizionecorrente == -1:
        
        codice[0] = cifra
        
    else:
    
        if posizionecorrente == len(codice) - 1:
            
            if codice[0] in cifreOK:
                
                codice[1] = codice[0]
                
            codice[0] = cifra
                
            codice[posizionecorrente] = -1
    
        else:
                        
            if codice[posizionecorrente + 1] in cifreOK:
                
                for _ in range(posizionecorrente, len(codice)):
                    
                    if not codice[_] in cifreOK:
                
                        codice[_] = cifra
                        
                        codice[posizionecorrente] = -1
                        
                        break
             
            else:
            
                codice[posizionecorrente] = -1
                
                codice[posizionecorrente + 1] = cifra
            
    return codice
    
    
    
    
    
def checkrisultato(risultato):
    
    global listatarget
    
    global target
    
    if listatarget[0] != "X":
        
        for letteratarget in listatarget:
            
            if risultato in target[letteratarget][1]:
            
                return letteratarget
    
        return ""
    
    else:
        
        if risultato[0] == 0 or risultato[1] == 0:
        
            return "X"
        
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

import copy

def decodificatore(conf):
    
    configurazione = copy.deepcopy(conf)
    
    tentativo = []
    lunghezzaCodice = configurazione[0]
    configurazione.pop(0)
    if len(configurazione) == 0:
        for j in range(lunghezzaCodice):
            tentativo.append(0)
    else:
        posUltimoTentativo = len(configurazione)-1
        
        esitoUltimoTentativo = configurazione[posUltimoTentativo][1]
        totEsitoUltimoTentativo = esitoUltimoTentativo[0]+esitoUltimoTentativo[1]
        ultimoTentativo = configurazione[posUltimoTentativo][0]
        cifreDistinte = {}
        numCifreDistinte = 0
        for i in range(len(ultimoTentativo)):
            if cifreDistinte.get(ultimoTentativo[i], None) == None:
                cifreDistinte[ultimoTentativo[i]] = True
                numCifreDistinte+=1

        if totEsitoUltimoTentativo==0:
            for j in range(lunghezzaCodice):
                tentativo.append(ultimoTentativo[j]+1)
                
        else:
            
            if totEsitoUltimoTentativo%2==0:
                if numCifreDistinte == totEsitoUltimoTentativo:
                    tentativoFratelliEsatti1 = False
                    tentativoFratelliEsatti2 = False
                    fratelloMinore = 0
                    fratelloMaggiore = 0
                    for i in range(len(ultimoTentativo)):
                        if fratelloMaggiore < ultimoTentativo[i]:
                            if fratelloMinore < fratelloMaggiore:
                                fratelloMinore = fratelloMaggiore
                            fratelloMaggiore = ultimoTentativo[i]
                        else:
                            if fratelloMinore < ultimoTentativo[i] and ultimoTentativo[i] < fratelloMaggiore:
                                fratelloMinore = ultimoTentativo[i]
                                
                    for i in range(posUltimoTentativo, -1, -1):
                        esitoTentativoIesimo = configurazione[i][1]
                        totEsitoTentativoIesimo = esitoTentativoIesimo[0]+esitoTentativoIesimo[1]
                        if totEsitoTentativoIesimo == totEsitoUltimoTentativo:
                            if esitoTentativoIesimo[0]%2== 0 and esitoTentativoIesimo[1]%2 == 0:
                                if tentativoFratelliEsatti1:
                                    tentativoFratelliEsatti2 = configurazione[i][0]
                                else:
                                    tentativoFratelliEsatti1 = configurazione[i][0]
                        else:
                            break
                
                    if tentativoFratelliEsatti1 and tentativoFratelliEsatti2:
                        posFratelloMinore = tentativoFratelliEsatti1.index(fratelloMinore)
                        posFratelloMaggiore = tentativoFratelliEsatti2.index(fratelloMinore)
                        for j in range(lunghezzaCodice):
                            if ultimoTentativo[j] < fratelloMinore:
                                tentativo.append(ultimoTentativo[j])
                            elif j==posFratelloMinore:
                                tentativo.append(fratelloMinore)
                            elif j==posFratelloMaggiore:
                                tentativo.append(fratelloMaggiore)
                            else:
                                tentativo.append(fratelloMaggiore+1)
                                
                    else:
                        posFratelloMinore = ultimoTentativo.index(fratelloMinore)
                        fratelloMinoreInserito = False
                        for j in range(lunghezzaCodice):
                            if ultimoTentativo[j] < fratelloMinore:
                                tentativo.append(ultimoTentativo[j])
                            elif j > posFratelloMinore and (not fratelloMinoreInserito):
                                tentativo.append(fratelloMinore)
                                fratelloMinoreInserito = True
                            else:
                                tentativo.append(fratelloMaggiore)
                            
                else:
                    cifraMaggiore = 0;
                    for i in range(lunghezzaCodice):
                        if cifraMaggiore < ultimoTentativo[i]:
                            cifraMaggiore = ultimoTentativo[i]
    
                    for j in range(lunghezzaCodice):
                        if cifraMaggiore == ultimoTentativo[j]:
                            tentativo.append(cifraMaggiore+1)
                        else:
                            tentativo.append(ultimoTentativo[j])
                            
            else:
                if totEsitoUltimoTentativo == 1:
                    tentativo.append(ultimoTentativo[0])
                    for j in range(1, lunghezzaCodice):
                        tentativo.append(ultimoTentativo[j]+1)

                else:
                    penultimoTentativo = configurazione[posUltimoTentativo-1]
                    if (penultimoTentativo[1][0] + penultimoTentativo[1][1]) %2==0:
                        cambioPosizioneVecchiFratelli = False
                        if( (totEsitoUltimoTentativo == 3 and (esitoUltimoTentativo[0] == 1 or esitoUltimoTentativo[1] == 1)) or (totEsitoUltimoTentativo > 3 and (esitoUltimoTentativo[0] == 2 or esitoUltimoTentativo[1] == 2)) ):
                            cambioPosizioneVecchiFratelli = True
                        vecchioFratelloMinore = 0
                        vecchioFratelloMaggiore = 0
                        fratelloCorrente = 0
                        for i in range(len(ultimoTentativo)):
                            if fratelloCorrente < ultimoTentativo[i]:
                                if vecchioFratelloMaggiore < fratelloCorrente:
                                    if vecchioFratelloMinore < vecchioFratelloMaggiore:
                                        vecchioFratelloMinore = vecchioFratelloMaggiore
                                    vecchioFratelloMaggiore = fratelloCorrente
                                fratelloCorrente = ultimoTentativo[i]
                            elif vecchioFratelloMaggiore < ultimoTentativo[i] and ultimoTentativo[i] < fratelloCorrente:
                                if vecchioFratelloMinore < vecchioFratelloMaggiore:
                                    vecchioFratelloMinore = vecchioFratelloMaggiore
                                vecchioFratelloMaggiore = ultimoTentativo[i]
                            elif vecchioFratelloMinore < ultimoTentativo[i] and ultimoTentativo[i] < vecchioFratelloMaggiore:
                                vecchioFratelloMinore = ultimoTentativo[i]
                                
                        posVecchioFratelloMinore = ultimoTentativo.index(vecchioFratelloMinore);
                        posVecchioFratelloMaggiore = ultimoTentativo.index(vecchioFratelloMaggiore);
                        fratelloCorrenteInserito = False;
                        for j in range(lunghezzaCodice):
                            if j==posVecchioFratelloMinore and cambioPosizioneVecchiFratelli:
                                tentativo.append(vecchioFratelloMaggiore)
                            elif j==posVecchioFratelloMaggiore and cambioPosizioneVecchiFratelli:
                                tentativo.append(vecchioFratelloMinore)
                            elif ultimoTentativo[j] != fratelloCorrente:
                                tentativo.append(ultimoTentativo[j])
                            elif fratelloCorrenteInserito:
                                tentativo.append(fratelloCorrente+1)
                            else:
                                tentativo.append(fratelloCorrente)
                                fratelloCorrenteInserito = True
                                
                    else:
                        cifraMaggiore = 0
                        for i in range(lunghezzaCodice):
                            if cifraMaggiore < ultimoTentativo[i]:
                                cifraMaggiore = ultimoTentativo[i]
                                
                        for j in range(lunghezzaCodice):
                            if cifraMaggiore == ultimoTentativo[j]:
                                tentativo.append(cifraMaggiore+1)
                            else:
                                tentativo.append(ultimoTentativo[j])
                                
    print("TENTATIVO", tentativo)
                                
    return tentativo

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
il numero 3 e' dovuto alle cifre 3,4,5 che compaiono tra le cifre del tentativo ma mai al posto giusto.

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
from itertools import permutations

# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti
primocheck=True
trova=True
primo=True
case=False
guessl=False
manda=False
secondo=False
vai=False
noNum=10
guessRand=False
lnumeri=[0,1,2,3,4,5,6,7,8,9]
listacandidati=[]
lnumcodice=[]
listaPerm=[]
slnumcodice=''
contRiprova=0
cont=0
fix=True
afix=0
bfix=0
distapp=0
permuta=True
tent_be=[]
srandom=''
appoggio=0
checkmin=False
contapp=0

def decodificatore(configurazione):
    global contRiprova, trova, noNum, guessRand, slnumcodice, listaPerm, case, listacandidati, guessl, cont
    global permuta, primo, vai, manda, secondo, fix, afix, bfix, tent_be, srandom, appoggio, lnumcodice, checkmin, contapp, primocheck
    ####trovare numero non presente nel codice
    if type(configurazione[len(configurazione)-1])==int:
        if primo==True or manda==True:
            #print('NUOVO CODICE')
            appoggio=configurazione[len(configurazione)-1]

            configurazione=[]
            configurazione.append(appoggio)

            primocheck=True
            trova=True
            contRiprova=0
            guessRand=False
            manda=False
            primo=True
            fix=True
            afix=0
            bfix=0
            lnumcodice=[]
            slnumcodice=''
            listaPerm=[]
            cont=0
            permuta=True
            distapp=0
            contapp=0
            checkmin=False



    if trova==True:
        ##print('entro trova', trova)
        if len(configurazione)>1:
            tent_be, tupla=configurazione[len(configurazione)-1]
            a, b=tupla
            if a+b==0:
                noNum=lnumeri[contRiprova]
                ####print('metto false  uguale a 0')
                trova=False
            else:
                lnumcodice.append(lnumeri[contRiprova])
                slnumcodice+=str(lnumeri[contRiprova])
                contRiprova+=1

        if trova==True:
            tent_be=[]
            lungCodice=configurazione[0]
            for _ in range (0,lungCodice):
                tent_be.append(lnumeri[contRiprova])
            ##print(tent_be)
            return tent_be
    ########################################

    if guessRand==False:
        tent_be, tupla=configurazione[len(configurazione)-1]
        a, b=tupla

        if a+b==0:
            ####print('0')
            tent_be.pop()
            if contRiprova<9:
                contRiprova+=1
                tent_be.append(lnumeri[contRiprova])
            else: guessRand=True

        elif a+b==1:
            ####print('1')
            numcodice=tent_be.pop()
            lnumcodice.append(numcodice)
            slnumcodice+=str(numcodice)

            if contRiprova<9:
                contRiprova+=1
                tent_be.append(lnumeri[contRiprova])
            else:
                guessRand=True
                ##print('finito, --> codici che somo presenti:', lnumcodice)
        if guessRand==False:
            return tent_be

    n=configurazione[0]
    tent_be, tupla=configurazione[len(configurazione)-1]
    a, b=tupla

    def confronto(tent, tentP):

        lunghezza=0
        for _ in range(0, configurazione[0]):
            ##print(_)
            elementotentP=int(tentP[_])
            if tent[_]!=elementotentP:
                lunghezza+=1
        ##print('confronto',tent,'con', tentP,'la dist:',lunghezza)
        return lunghezza



    def distanza(a, b, n):
        if n==6:
            if a==6 or b==6:
                return 6
            elif a==5 or b==5:
                return 5
            elif a==4 or b==4:
                return 4
            elif a==3 or b==3:
                return 3
        if n==7:
            if a==7 or b==7:
                return 7
            elif a==6 or b==6:
                return 6
            elif a==5 or b==5:
                return 5
            elif a==4 or b==4:
                return 4
        if n==7:
            if a==7 or b==7:
                return 7
            elif a==6 or b==6:
                return 6
            elif a==5 or b==5:
                return 5
            elif a==4 or b==4:
                return 4
        if n==8:
            if a==8 or b==8:
                return 8
            if a==7 or b==7:
                return 7
            elif a==6 or b==6:
                return 6
            elif a==5 or b==5:
                return 5
            elif a==4 or b==4:
                return 4



    if manda==True:
        '''if fix==True:
            tent_be, tupla=configurazione[len(configurazione)-2]
            afix, bfix=tupla
            fix=False'''
        if secondo==True:
            ##print(cont)
            '''risposta=listacandidati[cont]#int(contrandom)]
            cont+=1'''
            '''if distanza(a, b, n)<distanza(afix, bfix , n):
                #print(distanza(a, b, n),'minore di',distanza(afix, bfix , n))
                afix=a
                bfix=b
                vai=True
                #fix=True'''
            #else:
            if cont==len(listacandidati):
                #print('candidati finiti perche cont->',cont,'/',len(listacandidati))
                risposta='Finiti'
                #return risposta
            else:
                '''contrandom=random.choice(srandom)
                while contrandom=='':
                    contrandom=random.choice(srandom)
                srandom.replace(contrandom,'')'''
                #print('cont di risposta',cont)
                risposta=listacandidati[cont]#int(contrandom)]
                cont+=1



    if guessRand==True:
        #print('\n\nnumeri che compongono il codice da ',configurazione[0],'cifre',lnumcodice, 'str :', slnumcodice)
        n=configurazione[0]
        tent_be1, tupla=configurazione[len(configurazione)-1]
        a1, b1=tupla

        '''if a1==5 or b1==5:
            if primo==True:
                primo=False
                #vai=True'''

        if checkmin==True:
            #print('checkmin0',checkmin)
            tent_be2, tupla2=configurazione[len(configurazione)-2]
            a2, b2= tupla2
            #print(tupla2, tupla, distanza(a2,b2, n), distanza(a, b, n))
            '''if distanza(a, b, n)!=distanza(a2, b2 , n):
                dist1=distanza(a, b, n)
                dist2=distanza(a2, b2 , n)
                #print(dist1,'diverso', dist2)
                #checkmin=False
                primo=False
                vai=True
                #return'''
            dist1=distanza(a, b, n)
            dist2=distanza(a2, b2 , n)
            if distanza(a, b, n)==distanza(a2, b2 , n) and primo==True:
                #print(dist1,'uguale', dist2)
                pass
            else:
                dist1=distanza(a, b, n)
                dist2=distanza(a2, b2 , n)
                #print(dist1,'diverso', dist2)
                #checkmin=False
                primo=False
                vai=True



        '''if manda==False:
            tent_be, tupla=configurazione[len(configurazione)-1]
            a, b=tupla'''

        if permuta==True:
            permuta=False
            #print('creo lista combinazioni di ', slnumcodice)
            listaPerm=list(permutations(lnumcodice))

        if vai==True:

            #dist=distanza(a, b, n)
            #print('nuove distanze', dist1, dist2)
            #listacandidati=[]
            #print('creo lista candidati :')#, listacandidati)
            ##print('confronto',per,'con',tent_be,'- dist= ', dist)
            ##print('primocheck',primocheck)
            if primocheck==True:

                listacandidati=[]
                for per in listaPerm:
                    if n==6:
                        if dist1==4 and dist2==4:
                            if confronto(per, tent_be1)==4 or confronto(per, tent_be1)==2:
                                if confronto(per, tent_be2)==4 or confronto(per, tent_be2)==2:
                                    #print(per,'dista',dist1,'da',tent_be1,'e', 4, 'o', 2 ,'da ', tent_be2)
                                    ##print(per,'dist =', dist)
                                    listacandidati.append(per)
                        if dist1==4 or dist2==4:
                            if dist1==4:
                                distapp=dist1
                                dist1=dist2
                                dist2=distapp#dist2=4
                                tentappo=tent_be1
                                tent_be1=tent_be2
                                tent_be2=tentappo#tent_be2=4
                            if confronto(per, tent_be1)==dist1:
                                if confronto(per, tent_be2)==4 or confronto(per, tent_be2)==2:
                                    #print(per,'dista',dist1,'da',tent_be1,'e', 4, 'o', 2 ,'da ', tent_be2)
                                    ##print(per,'dist =', dist)
                                    listacandidati.append(per)
                        else:
                            if confronto(per, tent_be1)==dist1 and confronto(per, tent_be2)==dist2:
                                #print(per,'dista',dist1,'da',tent_be1,'e',dist2 ,'da ', tent_be2)
                                ##print(per,'dist =', dist)
                                listacandidati.append(per)
                    if n==7:

                        if dist1==4 or dist2==4:
                            ##print('dis1', dist1,'dist2',dist2)
                            if dist1==4:
                                distapp=dist1
                                dist1=dist2
                                dist2=distapp#dist2=4
                                tentappo=tent_be1
                                tent_be1=tent_be2
                                tent_be2=tentappo#tent_be2=4
                                if confronto(per, tent_be1)==dist1:
                                    if confronto(per, tent_be2)==4 or confronto(per, tent_be2)==3:
                                        #print(per,'dista',dist1,'da',tent_be1,'e', 4, 'o', 3 ,'da ', tent_be2)
                                        ##print(per,'dist =', dist)
                                        listacandidati.append(per)

                        if dist1==5 or dist2==5:
                            ##print('dis1', dist1,'dist2',dist2)
                            if dist1==5:
                                distapp=dist1
                                dist1=dist2
                                dist2=distapp#dist2=5
                                tentappo=tent_be1
                                tent_be1=tent_be2
                                tent_be2=tentappo#tent_be2=5
                            if confronto(per, tent_be1)==dist1:
                                if confronto(per, tent_be2)==5 or confronto(per, tent_be2)==2:
                                    #print(per,'dista',dist1,'da',tent_be1,'e', 5, 'o', 2 ,'da ', tent_be2)
                                    ##print(per,'dist =', dist)
                                    listacandidati.append(per)

                        else:
                            if confronto(per, tent_be1)==dist1 and confronto(per, tent_be2)==dist2:
                                #print(per,'dista',dist1,'da',tent_be1,'e',dist2 ,'da ', tent_be2)
                                ##print(per,'dist =', dist)
                                listacandidati.append(per)
                    if n==8:
                        if dist1==6 or dist2==6:
                            ##print('dis1', dist1,'dist2',dist2)
                            if dist1==6:
                                distapp=dist1
                                dist1=dist2
                                dist2=distapp#dist2=4
                                tentappo=tent_be1
                                tent_be1=tent_be2
                                tent_be2=tentappo#tent_be2=4
                                if confronto(per, tent_be1)==dist1:
                                    if confronto(per, tent_be2)==6 or confronto(per, tent_be2)==2:
                                        #print(per,'dista',dist1,'da',tent_be1,'e', 6, 'o', 2 ,'da ', tent_be2)
                                        ##print(per,'dist =', dist)
                                        listacandidati.append(per)

                        if dist1==5 or dist2==5:
                            ##print('dis1', dist1,'dist2',dist2)
                            if dist1==5:
                                distapp=dist1
                                dist1=dist2
                                dist2=distapp#dist2=5
                                tentappo=tent_be1
                                tent_be1=tent_be2
                                tent_be2=tentappo#tent_be2=5
                            if confronto(per, tent_be1)==dist1:
                                if confronto(per, tent_be2)==5 or confronto(per, tent_be2)==3:
                                    #print(per,'dista',dist1,'da',tent_be1,'e', 5, 'o', 3 ,'da ', tent_be2)
                                    ##print(per,'dist =', dist)
                                    listacandidati.append(per)

                        else:
                            if confronto(per, tent_be1)==dist1 and confronto(per, tent_be2)==dist2:
                                #print(per,'dista',dist1,'da',tent_be1,'e',dist2 ,'da ', tent_be2)
                                ##print(per,'dist =', dist)
                                listacandidati.append(per)


                primocheck=False
            else:
                #print('scrematura')
                #print('lista candidati:', listacandidati)
                #if a==4 or b==4:
                    #print('quattrooooo')
                    
                for candidato in listacandidati:
                    ##print(candidato)
                    #if len(listacandidati)>4:
                    if n==6:
                        if a==4 or b==4:
                            ##print('new scrematura')
                            if confronto(candidato, tent_be1)!=2 and confronto(candidato, tent_be1)!=4:
                                #print(candidato,' eliminato,', confronto(candidato, tent_be1) ,' non e o', 2,' o', 4)
                                listacandidati.remove(candidato)
                        else:
                            if confronto(candidato, tent_be1)!=dist1:
                                #print(candidato,' eliminato, non dista', dist1,' da', tent_be1)
                                listacandidati.remove(candidato)
                    if n==7:
                        if a==5 or b==5:
                            if confronto(candidato, tent_be1)!=5 and confronto(candidato, tent_be1)!=2:
                                #print(candidato,' eliminato,', confronto(candidato, tent_be1) ,' non e o', 5,' o', 2)
                                listacandidati.remove(candidato)
                        elif a==4 or b==4:
                            if confronto(candidato, tent_be1)!=4 and confronto(candidato, tent_be1)!=3:
                                #print(candidato,' eliminato,', confronto(candidato, tent_be1) ,' non e o', 4,' o', 3)
                                listacandidati.remove(candidato)
                        else:
                            if confronto(candidato, tent_be1)!=dist1:
                                #print(candidato,' eliminato, non dista', dist1,' da', tent_be1)
                                listacandidati.remove(candidato)
                    if n==8:
                        if a==6 or b==6:
                            if confronto(candidato, tent_be1)!=6 and confronto(candidato, tent_be1)!=2:
                                #print(candidato,' eliminato,', confronto(candidato, tent_be1) ,' non e o', 6,' o', 2)
                                listacandidati.remove(candidato)
                        elif a==5 or b==5:
                            if confronto(candidato, tent_be1)!=5 and confronto(candidato, tent_be1)!=3:
                                #print(candidato,' eliminato,', confronto(candidato, tent_be1) ,' non e o', 5,' o', 3)
                                listacandidati.remove(candidato)
                        else:
                            if confronto(candidato, tent_be1)!=dist1:
                                #print(candidato,' eliminato, non dista', dist1,' da', tent_be1)
                                listacandidati.remove(candidato)




                ##print('nuova lista candidati', listacandidati,'\n con lughezza', len(listacandidati) )
            cont=0
            manda=True
            '''contrandom=random.choice(srandom)
            risposta=listacandidati[int(contrandom)]'''
            risposta=listacandidati[cont]
            cont+=1
            vai=False
            secondo=True

        if primo==True:
            #print('contapp',contapp)
            if contapp==1:
                checkmin=True
                #primo=False
            contapp+=1
            #primo=False
            #vai=True

            x=slnumcodice
            risposta=[]
            for _ in range(n):
                y=random.choice(x)
                risposta+=[int(y)]
                x=x.replace(y,'')



        return risposta

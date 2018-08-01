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
from math import fabs
import random
import copy
nel_codice = []
codice = {}
non_codice =  {}
non_nelcodice = []
mai_piu = []
numeri_comb=[]
X = '0123456789'
pg = 0
ps = 0
before_pg = 0
before_ps = 0
bbefore_pg = 0
bbefore_ps = 0
via = False
special_case = False
# ESEMPIO di strategia che tira a caso una combinazione di N valori anche ripetuti
# Odio la logica

def decodificatore(configurazione):
    
    n = configurazione[0]
    
    
    if (n % 2) == 0:
        pari = True
    else:
        pari = False

    global nel_codice,codice,non_codice,non_nelcodice,mai_piu,X,pg,ps,via,before_pg,before_ps,numeri_comb,special_case,bbefore_pg, bbefore_ps
    print(codice)
    if len(configurazione) == 1:
        nel_codice = []
        codice = {}
        non_codice =  {}
        non_nelcodice = []
        mai_piu = []
        numeri_comb=[]
        X = '0123456789'
        pg = 0
        ps = 0
        before_pg = 0
        before_ps = 0
        bbefore_pg = 0
        bbefore_ps = 0
        via = False
        special_case = False
        
    check_number(configurazione)
    
    while len(nel_codice) != n:
 
        y = random.choice(X)
        X = X.replace(y,'')    
        risposta = []
    
        for _ in range(n):
            risposta += [int(y)]
        return risposta
    
    else:
        if len(mai_piu) == 0:
            mai_piu += [nel_codice]
            trova_restanti_numeri_non_nel_codice()
            return mai_piu[-1]
        else:
            
            
            bbbbefore_last_code, bbbbefore_suggest = configurazione[-5]
            bbbbefore_tot = bbbbefore_suggest[0] + bbbbefore_suggest[1]
            bbbbefore_sugg1, bbbbefore_sugg2 = bbbbefore_suggest
            
            bbbefore_last_code, bbbefore_suggest = configurazione[-4]
            bbbefore_tot = bbbefore_suggest[0] + bbbefore_suggest[1]
            bbbefore_sugg1, bbbefore_sugg2 = bbbefore_suggest
            
            bbefore_last_code, bbefore_suggest = configurazione[-3]
            bbefore_tot = bbefore_suggest[0] + bbefore_suggest[1]
            bbefore_sugg1, bbefore_sugg2 = bbefore_suggest
            
            before_last_code , before_suggest = configurazione[-2]
            before_tot = before_suggest[0] + before_suggest[1]
            before_sugg1, before_sugg2 = before_suggest
            
            last_code,suggest = configurazione[-1]
            tot = suggest[0] + suggest[1]
            sugg1,sugg2 = suggest
            
            before_via = via



            
            
            if (sugg1 == n) or (sugg2 == n):
                aggiorna_non_codice_0()
                via = True
                
            if sugg1 == 1 or sugg2 == 1 :
                via = True
             
                
            
            
            if via:
            
                if tot < n:
                    
    

                    
                        
                    if tot == 2 and special_case:
                        special_case = False

                        if bbbbefore_sugg1 > pg:
    
                            check_combination_fault_11(last_code,bbbbefore_last_code,suggest,bbbbefore_suggest)
           
                            return combination(n,bbefore_last_code)
                        elif bbbbefore_sugg1 < pg:
           
                            check_combination_fault_1(last_code,bbefore_last_code,suggest,bbefore_suggest)
                
                            return combination(n,bbefore_last_code)
                        
                    if tot == 2:
               
                        if before_pg > pg:
                            bbefore_last_code,bbefore_suggest = find(configurazione[:-2])
                            check_combination_fault_11(last_code,bbefore_last_code,suggest,bbefore_suggest)
               
                            return combination(n,bbefore_last_code)
                        elif before_pg < pg:
                            check_combination_fault_1(before_last_code,last_code,before_suggest,suggest)
                 
                            return combination(n,before_last_code)
                    
                    elif special_case:
                        special_case = False

                        if ((bbefore_sugg1 - 1 == before_sugg1) or (bbefore_sugg1 - 1 == before_sugg2)) and ((bbefore_sugg2 == before_sugg1) or (bbefore_sugg2 == before_sugg2)):
                            if (bbbefore_sugg1 or bbbefore_sugg2) < pg:
                                check_combination_fault_0(last_code,bbbefore_last_code,suggest,bbbefore_suggest,configurazione)
                                return combination(n,bbbefore_last_code)
                            elif (bbbefore_sugg1 or bbbefore_sugg2) > pg:
                                check_combination_fault_00(last_code,bbbbefore_last_code,suggest,bbbbefore_suggest)
                                return combination(n,bbbefore_last_code)
                        elif ((bbefore_sugg1 == before_sugg1) or (bbefore_sugg1 == before_sugg2)) and ((bbefore_sugg2 - 1 == before_sugg1) or (bbefore_sugg2 - 1 == before_sugg2)):
                            if (bbbefore_sugg1 or bbbefore_sugg2) < pg:
                                check_combination_fault_0(last_code,bbbefore_last_code,suggest,bbbefore_suggest,configurazione)
                                return combination(n,bbbefore_last_code)
                            elif (bbbefore_sugg1 or bbbefore_sugg2) > pg:
                                check_combination_fault_00(last_code,bbbefore_last_code,suggest,bbbefore_suggest)
                                return combination(n,bbbbefore_last_code)                     
                        elif ((before_sugg1 - 1 == sugg1) or (before_sugg1 - 1 == sugg2)) and ((before_sugg2 == sugg1) or (before_sugg2 == sugg2)):
                            check_nove9(configurazione)
                            return combination_fault_0(before_last_code,bbbefore_last_code,before_suggest,bbbefore_suggest) 
                        elif ((before_sugg1 == sugg1) or (before_sugg1 == sugg2)) and ((before_sugg2 - 1 == sugg1) or (before_sugg2 - 1 == sugg2)):
                            check_nove9(configurazione)     
                            return combination_fault_0(before_last_code,bbbefore_last_code,before_suggest,bbbefore_suggest)
                        
                    elif before_pg < pg:
                        check_combination_fault_0(last_code,before_last_code,suggest,before_suggest,configurazione)
                        return combination(n,before_last_code)
                    elif before_pg > pg:
                        check_combination_fault_00(last_code,bbefore_last_code,suggest,bbefore_suggest)
                        return combination(n,bbefore_last_code)
                    elif bbefore_pg < pg:           
                        check_combination_fault_0(last_code,before_last_code,suggest,bbefore_suggest,configurazione)        
                        return combination(n,before_last_code)
                    elif bbefore_pg > pg:  
                        check_combination_fault_00(last_code,bbbefore_last_code,suggest,bbbefore_suggest)       
                        return combination(n,bbefore_last_code)            
                bbefore_pg = before_pg
                bbefore_ps = before_ps
                before_pg = pg
                before_ps = ps
                if (before_pg == before_ps) and (before_pg != 0 and before_ps != 0) and pari:
                    if (sugg1 == sugg2) and (before_tot == 2):
                        aggiorna_posizione(configurazione,n)
                        return combination(n,last_code)                
                    return prova_9(n,configurazione)               
                aggiorna_posizione(configurazione,n)              
                if pari:
                    
                    if ((sugg1 != sugg2) and (sugg1 != before_sugg1) and (sugg1 != before_sugg2)) and (before_tot != n-1) and (before_tot != 1) and (before_tot != 2) and before_via:
                        if pg > before_pg:             
                            return combination_fault_0(last_code,before_last_code,suggest,before_suggest)
                        elif before_pg > pg:         
                            return combination_fault_0(before_last_code,last_code,before_suggest,suggest)
                    elif sugg1 == n or sugg2 == n:
                
                        aggiorna_non_codice_0()
                        return combination(n,last_code)
                    elif (sugg1 == sugg2) and before_tot == n:
               
                        return combination_fault_0(before_last_code,last_code,before_suggest,suggest)
                    elif (sugg1 == sugg2) and before_tot != n:
                            if bbefore_sugg1 != bbefore_sugg2:
                                return combination_fault_1(last_code,bbefore_last_code,suggest,bbefore_suggest)
                    elif before_tot == n-1:

                        if bbefore_pg < pg:
                            return combination_fault_0(last_code,bbefore_last_code,suggest,bbefore_suggest)
                        elif bbefore_pg > pg:
                            return combination_fault_0(bbefore_last_code,last_code,bbefore_suggest,suggest)
                        else:
                            if bbefore_pg == pg and bbefore_ps == ps:
                                aggiorna_noncodice(n,last_code,bbefore_last_code)
                            return combination(n,last_code)
                            
                    else:
                        if before_pg == pg and before_ps == ps:
                            aggiorna_noncodice(n,last_code,before_last_code)
                        return combination(n,last_code)
                else:
                    if ((sugg1 != sugg2) and (sugg1 != before_sugg1) and (sugg1 != before_sugg2)) and (before_tot != n-1) and (before_tot != 1) and (before_tot != 2) and before_via:
                        if pg > before_pg:
                            return combination_fault_0(last_code,before_last_code,suggest,before_suggest)
                        elif before_pg > pg:
                            return combination_fault_0(before_last_code,last_code,before_suggest,suggest)
                    elif sugg1 == n or sugg2 == n:
                        aggiorna_non_codice_0()
                        return combination(n,last_code)
                    else:
                        if before_pg == pg and before_ps == ps:
                            aggiorna_noncodice(n,last_code,before_last_code)
                        return combination(n,last_code)
                
                
                
            else:
                return combination(n,last_code)

def find(configurazione):
    n = configurazione[0]
    code,sugg = configurazione[-1]
    tot = sugg[0]+sugg[1]
    if tot == n:
        return code,sugg
    find(configurazione[:-1])

def aggiorna_noncodice(n,last_code,before_last_code):
    
    global non_codice
    
    for i in range(n):
        if last_code[i] != before_last_code[i]:
            try:
                if last_code[i] not in non_codice[i]:
                    non_codice[i]+=[last_code[i]]
            except KeyError:
                non_codice[i] = [last_code[i]]
                
                
def prova_9(n,configurazione):
    
    
    global codice, non_nelcodice,pg,ps,special_case
    
    last_code,suggest = configurazione[-1]
    
    risposta = copy.copy(last_code)
    
    numero_sbagliato = random.choice(non_nelcodice)
    
    for k in codice:
        posizione_numerogiusto = k
    
    risposta[posizione_numerogiusto] = numero_sbagliato
    
    special_case = True
    return risposta

def check_nove9(configurazione):
    
    

    
    global special_case,pg,ps
    
    _ , suggest = configurazione[-1]
    
    _ , b_suggest = configurazione[-2]
    
    num1 = suggest[0]
    num2 = suggest[1]
    num3 = b_suggest[0]
    num4 = b_suggest[1]
    
    if (num1+1 == num3) and (num2 == num4):
        pg = num3
        ps = num4
    elif (num1+1 == num4) and (num2 == num3):
        pg = num4
        ps = num3
    elif (num1 == num4) and (num2+1 == num3):
        pg = num3
        ps = num4
    elif (num1 == num3) and (num2+1 == num4):
        pg = num3
        ps = num4
    
    special_case = True

    
def check_number(configurazione):  
    global nel_codice,non_nelcodice
    if 2 <= len(configurazione) <= 11:
        last_code , suggest = configurazione[-1]
        num_tot = suggest[0]+suggest[1]        
        if num_tot == 1:
            nel_codice += [last_code[0]]
        elif num_tot == 0:
            non_nelcodice += [last_code[0]]
    
def combination(n,before_last_code):

    
    global mai_piu,non_codice,codice,pg,ps      
    while True:      
        risposta = copy.copy(before_last_code)   
        if len(codice) > 0:
            for key in codice:
                numer = codice[key]
                valore = risposta[key]                          
                for i in range(0,len(before_last_code)):                  
                    if before_last_code[i] == numer:                    
                        before_last_code[i] = valore                      
                risposta[key] = codice[key]                
        uno = random.randint(0,n-1)
        due = random.randint(0,n-1)       
        if uno == due:            
            pass       
        if len(codice) > 0:
            if (uno in codice) or (due in codice):
                continue       
        sposta_uno = risposta[uno]
        sposta_due = risposta[due]       
        if len(non_codice) > 0:
            try:
                if sposta_uno in non_codice[due]:
                    pass 
            except KeyError:
                risposta[due] = sposta_uno 
            try:
                if sposta_due in non_codice[uno]:
                    pass
            except KeyError:
                risposta[uno] = sposta_due   
        risposta[due] = sposta_uno
        risposta[uno] = sposta_due       
        if risposta not in mai_piu:
            mai_piu += [risposta]
            return mai_piu[-1]
            
            
            
def combination_fault_0(last_code,before_last_code,suggest,before_suggest):
    
    global non_nelcodice,numeri_comb,special_case
    posizioni = []
    sugg1,sugg2 = suggest
    b_sugg1, b_sugg2 = before_suggest

    risposta = best_move(last_code,before_last_code,suggest,before_suggest)
    
    if risposta != None:
        return risposta
    
    if (sugg1 == sugg2):
        return combination_fault_1(last_code,before_last_code,suggest,before_suggest)
    elif (b_sugg1 == b_sugg2):
        return combination_fault_1(last_code,before_last_code,suggest,before_suggest)
    
        
    for i in range(0,len(last_code)):
        if last_code[i] != before_last_code[i]:
            posizioni += [i]
            if last_code[i] not in numeri_comb:    
                numeri_comb +=[last_code[i]]
            if before_last_code[i] not in numeri_comb:
               numeri_comb +=[before_last_code[i]]
     
    risposta = copy.copy(last_code)
           
    while True:
        y = random.choice(non_nelcodice)
        if y not in risposta:
            break
    i = random.choice(posizioni)
    

    risposta[i] = y
    
    return risposta

def best_move(last_code,before_last_code,suggest,before_suggest):
 
    global pg,ps,before_pg,before_ps,codice

    n = len(last_code)
    c = 0
    for i in range(n):
        if last_code[i] != before_last_code[i]:
            c+=1
            if c > 2:
             
                return None
    
    if n == 6:
        if (before_pg == 1 and before_ps == 5) and (pg == 3 and ps == 3):
        
            for i in range(n):
                if last_code[i] != before_last_code[i]:
                    codice[i] = last_code[i]
                    
            return combination(n,last_code)
        elif (before_pg == 0 and before_ps == 6) and(pg == 2 and ps == 4):
       
            for i in range(n):
                if last_code[i] != before_last_code[i]:
                    codice[i] = last_code[i]
            
            return combination(n,last_code)
        return
    elif n == 8:
        sug1,sug2 = suggest
        b_sugg1, b_sugg2 = before_suggest
        if pg == 4 and before_pg == 2:
    
            for i in range(n):
                if last_code[i] != before_last_code[i]:
                    codice[i] = last_code[i]
                
  
            return combination(n,last_code)
        elif (before_pg == 2 and before_pg == 6) and (pg == 4 and ps == 4):

            for i in range(n):
                if last_code[i] != before_last_code[i]:
                    codice[i] = last_code[i]
                
          
            return combination(n,last_code)
    elif n ==7:
        if (before_pg == 1 and before_ps == 6) and (pg == 3 and ps == 4):

            for i in range(n):
                if last_code[i] != before_last_code[i]:
                    codice[i] = last_code[i]
            return combination(n,last_code)

        return

def combination_fault_1(last_code,before_last_code,suggest,before_suggest):
    global non_codice,non_nelcodice,numeri_comb
    
    
    
    n=len(last_code)
    
    if len(non_codice) == 0:
        return combination(n,last_code)
    

    
    risposta = []
    posizioni= []
    for i in range(n):
        if last_code[i] != before_last_code[i]:
            posizioni += [i]
            if last_code[i] not in numeri_comb:
                numeri_comb +=[last_code[i]]
    

    
    y = random.choice(non_nelcodice)
    

    for _ in range(n):
        risposta += [y]
    

    
    y = random.choice(numeri_comb)
    

    
    for i in range(n):
        if last_code[i] == y:
            risposta[i] = y
            posizione = i

    
    while True:
        
        l = random.choice(non_codice)

                
        for k in non_codice:
            if l == non_codice[k]:
                p = k
      
        if posizione != p:
            n = random.choice(l)
            if n not in risposta:
                risposta[p] = n
                return risposta

            
def check_combination_fault_1(last_code,before_last_code,suggest,before_suggest):
    
    global codice,pg,ps,numeri_comb,non_codice,codice
    
    num1,num2 = suggest

    for val in numeri_comb:
        if val in last_code:
            numero_presente = val
    for val in numeri_comb:
        if val not in last_code:
            numero_assente = val
    
    
    
    if num1 == 2 or num2 == 2:
            
        for i in range(0,len(last_code)):
            if numero_assente == before_last_code[i]:
                try:
                    if numero_assente not in non_codice[i]:
                        codice[i] = numero_assente
                        for val in nel_codice:
                            if val != numero_assente:
                                try:
                                    if val not in non_codice[i]:
                                        non_codice[i] += [val]
                                except KeyError:
                                    non_codice[i] = [val]
                    else:
                        codice[i] = numero_presente
                        for val in nel_codice:
                            if val != numero_presente:
                                try:
                                    if val not in non_codice[i]:
                                        non_codice[i] += [val]
                                except KeyError:
                                    non_codice[i] = [val]
                except KeyError:
                    return                             
        numeri_comb = []
    
    elif num1 == 1 and num2 == 1:
        for value in numeri_comb:
            for i in range(0,len(last_code)):
                if value == last_code[i]:
                    codice[i] = value
                    insert = value
                    for v in nel_codice:
                        if v != insert:
                            try:
                                if v not in non_codice[i]:
                                    non_codice[i] += [v]
                            except KeyError:
                                non_codice[i] = [v]
                                
        for val in numeri_comb:
            if val != insert:
                numero_sbagliato = val
                
        for i in range(0,len(before_last_code)):
            if numero_sbagliato == before_last_code[i]:
                try:
                    if numero_sbagliato not in non_codice[i]:
                        non_codice[i] += [numero_sbagliato]
                except KeyError:
                    non_codice[i] = [numero_sbagliato]
        
        if insert != before_last_code[i]:
            try:
                if insert not in non_codice[i]:
                    non_codice[i] += [insert]
            except KeyError:
                non_codice[i] = [insert]
                    
        
        numeri_comb = []
    
    numeri_comb = []
    
def check_combination_fault_11(last_code,before_last_code,suggest,before_suggest):
    
    global codice,pg,ps,numeri_comb,non_codice
    
    num1,num2 = suggest
    

    
    for val in numeri_comb:
        if val in last_code:
            numero_presente = val
        else:
            numero_assente = val
      
    if num1 == 2 or num2 == 2:
            
        for i in range(0,len(last_code)):
            if numero_presente == last_code[i]:
                try:
                    non_codice[i] += [numero_presente]
                except KeyError:
                    non_codice[i] = [value]
            
        for i in range(0,len(before_last_code)):
            if numero_presente == before_last_code[i]:
                try:
                    if numero_assente not in non_codice[i]:
                        codice[i] = numero_assente
                        for val in nel_codice:
                            if val != numero_assente:
                                try:
                                    if val not in non_codice[i]:
                                        non_codice[i] += [val]
                                except KeyError:
                                    non_codice[i] = [val]
                    else:
                        codice[i] = numero_presente
                        for val in nel_codice:
                            if val != numero_presente:
                                try:
                                    if val not in non_codice[i]:
                                        non_codice[i] += [val]
                                except KeyError:
                                    non_codice[i] = [val]
                except KeyError:
                    return
                                        
        numeri_comb = []
    
    elif num1 == 1 and num2 == 1:
        for value in numeri_comb:
            for i in range(0,len(last_code)):
                if value == last_code[i]:
                    codice[i] = value
                    insert = value
                    for v in nel_codice:
                        if v != insert:
                            try:
                                if v not in non_codice[i]:
                                    non_codice[i] += [v]
                            except KeyError:
                                non_codice[i] = [v]
                                
        for val in numeri_comb:
            if val != insert:
                numero_sbagliato = val
                
        for i in range(0,len(before_last_code)):
            if numero_sbagliato == before_last_code[i]:
                try:
                    if numero_sbagliato not in non_codice[i]:
                        non_codice[i] += [numero_sbagliato]
                except KeyError:
                    non_codice[i] = [numero_sbagliato]
        
        if insert != before_last_code[i]:
            try:
                if insert not in non_codice[i]:
                    non_codice[i] += [insert]
            except KeyError:
                non_codice[i] = [insert]
                    
        
        numeri_comb = []
    
    numeri_comb = []           

def check_combination_fault_0(last_code,before_last_code,suggest,before_suggest,configurazione):
    n=len(last_code)
    global codice,pg,ps,numeri_comb,non_codice,before_pg,before_ps
    

    before_pg = pg
    before_ps = ps


    
    num1, num2 = suggest

    for val in numeri_comb:
        if val in last_code:
            numero_presente = val
        elif val not in last_code:
            numero_assente = val
    
    if num1 == pg or num2 == pg:

        for value in numeri_comb:

            for i in range(0,len(last_code)):
                if value == last_code[i]:
       
                    codice[i] = value

                    insert = value

                    for v in nel_codice:
                        if v != insert:
                            try:
                                if v not in non_codice[i]:
                                    non_codice[i] += [v]
                            except KeyError:
                                non_codice[i] = [v]
      
        for val in numeri_comb:
            if val != insert:
                numero_sbagliato = val

        
        for i in range(0,len(before_last_code)):
            if numero_sbagliato == before_last_code[i]:
                try:
                    if numero_sbagliato not in non_codice[i]:
                        non_codice[i] += [numero_sbagliato]
                except KeyError:
                    non_codice[i] = [numero_sbagliato]
            
            if insert != before_last_code[i]:
                try:
                    if insert not in non_codice[i]:
                        non_codice[i] += [insert]
                except KeyError:
                    non_codice[i] = [insert]
            
        
        numeri_comb = []


        
    else:

        for i in range(0,len(last_code)):
            if last_code[i] in non_nelcodice:
                codice[i] = numero_presente
                insert = numero_presente
                for v in nel_codice:
                    if v != insert:
                        try:
                            if v not in non_codice[i]:
                                non_codice[i] += [v]
                        except KeyError:
                            non_codice[i] = [v]
                            
                            

                    
        for i in range(0,len(before_last_code)):
            if numero_assente == before_last_code[i]:
                try:
                    if numero_assente not in non_codice[i]:
                        non_codice[i] += [numero_assente]
                except KeyError:
                    non_codice[i] = [numero_assente]
            
            if insert != before_last_code[i]:
                try:
                    if insert not in non_codice[i]:
                        non_codice[i] += [insert]
                except KeyError:
                    non_codice[i] = [insert]
            
        
        numeri_comb = []

        
def check_combination_fault_00(last_code,before_last_code,suggest,before_suggest):
    n=len(last_code)
    global codice,pg,ps,numeri_comb,non_codice,before_pg,before_ps
    

    num1, num2 = suggest
 
    if num1 == pg or num2 == pg:
        for value in numeri_comb:
            for i in range(0,len(last_code)):
                if value == last_code[i]:
                    try:
                        if value not in non_codice[i]:
                            non_codice[i] += [value]
                    except KeyError:
                        non_codice[i] = value
                    
                    numero_sbagliato = value
        
        for v in numeri_comb:
            if v != numero_sbagliato:
                numero_giusto = v
                
        for i in range(0,len(last_code)):
            if last_code[i] in non_nelcodice:
                codice[i] = numero_giusto
                insert = before_last_code[i]
                for v in nel_codice:
                    if v != insert:
                        try:
                            if v not in non_codice[i]:
                                non_codice[i] += [v]
                        except KeyError:
                            non_codice[i] = [v]
                
        for i in range(0,len(before_last_code)):
            if before_last_code[i] != insert :
                try:
                    if insert not in non_codice[i]:
                        non_codice[i] += [insert]
                except KeyError:
                    non_codice[i] = [insert]
        
        
        numeri_comb = []
                        
        
    
    elif (before_pg == num1) or (before_pg == num2):

        for value in numeri_comb:
            for i in range(0,len(last_code)):
                if value == last_code[i]:
                    codice[i] = value
                    insert = value
                    for v in nel_codice:
                        if v != insert:
                            try:
                                if v not in non_codice[i]:
                                    non_codice[i] += [v]
                            except KeyError:
                                non_codice[i] = [v]
        
        for val in numeri_comb:
            if val != insert:
                numero_sbagliato = val
                    
        for i in range(0,len(before_last_code)):
            if numero_sbagliato == before_last_code[i]:
                try:
                    if numero_sbagliato not in non_codice[i]:
                        non_codice[i] += [numero_sbagliato]
                except KeyError:
                    non_codice[i] = [numero_sbagliato]
            
            if insert != before_last_code[i]:
                try:
                    if insert not in non_codice[i]:
                        non_codice[i] += [insert]
                except KeyError:
                    non_codice[i] = [insert]
            
        
        numeri_comb = []
        
    else:      
        for value in numeri_comb:
            for i in range(0,len(last_code)):
                if last_code[i] not in non_nelcodice:
                    try:
                        if before_last_code[i] not in non_codice[i]:
                            non_codice[i] +=[before_last_code[i]]
                    except KeyError:
                        non_codice[i] = [before_last_code[i]]
                if value == before_last_code[i]:
                    posizione = i
                if value not in last_code[i]:
                    insert = value
        
        codice[posizione] = insert
        for v in nel_codice:
                    if v != insert:
                        try:
                            if v not in non_codice[i]:
                                non_codice[i] += [v]
                        except KeyError:
                            non_codice[i] = [v]
        
        for val in numeri_comb:
            if val != insert:
                numero_sbagliato = val
                    
        for i in range(0,len(before_last_code)):
            if numero_sbagliato == before_last_code[i]:
                try:
                    if numero_sbagliato not in non_codice[i]:
                        non_codice[i] += [numero_sbagliato]
                except KeyError:
                    non_codice[i] = [numero_sbagliato]
            
            if insert != before_last_code[i]:
                try:
                    if insert not in non_codice[i]:
                        non_codice[i] += [insert]
                except KeyError:
                    non_codice[i] = [insert]   
        
        numeri_comb = []

def check_bestmove():
    global before_pg,before_ps,pg,ps
    
    if fabs(before_pg - pg) == fabs(before_ps - ps):
        return True
    if fabs(before_pg - ps) == fabs(before_pg - pg):
        return True
    if fabs(before_ps - pg) == fabs(before_pg - ps):
        return True
    if fabs(before_ps - ps) == fabs(before_ps - pg):
        return True
    
    return False
            
def aggiorna_non_codice_0():

    global non_codice, mai_piu 
    
    last_code = mai_piu[-1]
    
    for i in range(len(last_code)):
        try:
            
            if last_code[i] not in non_codice[i]:
                non_codice[i] += [last_code[i]]
            
        except KeyError:
            
            non_codice[i] = [last_code[i]]

  
def aggiorna_posizione(configurazione,n):
    
    global pg,ps,codice
    _ ,suggest = configurazione[-1]

    if len(codice) > 0:
        giuste = len(codice)
    
    num0 = suggest[0]
    num1 = suggest[1]
    
    if num0 == n:
 
        ps = num0
        pg = num1
    elif num1 == n:

        ps = num1
        pg = num0
    elif num1 == num0:

        pg = num1
        ps = num0
    elif num0 == 1 and num1 == n-1:
        pg = num0
        ps = num1
    elif num0 == n-1 and num1 == 1:
        pg = num1
        ps = num0

    elif num0 -1 == pg:
   
        pg = num0
        ps = num1

    elif num1 -1 == pg:
  
        pg = num1
        ps = num0

    elif num1 +1 == pg:

        pg = num1
        ps = num0
            
    elif num0 +1 == pg:

        pg = num0
        ps = num1
    elif num0 == pg and num1 == ps:

        pg = num0
        ps = num1
    elif num1 == pg and num0 == ps:

        pg = num1
        ps = num0
    
    else:
  
        while True:
            
            pg += 1
            
            if pg == num1:
                pg = num1
                ps = num0
                break
            elif pg == num0:
                pg = num0
                ps = num1
                break
    
    
    if n == 8:
        if len(codice) > 3:            
            if pg <= len(codice):
                a = pg
                b = ps
                ps = a
                pg = b
    else:
        if len(codice) > 2:            
            if pg <= len(codice):

                a = pg
                b = ps
                ps = a
                pg = b


def sudoku(n):
    
    global codice,non_codice,nel_codice
    
    for key in non_codice:
        if len(non_codice[key]) == n-1:
            for value in nel_codice:
                if value not in non_codice[key]:
                    
                    codice[key] = value


    for value in nel_codice:
        z = 0
        for key in non_codice:
            if value in non_codice[key]:
                z += 1
            if z == n-1:
                for i in range(n):
                        try:
                            if value not in non_codice[i]:
                                continue
                        except KeyError:
                 
                            codice[i] = value
     
                              


def trova_restanti_numeri_non_nel_codice():
    
    global X,non_nelcodice
    
    for el in X:
        non_nelcodice += [int(el)]


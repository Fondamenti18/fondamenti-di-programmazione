'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco di una macchinetta che gira su una pista di formula 1.

Il gioco consiste in un percorso di gara, rappresentato da una griglia di caratteri
(' '=vuoto, '#' = ostacolo, 'A....Z' = auto, '|' = traguardo 'O' = buca tutti gli altri caratteri sono ostacoli)
nella quale si trova la macchina del giocatore (un carattere 'A..Z'), che deve:
    correre attorno alla pista per un intero giro senza sbattere contro ostacoli o altre macchine
    raggiungere il traguardo
    fermarsi senza sbattere (vx=vy=0)

Il punteggio di gioco e' il numero di step che sono stati necessari a percorrere la gara e fermarsi senza sbattere.

Ad ogni istante il simulatore della macchinetta conosce:
    x, y:   la posizione della macchina sulla griglia di gioco
    vx, vy: la velocita' corrente della macchina
Ad ogni step della simulazione il giocatore puo' solo:
    incrementare di 1, decrementare di 1 o lasciare come sono i valodi vx, vy della velocita' (-1,0,+1)
corrispondentemente il simulatore:
    somma gli incrementi/decrementi alle due variabili vx,vy
    somma le velocita' vx,vy alla posizione x,y ottenendo la prossima posizione della macchina
    controlla se la nuova posizione e' vuota
        se la nuova posizione e' occupata (da un ostacolo o da un'altra macchina) il gioco termina senza completare la corsa
        se la posizione contiene una buca si slitta di un carattere a caso fino a restare sulla strada o su un ostacolo
        altrimenti si sposta la macchina sulla nuova posizione
    se il traguardo e' stato raggiunto nella direzione giusta e la macchina e' ferma (vx=vy=0) la gara termina
    altrimenti si riesegue un nuovo step (chiedendo alla funzione 'ai' del giocatore cosa fare)

Il programma che dovete realizzare e' l'AI che guida la macchina, che riceve come input:
    la griglia di gioco del passo precedente (comprese le altre macchine)
    la griglia di gioco del passo corrente (comprese le altre macchine)
    la posizione x,y della propria macchina
    la velocita' vx,vy della propria macchina
    il carattere che individua la vostra macchina
    il verso di rotazione (-1= si parte verso sinistra rispetto al traguardo, +1= si parte verso destra rispetto al traguardo)
    la posizione startx,starty di partenza della macchina
    (NUOVO) il numero di attraversamenti del traguardo fatti dalla macchina (contromano se negativo)
e deve produrre in output la coppia:
    ax, ay  variazione della velocita (coppia di valori -1,0,+1)
La simulazione di tutti i 3 percorsi di gara per la qualificazione (senza visualizzazione) deve impiegare al piu' 1 minuto.

In questo esercizio la valutazione avverra' in tre fasi:
    giro di qualificazione: 
        la macchina gira sulla pista di gara da sola, senza altri concorrenti su 3 piste in cui non sono presenti barriere di buche
        superare questa prova da' il punteggio minimo di qualificazione (18)
    giro di premio:
        la macchina gira su una pista di gara simile (ma diversa) da quella "Roma" che contiene barriere di buche
        superare questa prova da' il punteggio di qualificazione 24

    La classifica ottenuta nella qualificazione viene usata per determinare i gironi e poi il torneo di gara della fase successiva
    chi non completa il giro di qualificazione non partecipa al successivo torneo e non e' sufficiente

    Gironi e torneo ad eliminazione:
        (per ogni scontro vengono eseguite due gare, con A a sinistra e B a destra e viceversa)
        viene organizzato un torneo in cui prima si eseguono dei gironi di 4-5 auto
            Le due auto che ottengono il miglior punteggio sul girone partecipano alle eliminatorie successive
            Per ogni gara del girone vengono assegnati:
                3 punti a chi vince la gara
                1 punto per pareggio o scontro
                0 punti a chi perde
                a parita' di punteggio vince la macchina che ha fatto meno incidenti
                a parita' di incidenti viene simulata un'altra gara con una pista con barriere di buche (tipo "roma" per intenderci)

        Le due auto qualificate di ciascun girone partecipano ad una fase eliminatoria a scontro diretto
            l'auto vincente passa il turno (in caso di patta su esegue una gara aggiuntiva con barriere di buche casuali)

    La classifica finale della fase a scontro diretto determina i voti:
        I livelli del torneo ad eliminazione individuano i voti ottenuti, a seconda del numero di partecipanti (per esempio 6 livelli -> 2.1 voti per livello circa)
        Per avere la sufficienza bisogna aver completato almeno il giro di qualificazione sulle diverse piste
        Se una macchina ha ottenuto il voto 24 nella fase di qualificazione, il voto finale dell'esercizio e' almeno 24

COMPORTAMENTO: le auto che usano comportamenti scorrette non superano la qualificazione. Es.
    - precalcolare offline la strategia e inserirla nel programma
    - andare apposta contro l'auto dell'avversario
    - ...

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti

'''

from random     import randint
from copy import copy
from gwidget    import *


#def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty): # vecchia versione
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    
    print(laps)
    
    ax,ay=vx,vy
    if startx == x and starty == y: #Partenza
        if verso == 1:
            ax = -1
        else:
            ax = +1
        return ax,ay

    ax=0
    ay=0
    if (vx or vy) != 0:
        check_sband(griglia_corrente,griglia_precedente,x,y,vx,vy)
    
    ax,ay, helping = judge(griglia_corrente,x,y,vx,vy)
    
    if not helping:
        if vx == 2 and vy == 0:
            ax = -1
            return ax,ay
        if vy == 2 and vx == 0:
            ay = -1
            return ax,ay
        if vx == -2 and vy == 0:
            ax = 1
            return ax,ay
        if vy == -2 and vx == 0:
            ay = 1
            return ax,ay
        if vx == -1 and vy == 0:
            ax = 0
            return ax,ay
        if vy == -1 and vx == 0:
            ay = 0
            return ax,ay
        if vx == 1 and vy == 0:
            ax = 0
            return ax,ay
        if vy == 1 and vx == 0:
            ay = 0
            return ax,ay
        if vx == -1 and vy == -1:
            ax = 0
            ay = 0
            return ax, ay
        if vx == 1 and vy == -1:
            ay = 0
            ax = 0
            return ax,ay
        if vx == 2 and vy == -2:
            ax = -1
            ay = 1
            return ax,ay
        if vx == 1 and vy == 1:
            ax = 0
            ay = 0
            return ax,ay
        if vx == -1 and vy == 1:
            ax = 0
            ay = 0
            return ax,ay
    return ax,ay
    
    

def check_sband(griglia_corrente,griglia_precedente,x,y,vx,vy):   
    
    
    if griglia_corrente[y][x] != griglia_precedente[y-vy][x-vx]:
        print('')
    else:
        print('')
    
def judge(griglia_corrente,x,y,vx,vy):
    helping = False
    ax = 0
    ay = 0
    
    if griglia_corrente[y][x] == '|':
        ax = 1
        ay = 0
        helping = True
        return ax,ay,helping
    
    if vx < 0 and vy == 0: #verso sinistra   
        
        if griglia_corrente[y+vy][x+vx] == ' ':
            if griglia_corrente[y+vy][x+vx-1] == ' ' or griglia_corrente[y+vy][x+vx-1] == '|':
                ax = -1
                ay = 0
                print('156')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx-1] == ' ':
                ax = -1
                ay = -1
                print('161')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx] == ' ':
                ax = 0
                ay = -1
                print('166')
                return ax,ay,helping               
            elif griglia_corrente[y+vy+1][x+vx-1] == ' ':
                ax = -1
                ay = +1
                print('171')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx] == ' ':
                ax = 0
                ay = +1
                print('176')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx+1] == ' ':
                ax = 1
                ay = -1
                print('181')
                return ax,ay,helping
            elif griglia_corrente[y+vy][x+vx+1] == ' ':
                ax = 1
                ay = 0
                print('186')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx+1] == ' ':
                ax = 1
                ay = 1
                print('191')
                return ax,ay,helping
            else:
                print('194') 
                return ax,ay,helping
        
        elif griglia_corrente[y+vy][x+vx] == 'O':
            ax = 0
            ay = 0
            print('200')
            return ax,ay,helping
        elif griglia_corrente[y+vy][x+vx] == '|':
            ax = 0 
            ay = 0
            return ax,ay,helping
            
        
        
    elif vx < 0 and vy < 0: #verso alto sinistra
        
        if griglia_corrente[y+vy][x+vx] == ' ':
            if griglia_corrente[y+vy-1][x+vx-1] == ' ':
                ax = -1
                ay = -1
                print('211')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx] == ' ':
                ax = 0
                ay = -1
                print('216')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx+1] == ' ':
                ax = 1
                ay = -1
                print('221')
                return ax,ay,helping               
            elif griglia_corrente[y+vy][x+vx-1] == ' ':
                ax = -1
                ay = 0
                print('226')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx-1] == ' ':
                ax = -1
                ay = 1
                print('231')
                return ax,ay,helping
            else:
                print('234')
                return ax,ay,helping
                
        elif griglia_corrente[y+vy][x+vx] == 'O':
            ax = 0
            ay = 0
            print('240')
            return ax,ay,helping      
        elif griglia_corrente[y+vy][x+vx] == '#':
            if griglia_corrente[y+vy+1][x+vx] != '#':
                ay = +1
                ax = 0
                helping = True
                print('247')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx-1] !='#':
                ay = +1
                ax = -1
                helping = True
                print('253')
                return ax,ay,helping
            elif griglia_corrente[y+vy][x+vx-1] !='#':
                ay = 0
                ax = -1
                helping = True
                print('260')
                return ax,ay,helping
            elif griglia_corrente[y+vy][x+vx+1] !='#':
                ay = 0
                ax = 1
                helping = True
                print('260')
                return ax,ay,helping

            
    
    
    
    elif vx == 0 and vy < 0: #verso l'alto
        
        if griglia_corrente[y+vy][x+vx] == ' ':
            if griglia_corrente[y+vy-1][x+vx] == ' ':
                ax = 0
                ay = -1
                print('258')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx+1] == ' ':
                ax = 1
                ay = -1
                print('263')
                return ax,ay,helping
            elif griglia_corrente[y+vy][x+vx+1] == ' ':
                ax = 1
                ay = 0
                print('233')
                return ax,ay
            elif griglia_corrente[y+vy-1][x+vx-1] == ' ':
                ax = -1
                ay = -1
                print('273')
                return ax,ay,helping
            elif griglia_corrente[y+vy][x+vx-1] == ' ':
                ax = -1
                ay = 0
                print('278')
                return ax,ay,helping
            else: 
                ax = 0
                ay = 0
                print('283')
                return ax,ay,helping
        elif griglia_corrente[y+vy][x+vx] == 'O':
            ax = 0
            ay = 0
            print('288')
            return ax,ay,helping
            
            
            
    elif vx > 0 and vy < 0: #verso alto destra
        
        if griglia_corrente[y+vy][x+vx] == ' ':
            if griglia_corrente[y+vy-1][x+vx+1] == ' ':
                ax = 1
                ay = -1
                print('299')
                return ax,ay,helping
            elif griglia_corrente[y+vy][x+vx+1] == ' ':
                ax = 1
                ay = 0
                print('304')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx+1] == ' ':
                ax = 1
                ay = 1
                print('309')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx] == ' ':
                ax = 0
                ay = -1
                print('314')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx-1] == ' ':
                ax = -1
                ay = -1
                print('319')
                return ax,ay,helping
            else: 
                ax = 0
                ay = 0
                print('324')
                return ax,ay,helping
        elif griglia_corrente[y+vy][x+vx] == 'O':
            ax = 0
            ay = 0
            print('329')
            return ax,ay,helping
        elif griglia_corrente[y+vy][x+vx] == '#':
            if griglia_corrente[y+vy][x+vx-1] != '#':
                ax = -1
                ay = 0
                helping = True
                print('356')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx] != '#':
                ax = 0
                ay = 1
                helping = True
                print('369')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx+1] != '#':
                ax = 1
                ay = 1
                helping = True
                print('375')
                return ax,ay,helping
            
            
    elif vx > 0 and vy == 0: #verso destra
        
        if griglia_corrente[y+vy][x+vx] == ' ':
            if griglia_corrente[y+vy][x+vx+1] == ' ':
                ax = 1
                ay = 0
                print('305')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx+1] == ' ':
                ax = 1
                ay = 1
                print('309')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx] == ' ':
                ax = 0
                ay = 1
                print('314')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx+1] == ' ':
                ax = 1
                ay = -1
                print('320')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx] == ' ':
                ax = 0
                ay = -1
                print('325')
                return ax,ay,helping
            else:
                ax = 0
                ay = 0
                print('330')
                return ax,ay,helping
        elif griglia_corrente[y+vy][x+vx] == '0':
            print('ma caz')
            if griglia_corrente[y+vy+1][x+vx] != '0' or griglia_corrente[y+vy-1] != '0':
                print('non ci sono al centro')
            ax = 0
            ay = 0
            print('419')
            return ax,ay,helping
        
                
        elif griglia_corrente[y+vy][x+vx] == 'O':
            ax = 0
            ay = 0
            print('335')
            return ax,ay,helping
        elif griglia_corrente[y+vy][x+vx] == '#':
            if griglia_corrente[y+vy+1][x+vx-1] != '#':
                ax = -1
                ay = +1
                helping = True
                print('423')
                return ax,ay,helping
            
            
            
            
    elif vx > 0 and vy > 0: #verso basso destra
        
        if griglia_corrente[y+vy][x+vx] == ' ':
            if griglia_corrente[y+vy+1][x+vx+1] == ' ':
                ax = 1
                ay = 1
                print('347')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx] == ' ':
                ax = 0
                ay = 1
                print('352')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx-1] == ' ':
                ax = -1
                ay = 1
                print('357')
                return ax,ay,helping
            elif griglia_corrente[y+vy][x+vx+1] == ' ':
                ax = 1
                ay = 0
                print('362')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx+1] == ' ':
                ax = 1
                ay = -1
                print('367')
                return ax,ay,helping
            else:
                ax = 0
                ay = 0
                print('372')
                return ax,ay,helping
                
        elif griglia_corrente[y+vy][x+vx] == 'O':
            ax = 0
            ay = -1
            helping=True
            print('377')
            return ax,ay,helping
        
        elif griglia_corrente[y+vy][x+vx] == '#':
            if griglia_corrente[y+vy-1][x+vx] != '#':
                ax = 0
                ay = -1
                helping = True
                print('489')
                return ax,ay,helping
            if griglia_corrente[y+vy][x+vx-1] != '#':
                ax = -1
                ay = 0
                helping = True
                print('495')
                return ax,ay,helping
            
            
    elif vx == 0 and vy > 0: #verso basso
        
        if griglia_corrente[y+vy][x+vx] == ' ':
            if griglia_corrente[y+vy+1][x+vx] == ' ':
                ax = 0
                ay = 1
                print('387')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx-1] == ' ':
                ax = -1
                ay = 1
                print('393')
                return ax,ay,helping
            elif griglia_corrente[y+vy][x+vx-1] == ' ':
                ax = -1
                ay = 0
                print('387')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx+1] == ' ':
                ax = 1
                ay = 1
                print('403')
                return ax,ay,helping
            elif griglia_corrente[y+vy][x+vx+1] == ' ':
                ax = 1
                ay = 0
                print('408') 
                return ax,ay,helping
            else: 
                ax = 0
                ay = 0
                print('413')
                return ax,ay,helping
                
        elif griglia_corrente[y+vy][x+vx] == 'O':
            ax = 0
            ay = 0
            print('419')
            return ax,ay,helping
            
            
    elif vx < 0 and vy > 0: #verso basso sinistra
        
        if griglia_corrente[y+vy][x+vx] == ' ':
            if griglia_corrente[y+vy+1][x+vx-1] == ' ':
                ax = -1
                ay = 1
                print('429')
                return ax,ay,helping
            elif griglia_corrente[y+vy][x+vx-1] == ' ':
                ax = -1
                ay = 0
                print('434')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx-1] == ' ':
                ax = -1
                ay = -1
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx] == ' ':
                ax = 0
                ay = 1
                print('443')
                return ax,ay,helping
            elif griglia_corrente[y+vy+1][x+vx+1] == ' ':
                ax = 0
                ay = 0
                print('448')
                return ax,ay,helping
            else:
                ax = 0
                ay = 0
                print('453')
                return ax,ay,helping
                
        elif griglia_corrente[y+vy][x+vx] == 'O':
            ax = 0
            ay = 0
            print('456')
            return ax,ay,helping
        
        elif griglia_corrente[y+vy][x+vx] == '#':
            print('qui ')
            if griglia_corrente[y+vy][x+vx+1] != '#':
                ax = +1
                ay = 0
                helping = True
                print('584')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx] != '#':
                print('quiqui')
                ax = 0
                ay = -1
                helping = True
                print('594')
                return ax,ay,helping
            elif griglia_corrente[y+vy-1][x+vx-1] != '#':
                ax = -1
                ay = -1
                helping = True
                print('601')
                return ax,ay,helping
    print('483')
    return ax,ay,helping

















piste = { 'monza': [
            '###############################################################################################################',
            '####                     ######################################################################################',
            '###                       ##################*###*##***##*###*#*****###*########################################',
            '##                         #################**#**#*###*#**##*####*###*#*#######################################',
            '##       O                  ################*#*#*#*###*#*#*#*###*####*#*#######################################',
            '##         #######           ###############*###*#*###*#*##**##*####*****######################################',
            '###        #########          ##############*###*##***##*###*#*****#*###*######################################',
            '###         #########  O       ################################################################################',
            '####         #########          ###############################################################################',
            '####         ##########          ##############################################################################',
            '#####     O   ##########          #######################     #################################################',
            '#####         ###########       O  ###################          ###############################################',
            '######         ###########          ###############                 ###########################################',
            '#######         ###########           ##########                        #######################################',
            '########   O     ###########            O           O      ##     O                           #################',
            '#########         ###########                             ####                                    #############',
            '##########        ############                         ##########                O                   ##########',
            '###########       #############                    #################                                    #######',
            '##########        #######################################################################       O         #####',
            '#########        ###########################################################################               ####',
            '########   O    ###############################################################################             ###',
            '######         #################################################################################             ##',
            '######        ###################################################################################             #',
            '#####        #####################################################################################            #',
            '#####       #######################################################################################           #',
            '#####       #######################################################################################    O      #',
            '#####        ######################################################################################           #',
            '######        ####################################################################################           ##',
            '######      O  #########################     ####################################################           ###',
            '#######         ######################         #################################################           ####',
            '########         ###################             #############################################    O       #####',
            '#########                   O             #                      A|                                      ######',
            '##########                               ###         O            |       O           O                 #######',
            '###########                             #####                    X|                                  ##########',
            '############                           #######                   B|                               #############',
            '###############################################################################################################',
		],
    'anello': [
            '###############################################################################################################',
            '###############           O                                                                     ###############',
            '###########             O                    O                                                      ###########',
            '########              O                                           O                                    ########',
            '######O           ########################################################################### O          ######',
            '#####O        ################################################################################### O       #####',
            '####O      #########################################################################################       ####',
            '####     #############################################################################################     ####',
            '###     ###############################################################################################     ###',
            '###     ###############################################################################################     ###',
            '###    #################################################################################################    ###',
            '##     #################################################################################################     ##',
            '##     #################################################################################################     ##',
            '##    ###################################################################################################    ##',
            '##    ###################################################################################################    ##',
            '#     ###################################################################################################     #',
            '#     ###################################################################################################     #',
            '#  O #####################################################################################################O   #',
            '#    #####################################################################################################    #',
            '#    #####################################################################################################    #',
            '#    ##################################################################################################### O  #',
            '#    #####################################################################################################    #',
            '#    #####################################################################################################    #',
            '#    #####################################################################################################    #',
            '#  O #####################################################################################################  O #',
            '#     ###################################################################################################     #',
            '#     ###################################################################################################     #',
            '##    ###################################################################################################    ##',
            '##    ###################################################################################################    ##',
            '##     #################################################################################################     ##',
            '##     #################################################################################################     ##',
            '###    #################################################################################################    ###',
            '###     ###############################################################################################     ###',
            '###     ###############################################################################################     ###',
            '####     #############################################################################################     ####',
            '####       #########################################################################################       ####',
            '#####       O ###################################################################################         #####',
            '######         O  ###########################################################################            ######',
            '########                                       |A                                                      ########',
            '###########                            O       |X                                                   ###########',
            '###############                                |B                                               ###############',
            '###############################################################################################################',
    ],
    'roma': [
        '###############################################################################################################',
        '###############     O            OO   O   O   O   O   O   O   O   O   O   O  O            O     ###############',
        '###########         O            O O O O O O O O O O O O O O O O O O O O O O O            O         ###########',
        '########            O            O  O   O   O   O   O   O   O   O   O   O   OO            O            ########',
        '######            ####OOOO        ############################################       OOOO####            ######',
        '#####         ############OOO      ##########################################     OOO############         #####',
        '####       ##################OO     ########################################    OO##################       ####',
        '####OOOOO######################O     ######################################    O######################OOOOO####',
        '###     ########################O     ####################################    O########################     ###',
        '###     #########################O     ##################################    O#########################     ###',
        '###    ###########################O     ################################    O###########################    ###',
        '##     ############################O     ##############################    O############################     ##',
        '##     #############################O     ############################    O#############################     ##',
        '##    ###############################O     ##########################    O###############################    ##',
        '##    ################################O    O           O            O   O################################    ##',
        '#     #################################O               O               O#################################     #',
        '#     ##################################O              O              O##################################     #',
        '#    #####################################################################################################    #',
        '#OOOO#####################################################################################################OOOO#',
        '#OOOO#####################################################################################################OOOO#',
        '#    #####################################################################################################    #',
        '#     ##################################   OO OOO OOOO OOO OO OO O O  O##################################     #',
        '#     #################################    OO OOO OOOO OOO OO OO O O   O#################################     #',
        '##    ################################     OO OOO OOOO OOO OO OO O O    O################################    ##',
        '##    ###############################      #########################O    O###############################    ##',
        '##     #############################      ###########################O    O#############################     ##',
        '##     ############################      #############################O    O############################     ##',
        '###    ###########################      ###############################O    O###########################    ###',
        '###     #########################      #################################O    O#########################     ###',
        '###     ########################      ###################################O    O########################     ###',
        '####OOOOO######################      #####################################O    O######################OOOOO####',
        '####       ##################       #######################################O    OO##################       ####',
        '#####         ############         #########################################O     OOO############         #####',
        '######            ####            ###########################################O       OOOO####            ######',
        '########            O                        OO|A      O      O      O      O             O            ########',
        '###########         O                        OO|X      O      O      O      O             O         ###########',
        '###############     O                        OO|B      O      O      O      O             O     ###############',
        '###############################################################################################################',
    ],
}
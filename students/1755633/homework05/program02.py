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


python simulatore.py simulate --pista anello --tile 12'''

from random     import randint


libero=True
reset=False
resetV=False
controllo=False
bivio=10
stopAt=(0,0)
resetbivioleft=False

rightv=False
upv=False
downv=False
leftv=True
stopall=False
stopdef=False

right=True
up=False
down=False
left=False



def checkO(x,y,griglia_corrente):
    if right==True:
        if griglia_corrente[y][x+1]=='|':
            print('finish')
            return 0, 0, 18
        if griglia_corrente[y][x+1]=='O':
            print('salta right')
            c=0
            s=0
            while c<8:
                if griglia_corrente[y][x+1+c]==' ':
                    s+=1
                c+=1
            if s==0: return 0, 0, 3
            if s<2 and s!=0:
                if griglia_corrente[y-1][x+1]==' ': return 0, -1, 0
                if griglia_corrente[y+1][x+1]==' ': return 0, +1, 0
            return +1, 0, 2

    elif up==True:
        if griglia_corrente[y-1][x]=='O':
            '''
            c1=0
            while griglia_corrente[y-1-c1][x]=='O':
            c1+=1
            '''


            print('salta up')
            c=0
            s=0
            while c<8:
                if griglia_corrente[y-1-c][x]==' ':
                    s+=1
                c+=1
            if s==0: return 0, 0, 3
            if s<2 and s!=0:
                if griglia_corrente[y-1][x+1]==' ': return +1, 0, 0
                if griglia_corrente[y-1][x-1]==' ': return -1, 0, 1
            return 0, -1, 2

    elif left==True:
        if griglia_corrente[y][x-1]=='O':
            print('salta left')
            c=0
            s=0
            while c<8:
                print(griglia_corrente[y][x-1-c])
                if griglia_corrente[y][x-1-c]==' ':
                    s+=1 #variabile di spazio
                c+=1
            if s==0: return 0, 0, 3
            if s<2 and s!=0:
                print('entradentros')
                if griglia_corrente[y-1][x-1]==' ': return 0, -1, 0
                if griglia_corrente[y+1][x-1]==' ': return 0, +1, 1
            return -1, 0, 2
            #return -1, 0, False
    elif down==True:
        if griglia_corrente[y+1][x]=='O':
            print('salta down')
            c=0
            s=0
            while c<8:
                if griglia_corrente[y+1+c][x]==' ':
                    s+=1
                c+=1
            if s==0: return 0, 0, 3
            if s<2 and s!=0:
                if griglia_corrente[y+1][x+1]==' ': return +1, 0, 0
                if griglia_corrente[y+1][x-1]==' ': return -1, 0, 0
            return 0, +1, 0
    return 0, 0, 0

def checkOv_(x,y,griglia_corrente):
    if rightv==True:
        if griglia_corrente[y][x+1]=='O':
            print('salta rightv')
            c=0
            s=0
            while c<8:
                if griglia_corrente[y][x+1+c]==' ':
                    s+=1
                c+=1
            if s==0: return 0, 0, 3
            if s<2 and s!=0:
                if griglia_corrente[y-1][x+1]==' ': return 0, -1, 0
                if griglia_corrente[y+1][x+1]==' ': return 0, +1, 0
            return +1, 0, 2

    elif upv==True:
        if griglia_corrente[y-1][x]=='O':
            '''
            c1=0
            while griglia_corrente[y-1-c1][x]=='O':
            c1+=1
            '''


            print('salta upv')
            c=0
            s=0
            while c<8:
                if griglia_corrente[y-1-c][x]==' ':
                    s+=1
                c+=1
            if s==0: return 0, 0, 3
            if s<2 and s!=0:
                if griglia_corrente[y-1][x+1]==' ': return +1, 0, 0
                if griglia_corrente[y-1][x-1]==' ': return -1, 0, 1
            return 0, -1, 2

    elif leftv==True:
        if griglia_corrente[y][x-1]=='|':
            print('finish')
            return 0, 0, 18
        if griglia_corrente[y][x-1]=='O':
            print('salta leftv')
            c=0
            s=0
            while c<8:
                print(griglia_corrente[y][x-1-c])
                if griglia_corrente[y][x-1-c]==' ':
                    s+=1 #variabile di spazio
                c+=1
            if s==0: return 0, 0, 3
            if s<2 and s!=0:
                print('entradentros')
                if griglia_corrente[y-1][x-1]==' ': return 0, -1, 0
                if griglia_corrente[y+1][x-1]==' ': return 0, +1, 1
            return -1, 0, 2
            #return -1, 0, False
    elif downv==True:
        if griglia_corrente[y+1][x]=='O':
            print('salta downv')
            c=0
            s=0
            while c<8:
                if griglia_corrente[y+1+c][x]==' ':
                    s+=1
                c+=1
            if s==0: return 0, 0, 3
            if s<2 and s!=0:
                if griglia_corrente[y+1][x+1]==' ': return +1, 0, 0
                if griglia_corrente[y+1][x-1]==' ': return -1, 0, 0
            return 0, +1, 0
    return 0, 0, 0


def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty):
    '''inserite qui il vostro codice, y=42 x=111, y*x'''

    global libero, reset, controllo, stopAt, rightv, upv, downv, leftv, resetV, bivio, resetbivioleft, stopall
    global stopdef, right, down , left, up
    print('nuova pista')
    if verso==1:
        print('verso 1')
        if stopall==True:
            if stopdef==True:
                print('reset all')
                libero=True
                reset=False
                resetV=False
                controllo=False
                bivio=10
                stopAt=(0,0)
                resetbivioleft=False
                return 0,0
            else:
                stopdef=True
                return -1, 0

        stopY,stopX=stopAt
        '''if resetbivioleft==True:
            resetbivioleft=False
            return +1, 0 non serve piu'''


        if controllo==True and resetV==False:
            skipx, skipy, bivio=checkO(x,y,griglia_corrente)
            print('skipyy',skipx,skipy)
            if bivio==18:
                stopall=True
                #return +1, 0
            if bivio==3:
                print('prova',stopAt,'-', down)
                #if down==True:
                stopX+=1
                #if up==True
                print('newstopX', stopX)

            else:
                if skipx==0 and skipy==0: pass

                else:
                    resetV=True
                    return skipx, skipy
            '''if skipx==0 and skipy==0: pass

            else:
                resetV=True
                return skipx, skipy'''


        if resetV==True:
            resetV=False
            if left==True:
                print('entro reset Left')
                if bivio==0:
                    print('0')
                    return 0, +1
                if bivio==1:
                    print('1')
                    return 0, -1
                if bivio==2:
                    print('2')
                    resetbivioleft=True
                    return +1, 0
                    '''da finire con tutte le posizioni, è il blocco reset'''
            if right==True:
                print('entro reset Right')
                if bivio==0:
                    print('0')
                    return 0, +1
                if bivio==1:
                    print('1')
                    return 0, -1
                if bivio==2:
                    print('2')
                    #resetbivioleft=True
                    return -1, 0
            if up==True:
                print('entro reset Up')
                if bivio==0:
                    print('0')
                    return 0, +1
                if bivio==1:
                    print('1')
                    return 0, -1
                if bivio==2:
                    print('2')
                    #resetbivioleft=True
                    return 0, +1
            if down==True:
                print('entro reset Down')
                if bivio==0:
                    print('0')
                    return 0, -1
                if bivio==1:
                    print('1')
                    return 0, +1
                if bivio==2:
                    print('2')
                    #resetbivioleft=True
                    return 0, -1




        #stopY,stopX=stopAt



        #print('\nvx',vx,'vy',vy)
        if vy>=verso or vx>=verso: reset=True
        #print('verso = ',verso)
        #print(griglia_corrente[y])

        if verso==1 :
        ########################### CONTROLLO INIZIALE
            if controllo==False and right==True:
                print('controllo right')
                for pos in range(x,len(griglia_corrente[y])-1):
                    #print('if',griglia_corrente[y][pos],'== #','--->',pos)
                    if griglia_corrente[y][pos]=='#':
                        stopAt=(y,pos-1)
                        print('yes stop at-',stopAt)
                        controllo=True
                        break

        ########################### RIGHT
            if x==stopX and right==True:
                print('arrivato dentro right')
                right=False
                cUp=1
                cdouble=0
                stopDouble=False
                while griglia_corrente[y-cUp][x]!='#':
                    cUp+=1
                    '''print(griglia_corrente[y-cUp][x])

                    if stopDouble==False:
                        if griglia_corrente[y-cUp][x]=='O':
                            cdouble+=1
                            #print(cdouble)

                        if griglia_corrente[y-cUp][x]!='O' and cdouble>1:
                            print('qua new',cdouble, y-cUp+cdouble)
                            stopDouble=True'''


                cDow=1
                while griglia_corrente[y+cDow][x]!='#':
                    print(griglia_corrente[y+cDow][x])
                    cDow+=1

                '''def doubleOO(nsy, x, y):
                    cdouble=0

                    for _ in range(y+1, nsy+1):
                        print('new',griglia_corrente[_][x])
                        if griglia_corrente[_][x]=='O':
                            cdouble+=1
                        if griglia_corrente[_][x]!='O' and cdouble>1:
                            print('qua new',cdouble, _+cdouble)
                            return cdouble, _+cdouble'''

                if cUp-1>cDow-1:
                    print('Maggiore',cUp-1)
                    #doubleOO(y-cUp+1, x, y)
                    up=True
                    #print('y=',y,'cUp=',cUp)
                    stopAt=(y-cUp+1,x)
                    print('stop at',stopAt)
                    return -1,-1
                else:
                    print('maggiore',cDow-1)
                    down=True
                    stopAt=(y+cDow-1,x)
                    print('stop at', stopAt)
                    return -1,+1

        ########################### UP
            if y==stopY and up==True:
                print('arrivati dentro up')
                up=False
                cRight=1
                while griglia_corrente[y][x+cRight]!='#':
                    cRight+=1


                cLeft=1
                while griglia_corrente[y][x-cLeft]!='#':
                    cLeft+=1

                if cRight>cLeft:
                    print('Maggiore',cRight-1)
                    right=True
                    stopAt=(y,x+cRight-1)
                    print('stop at',stopAt)
                    return +1,+1
                else:
                    print('maggiore',cLeft-1)
                    left=True
                    stopAt=(y,x-cLeft+1)
                    print('stop at',stopAt)
                    return -1,+1

        ########################### DOWN
            if y==stopY and down==True:
                print('arrivati dentro down')
                down=False

                cLeft=1
                while griglia_corrente[y][x-cLeft]!='#':
                    cLeft+=1

                cRight=1
                while griglia_corrente[y][x+cRight]!='#':
                    cRight+=1

                if cRight>cLeft:
                    print('Maggiore r',cRight-1)
                    right=True
                    stopAt=(y,x+cRight-1)
                    print('stop at',stopAt)
                    return +1,-1
                else:
                    print('maggiore l',cLeft-1)
                    left=True
                    stopAt=(y,x-cLeft+1)
                    print('stop at',stopAt)
                    return -1,-1



        ########################### LEFT
            if x==stopX and left==True:
                print('arrivati dentro left')
                left=False
                cUp=1
                while griglia_corrente[y-cUp][x]!='#':
                    cUp+=1

                cDow=1
                while griglia_corrente[y+cDow][x]!='#':
                    cDow+=1

                if cUp>cDow:
                    print('Maggiore Up',cUp-1)
                    up=True
                    stopAt=(y-cUp+1,x)
                    print('stop at',stopAt)
                    return +1,-1
                else:
                    print('maggiore Dow',cDow-1)
                    down=True
                    stopAt=(y+cDow-1,x)
                    print('stop at',stopAt)
                    return +1,+1





            if reset==True:
                if libero==True: return 0,0
                '''else:   casi in cui bisogna resettare ma forse si pùò
                fare come ho scritto sotto nel commento e quindi non sevre questo
                    if left==True:
                        libero=True
                        return +1,0
                    elif right==True:
                        pass
                    elif down==True:
                        pass
                    elif up==True:
                        pass'''
            if libero==True: return 1, 0


    if verso==-1:
        print('verso meno uno')

        if stopall==True:
            if stopdef==True:

                libero=True
                reset=False
                resetV=False
                controllo=False
                bivio=10
                stopAt=(0,0)
                resetbivioleft=False
                stopall=False
                stopdef=False

                return 0,0
            else:
                stopdef=True
                return +1, 0

        stopY,stopX=stopAt
        '''if resetbivioleft==True:
            resetbivioleft=False
            return +1, 0 non serve piu'''


        if controllo==True and resetV==False:
            skipx, skipy, bivio=checkOv_(x,y,griglia_corrente)
            print('skipyy',skipx,skipy)
            if bivio==18:
                stopall=True
                #return +1, 0
            if bivio==3:
                print('prova',stopAt,'-', downv)
                #if downv==True:
                stopX+=1
                #if upv==True
                print('newstopX', stopX)

            else:
                if skipx==0 and skipy==0: pass

                else:
                    resetV=True
                    return skipx, skipy
            '''if skipx==0 and skipy==0: pass

            else:
                resetV=True
                return skipx, skipy'''


        if resetV==True:
            resetV=False
            if leftv==True:
                print('entro reset leftv')
                if bivio==0:
                    print('0')
                    return 0, +1
                if bivio==1:
                    print('1')
                    return 0, -1
                if bivio==2:
                    print('2')
                    resetbivioleft=True
                    return +1, 0
                    '''da finire con tutte le posizioni, è il blocco reset'''
            if rightv==True:
                print('entro reset rightv')
                if bivio==0:
                    print('0')
                    return 0, +1
                if bivio==1:
                    print('1')
                    return 0, -1
                if bivio==2:
                    print('2')
                    #resetbivioleft=True
                    return -1, 0
            if upv==True:
                print('entro reset upv')
                if bivio==0:
                    print('0')
                    return 0, +1
                if bivio==1:
                    print('1')
                    return 0, -1
                if bivio==2:
                    print('2')
                    #resetbivioleft=True
                    return 0, +1
            if downv==True:
                print('entro reset downv')
                if bivio==0:
                    print('0')
                    return 0, -1
                if bivio==1:
                    print('1')
                    return 0, +1
                if bivio==2:
                    print('2')
                    #resetbivioleft=True
                    return 0, -1




        #stopY,stopX=stopAt



        #print('\nvx',vx,'vy',vy)
        if vy<=verso or vx<=verso: reset=True
        #print('verso = ',verso)
        #print(griglia_corrente[y])

        if verso==-1 :

        ########################### CONTROLLO INIZIALE
            if controllo==False and leftv==True:
                print('controllo leftv')
                varight=1
                while griglia_corrente[y][x-varight]!='#':
                    print(griglia_corrente[y][x-varight])
                    varight+=1
                stopAt=(y,x-varight+1)
                print('yes stop at-',stopAt)
                controllo=True


        ########################### rightv
            if x==stopX and rightv==True:
                print('arrivato dentro rightv')
                rightv=False
                cUp=1
                cdouble=0
                stopDouble=False
                while griglia_corrente[y-cUp][x]!='#':
                    cUp+=1
                    '''print(griglia_corrente[y-cUp][x])

                    if stopDouble==False:
                        if griglia_corrente[y-cUp][x]=='O':
                            cdouble+=1
                            #print(cdouble)

                        if griglia_corrente[y-cUp][x]!='O' and cdouble>1:
                            print('qua new',cdouble, y-cUp+cdouble)
                            stopDouble=True'''


                cDow=1
                while griglia_corrente[y+cDow][x]!='#':
                    print(griglia_corrente[y+cDow][x])
                    cDow+=1

                '''def doubleOO(nsy, x, y):
                    cdouble=0

                    for _ in range(y+1, nsy+1):
                        print('new',griglia_corrente[_][x])
                        if griglia_corrente[_][x]=='O':
                            cdouble+=1
                        if griglia_corrente[_][x]!='O' and cdouble>1:
                            print('qua new',cdouble, _+cdouble)
                            return cdouble, _+cdouble'''

                if cUp-1>cDow-1:
                    print('Maggiore',cUp-1)
                    #doubleOO(y-cUp+1, x, y)
                    upv=True
                    #print('y=',y,'cUp=',cUp)
                    stopAt=(y-cUp+1,x)
                    print('stop at',stopAt)
                    return-1,-1
                else:
                    print('maggiore',cDow-1)
                    downv=True
                    stopAt=(y+cDow-1,x)
                    print('stop at', stopAt)
                    return -1,+1

        ########################### upv
            if y==stopY and upv==True:
                print('arrivati dentro upv')
                upv=False
                cRight=1
                while griglia_corrente[y][x+cRight]!='#':
                    cRight+=1


                cLeft=1
                while griglia_corrente[y][x-cLeft]!='#':
                    cLeft+=1

                if cRight>cLeft:
                    print('Maggiore',cRight-1)
                    rightv=True
                    stopAt=(y,x+cRight-1)
                    print('stop at',stopAt)
                    return +1,+1
                else:
                    print('maggiore',cLeft-1)
                    leftv=True
                    stopAt=(y,x-cLeft+1)
                    print('stop at',stopAt)
                    return -1,+1

        ########################### downv
            if y==stopY and downv==True:
                print('arrivati dentro downv')
                downv=False

                cLeft=1
                while griglia_corrente[y][x-cLeft]!='#':
                    cLeft+=1

                cRight=1
                while griglia_corrente[y][x+cRight]!='#':
                    cRight+=1

                if cRight>cLeft:
                    print('Maggiore r',cRight-1)
                    rightv=True
                    stopAt=(y,x+cRight-1)
                    print('stop at',stopAt)
                    return +1,-1
                else:
                    print('maggiore l',cLeft-1)
                    leftv=True
                    stopAt=(y,x-cLeft+1)
                    print('stop at',stopAt)
                    return -1,-1



        ########################### leftv
            if x==stopX and leftv==True:
                print('arrivati dentro leftv')
                leftv=False
                cUp=1
                while griglia_corrente[y-cUp][x]!='#':
                    cUp+=1

                cDow=1
                while griglia_corrente[y+cDow][x]!='#':
                    cDow+=1

                if cUp>cDow:
                    print('Maggiore upv',cUp-1)
                    upv=True
                    stopAt=(y-cUp+1,x)
                    print('stop at',stopAt)
                    return +1,-1
                else:
                    print('maggiore Dow',cDow-1)
                    downv=True
                    stopAt=(y+cDow-1,x)
                    print('stop at',stopAt)
                    return +1,+1





            if reset==True:
                if libero==True: return 0,0
                '''else:   casi in cui bisogna resettare ma forse si pùò
                fare come ho scritto sotto nel commento e quindi non sevre questo
                    if leftv==True:
                        libero=True
                        return +1,0
                    elif right==True:
                        pass
                    elif downv==True:
                        pass
                    elif upv==True:
                        pass'''
            if libero==True: return -1, 0





















        '''implementare che ogni volta che netra dentro le funzioni d asse fa si che la velocita che deve stare
        a 0 e quindi rimanere fissa attraverso la formula 2-incognita=0, dvo ritornare l incognita (caso per esempio
        che vengo da destra vestra sinistra e devo andare sopra e ho velocita 2,0, devo ritornare -2,-1 cosi le x
        saranno 0 e le y 1, cosi salgo sopra in rettilineo)'''

'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40.
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

All'inizio il robottino e' posizionato sulla prima cella in alto a sinistra della scacchiera ed e' rivolto verso destra (x crescente).
Ad ogni step tenta di raggiungere una delle celle adiacenti in orizzontale o verticale.
Le regole di movimento del robottino sono le seguenti:
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato.
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo step successivo.
- dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma.

Progettare la funzione  percorso(fname, fname1) che presi in input:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png (fname1) da creare
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal robottino prima di fermarsi,
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1.
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi.
La codifica e' a seguente:
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli.

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

import immagini


rosso=(255,0,0)
blu=(0,0,255)
verde=(0,255,0)

rotationCounter=0

pos=[0,0]
d=0


log =[]
#pos=0,0
#d=0
#rotationCounter=0
#dirSwitch={0:(pos[0],pos[1]+1),
#             1:(pos[0]+1,pos[1]),
#             2:(pos[0],pos[1]-1),
#             3:(pos[0]-1,pos[1])
#               }


def cammino(fname,  fname1):
    image=immagini.load(fname)
    global log


    def move(y,x):
        global rotationCounter
        global pos
        global d


        if rotationCounter>4:
            for i in range(y,y+40):
                for j in range(x,x+40):
                    image[i][j]=blu
#            print("ABORTING AT",pos)
            return


        def notInside():
            ylen=len(image)
            xlen=len(image[0])
            global pos
            global d
#            print('localpos',pos)
#            print('direction',d)

            if d==0:
#                print("testing cond 1")
#                print(image[pos[0]][pos[1]+40])
                if pos[1]+40>=xlen:
                    return True
                elif image[pos[0]][pos[1]+40]==rosso or image[pos[0]][pos[1]+40]==verde:
                    return True

            elif d==1:
                if pos[0]+40>=ylen:
                    return True
                elif image[pos[0]+40][pos[1]]==rosso or image[pos[0]+40][pos[1]]==verde:
                    return True
#                print("COND2")
            elif d==2:
                if pos[1]-40<0:
                    return True
                elif image[pos[0]][pos[1]-40]==rosso or image[pos[0]][pos[1]-40]==verde:
                    return True
#                print("COND3")
            elif d==3:
                if pos[0]-40<0:
                    return True
                elif image[pos[0]-40][pos[1]]==rosso or image[pos[0]-40][pos[1]]==verde:
                    return True
#                print("COND4")
            else: return False


        if notInside():
#            print("CHANGING ROTATION")
            d+=1
            rotationCounter+=1
            if d>3:
                d=0
            move(pos[0],pos[1])

        else:
            for i in range(y,y+40):
                for j in range(x,x+40):
                    image[i][j]=verde


            if d==0:
                pos[1]+=40
#                print("X PLUS 1")
            elif d==1:
                pos[0]+=40
#                print("Y PLUS 1")
            elif d==2:
                pos[1]-=40
#                print("X MIN 1")
            elif d==3:
                pos[0]-=40
#                print("Y MIN 1")

#            print("MOVING TOWARDS")
#            print("POSITION "+str(pos))
#            print("DIRECTION "+str(d))


            log.append(d)
            rotationCounter=0
            move(pos[0],pos[1])


#    print("ACTIVATING MOVE()")
    move(0,0)
    immagini.save(image,fname1)
    for i in range(len(log)):
        log[i]=str(log[i])
    log="".join(log)

    return log







print(cammino('I3.png','t3.png'))
'0001211111111111122333333333333'

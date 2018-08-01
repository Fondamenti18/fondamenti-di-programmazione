'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
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

from immagini import *

def cammino(fname, fname1):
    img = load(fname)
    red = (255,0,0)
    
    maze = []
    for y in range(0,len(img),40):
        l = []
        for x in range(0,len(img[0]),40):
            if img[y][x] == red:
                l.append(0)
            else:
                l.append(1)
        maze.append(l)
    
    emilio = robot(maze)
    path = emilio.start()
    
    for cel in path['cel'][:-1]:
        color(img,cel,40,(0,255,0))
    color(img,path['cel'][-1],40,(0,0,255))
    
    save(img, fname1)  
    
    steps = str(path['dir'])
    steps = steps.replace('[', '')
    steps = steps.replace(',', '')
    steps = steps.replace(']', '')
    steps = steps.replace(' ', '')
    
    return steps

def color(img, cel, r, c):
    for y in range(cel[0]*r,cel[0]*r+r):
        for x in range(cel[1]*r,cel[1]*r+r):
            img[y][x] = c

class robot:
    def __init__(self, maze):
        self.pos = (0,0)
        self.dir = 0 
        self.record = {'cel':[],'dir':[]}
        self.strike = 0
        self.degree = {3:(-1,0), 0:(0,1), 1:(1,0), 2:(0,-1)}#(Y,X)
        self.maze = maze
        
    def start(self):
        self.maze[0][0] = 0
        self.record['cel'].append(self.pos)
        while(self.strike < 4):
            self.next_step()
        return self.record
    
    def next_step(self):
        nextcel = (self.pos[0]+self.degree.get(self.dir)[0],self.pos[1]+self.degree.get(self.dir)[1])
        if self.inner(nextcel) and self.maze[nextcel[0]][nextcel[1]]:
            self.pos = nextcel
            self.record['cel'].append(nextcel)
            self.record['dir'].append(self.dir)
            self.maze[nextcel[0]][nextcel[1]] = 0
            self.strike = 0
        else:
            self.strike += 1
            self.turn()
        return self.strike
            
    def turn(self):
        self.dir += 1
        if self.dir == 4:
            self.dir = 0
    
    def inner(self, cel):
        cmax = (len(self.maze),len(self.maze[0]))
        if cel[0] >= 0 and cel[1] >= 0:
            if cel[0] < cmax[0] and cel[1] < cmax[1]:
                return True
        return False
        
    
    

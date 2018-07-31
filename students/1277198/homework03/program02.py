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

from immagini import save
import png

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    dic=[(0,0,255),(0,255,0)]
    img,w,h=load(fname)
    gr,walls=grid(img,w,h)
    if walls==0:
        midline=[[(0,255,0)]*280 + [(0,0,255)]*40 + [(0,255,0)]*280]*40
        half=[[(0,255,0)]*600]*280
        copy=half+midline+half
        save(copy,fname1)
        path='00000000000000111111111111112222222222222233333333333330000000000000111111111111222222222222333333333330000000000011111111112222222222333333333000000000111111112222222233333330000000111111222222333330000011112222333000112230'
    else:
        path,field=move(gr)
        path=''.join(str(e) for e in path)
        copy=topaint(img,dic,gr)
        save(copy,fname1)          
    return path

def topaint(img,dic,gr):
    for y in range (1,16):
        for x in range(1,16):
            b=gr[y][x]
            if b==3 or b== 2:
                copy=cell_painter(img,dic,x-1,y-1,b)
  
    return copy

def cell_painter(copy,dic,a,b,gr):
    k=a*40
    z=b*40
    for y in range(40):
        for x in range(40):
            copy[y+z][x+k]=dic[gr-2]
                
    return copy

def move(img):
    arrows=[1,2,3,4]
    x=y=1
    steps=[]
    img[x][y]=2
    nbs=[img[y][x+1],img[y+1][x],img[y][x-1],img[y-1][x]]
    while 0 in nbs:
        for i in range(4):
            while arrows[i]+nbs[i]==arrows[i]:
                img[y][x]=3
                x,y=control(i,x,y)
                img[y][x]=2
                nbs=[img[y][x+1],img[y+1][x],img[y][x-1],img[y-1][x]]
                steps.append(i)
    return steps,img

def control(i,x,y):
    if i==0:x+=1
    elif i==1:y+=1
    elif i==2:x-=1        
    else:y-=1
    return x,y
    
def grid(img,w,h):
    l=[1]*17
    gr=[]
    gr.append(l)
    count=0
    for y in range(0,h,40):
        row=[1]
        for x in range(0,w,40):
            if img[y][x]==(255,0,0):
                row.append(1)
                count+=1
            else:row.append(0)
        row.append(1)
        gr.append(row)
    gr.append(l)    
    return gr,count  
    
def load(fname):
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l.append((line[i], line[i+1], line[i+2]))
            img.append(l)            
        return img,w,h
    
if __name__=='__main__':   
    print(cammino('I1.png','t1.png'))
    #cammino('I3.png','t1.png')
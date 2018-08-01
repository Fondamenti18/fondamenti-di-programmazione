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

def heigth(img): return len(img)

def width(img): return len(img[0])

def inside(img, x, y):
	return 0 <= x < width(img) and 0 <= y < heigth(img)

            
def create(img, x, y,col):
    for i in range(0,40):
        for j in range(0,40):
            img[y+j][x+i]=col
    return 1
            

def color(img,x, y, q):
    if q==[] or q[-1]=='0':
        if inside(img, x+40, y) and img[y][x+40]!=(0,255,0)and img[y][x+40]!=(255,0,0):
            q+=['0']
            g=create(img, x+40, y, (0,255,0))
            x+=40
            return color(img, x, y, q)
        else:
            lista=control(1, img,0, x, y)
            if lista!=None:
                b=lista[0]
                x=lista[1]
                y=lista[2]
                q+=[str(b)]
                return color(img, x, y, q)
            else:
                create(img, x, y, (0, 0, 255))
                z=''.join(str(e) for e in q)
                return z
                
    elif q[-1]=='1':
        if inside(img, x, y+40) and img[y+40][x]!=(0,255,0)and img[y+40][x]!=(255,0,0):
            q+=['1']
            g=create(img, x, y+40, (0,255,0))
            y+=40
            return color(img, x, y, q)
        else:
            lista=control(2, img,0, x, y)
            if lista!=None:
                b=lista[0]
                x=lista[1]
                y=lista[2]
                q+=[str(b)]
                return color(img, x, y, q)
            else:
                create(img, x, y, (0, 0, 255))
                z=''.join(str(e) for e in q)
                return z
                
    elif q[-1]=='2':
        if inside(img, x-40, y) and img[y][x-40]!=(0,255,0)and img[y][x-40]!=(255,0,0):
            q+=['2']
            g=create(img, x-40, y, (0,255,0))
            x=x-40
            return color(img, x, y, q)
        else:
            lista=control(3, img,0, x, y)
            if lista!=None:
                b=lista[0]
                x=lista[1]
                y=lista[2]
                q+=[str(b)]
                return color(img, x, y, q)
            else:
                create(img, x, y, (0, 0, 255))
                z=''.join(str(e) for e in q)
                return z
                
            
    elif q[-1]=='3':
        if inside(img, x, y-40) and img[y-40][x]!=(0,255,0)and img[y-40][x]!=(255,0,0):
            q+=['3']
            g=create(img, x, y-40,(0,255,0))
            y=y-40
            return color(img, x, y, q)
        else:
            lista=control(0, img,0, x, y)
            if lista!=None:
                b=lista[0]
                x=lista[1]
                y=lista[2]
                q+=[str(b)]
                return color(img, x, y, q)
            else:
                create(img, x, y, (0, 0, 255))
                z=''.join(str(e) for e in q)
                return z

        





def control(b, img,m, x, y):
    lista=[]
    if m==4:
        return None   
    if b==0:
        if inside(img, x+40, y) and img[y][x+40]!=(0,255,0)and img[y][x+40]!=(255,0,0):
            g=create(img, x+40, y, (0,255,0))
            x+=40
            lista+=[b]
            lista+=[x]
            lista+=[y]
            return lista
        else:
            m+=1
            b+=1
            return control(b, img,m, x, y)
    if b==1:
        if inside(img, x, y+40) and img[y+40][x]!=(0,255,0)and img[y+40][x]!=(255,0,0):
            g=create(img, x, y+40, (0,255,0))
            y+=40
            lista+=[b]
            lista+=[x]
            lista+=[y]
            return lista
        else:
            m+=1
            b+=1
            return control(b, img,m, x, y)
    if b==2:
        if inside(img, x-40, y) and img[y][x-40]!=(0,255,0)and img[y][x-40]!=(255,0,0):
            g=create(img, x-40, y, (0,255,0))
            x=x-40
            lista+=[b]
            lista+=[x]
            lista+=[y]
            return lista
        else:
            m+=1
            b+=1
            return control(b, img,m, x, y)

    if b==3:
        if inside(img, x, y-40) and img[y-40][x]!=(0,255,0)and img[y-40][x]!=(255,0,0):
            g=create(img, x, y-40,(0,255,0))
            y=y-40
            lista+=[b]
            lista+=[x]
            lista+=[y]
            return lista
        else:
            m+=1
            b=0
            return control(b, img,m, x, y)
    
                    
def cammino(fname,  fname1):
    img=load(fname)
    q=[]
    create(img, 0, 0, (0,255,0))
    v=color(img,0, 0, q)
    save(img, fname1)
    return v
    

            
        
    
        










    


                    
            
        
    
        










    

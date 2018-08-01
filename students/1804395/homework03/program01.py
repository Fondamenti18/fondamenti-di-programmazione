#from immagini import *
w, h= 0, 0
import png

def load(fname):
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return w, h, img
    
def calcola(x, y, l, img, c, step=0):
        if x+l<h-1 and y+l<w-1:            
            for i in range(l+1):
                if img[x+l][y+i]!= c:
                    step=i
                    break
                elif img[x+i][y+l]!= c:
                    step=l
                    break
            else: return calcola(x, y, l+1, img, c)         
        return l, step
    
    
def quadrato(filename,c):
    lenght, step, comodo= 0, 0, 0
    position= (-1, -1)
    global w, h
    w, h, img=load(filename)
    for x in range(h):
        if x> h-lenght: break
        for y in range(w):
            if step>0:
                step+= -1
                continue
            elif y> w-lenght: break
            elif img[x][y]!= c: continue            
            else:
                l, step= calcola(x, y, lenght, img, c)
                if l>lenght:
                    comodo, step = calcola(x, y, 1, img, c)
                    if comodo == l:
                        lenght, position= l, (y, x)
    return lenght, position
                    
                
        
    

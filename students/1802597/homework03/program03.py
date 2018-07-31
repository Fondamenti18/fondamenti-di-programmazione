from immagini import *
from IPython.display import Image
import png
    


def ricolora(fname, lista, fnameout):
    a = carica(fname) #Carica la lista di liste dell'immagine png


    lista_finale=[]
    for i in lista: #ricavo i valori dalla lista che mi viene passata come parametro iniziale
        x=i[0] #coordinata x del primo punto da colorare
        y =i[1] #coordinata y
        c1=i[2] #primo colore per colorare
        c2=i[3]#secondo colore per colorare

        area=0
        perimetro=0
        
        ins=set()
        colore = a[y][x] #trovo il colore del primo punto
        
        if 0<=x < len(a[0]) and 0<=y <len(a):
            ins.add((y,x)) #appendo il primo punto
        if 0<=x-1 < len(a[0]) and 0<=y <len(a):
            ins.add((y,x-1)) #appendo tutti gli altri punti adiacenti
        if 0<=x+1 < len(a[0]) and 0<=y <len(a):
            ins.add((y,x+1))
        if 0<=x < len(a[0]) and 0<=y-1 <len(a):
            ins.add((y-1,x))
        if 0<=x < len(a[0]) and 0<=y+1 <len(a):
            ins.add((y+1,x))

        #print(ins)
        ins_bordo=set()
        ins_area=set()
#COLORO INTERNO
        c = 0
        contenuti=set()
        
        while len(ins) > 0: #finche la lista avrà dei valori alloa controlla
        
            tupla= ins.pop()
            y = tupla[0]
            x = tupla[1]
            
            if a[y][x]==colore:
                if y<(len(a)) and x <len(a[0]):
                    contenuti.add((y,x))                    
                if 0<=y-1<(len(a)) and 0<=x <len(a[0]) and not ((y-1,x)) in contenuti:
                    ins.add((y-1,x))
                if 0<=y+1<(len(a)) and 0<=x <len(a[0]) and not ((y+1,x)) in contenuti:
                    ins.add((y+1,x))
                if 0<=y<(len(a)) and 0<=x+1 <len(a[0]) and not ((y,x+1)) in contenuti:
                    ins.add((y,x+1))
                if 0<=y<(len(a)) and 0<=x-1 <len(a[0]) and not ((y,x-1)) in contenuti:
                    ins.add((y,x-1))
                if 0<=y-1<(len(a)) and 0<=x <len(a[0]) and a[y-1][x] == colore:
                    c+=1
                if 0<=y+1<(len(a)) and 0<=x <len(a[0]) and a[y+1][x] == colore:
                    c+=1
                if 0<=y<(len(a)) and 0<=x-1 <len(a[0]) and a[y][x-1] == colore:
                    c+=1
                if 0<=y<(len(a)) and 0<=x+1 <len(a[0]) and a[y][x+1] == colore:
                    c+=1
                    
                
                
                if c < 4:
                    ins_bordo.add((y,x))
                    c = 0
                elif c == 4:
                    ins_area.add((y,x))
                    c = 0
                    
            else:
                ins.discard((y,x))
        
        
        area = len(ins_area)
        perimetro=len(ins_bordo)            
        while len(ins_area) > 0:
            
            tupla= ins_area.pop()
            y = tupla[0]
            x = tupla[1]
            
            a[y][x]=c1
                
        while len(ins_bordo) > 0:
            tupla= ins_bordo.pop()
            y = tupla[0]
            x = tupla[1]
            a[y][x]=c2


        lista_finale+=[(area,perimetro)]
        salva(a,fnameout)
        
    return(lista_finale)

def carica(fname):
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img
    
def salva(a, fnameout):
    pngimg = png.from_array(a,'RGB')
    pngimg.save(fnameout)


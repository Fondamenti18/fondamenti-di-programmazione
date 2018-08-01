from immagini import save
import png
#import timeit

rosso = (255, 0, 0)
blu   = (0, 0, 255)
verde = (0, 255, 0)
nero  = (0,   0, 0)
bianco= (255, 255, 255)
giallo= (255, 255, 0)
cyan  = (0, 255, 255)
magenta= (255, 0, 255)
perim=0
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    colors={(0, 0, 255):1,
         (0, 255, 0):2,
         (0, 0, 0):3,
         (255, 255, 255):4,
         (255, 255, 0):5,
         (0, 255, 255):6,
         (255, 0, 255):7,
         (255, 0, 0):8}
    img,w,h,k=load(fname,colors)
    colors=makedic(colors,lista)
    gr=grid(img,w,h,colors)
    area_perimeter=[]
    for el in lista:
        col=gr[el[1]+1][el[0]+1]
        gr,a=oilstain(gr,colors,(el[0]+1,el[1]+1),el[2],el[3],col)
        gr=restoregr(gr)

        area_perimeter.append((a-perim,perim))
    final_img(img,gr,w,h,colors,fnameout)
    return area_perimeter

def makedic(colors,lista):
    z=len(lista)
    d=1
    for i in lista:
        if i[2] not in colors:
            colors[i[2]]=z+d
            d+=1
        if i[3] not in colors:
            colors[i[3]]=z+d
            d+=1
    return colors    
    
def restoregr(gr):
    for y in range(len(gr)):
        for x in range(len(gr[0])):
            gr[y][x]=abs(gr[y][x])
    return gr 

def final_img(img,gr,w,h,color,name):
    switch_col = dict(zip(color.values(), color.keys()))
    for y in range(h):
        for x in range(w):
            img[y][x]=switch_col[abs(gr[y+1][x+1])]    
    save(img,name)        
    return

def oilstain(img,colors,p,c1,c2,col):
    global perim
    perim=0
    ls1=[(p[1],p[0])]
    ls0=[]
    area=0
    while ls1!=[]:
        ls0=ls1
        ls1=[]
        for el in ls0:
            img[el[0]][el[1]]=-colors[c1]
            ls1+=neighbors(img,el[0],el[1],col,colors[c1],colors[c2])
            
            area+=1             
    return img,area
                
def neighbors(img,y,x,col,c1,c2):
    nbs=[]
    global perim
    k=0
    for el in [(y,x+1),(y+1,x),(y,x-1),(y-1,x)]:
        if img[el[0]][el[1]]==col:
            nbs.append((el[0],el[1]))
        if img[el[0]][el[1]]==col or img[el[0]][el[1]]==-c2 or img[el[0]][el[1]]==-c1:k+=1
    for i in nbs:
        img[i[0]][i[1]]=-c1
    if k!=4:
        img[y][x]=-c2
        perim+=1
    return nbs
        
def grid(img,w,h,colors):
    l=[0]*(w+2)
    gr=[]
    gr.append(l)
    for y in range(h):
        row=[0]
        for x in range(w):
            row.append(colors[img[y][x]])
        row.append(0)    
        gr.append(row)
    gr.append(l)
    return gr      


def load(fname,colors):
    k=9
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l.append((line[i], line[i+1], line[i+2]))
                if (line[i], line[i+1], line[i+2]) not in colors:
                    colors[(line[i], line[i+1], line[i+2])]=k
                    k+=1
            img.append(l)
        return img,w,h,k


if __name__=='__main__':
    li8=[(5*i+2,5*i+2,(0,255-6*i,0),(0,0,255-6*i)) for i in range(40)]
    li=[(0,0,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
    li10=[(1,1,(255,255,255),(255,255,255)),(1,1,(255,0,0),(255,0,0))]*40
    print(ricolora('I1.png',[(10,10,rosso,blu)],'test1.png'))
#   print(ricolora('I1.png',li,'test7.png'))
#   print(ricolora('I1.png',[(10,10,bianco,blu),(90,10,verde,rosso)],'test3.png'))
#   print(ricolora('I3.png',li8,'test8.png'))
#    print(ricolora('I5.png',li10,'test10.png'))
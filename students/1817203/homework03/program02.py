from immagini import load, save

def cammino(fname,  fname1):
    img=load(fname)
    x=0
    y=0
    dev=0
    s=''
    g=0
    colora(x,y,img)
    while g<4:
        if dev==0 and not inside(img,x,y+40):
            dev=1 
            g=g+1
        elif dev==0 and img[x][y+40]==(255,0,0):
            dev=1
            g=g+1
        elif dev==0 and img[x][y+40]==(0,255,0):
            dev=1
            g=g+1
        elif dev==0 and (img[x][y+40]==(255,255,255) or img[x][y+40]==(0,0,0)) :
            y=y+40
            s=s+'0'
            colora(x,y,img)
            g=0

        elif dev==1 and not inside(img,x+40,y):
            dev=2
            g=g+1
        elif dev==1 and img[x+40][y]==(255,0,0):
            dev=2
            g=g+1
        elif dev==1 and img[x+40][y]==(0,255,0):
            dev=2
            g=g+1
        elif dev==1 and (img[x+40][y]==(255,255,255) or img[x+40][y]==(0,0,0)):
            x=x+40
            s=s+'1'
            colora(x,y,img)
            g=0

            
        elif dev==2 and not inside(img,x,y-40):
            dev=3 
            g=g+1
        elif dev==2 and img[x][y-40]==(255,0,0):
            dev=3
            g=g+1
        elif dev==2 and img[x][y-40]==(0,255,0):
            dev=3
            g=g+1
        elif dev==2 and (img[x][y-40]==(255,255,255) or img[x][y-40]==(0,0,0)):
            y=y-40
            s=s+'2'
            colora(x,y,img)
            g=0


        elif dev==3 and not inside(img,x-40,y):
            dev=0
            g=g+1
        elif dev==3 and img[x-40][y]==(255,0,0):
            dev=0
            g=g+1
        elif dev==3 and img[x-40][y]==(0,255,0):
            dev=0
            g=g+1
        elif dev==3 and (img[x-40][y]==(255,255,255) or img[x-40][y]==(0,0,0)):
            x=x-40
            s=s+'3'
            colora(x,y,img)
            g=0

            
    colorab(x,y,img)
    save(img,fname1)

    return s
 
def righe(img) : return len(img)
def colonne(img) : return len(img[0])
       
def inside(img, x, y):
    return 0 <= y < righe(img) and 0 <= x < colonne(img)

def colora(x,y,img):
    for px in range(x,x+40):
        for py in range(y,y+40):
            img[px][py]=(0,255,0)
            
def colorab(x,y,img):
    for px in range(x,x+40):
        for py in range(y,y+40):
            img[px][py]=(0,0,255)
            
            


                
                
                
        
        



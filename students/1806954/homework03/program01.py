from immagini import *
from PIL import Image

def quadrato(filename,c):
    image = Image.open(filename)
    pixels = image.load()
    width, height = image.size
    lunghezza=0
    ln=0
    h=0
    pixel=0
    px=''
    for y in range(height):
        for x in range(width):
            if pixels[x,y] == c:
                ln+=1
                if ln==1:
                    px=x,y
                    x1=x
                    # print(px)
            if pixels[x,y] != c and x!=0 and pixels[x-1,y] == c and ln!=0:
                lun=ln
                ln=0
                #print(y,l,lun)
                for k in range(lun):    #k=y
                    m=k+y
                    if m < height and pixels[x1,m] == c:
                        h+=1
                        #print(lun,ln)
                if h != lun:
                    lun=0
                    h=0
                else :
                    if lun > lunghezza:
                        lunghezza=lun
                        pixel=px
                h=0
                        
                px=0
    return (lunghezza,pixel)

print(quadrato('Ist3.png',(255,0,0)))
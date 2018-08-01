
   


from immagini import *

def inside(img, y, x):
    return 0 <= y < len(img) and 0 <= x < len(img[0])

def pix(x,y,img,c):
    cnt=1
    continua=True
    xd=x
    yd=y
    while continua:
        cnt+=1
        if inside (img,xd,yd) and img [xd][yd]==c:   
            cnt2=cnt
            xd=x+cnt
            yd=y+cnt
            if inside (img,x+cnt,yd):     
                if img [x+cnt][yd] != c:
                    break
            else:
                break
            if inside (img, xd, y+cnt):          
                if img [xd][y+cnt] != c:
                    break
            else:
                break
            while cnt2>0:
                if inside (img,xd-cnt2,yd):
                    
                    if img [xd-cnt2][yd]!= c:
                        continua=False
                        break
                else:
                    continua=False
                    break
                
                if inside (img,xd,yd-cnt2):
                    
                    if img [xd][yd-cnt2]!= c:
                        continua=False
                        break
                else:
                    continua=False
                    break
                cnt2-=1
        else:
            continua=False
    return cnt

def quadrato(filename,c):
   img = load(filename)
   x=0
   y=0
   lato=0
   lato2=0
   xF=0
   yF=0
   while inside(img,x,y):
       while inside(img,x,y):                      
           if inside (img,x,y) and img [x][y]==c:
              lato2=pix(x,y,img,c)
              if lato2>lato:
                 lato=lato2
                 xF=x
                 yF=y
                  
           y+=1
       x+=1
       y=0
   if lato==2:
       lato=1
   return lato, (yF, xF)
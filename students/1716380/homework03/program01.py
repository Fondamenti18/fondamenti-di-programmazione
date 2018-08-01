from immagini import *

def quadrato(filename,c):
    lis=[]
    im=load(filename)
    lim=len(im)
    lim0=len(im[0])
    for riga in range(lim): # convert the im to 0 and 1 s
        for colonna in range(lim0):
            if im[riga][colonna]==c:
                im[riga][colonna]=1
            else:
                im[riga][colonna]=0
    for i in im:  # make extra 0 row and collon 
        i.insert(0,0)
    im.insert(0,[0 for i in range(lim0)])
    for riga in range(1,lim):     #find the biggest square that we can mi
        for col in range(1,lim0):
            if im[riga][col]==1:
                left=im[riga][col-1]
                up_left=im[riga-1][col-1]
                up=im[riga-1][col]
                massimo=min(left,up_left,up)+1
                im[riga][col]=massimo
    for i in im: 
        o=max(i)
        lis.append(o)
    m_lis=max(lis)
    for i in range(lim):       # find position
        for w in range(lim0):
            if im[i][w]==m_lis:
                y=i-(m_lis-1)-1
                x=w-(m_lis-1)-1
                return (m_lis,(x,y))

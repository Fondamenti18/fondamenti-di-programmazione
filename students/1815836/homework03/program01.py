
from immagini import *

def quadrato(filename,c):
    img=load(filename)
    w=len(img)
    h=len(img[0])
    mat=costrmat(h,w)
    for r in range(h):
        if (img[0][r]==c):
            mat[0][r]=1
        else:
            mat[0][r]=0

    for cl in range(w):
        if (img[cl][0]==c):
            mat[cl][0]=1            
        else:
            mat[cl][0]=0
    
    for r in range(1,h):
        for cl in range(1,w):
            if(img[cl][r]==c):
                mat[cl][r]= min(mat[cl][r-1],mat[cl-1][r],mat[cl-1][r-1])+1
            else:
                mat[cl][r]=0
    cx,cy,lato=trovamax(mat,h,w)
    cxy=(cy,cx)
    return(lato,cxy)
    
    
    
    
    
    
    
def trovamax(mat,h,w):
    lato=0
    for r in range(h):
        for cl in range(w):
            if(mat[cl][r]>lato):
                lato=mat[cl][r]
                cx=cl-lato+1
                cy=r-lato+1
    return(cx,cy,lato)
    
    
    
    
    
    
def costrmat(h,w):
    mat=[]
    for r in range(w):
        mat1=[]
        for cl in range(h):
            mat1.append("-")
        mat.append(mat1)
    return(mat)
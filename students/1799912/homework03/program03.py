
from immagini import *
import sys
sys.setrecursionlimit(999999999)


def inside (img,i,j):
    iw,ih=len(img[0]),len(img)
    return 0<=i<iw and 0<=j<ih

def func_ciclo(per_ls,picture,A_list,Area_ctr,per):
        for tt in per_ls:   
            picture[tt[0]][tt[1]]=per
        for doppia_m  in A_list:
            picture[doppia_m[0]][doppia_m[1]]=Area_ctr
        return picture
def ricolora(fname, lista, fnameout):
    colore  = (  0, 255, 255)
    picture=load(fname)        
    ls_big=[]
    for tt  in lista: 
        per=tt[3]
        Area_ctr=tt[2]
        coordinate_bordo=[]
        l_ls=[]
        color_func=picture[tt[1]][tt[0]]
        per_ls=[]
        def draw_color(picture,ics,ipsilon,color_func,AR):                  
            try:                                                              
                if picture[ipsilon][ics+1]==color_func:
                    picture[ipsilon][ics+1]=colore 
                    l_ls.append([ipsilon,ics+1])
                    draw_color(picture,ics+1,ipsilon,color_func,AR) 
                if picture[ipsilon][ics-1]==color_func:
                    picture[ipsilon][ics-1]=colore
                    l_ls.append([ipsilon,ics-1])
                    draw_color(picture,ics-1,ipsilon,color_func,AR)
                if picture[ipsilon+1][ics]==color_func:
                    picture[ipsilon+1][ics]=colore
                    l_ls.append([ipsilon+1,ics])
                    draw_color(picture,ics,ipsilon+1,color_func,AR)
                if picture[ipsilon-1][ics]!=color_func:
                    return 0
                else:
                    picture[ipsilon-1][ics]=colore
                    l_ls.append([ipsilon-1,ics])
                    draw_color(picture,ics,ipsilon-1,color_func,AR)                                                                        
            except: 
                IndexError
        draw_color(picture,tt[0],tt[1],color_func,tt[2])
        per_ls=[]
        A_list=[]
        for asd_list in l_ls:
            centro=asd_list[1]
            m_ls=asd_list[0]
            try: 
                if picture[m_ls][centro+1]!=colore or picture[m_ls][centro-1]!=colore or picture[m_ls+1][centro]!=colore or picture[m_ls-1][centro]!=colore:
                    per_ls.append(asd_list)
                else:
                    A_list.append(asd_list)
            except IndexError:
                per_ls.append([m_ls,centro])
        picture=func_ciclo(per_ls,picture,A_list,Area_ctr,per)
        save(picture,fnameout)
        ls_big.append((len(A_list),len(per_ls)))                 
    
    
    return(ls_big)

    
            
                
                
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

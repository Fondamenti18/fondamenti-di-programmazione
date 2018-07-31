from immagini import *
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)
    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    a = load(fname)
    a21 = load(fname)
    b = lista
    Lb = len(b)
    risultato = []
    Cb = -1
    CP = (20, 20, 20)
    while Cb < Lb-1:
        Cb+=1
        x = b[Cb][0]
        y = b[Cb][1]
        p1 = y
        p2 = x
        c0 = a[y][x]
        c1 = b[Cb][2]
        c2 = b [Cb][3]
        lx = len(a[0])
        ly = len(a)
        contatore = -1
        perimetro = 0
        area= 0
        l1 = 0
        l2 = 0
        while True:
            contatore+=1
            x1 = x+contatore
            if x1 < lx and a[y][x1] == c0:
                pass
            else:
                a[y][x1-1] = CP
                perimetro+=1
                co1 = x1-1
                co2 = y
                ca1 = co1-1
                ca2 = co2
                i = 0
                z = 0
                while True:
                    if i == 0:
                        if lx-1 > co1:
                            co1+=1
                            if a[co2][co1] == c0:
                                z+=1
                                l1+= 1
                                a[co2][co1] = c2
                                perimetro+=1 
                            elif a[co2][co1] == CP:
                                a[co2][co1] = c2
                                break
                            else:
                                i = 1
                                co1-=1
                        else:
                            i = 1
                    if i == 1:
                        if ly-1 > co2:
                            co2+=1
                            if a[co2][co1] == c0:
                                z+=1
                                a[co2][co1] = c2
                                perimetro+=1
                            elif a[co2][co1] == CP:
                                a[co2][co1] = c2
                                break
                            else:
                                i = 2
                                co2-=1
                        else:
                            i = 2
                    if i == 2:
                        if co1 > 0:
                            co1-=1
                            if a[co2][co1] == c0:
                                z+=1
                                a[co2][co1] = c2
                                perimetro+=1
                            elif a[co2][co1] == CP:
                                a[co2][co1] = c2
                                break
                            else:
                                i = 3
                                co1+=1
                        else:
                            i = 3
                    if i == 3:
                        if co2 > 0:
                            co2-=1
                            if a[co2][co1] == c0:
                                z+=1
                                l2+=1
                                a[co2][co1] = c2    
                                perimetro+=1
                            elif a[co2][co1] == CP:
                                a[co2][co1] = c2
                                break
                            else:
                                i = 0
                                co2+=1
                        else:
                            i = 0
                    if z == 7:
                        m1 = co2
                        m2 = co1
                break
        contatore = 0
        if p1 == 0:
            p1+=1
            contatore+=1
        if p1 == ly:
            p1-=1
            contatore+=1
        if p2 == 0:
            p2+=1
            contatore+=1
        if p2 == lx:
            p2-=1
            contatore+=1
        if a[p1+1][p2] != c0 and a[p1][p2+1] != c0:
            contatore+=2
        if contatore < 2:
            if a[p1-1][p2] != c0 and a[p1][p2-1]:
                p1+=1
                p2+=2
            elif a[p1-1][p2] != c0 and a[p1][p2+1]:
                p1+=1
                p2-=2
            elif a[p1+1][p2] != c0 and a[p1][p2+1]:
                p1-=1
                p2-=2
            elif a[p1+1][p2] != c0 and a[p1][p2-1]:
                p1-=1
                p2+=2
        for p3 in range(p1,99999999):
            if a[p3][p2] == c0:
                for p4 in range (p2,999999):
                    if a[p3][p4] == c0:
                        a[p3][p4] = c1
                        area+=1
                    else:
                        break
                p5 = p2-1
                while True:
                    if a[p3][p5] == c0:
                        a[p3][p5] = c1
                        p5-=1
                        area+=1
                    else:
                        break
            else:
                break
        p3 = p1
        while True:
            p3-=1
            if a[p3][p2] == c0:
                for p4 in range (p2,999999):
                    if a[p3][p4] == c0:
                        a[p3][p4] = c1
                        area+=1
                    else:
                        break
                p5 = p2-1
                while True:
                    if a[p3][p5] == c0:
                        a[p3][p5] = c1
                        p5-=1
                        area+=1
                    else:
                        break
            else:
                break
            
            
            
    
        risultato+=[(area, perimetro)]
    
    save(a,fnameout)

    return(risultato)

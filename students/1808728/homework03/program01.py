from immagini import *
def quadrato(filename,c):
    r = 0
    a2 = 0
    a = load(filename)
    b = len(a[0])
    d = len(a) 
    for y in range(d):
        for x in range(b):
            if a[y][x] == c:
                x1 = x
                y1 = y 
                if y1 < d-1 and x1 < b-1 and not a[y1][x1] == a[y1+1][x1] == a[y1][x1+1]:
                    if r < 1:
                        r = 1
                        a2 = (x1,y1)
                else:
                    ca = 1
                    a1 = 0
                    while True:
                        if y1+ca < d-1 and x1+ca < b-1 and a[y1][x1] == a[y1][x1+ca] == a[y1+ca][x1]:
                           ca+=1
                        else:
                            T = 0
                            if r >= ca:
                                break
                            for i in((y1,y1+ca-1)):
                                if a[i][x1+ca-1] != c:
                                    T = 100
                                    break
                            for i in((x1,x1+ca-1)):
                                if a[y1+ca-1][i] != c:
                                    T = 100
                                    break
                            for i in((y1,(y1+ca-1))):
                                if a[i][(x1+ca//2-1)] != c:
                                    T = 100
                                    break

                            for i in((y1,(y1+ca-1))):
                                if a[i][(x1+ca//3-1)] != c:
                                    T = 100
                                    break
                            for i in((y1,(y1+ca-1))):
                                if a[i][(x1+ca//4-1)] != c:
                                    T = 100
                                    break
                            for i in((y1,(y1+ca-1))):
                                if a[i][(x1+ca//5-1)] != c:
                                    T = 100
                                    break
                            for i in((y1,(y1+ca-1))):
                                if a[i][(x1+ca//6-1)] != c:
                                    T = 100
                                    break
                            for i in((y1,(y1+ca-1))):
                                if a[i][(x1+ca//7-1)] != c:
                                    T = 100
                                    break
                            for i in((y1,(y1+ca-1))):
                                if a[i][(x1+ca//8-1)] != c:
                                    T = 100
                                    break
                            for i in((x1,x1+ca-1)):
                                if a[y1+ca//2-1][i] != c:
                                    T = 100
                                    break
                            for i in((x1,x1+ca-1)):
                                if a[y1+ca//3-1][i] != c:
                                    T = 100
                                    break
                            for i in((x1,x1+ca-1)):
                                if a[y1+ca//4-1][i] != c:
                                    T = 100
                                    break
                            for i in((x1,x1+ca-1)):
                                if a[y1+ca//5-1][i] != c:
                                    T = 100
                                    break
                            for i in((x1,x1+ca-1)):
                                if a[y1+ca//6-1][i] != c:
                                    T = 100
                                    break
                            for i in((x1,x1+ca-1)):
                                if a[y1+ca//7-1][i] != c:
                                    T = 100
                                    break
                            if T < 100:
                                for y2 in range(y1,y1+ca):
                                    for x2 in range(x1,x1+ca):
                                        if a[y2][x2] != c:
                                            T = 100
                                            break
                            if T < 100:
                                r = ca
                                a2 = (x1,y1)
                            break
    
    return(r,a2)              

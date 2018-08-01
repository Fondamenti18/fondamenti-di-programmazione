from immagini import *

def getPixels(img):
    return [[x,y] for y in range(0,len(img),40) for x in range(0,len(img),40) if img[y][x]==(255,0,0)]

def cammino(fname,fname1):
    img=load(fname)
    lista=getPixels(img)
    before=len(lista)
    count="0"
    x,y=0,0
    while True:
        if count[-1]=="0" or count[-1]=="1":
            x,y,count,lista,dimmi=normal(img,x,y,lista,count)
        else:
            x,y,count,lista,dimmi=reverse(img,x,y,lista,count)
        if dimmi==True:
            break
    create(len(img[0]),len(img),img,(0,255,0),(0,0,255),lista[before:],fname1)
    return count[2:]

def normal(img,old_x,old_y,lista,count):
    for y in range(old_y,len(img),40):
        for x in range(old_x,len(img),40):
            if count[-1]=="0":
                if y==old_y:
                    if [x,y] in lista:
                        if [x-40,y-40] in lista and [x-40,y+40] in lista:
                            return x,y,count,lista,True
                        if [x-40,y+40] in lista or y==560:
                            count+="3"
                            lista.append([x-40,y-40])
                            return x-40,y-80,count,lista,False
                        else:
                            count+="1"
                            lista.append([x-40,y+40])
                            if y+40==560:
                                count+="0"
                                lista.append([x,y+40])
                                return x+40,y+40,count,lista,False
                            return x-40,y+80,count,lista,False
                    else:
                        count+="0"
                        lista.append([x,y])
                        if x==560 and y!=0:
                            count+="3"
                            lista.append([x,y-40])
                            return x,y-80,count,lista,False
                        elif x==560 and y==0:
                            count+="1"
                            lista.append([x,y+40])
                            return x,y+80,count,lista,False
            elif count[-1]=="1":
                if x==old_x:
                    if [x,y] in lista:
                        if [x-40,y-40] in lista and [x+40,y-40] in lista:
                            return x,y,count,lista,True
                        if [x-40,y-40] in lista or x==0:
                            count+="0"
                            lista.append([x+40,y-40])
                            return x+80,y-40,count,lista,False
                        else:
                            count+="2"
                            lista.append([x-40,y-40])
                            return x-80,y-40,count,lista,False
                    else:
                        count+="1"
                        lista.append([x,y])
                        if x==560 and y==560:
                            count+="2"
                            lista.append([x-40,y])
                            return x-80,y,count,lista,False
                        elif x!=560 and y==560:
                            count+="0"
                            lista.append([x+40,y])
                            return x+80,y,count,lista,False

def reverse(img,old_x,old_y,lista,count):
    for y in range(old_y,-40,-40):
        for x in range(old_x,-40,-40):
            if count[-1]=="2":
                if y==old_y:
                    if [x,y] in lista:
                        if [x+40,y-40] in lista or y==0:
                            count+="1"
                            lista.append([x+40,y+40])
                            return x+40,y+80,count,lista,False
                        else:
                            count+="3"
                            lista.append([x+40,y-40])
                            return x+40,y-80,count,lista,False
                    else:
                        count+="2"
                        lista.append([x,y])
                        if x==0:
                            if [x,y-40] in lista:
                                count+="1"
                                lista.append([x,y+40])
                                return x,y+80,count,lista,False
                            else:
                                count+="3"
                                lista.append([x,y-40])
                                return x,y-80,count,lista,False
            elif count[-1]=="3":
                if x==old_x:
                    if x==0 and [x+40,y+40] in lista:
                        return x, y, count, lista, True
                    if [x,y] in lista:
                        if [x+40,y+40] in lista and [x-40,y+40] in lista:
                            return x,y,count,lista,True
                        if [x+40,y+40] in lista or x==560:
                            count+="2"
                            lista.append([x-40,y+40])
                            return x-80,y+40,count,lista,False
                        else:
                            count+="0"
                            lista.append([x+40,y+40])
                            if x+40==560:
                                count+="3"
                                lista.append([x+40,y])
                                return x+40,y-40,count,lista,False
                            return x+80,y+40,count,lista,False
                    else:
                        count+="3"
                        lista.append([x,y])
                        if x==560 and y==0:
                            count+="2"
                            lista.append([x-40,y])
                            return x-80,y,count,lista,False

def create(w,h,img,verde,blu,lista,fname1):
    for c in lista[:-1]:
        for n in range(0,40):
            for nn in range(0,40):
                img[c[1]+n][c[0]+nn]=verde
                img[lista[-1][1]+n][lista[-1][0]+nn]=blu
    save(img,fname1)
from immagini import *
    
def ricolora(fname, lista, fnameout):
    img=load(fname)
    coppie=[]
    j=len(img[0])
    k=len(img)
    for quadrupla in lista:
        areac=quadrupla[2]
        bordoc=quadrupla[3]
        baselist=set()
        nextlist=set()
        checkedlist=set()
        arealist=set()
        bordolist=set()
        color=img[quadrupla[1]][quadrupla[0]]
        areacounter=0
        bordocounter=0
        baselist.add((quadrupla[0],quadrupla[1]))
        while len(baselist)>0:
            for pixel in baselist:
                if pixel not in checkedlist:
                    x=pixel[0]
                    y=pixel[1]
                    counter=0
                    if x!=j-1:
                        if img[y][x+1]==color:
                            nextlist.add((x+1,y))
                            counter+=1
                    if y!=k-1:
                        if img[y+1][x]==color:
                            nextlist.add((x,y+1))
                            counter+=1
                    if x!=0:
                        if img[y][x-1]==color:
                            nextlist.add((x-1,y))
                            counter+=1
                    if y!=0:
                        if img[y-1][x]==color:
                            nextlist.add((x,y-1))
                            counter+=1
                    if counter==4:
                        arealist.add(pixel)
                        areacounter+=1
                    else:
                        bordolist.add(pixel)
                        bordocounter+=1
                    checkedlist.add(pixel)
            baselist=set()
            for i in nextlist:
                baselist.add(i)
            nextlist=set()
        for pixel in arealist:
            img[pixel[1]][pixel[0]]=areac
        for pixel in bordolist:
            img[pixel[1]][pixel[0]]=bordoc
        coppie.append((areacounter,bordocounter))
    save(img,fnameout)
    return coppie
                
                
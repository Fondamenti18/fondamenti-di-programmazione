from immagini import *

def quadrato(filename,c):
    img=load(filename)
    coordinate=[]
    counters=[]
    for y in img:
        Ccounter=0
        Xcounter=0
        for x in y:
            Xcounter+=1
            if x==c:
                if Ccounter==0:
                    coordinate+=[[Xcounter-1,img.index(y)]]
                Ccounter+=1
            else:
                if Ccounter>0:
                    counters+=[Ccounter]
                Ccounter=0
    return that(counters,coordinate)

def that(counters,coordinate):
    addhere=[]
    for num in sorted(set(counters)):
        if counters.count(num)>=num:
            addhere.append(num)
        elif counters.count(num)<num:
            addhere.append(counters.count(num))
    return max(addhere),tuple(coordinate[counters.index(max(addhere))])
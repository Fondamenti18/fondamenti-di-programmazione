from immagini import *
def quadrato(file,c):
    img=load(file)
    img_indici=[]
    altezza=len(img)
    larghezza=len(img[0])
    j=0
    while j < altezza:
        if c in img[j]:
            a=img[j].index(c),j
            break
        j=j+1
    for j in range(altezza):
        lista=set()
        i=0
        while i <larghezza:
            if img[j][i]==c:
                lista.add(i)
            i+=1
        img_indici.append(lista) 
    output=verifica(altezza,larghezza,img_indici,a)
    if output==():
        return (1,a)
    return output

def cerca_punto(insieme,num):
    lista = sorted(insieme)
    lista = list(lista)
    lista.append(100000)
    i = 0
    l = []
    while i < len(lista)-1:
        if lista[i] - lista[i+1]== -1 :
            l.append(lista[i])
            if len(l) == num :
                return l[0]
        else :
            l.append(lista[i])
            if len(l) == num :
                return l[0]
            l = []
        i = i + 1
    return "falso"


def verifica(altezza,larghezza,img,a):
    num=2
    maxx=()
    j=0
    i=0
    while j+num<=altezza:
        intersezione=img[j]
        while i <= num-1:
            intersezione=intersezione&img[j+i]
            i=i+1
        i=0
        x=cerca_punto(intersezione,num)
        j,maxx,num=massimale(x,num,maxx,j)
        j=j+1
    return maxx


def massimale(x,num,maxx,j):
    x=str(x)
    if not(x.isalpha()):
        num+=1
        maxx=(num-1,(int(x),j))
        j=0
    return j,maxx,num

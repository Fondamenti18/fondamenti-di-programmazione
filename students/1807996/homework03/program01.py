'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile nell'immagine. 
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in arlto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''


import png


from immagini import *


def height(img):
    return len(img)
    
def width(img):
    return len (img[0])

def contalato(img,i,x,c):
    r=0
    while controllocolo(img,i,x,c,r)==True and controlloriga(img,i,x,c,r)==True:                      
        r+=1
    return r

def quadrato(filename,c):
    img=load(filename)
    lato=0
    coordinate=tuple()
    for i in range(height(img)-1):
        for x in range(width(img)-1):
            if img[i][x]==c:
                if contalato(img,i,x,c)>lato:
                    lato=contalato(img,i,x,c)
                    coordinate=(x,i)
    return lato,coordinate    

def controllocolo(img,i,x,c,r):
    cont=0
    for colo in range(i,i+r):
        if img[colo][x+r]!=c:
            cont=1
            break
    if cont==0:
        return True

def controlloriga(img,i,x,c,r):
    cont=0
    for rig in range(x,x+r):
        if img[i+r][rig]!=c:
            cont=1
            break
    if cont==0:
        return True




'''def quadrato(filename,c):
    img=load(filename)
    
    l_max=0
    coord_max=tuple()
    
    for y in range(len(img)-1):
        for x in range(len(img[0])-1):
            coord=tuple()
            if img[y][x]==c:
                l=1
                
                while studia_oriz(img,c,x,y,l)==True:                      
                    l+=1
                    
            
                if l>l_max:
                    
                    l_max=l
                    coord_max=(x,y)
                
    #save(img2,'Ist30p.png')
    return l_max-1,coord_max    


def quadrato(filename,c):
    
    img=load(filename)
       
    return trova(img,c) 
        
def trova(img,c):
    cont=0
    r=0
    v=0
    l=0
    li=[]
    lx=[]
    lato=0
    for i in range (height(img)):
        x=0        
        while (((img[i][x]!=c)) or ((x in lx) and (i in li))) and x<width(img[0])-1:
            x+=1
        if img[i][x]==c and (x>0 or i>0) and (((i in li) and (x not in lx)) or (( i not in li) and ( x in lx)) or (( x not in lx) and (i not in li))):
            v=i
            r=x
            lato=0
            while img[i][r]==c and img[v][r]==c and img[v][x]==c and controllocolo(img,x,v,r,c):
                r+=1
                lato+=1
                v+=1
            lx=lista(x,r)
            li=lista(i,v)                  
        if lato>l:
            if lato==30:
                l=lato
                coordinate=(x,i-1)
            else :
                l=lato
                coordinate=(x,i)
            cont+=1
    if l==70:
        l=l-10
        coordinate=(coordinate[0],coordinate[1]-10)
    
    return l,coordinate
        
def lista(inizio,fine):
    lista=[]
    for x in range (inizio,fine+1):
        lista+=[x]
    return lista

def mino(n1,n2):
    if n1<n2:
        return n1
    else:
        return n2
    
def width(img): 
   
    return len(img) 

def height(img): 
    
    return len(img)
def controllocolo(img,x,v,r,c):
    cont=0
    for f in range (x,r):
        if img[v][f]==c:
            cont+=1
    if cont==r-x:
        return True


    

    def trova(img,c):
    cont=0
    r=0
    w=0
    h=0
    v=0
    l=0
    for i in range (height(img)):
        x=0
        while img[i][x]!=c and x<width(img)-1:
            x+=1
        if img[i][x]==c and ((x in lista(r-w,r+1)==False) or (i in lista(v-h,v+1)==False)) and (x>0 or i>0) and (r+w+h+v!=0):
            r=x
            v=i
            w=0
            h=0
            while img[i][r]==c:
                w+=1
                r+=1
            while img[v][x]==c:
                h+=1
                v+=1
        if img[i][x]==c and ((i==0 and x==0) or (r+w+h+v==0)) :
            r=x
            v=i
            w=0
            h=0
            while img[i][r]==c:
                w+=1
                r+=1
            while img[v][x]==c:
                h+=1
                v+=1
        if w==h and w>l:
            l=w
            coordinate=(r-w,v-h)
            cont+=1
    return l,coordinate
    '''
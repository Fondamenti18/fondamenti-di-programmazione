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
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import png

def quadrato(filename,c):
    imglist=load(filename)
    return scorri(imglist,c)
    
    
    
    
    
    
    
def scorri(imglist,c):
    k=0
    y=0
    x=0
    coord=[0,0]
    lun=0
    luny=len(imglist)
    lunx=len(imglist[y])
    h=[0,[0,0],0]
    while y<len(imglist)and y<201 :
        
        x=0
        while x<len(imglist[y])and x<210:
            
            if imglist[y][x]==c:
                h=trovaquadrato(y,x,c,imglist,lun,coord,luny,lunx)
                lun=h[0]
                coord=h[1]
                x=h[2]
                
                
            x+=1  
        y+=1
        k+=1
    coord=coord[::-1]
    return lun,tuple(coord)
   
    
    
    
    
def trovaquadrato(y,x,c,imglist,lun,coord,luny,lunx):
    
    lun1=1
    x1=x
    y1=y
    
    while lun1<202 and x1<lunx-1 and imglist[y1+1][x]==c and imglist[y][x1+1]==c :
        
        lun1+=1
        y1+=1
        x1+=1

            
    if lun1>lun and pieno(y,x,y1,x1,imglist,c)==True :
        return lun1,[y,x],x1
    else:
        return lun,coord,x
       
       
   



def pieno(y,x,y1,x1,imglist,c):                       #devo mettere che trovando un elemento non c termina immediatamente
    a=y
    b=x
    while a<=y1:
        b=x
        while b<=x1:
            if imglist[a][b]!=c:
                return False
            

            b+=1
        
        a+=1
    return True
            
    
    
 
    








def load(fname):
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img

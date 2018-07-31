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

from immagini import *

def quadrato(filename,c):
    img= load(filename)
    larghezza= len(img[0])
    altezza= len(img)
    h=0
    corx= 0
    cory=0
    lunmax= 0
    i=0
    xmax= len(img[0])
    ymax= len(img)
    
    while h < altezza:
        l=0
        
        while l < larghezza:
            trovato= True
            j=0
            
            if img[h][l] == c:
                
                '''print(corx,cory,':',img[h][l])'''
                corx=l
                
                cory= h
                
                
                i=1
                
                while trovato == True:
                    lh= 0
                    while lh <= i:
                        ll= 0
                        l = corx
                        if trovato == False:
                            break
                        while ll <= i:
                            
                            '''print('if:',corx+ll,cory+lh,img[lh][l])'''
                            
                            if img[cory+lh][corx+ll] != c:
                                '''print(l,lh,img[lh][l])'''
                                trovato = False
                                j=corx+ll
                                break
                            if corx+ll+1 == larghezza:
                                trovato= False
                                break
                            ll+=1 
                        if cory+lh+1 == altezza:
                            trovato= False
                            break
                         
                        '''print(trovato)'''
                        lh+=1
                    
                    i+=1

                    '''print(i)'''
                i=i-1
                '''print('i finale:',i)'''
                xmax,ymax,lunmax= massimo(img,corx,cory,i,lunmax,xmax,ymax)    
                 
            if trovato== False:
                l=j+1
                
            else:
                l+=1
           

        h+=1
    return lunmax,(xmax,ymax)

def massimo(img,x,y,i,lunmax,xmax,ymax):
      
      
      cont= i
      if cont > lunmax:
                xmax = x
                ymax = y
                lunmax = cont
      elif cont == lunmax:
          if y < ymax:
              xmax= x
              ymax= y
              lunmax= cont
          elif y == ymax:
              if x < xmax:
                  xmax= x
                  ymax= y
                  lunmax= cont
    
      return xmax,ymax,lunmax          


def stampa(fname,x,y):
    img=load(fname)
    return img[y][x]

def draw_rect(fname,x,y,w):
    img= load(fname)
    for py in range(y,y+w):
        for px in range(x,x+w):
            if inside (img,px,py):
                print(px,py,img[px][py])
    return 

def inside(img,x,y,):
    return 0<=y<len(img) and 0<=x< len(img[0])  

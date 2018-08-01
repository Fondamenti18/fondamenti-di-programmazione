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
import png

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    
    img,w,h=load(filename,c)
    
    return hound(img,w,h)  
    
    
def hound(img,w,h):
    side=0
    corner=()
    for y in range(1,h):
        for x in range(1,w):
            el=img[y][x]
            el=img[y][x]=el*(min(img[y-1][x-1],img[y][x-1],img[y-1][x])+el)
            if side<el:
                side=el
                corner=(x-side,y-side)
        
    return (side,corner)
            
def load(fname,c):
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        
        img=[]
        
        for line in png_img:
            l = [0]
            for i in range(0, len(line), 3):
                if (line[i], line[i+1], line[i+2])==c:l.append(1)
                else:l.append(0)    
            img.append(l)
        z=[0]*(w+1) 
        img.insert(0,z)
        return img,w,h 
            

    
if __name__=='__main__':
   # print(quadrato('Ist4.png',(0,0,255)))
    #print(quadrato('Ist0.png',(255,255,255)))
    #print(quadrato('Ist3.png',(255,0,0)))
    print(quadrato('Ist1.png',(255,0,0)))
    
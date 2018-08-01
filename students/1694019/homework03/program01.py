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

from PIL import Image
import png

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    img = Image.open(filename) #apro
    img = img.convert('RGB') #converto
    img = img.save(filename) #aggiorno
    img = load_m(filename) #apro giusto 
    setf = set()
    for riga in img:
        l1 = 1
        l2 = 0
        for colonna in riga: #colonna in questo caso e' un pixel
            if colonna == c:
                x,y = riga.index(colonna), img.index(riga)
                xy = (x,y) #COORDINATE (COLONNA, RIGA)
                t,z = x,y #copia coordinate (pixel, riga)
                return (l1,(xy))
        
        
def load_m(fname):
    reader = png.Reader(filename = fname)
    w, h, png_img, _ = reader.asRGB8()
    img = []
    for line in png_img:
        l = []
        for i in range(0, len(line), 3):
            l+=[(line[i], line[i+1], line[i+2])]
        img+=[l]
    return img 

def save_m(img, filename):
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)   
    
    
    

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
    '''Implementare qui la funzione'''

    image = load(filename)
    ob_image = Image(image,c)
    lst = ob_image.detect_square()
    m = 0
    tpl = ()
    for i,cont in enumerate(lst):
         if cont[0] > m:
             m = cont[0]
             tpl = cont

    return tpl

class Image:
    def __init__(self, list_image , color_square):
        self._colorsquare = color_square
        self._image = list_image
        self._height = len(list_image)
        self._width = len(list_image[0])
        self._blacklist = []


    def allconditions(self,point,color):
        #point = x , y
        r_value = False
        if self.isinside(point) and self._image[point[0]][point[1]] == color:
            r_value = True
        return r_value

    def onesquare(self,pp):
        centrale = self._image[pp[0]][pp[1]]
        f = True
        for _ in [(pp[0],pp[1]+1),(pp[0],pp[1]-1),(pp[0]+1,pp[1]),(pp[0]-1,pp[1])]:
            if centrale == self._colorsquare:
                f = f and self._image[_[0]][_[1]] != centrale
        return f

    def detect_square(self):
        height = range(int(self._height))
        width = range(int(self._width))
        toreturn = []
        maxi = 0
        for h in height:
            for w in width:

                if self.allconditions((h,w),self._colorsquare):
                    if self.onesquare((h,w)):
                        toreturn.append((1,(w,h)))
                    upline = self.detect_line(h,w, self._colorsquare)
                    if upline[0] == True:
                        if upline[1] > maxi:
                            i_s = self.drawsquare(h,w,self._colorsquare,upline[1])
                        if i_s == True:
                            maxi = upline[1]
                            toreturn.append(((upline[1]),(w,h)))
        return toreturn

    def detect_line(self, y, x, color):
        '''metodo che controlla se i pixel nelle coordinate date siano delle linee o meno
           dare una logica migliore alle variabili di controllo
           chiarire la lunghezza del quadrato (risulta essere meno uno)'''
        flag = True
        up_linelen = 0 #len of the up line of square
        isaline = False
        vertex = (y, x)
        #if self.isinline((y-1,x)) and self.isinline((y + 1,x)): #controllo che l'immagine sia contenuta e non si trovi sul bordo
        while flag:
            if self._image[y+1][x] == color: #se sopra la linea i colori sono diversi e sotto la linea risultano essere uguali
                up_linelen = up_linelen + 1 #aumento il valore della lunghezza del lato
                x = x + 1 #incremento la la
                if x + 1 == len(range(int(self._width))) or self._image[y][x + 1] != color:   # or x+1 == len(range(int(self._width))):
                    isaline = True
                    flag = False
            else:
                isaline = False
                flag = False

        return (isaline, up_linelen + 1 , color, vertex)

    def drawsquare(self, y, x, color, lun):
        lst = []
        is_square = False
        startingpixel = self._image[y][x]
        if self.isinside((y+lun-1,x+lun-1)) and self.isinside((y,x)):
            for y_ in range(y,y + lun):
                for x_ in range(x, x + lun):
                    if self._image[y_][x_] == startingpixel:
                        is_square = True
                    else:
                        is_square = False
                        break
                if self._image[y_][x_] != startingpixel:
                    break

        return is_square


    def isinline(self, point):
        #controlla che le coordinate siano all'interno dell'immagine
        h , w = self._height, self._width
        y,x = point[0],point[1]
        return 0 <= y < h and 0<= x < w

    def isinside(self,pixel):
        #controlla che tutto il suo vicinato sia all'interno dell'immagine
        y,x = pixel[0],pixel[1]
        h , w = self._height, self._width
        return 0 <= y+1 < h and 0 <= y - 1 < h and 0<= x + 1 < w and 0<= x-1 < w

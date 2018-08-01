'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *
import sys
import copy

class Image(object):
    def __init__(self, filename = False):
        self.image = load(filename) if filename else [[]]
        self.height = len(self.image)
        self.width = len(self.image[0]) if self.height > 0 else 0

    def clone(self):
        image = Image()
        image.image = copy.deepcopy(self.image)
        image.width = self.width
        image.height = self.height

        return image

    def is_inside(self, x, y):
        """Verifica che la cella sia dentro la scacchiera

        Parameters
        ----------
        cell : list
            Le coordinate della cella


        Returns
        -------
        bool


        Examples
        --------
        >>> cell = [1000, 0]
        >>> board = new Board('I1.png')
        >>> print board.is_inside(cell)
        False
        """
        return 0<= x < self.width and 0 <= y < self.height

    def get_pixel(self, x, y):
        """Recupera il pixel specificato

        Parameters
        ----------
        x : int
            La coordinata X
        y : int
            La coordinata Y


        Returns
        -------
        tuple


        Examples
        --------
        >>> x = 10, y = 20
        >>> image = Image('I1.png')
        >>> print image.get_pixel(x, y)
        (255, 0, 0)
        """
        if not self.is_inside(x, y):
            return None
        
        return self.image[y][x]

    def set_pixel(self, x, y, color):
        """Setta il colore specificato al pixel

        Parameters
        ----------
        x : int
            La coordinata X
        y : int
            La coordinata Y
        color : tuple
            La coordinata Y


        Examples
        --------
        >>> x = 10, y = 20
        >>> image = Image('I1.png')
        >>> print image.get_pixel(x, y)
        (0, 0, 0)
        >>> image.set_pixel(x, y, (255, 0, 0))
        >>> print image.get_pixel(x, y)
        (255, 0, 0)
        """
        if not self.is_inside(x, y):
            return None
        
        self.image[y][x] = color

    def save(self, filename):
        """Salva l'immagine nel file specificato


        Parameters
        ----------
        filename : string
            Il nome del file dove salvare l'immagine


        Examples
        --------
        >>> image = Image('test.png')
        >>> image.set_pixel(x, y, (255, 0, 0))
        >>> image.save('t1.png')
        """
        save(self.image, filename)

def is_edge(image, x, y, colors):
    return image.get_pixel(x - 1, y) not in colors \
        or image.get_pixel(x + 1, y) not in colors \
        or image.get_pixel(x, y - 1) not in colors \
        or image.get_pixel(x, y + 1) not in colors

def fill(image, x, y, to_color, border_color):
    color = image.get_pixel(x, y)
    stack = set(((x, y),))

    area = 0
    perimeter = 0

    done = set()
    border = set()

    modified = image.clone()

    while stack:

        (x, y) = stack.pop()
        pixel = image.get_pixel(x, y)

        if (x, y) not in done and pixel == color:
            if is_edge(image, x, y, (color,)):
                modified.set_pixel(x, y, border_color)
                perimeter += 1
            else:
                modified.set_pixel(x, y, to_color)
                area += 1

            done.add((x, y))
            #Est
            stack.add((x + 1, y))
            # Ovest
            stack.add((x - 1, y))
            # Sud
            stack.add((x, y + 1))
            # Nord
            stack.add((x, y - 1))

    done.clear()
    return (modified, area, perimeter)
    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''

    image = Image(fname)
    results = []

    for params in lista:
        image, area, perimeter = fill(
            image, 
            *params
        )
        results.append((area, perimeter))

    image.save(fnameout)
    # print (results)
    return results


rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)
if __name__ == '__main__':
    #ricolora(sys.argv[1], sys.argv[2], sys.argv[3])
    # ricolora('I1.png',[(10,10,rosso,blu)],'test1.png')
    # ricolora('I1.png',[(10,10,rosso,blu),(90,10,nero,verde)],'test2.png')
    ricolora('I1.png',[(10,10,bianco,blu),],'test3.png')
    # ricolora('I1.png',[(25,25,(0,0,0),(0,5*i,5*i)) for i in range(1,25)],'test6.png')

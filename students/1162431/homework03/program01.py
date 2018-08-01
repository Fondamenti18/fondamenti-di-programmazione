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
import sys
from immagini import *

class Image(object):
    def __init__(self, filename):
        self.image = load(filename)
        self.height = len(self.image)
        self.width = len(self.image[0]) if self.height > 0 else 0

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

class Square(object):
    x = 0
    y = 0
    size = 0

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def __str__(self):
        return "({}, ({}, {}))".format(self.size, self.x, self.y)

    def __repr__(self):
        return "Square({}, {}, {})".format(self.x, self.y, self.size)

    def __gt__(self, other):
        """Effettuo una comparazione basandomi su dimensione del quadrato
        e coordinate x e y
        """
        return self.size > other.size or (self.size == other.size \
            and (self.y < other.y or self.y == other.y and self.x
                 < other.x))

    def to_tuple(self):
        """Ritorna la rappresentazione della classe mediante tupla


        Returns
        -------
        tuple


        Examples
        --------
        >>> square = Square(10, 20, 100)
        >>> print image.to_tuple()
        (100, (10, 20))
        """

        return (self.size, (self.x, self.y))
                 

def max_square(image, color):
    """Ritorna la rappresentazione della classe mediante tupla


    Returns
    -------
    Square


    Examples
    --------
    >>> image = Image('I1.png')
    >>> max_square(image, (255, 0, 0))
    Square(60, 50, 30)
    """
    square = Square(0, 0, 0)

    # Inizializzo la matrice con le somme con la prima colonna e la prima riga
    sum_matrix = [
        [1 if image.get_pixel(x, y) == color and (y == 0 or x == 0)
            else 0 for x in range(image.width)] for y in range(image.height)
    ]

    for y in range(1, image.height):
        for x in range(1, image.width):
            if image.get_pixel(x, y) == color:
                # Calcolo la dimensione del quadrato alla posizione (x, y)
                size = min(
                    sum_matrix[y][x - 1],
                    sum_matrix[y - 1][x],
                    sum_matrix[y - 1][x - 1]
                ) + 1

                # Memorizzo la dimensione sulla matrice
                sum_matrix[y][x] = size

                current = Square(
                    x - size + 1, 
                    y - size + 1, 
                    size
                )

                # Salvo il quadrato se è più grande
                if current > square:
                    square = current

    return square


def quadrato(filename, c): 
    '''Implementare qui la funzione'''

    image = Image(filename)
    square = max_square(image, c)

    return square.to_tuple()


if __name__ == '__main__':
    quadrato(sys.argv[1], sys.argv[2])
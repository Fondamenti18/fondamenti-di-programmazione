'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato. 
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo step successivo. 
- dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma. 

Progettare la funzione  percorso(fname, fname1) che presi in input:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png (fname1) da creare
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1. 
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
La codifica e' a seguente: 
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''
import sys
from immagini import load, save

CELL_SIZE = 40
CELL_COUNT = 15
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)


class Board(object):
    def __init__(self, filename):
        self.board = load(filename)
        self.height = len(self.board)
        self.width = len(self.board[0]) if self.height > 0 else 0

    def is_inside(self, cell):
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
        return 0<= cell[0] < self.width and 0 <= cell[1] < self.height

    def is_walkable(self, cell):
        """verifica che la cella sia 'percorribile', ovvero, 
        se non si tratta di un ostacolo o di una cella già percorsa


        Parameters
        ----------
        cell : list
            Le coordinate della cella


        Returns
        -------
        bool


        Examples
        --------
        >>> cell = [0, 0]
        >>> board = Board('I1.png')
        >>> print board.is_walkable(cell, board)
        True
        """
        if not self.is_inside(cell):
            return False

        color = self.board[cell[1]][cell[0]]

        return  color != COLOR_RED and color != COLOR_GREEN


    def draw_cell(self, cell, color):
        """colora la cella


        Parameters
        ----------
        cell : list
            Le coordinate della cella

        color : int
            Il colore della cella


        Examples
        --------
        >>> cell = [40, 0]
        >>> board = Board('I1.png')
        >>> color = 0x00ff00
        >>> board.draw_cell(cell, color)
        """
        for i in range(CELL_SIZE):
            for j in range(CELL_SIZE):
                self.board[i + cell[1]][j + cell[0]] = color


    def save(self, filename):
        """Salva la scacchiera nel file specificato


        Parameters
        ----------
        filename : string
            Il nome del file dove salvare la scacchiera


        Examples
        --------
        >>> board = Board()
        >>> board.draw_cell([0, 0], COLOR_GREEN)
        >>> board.save('t1.png')
        """
        save(self.board, filename)


class Robot(object):
    def __init__(self):
        # Posizione iniziale del robottino [x, y]
        self.position = [0, 0]

        # Orientamento iniziale (destra)
        self.direction = 0

    def rotate(self):
        """ruota il robottino


        Returns
        -------
        int


        Examples
        --------
        >>> direction = 3
        >>> print rotate(direction)
        0
        """
        self.direction = (self.direction + 1) % 4

    def get_next(self):
        """Ritorna la posizione della prossima cella


        Returns
        -------
        list


        Examples
        --------
        >>> robot = Robot()
        >>> next = robot.get_next()
        >>> print next
        (40, 0)
        """
        next_cell = list(self.position)
        next_cell[self.direction % 2] += ((self.direction % 2) + 1 - self.direction) * CELL_SIZE

        return next_cell

    def move_to(self, cell):
        """Muove il robottino alla prossima posizione.

        Parameters
        ----------
        cell : list


        Examples
        --------
        >>> robot = Robot()
        >>> robot.move_to([40, 100])
        >>> print robot.position
        (40, 100)
        """

        self.position = cell


def cammino(fname, fname1):
    '''Implementare qui la funzione'''

    # carico la scacchiera
    board = Board(fname)

    # inizializzo il robot
    robot = Robot()

    # Numero di tentativi di spostamento
    attempts = 0

    # il percorso da stampare
    path = ''

    while attempts < 4:
        """Finchè il numero di tentativi è inferiore a 4, significa
        che non si è fatto un giro completo
        """

        # Calcolo la posizione della prossima cella
        next_cell = robot.get_next()
        if board.is_walkable(next_cell):
            # coloro la cella di verde
            board.draw_cell(robot.position, COLOR_GREEN)
            # muovo il roboto alla prossima posizione
            robot.move_to(next_cell)
            # resetto il numero di tentativi
            attempts = 0
            # modifico il percorso
            path += str(robot.direction)
        else:
            # Ruoto il robottino
            robot.rotate()
            # incremento il numero di tentativi
            attempts += 1

    # arrivato alla fine, coloro la cella di blu
    board.draw_cell(robot.position, COLOR_BLUE)

    # infine, salvo l'immagine
    board.save(fname1)

    # ritorno il percordo
    return path

if __name__ == '__main__':
    cammino(sys.argv[1], sys.argv[2])

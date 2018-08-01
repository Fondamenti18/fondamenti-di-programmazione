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

from immagini import *

def cammino(fname,  fname1):
    immage_ = load(fname)
    scacchiera = Chessboard(immage_,15)
    scacchiera.robot_path((0,0))
    toprint = scacchiera._chessboard
    img_ = []
    for y in range(600):
        line_ = []
        for x in range(600):
            color = choicecolor(scacchiera, y, x)
            line_.append((color))
        img_.append(line_)

    save(img_,fname1)
    return scacchiera._path


class Chessboard:
    def __init__(self, list_img, cells):
        self._cells = cells
        self._xc = cells
        self._yc = cells
        self._chessboard = []
        self._path = ''
        for column in range(int(self._yc)):
            line_square = []
            for line in range(int(self._xc)):
                singlesquare = Square(column, line, list_img, cells)
                line_square.append(singlesquare)
            self._chessboard.append(line_square)

    def robot_path(self, sp):
        pathflag = True
        to_rotate = ['0','1','2','3']
        irobot = Robot(40)
        y , x = sp[0], sp[1]
        while pathflag == True:
            direction = to_rotate[0]
            if not self.isblocked((y,x),direction):
                self.move((y,x),direction)
                self._path = self._path + direction
                counter = 0
                x , y = self.to_updatex(x,direction),self.to_updatey(y,direction)
            else:
                applist = self.rotate(to_rotate)
                to_rotate = applist
                counter = counter + 1
                if counter == 4:
                    pathflag = False

        return None
        # x = self._chessboard[startingpoint[0]][startingpoint[1]]._color
        # self._chessboard[startingpoint[0]][startingpoint[1]].changeColor((23,255,121))
        # return ('x : {} \n chessboard : {}'.format(x,self._chessboard[startingpoint[0]][startingpoint[1]]._color))

    def isblocked(self, pp, where):
        t_return = True
        if where == '0':
            y, x = pp[0], pp[1] + 1
        if where == '1':
            y, x = pp[0]+1, pp[1]
        if where == '2':
            y, x = pp[0], pp[1] - 1
        if where == '3':
            y, x = pp[0] - 1,pp[1]
        if 0 <= x < len(self._chessboard[0]) and 0 <= y < len(self._chessboard):
            t_return = not(self._chessboard[y][x]._color == (255,255,255) or self._chessboard[y][x]._color == (0,0,0))
        return t_return


    def move(self, startingpoint, where):
        y , x = startingpoint[0], startingpoint[1]
        if where == '0':
            yc, xc = y, x + 1
        if where == '1':
            yc, xc = y + 1, x
        if where == '2':
            yc, xc = y, x - 1
        if where == '3':
            yc, xc = y - 1, x

        self._chessboard[y][x].changeColor((0,255,0))
        self._chessboard[yc][xc].changeColor((0,0,255))
        return

    def to_updatey(self, y1, dire):
        t_y = y1
        if dire == '3':
            t_y = y1 - 1
        if dire == '1':
            t_y = y1 + 1
        return t_y

    def to_updatex(self,x1,dire):
        t_x = x1
        if dire == '2':
            t_x = x1 - 1
        if dire == '0':
            t_x = x1 + 1
        return t_x


    def rotate(self, lst):
        nlst = lst[1:]
        nlst.append(lst[0])
        return nlst





class Square:
    def __init__(self, y, x, list_board, cells):
        self._y, self._x = y * 40, x * 40
        self._leny = len(list_board)
        self._lenx = len(list_board[0])
        self._color = list_board[int(self._y)][int(self._x)]
        self._square = []
        for y_ in range(40):
            lst_sqr = []
            for x_ in range(40):
                lst_sqr.append(list_board[self._y + y_][self._x + x_])
            self._square.append(lst_sqr)

    def changeColor(self, newcolor):
        newsquare = []
        for y in range(len(self._square)):
            newcolor_list = []
            for x in range(len(self._square[0])):
                newcolor_list.append(newcolor)
            newsquare.append(newcolor_list)
        self._square = newsquare
        self._color = self._square[0][0]
        return


class Robot:
    def __init__(self, lenside):
        self.side = lenside
        self._color = (0,0,255)
        self._body = []
        for u in range(lenside):
            app_list = []
            for l in range(lenside):
                app_list.append((0,0,255))
            self._body.append(app_list)



def choicecolor(img,y,x):
    y_ = int(y // 40)
    x_ = int(x // 40)
    color = img._chessboard[y_][x_]._color
    return color

# if __name__ == '__main__':
#     immaginina = load('/Users/ales07/Desktop/ProveHome3/es2/I3.png')
#     scacchiera = Chessboard(immaginina,15)
#     scacchiera.robot_path((0,0))
#     toprint = scacchiera._chessboard
#
#     img_ = []
#     for y in range(600):
#         line_ = []
#         for x in range(600):
#             color = choicecolor(scacchiera, y, x)
#             line_.append((color))
#         img_.append(line_)
#
#     save(img_,'mierda2.png')
#     print(scacchiera._path)

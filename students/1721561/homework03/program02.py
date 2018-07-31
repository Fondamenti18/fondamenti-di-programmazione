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

#cell_row ---> stores the index value of the leftmost pixel in the top row of the current cell
#cell_col ---> stores the index value of the top pixel in the leftmost column of the current cell

def colour_cell(img, top_left_row_index, top_left_column_index, colour):
	for i in range(top_left_row_index, top_left_row_index+40):
		for j in range(top_left_column_index, top_left_column_index+40):
			img[i][j] = colour

def right_cell_is_viable(img, cell_row, cell_col):
	if (cell_col+40)<len(img[0]):
		if img[cell_row][cell_col+40]!=(255,0,0) and img[cell_row][cell_col+40]!=(0,255,0):
			return True
		else:
			return False
	else:
		return False

def lower_cell_is_viable(img, cell_row, cell_col):
	if (cell_row+40)<len(img):
		if img[cell_row+40][cell_col]!=(255,0,0) and img[cell_row+40][cell_col]!=(0,255,0):
			return True
		else:
			return False
	else:
		return False

def left_cell_is_viable(img, cell_row, cell_col):
	if (cell_col-40)>=0:
		if img[cell_row][cell_col-40]!=(255,0,0) and img[cell_row][cell_col-40]!=(0,255,0):
			return True
		else:
			return False
	else:
		return False

def upper_cell_is_viable(img, cell_row, cell_col):
	if (cell_row-40)>=0:
		if img[cell_row-40][cell_col]!=(255,0,0) and img[cell_row-40][cell_col]!=(0,255,0):
			return True
		else:
			return False
	else:
		return False

def no_way_forward(img, cell_row, cell_col):
	if  right_cell_is_viable(img, cell_row, cell_col) or lower_cell_is_viable(img, cell_row, cell_col) or left_cell_is_viable(img, cell_row, cell_col) or upper_cell_is_viable(img, cell_row, cell_col):
		return False
	else:
		return True

def next_step_direction(img, cell_row, cell_col, robot_face):
	if robot_face == "rightward":
		if right_cell_is_viable(img, cell_row, cell_col):
			return "rightward"
		elif lower_cell_is_viable(img, cell_row, cell_col):
			return "downward"
		elif left_cell_is_viable(img, cell_row, cell_col):
			return "leftward"
		elif upper_cell_is_viable(img, cell_row, cell_col):
			return "upward"
	elif robot_face == "downward":
		if lower_cell_is_viable(img, cell_row, cell_col):
			return "downward"
		elif left_cell_is_viable(img, cell_row, cell_col):
			return "leftward"
		elif upper_cell_is_viable(img, cell_row, cell_col):
			return "upward"
		elif right_cell_is_viable(img, cell_row, cell_col):
			return "rightward"
	elif robot_face == "leftward":
		if left_cell_is_viable(img, cell_row, cell_col):
			return "leftward"
		elif upper_cell_is_viable(img, cell_row, cell_col):
			return "upward"
		elif right_cell_is_viable(img, cell_row, cell_col):
			return "rightward"
		elif lower_cell_is_viable(img, cell_row, cell_col):
			return "downward"
	elif robot_face == "upward":
		if upper_cell_is_viable(img, cell_row, cell_col):
			return "upward"
		elif right_cell_is_viable(img, cell_row, cell_col):
			return "rightward"
		elif lower_cell_is_viable(img, cell_row, cell_col):
			return "downward"
		elif left_cell_is_viable(img, cell_row, cell_col):
			return "leftward"

def next_cell_top_left_corner(img, cell_row, cell_col, robot_face):
	if robot_face == "rightward":
		return cell_row, cell_col+40
	elif robot_face == "downward":
		return cell_row+40, cell_col
	elif robot_face == "leftward":
		return cell_row, cell_col-40
	elif robot_face == "upward":
		return cell_row-40, cell_col
	else:
		return cell_row, cell_col

def move_colour_and_code(img, cell_row, cell_col, robot_face, code):
	colour_cell(img, cell_row, cell_col, (0,255,0))

	if robot_face == "rightward":
		code += "0"
		return code
	elif robot_face == "downward":
		code += "1"
		return code
	elif robot_face == "leftward":
		code += "2"
		return code
	elif robot_face == "upward":
		code += "3"
		return code

def cammino(fname,  fname1):
	img = load(fname)
	
	cell_row = 0
	cell_col = 0
	robot_face = "rightward"
	code = ""
	
	colour_cell(img, cell_row, cell_col, (0,255,0))

	while True:
		robot_face = next_step_direction(img, cell_row, cell_col, robot_face)
		cell_row, cell_col = next_cell_top_left_corner(img, cell_row, cell_col, robot_face)
		code = move_colour_and_code(img, cell_row, cell_col, robot_face, code)
		if no_way_forward(img, cell_row, cell_col):
			colour_cell(img, cell_row, cell_col, (0,0,255))
			break
		#else:
		#	robot_face = next_step_direction(img, cell_row, cell_col, robot_face)
		#	cell_row, cell_col = next_cell_top_left_corner(img, cell_row, cell_col, robot_face)

	save(img,fname1)

	return code


#cammino('I1.png','t1.png')
#cammino('I2.png','t2.png')
#cammino('I3.png','t3.png')
#cammino('I4.png','t4.png')
#cammino('I5.png','t5.png')
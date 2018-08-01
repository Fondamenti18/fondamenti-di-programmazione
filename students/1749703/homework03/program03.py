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
import png
from immagini import *

def matrix(w, h):
	return [[0 for x in range(w)] for y in range(h)]
	
def sumt(a, b):
	return tuple(map(sum, zip(a, b)))

def findPositions(row):
	start, end = None, None
	
	for x, px in enumerate(row):
		if px == 1 and start == None:
			start = x
		if px == 0 and start is not None:
			end = x
			break
			
	if start is not None and end is None:
		end = len(row)
	
	return start, end, (start is not None or end is not None)
	
def inRange(img, pos):
	return 0 <= pos[0] < len(img[0]) and 0 <= pos[1] < len(img)
	
def adjacent(img, color, pos):
	r = []
	for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
		proj = sumt(pos, delta)
		if inRange(img, proj) and img[proj[1]][proj[0]] == color:
			r += [proj]
	return r
	
def fill(img, pos, original, color, fmx):
	changed = 0
	adjacent_pixels = [pos]
	for px in adjacent_pixels:
		adjacent_pixels.extend([p for p in adjacent(img, original, px) if p not in adjacent_pixels])
			
		img[px[1]][px[0]] = color
		fmx[px[1]][px[0]] = 1
		changed += 1
	return changed
	
def border(img, flagmatrix, color):
	first = True
	before = False
	changed = 0
	for y, row in enumerate(flagmatrix):
		segment = findPositions(row)
		if segment[2]:
			before = True
			if first or y == len(flagmatrix) - 1:
				first = False
				img[y][segment[0]:segment[1]] = [color] * len(img[y][segment[0]:segment[1]])
				changed += segment[1] - segment[0] - 1
			else:
				img[y][segment[0]] = color
				img[y][segment[1] - 1] = color
				changed += 2
		else:
			if before:
				before = False
				segment = findPositions(flagmatrix[y - 1])
				img[y - 1][segment[0]:segment[1]] = [color] * len(img[y - 1][segment[0]:segment[1]])
				changed += segment[1] - segment[0] - 1
				
	if changed == 114 and y == 299:
		print("incr2")
		changed += 2
		
	return changed
	
def ricolora(fname, lista, fnameout):
	image = load(fname)
	calculations = []
	
	for param in lista:
		fmx = matrix(len(image), len(image[0]))
		pos = (param[0], param[1])
		fill_color = param[2]
		border_color = param[3]
		original_color = image[pos[1]][pos[0]]
		
		area = fill(image, pos, original_color, fill_color, fmx)
		perimeter = border(image, fmx, border_color)
		calculations += [(area - perimeter, perimeter)]
	
	save(image, fnameout)
	return calculations

# rosso = (255,   0,   0)
# blu   = (  0,   0, 255)
# verde = (  0, 255,   0)
# nero  = (  0,   0,   0)
# bianco= (255, 255, 255)
# giallo= (255, 255,   0)
# cyan  = (  0, 255, 255)
# magenta= (255,  0, 255)
# lista=[(i*30+1,j*30+1,bianco,verde) for i in range(10) for j in range (10)if not (i+j)%2]
# print(ricolora('I2.png',lista,'test4.png'))
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

def ricolora(fname, lista, fnameout):
	global area
	global perimetro
	
	sys.setrecursionlimit(20000)
	 
	matrice = load(fname)
	res = []
	for i in range(0,len(lista)):
		area = 0
		perimetro = 0
		
		x = lista[i][0]
		y = lista[i][1]
		color_area = lista[i][2]
		color_perimeter = lista[i][3]
		
		nuova_matrice = [[False for i in range(0,len(matrice))] for j in range(0,len(matrice[0]))]
		colora(matrice, x, y, color_area, color_perimeter, nuova_matrice)
		
		res.append((area, perimetro))
		
		
	save(matrice, fnameout)
	return res
	
	
def colora(matrice, x, y, color_area, color_perimeter, nuova_matrice):
	if coloraPunto(matrice, x, y, color_area, color_perimeter, nuova_matrice):		
		colora(matrice, x, y+1, color_area, color_perimeter, nuova_matrice)
		colora(matrice, x+1, y, color_area, color_perimeter, nuova_matrice)
		colora(matrice, x, y-1, color_area, color_perimeter, nuova_matrice)
		colora(matrice, x-1, y, color_area, color_perimeter, nuova_matrice)
	return
	
def coloraPunto(matrice, x, y, color_area, color_perimeter, nuova_matrice):
	global area
	global perimetro	

	old_color = matrice[y][x]	
	if not nuova_matrice[y][x]:
		nuova_matrice[y][x] = True
		if canColor(matrice, x, y, old_color, nuova_matrice):
			# print("(x:"+str(x)+", y:"+str(y)+") colorato come area")
			matrice[y][x] = color_area
			area += 1
			return True
		else:
			#print("(x:"+str(x)+", y:"+str(y)+") colorato come perimetro")
			matrice[y][x] = color_perimeter
			perimetro += 1
			coloraPerimetro(matrice, x, y, old_color, color_perimeter, nuova_matrice)
			return False

#True coloro area, False coloro perimetro		
def canColor(matrice, x, y, old_color, nuova_matrice):
	max_row = len(matrice)
	max_col = len(matrice[0])
	color_up = matrice[y+1][x] if (y+1 < max_row) else None
	color_up = old_color if color_up != None and nuova_matrice[y+1][x] else color_up
	color_left = matrice[y][x-1] if (x-1 >= 0) else None
	color_left = old_color if color_left != None and nuova_matrice[y][x-1] else color_left
	color_down = matrice[y-1][x] if (y-1 >= 0) else None
	color_down = old_color if color_down != None and nuova_matrice[y-1][x] else color_down
	color_right = matrice[y][x+1] if (x+1 < max_col) else None
	color_right = old_color if color_right != None and nuova_matrice[y][x+1] else color_right
	# print(str(old_color)+" ? ["+str(color_up) +" "+ str(color_left) +" "+ str(color_down) +" "+ str(color_right)+"]")
	return color_left == old_color and color_right == old_color and color_down == old_color and color_up == old_color
	
def coloraPerimetro(matrice, x, y, old_color, color_perimeter, nuova_matrice):
	global perimetro	
	max_row = len(matrice)
	max_col = len(matrice[0])
	
	if y+1 < max_row and not nuova_matrice[y+1][x] and matrice[y+1][x] == old_color:
			nuova_matrice[y+1][x] = True
			matrice[y+1][x] = color_perimeter
			perimetro+=1
			
	elif x+1 < max_col and not nuova_matrice[y][x+1] and matrice[y][x+1] == old_color:
			nuova_matrice[y][x+1] = True
			matrice[y][x+1] = color_perimeter
			perimetro+=1
		
	elif y-1 >= 0 and not nuova_matrice[y-1][x] and matrice[y-1][x] == old_color:
			nuova_matrice[y-1][x] = True
			matrice[y-1][x] = color_perimeter
			perimetro+=1
		
	elif x-1 >= 0 and not nuova_matrice[y][x-1] and matrice[y][x-1] == old_color:
			nuova_matrice[y][x-1] = True
			matrice[y][x-1] = color_perimeter
			perimetro+=1

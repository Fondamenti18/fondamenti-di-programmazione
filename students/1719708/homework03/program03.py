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
    
def ricolora(fname, lista, fnameout):
	image = load(fname)
	result = []
	for tupla in lista:
		c = image[tupla[1]][tupla[0]]
		csi = []
		y_max = [len(image), 0]
		pixels = []
		per = []
		x_connected(image, csi, tupla[0], tupla[1], c)
		y_connected(image, csi, tupla[1], c, pixels, per)
		color(image, pixels, tupla[2])
		color(image, per, tupla[3])
		result += [(len(pixels), len(per))]
	save(image, fnameout)
	return result
	
def x_connected(image, csi, x, y, c):
	x1 = x
	while x1 >= 0 and image[y][x1] == c:
		csi += [x1]
		x1 += -1
	x1 = x + 1
	while x1 < len(image[0]) and image[y][x1] == c:
		csi += [x1]
		x1 += 1
		
def y_connected(image, csi, y, c, pixels, per):
	for x in csi:
		y1 = y
		while y1 >= 0 and image[y1][x] == c:
			if around(image, x, y1, c):
				pixels += [[x, y1]]
			else:
				per += [[x, y1]]
			y1 += -1
		y1 = y + 1
		while y1 < len(image) and image[y1][x] == c:
			if around(image, x, y1, c):
				pixels += [[x, y1]]
			else:
				per += [[x, y1]]
			y1 += 1
			
def around(image, x, y, c):
	if y == 0 or x == 0:
		return False
	if y == len(image) - 1 or x == len(image[0]) - 1:
		return False
	return image[y - 1][x] == c and image[y][x - 1] == c and image[y + 1][x] == c and image[y][x + 1] == c
			
def color(image, p_c, c1):
	for p in p_c:
		image[p[1]][p[0]] = c1
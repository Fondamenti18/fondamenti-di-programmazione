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
Il perimetro della zona colorata e' l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno e' di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perche' sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],'OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro e' il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *
 
def get_adj_connected_pixels (img, x_, y_):
	connections = set()
	for x,y in [(x_+i,y_+j) for i in (-1,0,1) for j in (-1,0,1) if i == 0 or j == 0]:
		if 0<=x<len(img[0]) and 0<=y<len(img) and (x,y)!=(x_,y_):
			if img[y][x]==img[y_][x_]:
				if (x,y)!=(x_,y_):
					connections.add((x,y))
	return connections

def get_connected_pixels_recursively(img, x_, y_, all_connections):
	new_connections = get_adj_connected_pixels(img, x_, y_)
	while new_connections:
		for p in new_connections:
			if p not in all_connections:
				all_connections.add(p)
				more_connections=get_adj_connected_pixels(img, p[0], p[1])
				new_connections = new_connections|more_connections
		new_connections = new_connections - all_connections
	return all_connections

def ricolora(fname, lista, fnameout):
	img = load(fname)
	result = []
	for seq in lista:
		all_connections = set()
		all_connections.add((seq[0],seq[1]))
		area = get_connected_pixels_recursively(img,seq[0],seq[1],all_connections)
		bordo = set()
		for p in area:
			if len(get_adj_connected_pixels(img,p[0],p[1]))<4:
				bordo.add(p)
		interno = area - bordo
		for p in interno:
			img[p[1]][p[0]] = seq[2]
		for p in bordo:
			img[p[1]][p[0]] = seq[3]
		pair = (len(interno),len(bordo))
		result.append(pair)
		
	save (img, fnameout)

	return result
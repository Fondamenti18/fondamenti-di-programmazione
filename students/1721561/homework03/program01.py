#'''
#Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
#di vari colori i cui assi sono sempre parallei agli assi dell'immagine.
#
#Vedi ad esempio l'immagine Img1.png
#
#Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .
#
#Scrivere una  funzione quadrato(filename, C) che prende in input:
#- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena descritta.
#- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)
#
#La funzione deve restituire nell'ordine:
#- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile nell'immagine. 
#- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
#all'interno dell'immagine del punto in alto a sinistra del quadrato. 
#
#In caso ci siano piu' quadrati di dimensione massima, va considerato quello il cui punto 
#in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 
#
#Si puo' assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.
#
#Per gli esempi vedere il file grade01.txt
#
#ATTENZIONE: Il timeout e' impostato a 10*N secondi (con N numero di test del grader).
#'''

from immagini import *

def quadrato(filename,c):
	
	img = load(filename)

	support_matrix = [[0 for column in range(len(img[0]))] for row in range(len(img))]
	
	max_size = 0
	max_row_index = 0
	max_column_index = 0
	
	for i in range(len(img)):
		for j in range(len(img[0])):
			
			if i==0 or j==0 and img[i][j]==c:
				support_matrix[i][j] = 1
			elif img[i][j]==img[i-1][j] and img[i][j]==img[i][j-1] and img[i][j]==img[i-1][j-1] and img[i][j]==c:
				support_matrix[i][j] = min(support_matrix[i-1][j], support_matrix[i][j-1], support_matrix[i-1][j-1]) + 1
			elif img[i][j]!=img[i-1][j] and img[i][j]!=img[i][j-1] and img[i][j]!=img[i-1][j-1] and img[i][j]!=img[i+1][j] and img[i][j]!=img[i][j+1] and img[i][j]!=img[i+1][j+1] and img[i][j]==c:
				max_size = 1
				max_row_index = i - max_size + 1
				max_column_index = j - max_size + 1
			else:
				support_matrix[i][j] = 1
			
			if support_matrix[i][j] > max_size:
				max_size = support_matrix[i][j]
				max_row_index = i - max_size + 1
				max_column_index = j - max_size + 1
	
	return (max_size, (max_column_index, max_row_index))


#print quadrato('Ist0.png',(255,255,255))
#print quadrato('Ist1.png',(255,0,0))
#print quadrato('Ist2.png',(255,0,0))
#print quadrato('Ist3.png',(255,0,0))
#print quadrato('Ist4.png',(0,0,255))
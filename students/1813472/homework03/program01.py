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


 
from immagini import *


 
def quadrato(filename,c):
		max=0
		img=load(filename)
		t=[len(img),len(img[0])]
		g=[0,0]
		escludix=0
		escludiy=0 
		for x in range(0,len(img)):
			for y in range(0,len(img[0])):
				if c == img[x][y] and not(y<escludiy and x<escludix ) :
					
					g[0]=x
					g[1]=y
					limitx=1
					limity=1
					
					latoDaVerificare=1
					for z in range(g[0],len(img)):
						if c!=img[z][g[1]]:
							limitx=z
							break
					for s in range(g[1],len(img[0])):
						if c!=img[g[0]][s]:
							limity=s
							break
					if limitx-g[0]>limity-g[1]:
						latoDaVerificare=limity-g[1]
					else:
						latoDaVerificare=limitx-g[0]
					latoEffettivo=0
					
					for z in range(g[0],g[0]+latoDaVerificare):	
						for s in range(g[1],g[1]+latoDaVerificare):
							
							if c!=img[z][s]:
								if  z>escludix or s>escludiy  :
									escludix=z
									escludiy=s
								if z-g[0]>s-g[1]:
									latoEffettivo=s-g[1]
								else:
									latoEffettivo=z-g[0]
								break
								
						if latoEffettivo>0:
						
							break
					if latoEffettivo==0:
						latoEffettivo=latoDaVerificare 
								
					if latoEffettivo==max and(g[1]<t[1] or (g[1]==t[1] and g[0]<t[0])) :
						
						max=latoEffettivo
						t=[g[1],g[0]]
					
					if latoEffettivo>max: 
						
						max=latoEffettivo
						t=[g[1],g[0]]						
						
					
							
        
		result=(max, (t[0],t[1])) 
		return result

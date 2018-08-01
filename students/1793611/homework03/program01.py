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

In caso ci siano piu' quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si puo' assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout e' impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import *

def quadrato(filename,c):
	imm=load(filename)
	rquad=(0,(-1,-1))
	nrig=len(imm)
	ncol=len(imm[0])
	for nr in range(nrig):
		if (nrig-1-nr)<rquad[0]: break
		nc=0
		while nc<ncol:
			oriz=0
			lato=0
			if (imm[nr][nc])==c:
				lato=lato+1
				no=0
				if (nc+lato)<ncol and (nr+lato)<nrig:
					while (imm[nr+lato][nc+lato])==c:
						for nl in range(1,lato+1):
							if (imm[nr+lato-nl][nc+lato]!=c) or (imm[nr+lato][nc+lato-nl]!=c):
								if (imm[nr+lato-nl][nc+lato]!=c): oriz=nl-1
								no=1
								break
						if no==1: break
						lato=lato+1
						if (nc+lato)>=ncol or (nr+lato)>=nrig: break
					if lato>rquad[0]: rquad=(lato,(nc,nr))
			nc=nc+oriz+1
	return rquad

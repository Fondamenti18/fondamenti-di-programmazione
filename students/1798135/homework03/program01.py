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

#def quadrato(filename,c):
def quadrato(filename,c):

	img=load(filename)
	diz={}
	lista=[]
	massimo=0
	altezza=len(img)
	lunghezza=len(img[0])
	for riga in range(altezza):
		if c in img[riga]:

			contatore=0
			lato={}
			for colore in range(lunghezza):
				#vede quante volte c'è il colore

				if img[riga][colore] ==c:
					contatore=contatore+1

				elif contatore >1:
					inizio=(riga,colore-contatore)
					lato[inizio]=contatore
					contatore=0



				elif contatore ==1:
					inizio=(colore-contatore,riga)
					diz[inizio]=1
					massimo=1
					contatore=0
			#crea una lista
			#print (lato)
			for L_M in lato.keys():
				lista=[]
				#print(altezza,"  altezza ",lunghezza," lunghezza ",L_M," contiene",lato[L_M])
				if lato[L_M]<=massimo:
					continue

				else:


					for ii in range(lato[L_M]):
						colori=0

						for jj in range(lato[L_M]):
							if L_M[0]+jj<altezza:
								if img[L_M[0]+jj][L_M[1]+ii]==c:
									colori=colori+1


								else:
									#lista=lista+[colori]
									break
						lista=lista+[colori]

						#print(len(lista),"    ",ii)


					#print(lista)
					if lista:

						valori=cerca_quadrati(lista,massimo)
						#print(valori)
						if valori:
							if valori[0]>massimo:
								massimo=valori[0]
								#print(L_M,"  ",lato[L_M])
								chiave=(L_M[1]+valori[1],L_M[0])
								#print(chiave)
								diz[chiave]=massimo
								#print(diz)
	for ris in diz:
		if diz[ris]==massimo:
			return (massimo,ris)



def cerca_quadrati(lista,massimo):
	grandezza=0
	massimolocale=0
	for q in range(len(lista)):
		avanti=1
		indietro=1

		if lista[q]>massimo:
			for p in range(1,lista[q]):

				if (q-indietro)>=0:
					if lista[q-indietro]>=lista[q]:
						indietro+=1

					elif (q+avanti)<=len(lista)-1:
						if lista[q+avanti]>=lista[q]:
							avanti+=1

				elif (q+avanti)<=len(lista)-1:
					if lista[q+avanti]>=lista[q]:
						avanti+=1

				else:
					break
			avanti-=1
			indietro-=1
			#print("indietro",indietro,"avanti",avanti," grandezza ",massimo)
			grandezza=avanti+indietro+1
			if massimo<grandezza:
				massimo=grandezza
				massimolocale=grandezza
				zero=q-indietro

	if(massimolocale>1):
		risultato=[massimolocale,zero]
		return risultato
	else:
		return None

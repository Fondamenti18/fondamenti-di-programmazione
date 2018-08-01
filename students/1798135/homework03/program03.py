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
 
'''

from immagini import *
    
def ricolora(fname, lista, fnameout):
	img=load(fname)
	salvataggio=[]
	for x,y,c1,c2 in lista:
		connessi={}
		bordo=0
		area=0
		colore=img[y][x]
		cerca=True
		primo=False
		count=0
		locale=[]
		perimetro={}
		a=0
		p=0
		#primo ciclo per preparare il tutto
		for i in range(len(img[y])):
			if img[y][i]==colore:
				#print(" trovato  i ",i,"  x",x)
				count+=1
				if x == i:
					primo=True
			elif primo:
				inizio=(y,i-count)
				base=[i-count,count]
				old=[i-count,count]
				connessi[inizio]=count
				count=0
				primo=False
				break

			else:
				count=0
		if primo:
			inizio=(y,i-count+1)
			base=[i-count,count]
			old=[i-count,count]
			connessi[inizio]=count
			count=0
		#print(base)
		sopra=1
		sotto=1
		switch=True
		#ricerca di connessioni molto simile a prima

		
		while(cerca):
			
			
			temp=[]
			#primo blocco per cercare sorpa
			if y-sopra>=0 and switch:
				for i in range(len(img[y])):
					#print(img[y-sopra][i])
					if img[y-sopra][i]==colore:
						#print("trovato ad ",i,"  con count",count)
						count+=1

					elif count>0:
						inizio=(y-sopra,i-count)
						temp=temp+[i-count,count,inizio]
						count=0

				if count>0:
					inizio=(y-sopra,i-count+1)
					temp=temp+[i-count,count,inizio]
					count=0
				sopra+=1

			#secondo blocco per cercare sotto
			elif y+sotto<len(img[0]):
				for i in range(len(img[y])):
					if img[y+sotto][i]==colore:
						#print("ne ho trovato uno sotto")
						count+=1
					elif count>0:
						inizio=(y+sotto,i-count)
						temp=temp+[i-count,count,inizio]
						count=0
				if count>0:
					inizio=(y+sotto,i-count+1)
					temp=temp+[i-count,count,inizio]
					count=0
				sotto+=1
			else:
				cerca=False
			#print(sotto,"  sotto   y",y)
			#print(temp,"  andato sotto ",sotto," volta sopra",sopra," len old ",len(old))
			#ciclo per controllare connessioni
			for i in range(0,len(temp),3):
				s1=set(range(temp[i],temp[i+1]+temp[i]-1))
				for j in range(0,len(old),2):
					s2=set(range(old[j],old[j+1]+old[j]-1))
					if len(s1&s2)>0:
						#print(i," ",j," old ",old)
						connessi[temp[i+2]]=temp[i+1]
						locale=locale+[temp[i],temp[i+1]]
						#if len(s2-s1)>0:

			#aggiornamento variabili importanti
			if len(locale)>0:
				#print("ho aggiornato il confronto")
				old=locale[:]
				locale=[]
			elif switch:
				switch=False
				if y-sopra>=0:
					#print(y," 0 ",sopra)
					perimetro[y-sopra+2]=(old[0],old[1])
				else:
					#print(y," 1 ",sopra)
					perimetro[y-sopra+1]=(old[0],old[1])
				old=base[:]

			else:
				if y+sotto<len(img[0]) and y-sopra<0:
					#print(y," 0 ",sotto)
					perimetro[y+sotto-3]=(old[0],old[1])
				elif  y+sotto<len(img[0]) and y-sopra>=0:
					perimetro[y+sotto-2]=(old[0],old[1])
				else:
					#print(y," 1 ",sotto)
					perimetro[y+sotto-1]=(old[0],old[1])
				cerca=False
		#print(connessi)
		#ora si ricolora k ha posizione d'inizio come chiave  e come valore la lunghezza della riga
		for k in connessi.keys():
			if connessi[k]>2:
				#coloro i pixel di bordo
				img[k[0]][k[1]]=c2
				#print(k[0]," k0    k1 ",k[1]," k[1]+connessi[k] ",k[1]+connessi[k])
				img[k[0]][k[1]+connessi[k]-1]=c2
				p=p+2
				for i in range(k[1]+1,k[1]+connessi[k]-1):
					img[k[0]][i]=c1
					a=a+1
			elif connessi[k]==2:
				img[k[0]][k[1]]=c2
				img[k[0]][k[1]+connessi[k]]=c2
				p=p+2
			else:
				img[k[0]][k[1]]=c2
				p=p+1
		#print(perimetro,"sopra",sopra,"sotto",sotto)
		for last in perimetro.keys():
			for i in range(perimetro[last][0],perimetro[last][1]+perimetro[last][0]):
				if img[last][i]==c1:
					img[last][i]=c2
					p=p+1
					a=a-1
		#print(a," ",p)
		salvataggio=salvataggio+[(a,p)]
		save(img,fnameout)
	return salvataggio

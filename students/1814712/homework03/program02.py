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

import immagini

"""def cammino(fname,  fname1):
	print("lsdjflk")
	img = immagini.load(fname)
	l = len(img)  
	mossa = ''
	fine = 0
	p_robot_x = 0
	p_robot_y = 0
	rosso = (255,0,0)
	verde = (0,255,0)
	blu = (0,0,255)
	while not fine:
		img[p_robot_x][p_robot_y] = verde
		print("posizione corrente = (", p_robot_x, p_robot_y, ")")
		if p_robot_y < l - 40 and img[p_robot_x][p_robot_y + 40] != rosso and img[p_robot_x][p_robot_y + 40] != verde:
			p_robot_y = p_robot_y + 40
			mossa = mossa + '0'
		
		elif p_robot_x < l - 40 and  img[p_robot_x + 40][p_robot_y] != rosso and img[p_robot_x + 40][p_robot_y] !=verde:
			p_robot_x = p_robot_x - 40
			mossa = mossa + '1'
			
		
		elif p_robot_y > 40 and img[p_robot_x][p_robot_y - 40] != rosso and img[p_robot_x][p_robot_y - 40] != verde:
			p_robot_y = p_robot_y - 40
			mossa = mossa + '2'
			
		
		elif p_robot_x > 40 and img[p_robot_x - 40][p_robot_y] != rosso and img[p_robot_x - 40][p_robot_y] != verde:
			p_robot_x = p_robot_x + 40
			mossa = mossa + '3'
		
		else:
			img[p_robot_x][p_robot_y] = blu
			fine = True	
	immagini.save(img, fname1)
	return mossa """
	

def cammino(fname,  fname1):
	img = immagini.load(fname)
	l = len(img)  
	mossa = '0'
	fine = False
	p_robot_i = 0
	p_robot_j = 0
	rosso = (255,0,0)
	verde = (0,255,0)
	blu = (0,0,255)
	
	while not fine:
		for i in range(40) :
			for j in range(40) :
				img[p_robot_i + i][p_robot_j + j] = verde
		
		#print("posizione corrente = (", p_robot_i, p_robot_j, "), mossa = ", mossa)
		
		mossa_new = mossa[len(mossa) - 1]
		bloc = 0
		#print(muovi(mossa_new, p_robot_i, p_robot_j, img, l, verde, rosso))
		while not muovi(mossa_new, p_robot_i, p_robot_j, img, l, verde, rosso)[0] and bloc <= 4 :
			#print("nel while, muovi(", mossa_new, p_robot_i, p_robot_j, ") = ", muovi(mossa_new, p_robot_i, p_robot_j, img, l, verde, rosso))
			mossa_new = str((int(mossa_new) + 1) % 4)
			bloc += 1
			
		if bloc >= 4 :
			for i in range(40) :
				for j in range(40) :
					img[p_robot_i + i][p_robot_j + j] = blu
			fine = True
			
		else :
			mossa = mossa + mossa_new
			p_robot_i = muovi(mossa_new, p_robot_i, p_robot_j, img, l, verde, rosso)[1]
			p_robot_j = muovi(mossa_new, p_robot_i, p_robot_j, img, l, verde, rosso)[2]
			
	immagini.save(img, fname1)
	return mossa[1:]


def muovi(mossa, corr_i, corr_j, img, l, verde, rosso) :
		if mossa == '0' :
			j = corr_j + 40
			if j < l and img[corr_i][j] != verde and img[corr_i][j] != rosso :
				return (True, corr_i, j)
			else :
				return (False, corr_i, j)
		elif mossa == '1' :
			i = corr_i + 40
			if i < l and img[i][corr_j] != verde and img[i][corr_j] != rosso :
				return (True, i, corr_j)
			else :
				return (False, i, corr_j)
		elif mossa == '2' :
			j = corr_j - 40
			if j >= 0 and img[corr_i][j] != verde and img[corr_i][j] != rosso :
				return (True, corr_i, j)
			else :
				return (False, corr_i, j)
		elif mossa == '3' :
			i = corr_i - 40
			if i >= 0 and img[i][corr_j] != verde and img[i][corr_j] != rosso :
				return (True, i, corr_j)
			else :
				return (False, i, corr_j)
		else :
			return (False, corr_i, corr_j)

		
			 	
			 		
			 
			 
			 	
	
	
	
	
	
	
	
	
  

import immagini

def quadrato(filename,c):
	img = immagini.load(filename)
	h = len(img)  
	w = len (img[0])
	l_max = 0
	p = (0,0)
	for i in range(h):
		for j in range(w):
			if img[i][j] == c:
				l = 0 
				j_app = j
				while j < w and img[i][j] == c:
					l+=1
					j+=1
					cont = 0
				if i + l > h :
					cont = -1
				else :
					for j1 in range(j_app, j):
						for i1 in range(i, i + l):
							if img[i1][j1] != c:
								cont = -1
								break
						if cont == -1:
							break
				if cont != -1 and l > l_max:
					p = (j_app, i)
					l_max = l
	return (l_max,p)
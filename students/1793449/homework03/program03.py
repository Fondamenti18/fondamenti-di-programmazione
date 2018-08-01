from immagini import *

def righe(img) : return len(img)
def colonne(img) : return len(img[0])

def inside(img, x, y):
	return 0 <= y < righe(img) and 0 <= x < colonne(img)

def checkx(ad, l):
	for x in ad:
		if x not in l:
			l.append(x)

def checklen(ad, area, perimetro, b):
	if len(ad) == 4:
		area.append([b[0],b[1]])
	elif len(ad) < 4:
		perimetro.append([b[0],b[1]])

def checkcol(area, perimetro, img, col1, col2):
	for x in area:
		img[x[0]][x[1]] = col1
	for x in perimetro:
		img[x[0]][x[1]] = col2

def ricolora(fname, lista, fnameout):
	img = load(fname)
	ret = []
	for a in lista:
		col1 = a[2]
		col2 = a[3]
		n = (a[0],a[1])
		l = ([n])
		col = img[a[0]][a[1]]
		area = []
		perimetro = []
		for b in l:
			ad = []
			if inside(img, b[0]-1, b[1]) == True:
				if img[b[0]-1][b[1]] != col:
					pass
				else:
					ad.append(([b[0]-1,b[1]]))
			if inside(img, b[0]+1, b[1]) == True:
				if img[b[0]+1][b[1]] != col:
					pass
				else:
					ad.append(([b[0]+1,b[1]]))
			if inside(img, b[0], b[1]-1) == True:
				if img[b[0]][b[1]-1] != col:
					pass
				else:
					ad.append(([b[0],b[1]-1]))
			if inside(img, b[0], b[1]+1) == True:
				if img[b[0]][b[1]+1] != col:
					pass
				else:
					ad.append(([b[0],b[1]+1]))
			checkx(ad,l)
			checklen(ad, area, perimetro, b)
		checkcol(area, perimetro, img, col1, col2)
		ret.append((len(area)-1,len(perimetro)))
	save(img,fnameout)
	return ret

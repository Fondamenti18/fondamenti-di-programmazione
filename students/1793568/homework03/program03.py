from immagini import *

def check_up(x,y,img,c):
	if (y-1 >= 0 and img[y-1][x] == c):
		return True
	else:
		return False

def check_down(x,y,img,c):
	if (y+1 < len(img) and img[y+1][x] == c):
		return True
	else:
		return False

def check_right(x,y,img,c):
	if (x+1 < len(img[y]) and img[y][x+1] == c):
		return True
	else:
		return False

def check_left(x,y,img,c):
	if (x-1 >= 0 and img[y][x-1] == c):
		return True
	else:
		return False
	

def build_nb(x,y,img,cv,old,nbr):
	if check_right(x,y,img,cv) and (x+1,y) not in old and (x+1,y) not in set(nbr):
		nbr += [(x+1,y)]
	if check_left(x,y,img,cv) and (x-1,y) not in old and (x-1,y) not in set(nbr):
		nbr += [(x-1,y)]
	if check_up(x,y,img,cv) and (x,y-1) not in old and (x,y-1) not in set(nbr):
		nbr += [(x,y-1)]
	if check_down(x,y,img,cv) and (x,y+1) not in old and (x,y+1) not in set(nbr):
		nbr += [(x,y+1)]
	return nbr

def colorate_square(x,y,c1,img,cv,old):
	nb = []
	nb = build_nb(x,y,img,cv,old,nb)
	img[y][x] = c1
	old.add((x,y))
	while(nb[:] != []):
		c = nb[0]
		nb = build_nb(c[0],c[1],img,cv,old,nb)
		if (c[0],c[1]) not in old:
			old.add((c[0],c[1]))
		img[c[1]][c[0]] = c1
		del nb[0]


def colorate_perimeter(old,img,c2):
	AP = 0
	AI = 0
	for el in old:
		if (el[0]+1,el[1]) not in old:
			AP += 1
			img[el[1]][el[0]] = c2
		elif (el[0]-1,el[1]) not in old:
			AP += 1
			img[el[1]][el[0]] = c2
		elif (el[0],el[1]+1) not in old:
			AP += 1
			img[el[1]][el[0]] = c2
		elif (el[0],el[1]-1) not in old:
			AP += 1
			img[el[1]][el[0]] = c2
		else:
			AI += 1
	return (AI,AP)

def ricolora(fname, lista, fnameout):
	img = load(fname)
	R = []
	for el in lista:
		AI = []
		AP = 0
		old = set()
		x = el[0]
		y = el[1]
		c1 = el[2]
		c2 = el[3]
		colorate_square(x,y,c1,img,img[y][x],old)
		R += [colorate_perimeter(old,img,c2)]
	save(img,fnameout)
	return R

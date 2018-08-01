from immagini import *

def Colora(img,y,x,m,f):
	miny = 0
	maxy = 0
	minx = 0
	maxx = 0
	if f:
		c = (0,0,255)
	else:
		c = (0,255,0)

	if m == 0:
		miny = y
		maxy = y+40
		minx = x
		maxx = x+40
	if m == 1:
		miny = y
		maxy = y+40
		minx = x-39
		maxx = x+1
	if m == 2:
		miny = y-39
		maxy = y+1
		minx = x-39
		maxx = x+1
	if m == 3:
		miny = y-39
		maxy = y+1
		minx = x
		maxx = x+40

	for i in range(miny,maxy):
		for j in range(minx,maxx):
			img[i][j] = c


def check_status(img,posy,posx,maximg,m):
	if (m == 0 and posx+40 >= maximg) or (m == 1 and posx-40 < 0) or (m == 2 and posy+40 >= maximg) or (m == 3 and posy-40 < 0):
		return False
	elif m == 0 and (img[posy][posx+40] == (255,0,0) or img[posy][posx+40] == (0,255,0)):
		return False
	elif m == 1 and (img[posy][posx-40] == (255,0,0) or img[posy][posx-40] == (0,255,0)):
		return False
	elif m == 2 and (img[posy+40][posx] == (255,0,0) or img[posy+40][posx] == (0,255,0)):
		return False
	elif m == 3 and (img[posy-40][posx] == (255,0,0) or img[posy-40][posx] == (0,255,0)):
		return False
	else:
		return True

def check_max_img(img,m):
	if m == 0:
		return len(img[0])
	else:
		return len(img)


def go_rigth(img,posy,posx):
	l = check_max_img(img,0)
	if check_status(img,posy,posx,l,0):
		return True
	else:
		return False

def go_left(img,posy,posx):
	l = check_max_img(img,0)
	if check_status(img,posy,posx,l,1):
		return True
	else:
		return False

def go_up(img,posy,posx):
	l = check_max_img(img,1)
	if check_status(img,posy,posx,l,3):
		return True
	else:
		return False

def go_down(img,posy,posx):
	l = check_max_img(img,1)
	if check_status(img,posy,posx,l,2):
		return True
	else:
		return False

def walk(img):
	M = 0
	x = 0
	y = 0
	s = ""

	while(go_rigth(img,y,x) == True or go_left(img,y,x) == True or go_down(img,y,x) == True or go_up(img,y,x) == True):

		if M == 0:
			if go_rigth(img,y,x):
				Colora(img,y,x,0,False)
				x += 40
				s += "0"
				
			else:
				Colora(img,y,x,0,False)
				x += 39
				M = 2
				#s += "0"

		if M == 2:
			if go_down(img,y,x):
				Colora(img,y,x,1,False)
				y += 40
				s += "1"
				
			else:
				Colora(img,y,x,1,False)
				y += 39
				M = 1
				#s += "1"

		if M == 1:
			if go_left(img,y,x):
				Colora(img,y,x,2,False)
				x -= 40
				s += "2"
				
			else:
				Colora(img,y,x,2,False)
				x -= 39
				M = 3

		if M == 3:
			if go_up(img,y,x):
				Colora(img,y,x,3,False)
				y -= 40
				s += "3"
				
			else:
				Colora(img,y,x,3,False)
				y -= 39
				M = 0
	if M == 1:
		Colora(img,y,x,2,True)
	elif M == 2:
		Colora(img,y,x,1,True)
	else:
		Colora(img,y,x,M,True)

	return s


def cammino(fname,  fname1):
	img = load(fname)
	s = walk(img)
	save(img,fname1)
	return s


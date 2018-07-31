from immagini import *

def calculate_square(x,mx,y,my,img,c):
	for i in range(y,my):
		for j in range(x,mx):
			if (img[i][j] != c):
				return False
	return True

def check_diag(x,xf,y,yf,img,c,maxl):
	xf -= 1
	yf -= 1

	while xf > 1 and yf > 1:
		if xf-x > maxl:
			if calculate_square(x,xf,y,yf,img,c):
				return (xf-x)
			else:
				xf -= 1
				yf -= 1
		else:
			break
	return maxl

def check_square(img,x,y,c,maxl):
	xf = x
	yf = y

	while(yf < len(img) and xf < len(img[yf])) and (img[yf][xf] == c):
		xf += 1
		yf += 1
	if xf-x > maxl:
		if calculate_square(x,xf,y,yf,img,c):
			return (xf-x)
		else:
			return check_diag(x,xf,y,yf,img,c,maxl)
	else:
		return 0
		
def quadrato(filename,c):
	img = load(filename)
	maxl = 0
	C = [0,0]

	for y in range(len(img)):
		for x in range(len(img[y])):
			if img[y][x] == c:
				App = check_square(img,x,y,c,maxl)
				if App > maxl:
					C[0] = x
					C[1] = y
					maxl = App

	return (maxl,(C[0],C[1]))